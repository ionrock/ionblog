import csv
import gzip
import traceback

from datetime import datetime
from pprint import pformat

import requests

from pangaea.client.models import Datafile
from pangaea.client.utils import get_gzipped_record_count


SELECTED_VALUES = {
    '1': 'selected',
    '2': 'not selected',
    '8': 'skipped',
    '9': 'not asked'
}

OPINION_VALUES = {
    '0': 'neutral',
    '1': 'positive',
    '2': 'negative',
    '9': 'not asked'
}

CONSTANT_COLUMNS = [
    {'name': 'brand_id', 'type': 'int'},
    {'name': 'region', 'type': 'string'},
    {'name': 'category_id', 'type': 'int'},
    {'name': 'pmxid', 'type': 'string'},
    {'name': 'date', 'type': 'datetime'},
    {'name': 'weight', 'type': 'float'},
    {'name': 'likelybuy', 'type': 'int'},
]

SELECTED_COLUMNS = [
    {'name': 'adaware', 'type': 'int', 'values': SELECTED_VALUES},
    {'name': 'aided', 'type': 'int', 'values': SELECTED_VALUES},
    {'name': 'consider', 'type': 'int', 'values': SELECTED_VALUES},
    {'name': 'current_own', 'type': 'int', 'values': SELECTED_VALUES},
    {'name': 'former_own', 'type': 'int', 'values': SELECTED_VALUES},
    {'name': 'wom', 'type': 'int', 'values': SELECTED_VALUES},
]


OPINION_COLUMNS = [
    {'name': 'buzz', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'impression', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'quality', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'recommend', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'reputation', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'satisfaction', 'type': 'int', 'values': OPINION_VALUES},
    {'name': 'value', 'type': 'int', 'values': OPINION_VALUES},
]

METRIC_COLUMNS = SELECTED_COLUMNS + OPINION_COLUMNS

SCHEMA = CONSTANT_COLUMNS + SELECTED_COLUMNS + OPINION_COLUMNS

COLS = [col['name'] for col in SCHEMA]


def csv_reader(fname):
    return csv.DictReader(open(fname))


def csv_writer(fh, columns=None):
    columns = columns or COLS
    return csv.DictWriter(fh, fieldnames=columns)


def brands_from_columns(cols):
    return set([
        col.split('.')[1]
        for col in cols
        if col.startswith('brand.')
    ])


def convert_to_metric_rows(brands, row, constants=None, metrics=None):
    metrics = metrics or METRIC_COLUMNS
    constants = constants or CONSTANT_COLUMNS

    # Likely buy is somewhat special...
    likelybuy_brand = row.get('likelybuy', None)

    for brand in brands:
        # Add our brand
        row['brand_id'] = brand

        # Initialize our row with our constants
        metric_row = {
            col['name']: row[col['name']]
            for col in constants if col['name'] != 'likelybuy'
        }

        metric_row['likelybuy'] = ''
        if likelybuy_brand == brand:
            metric_row['likelybuy'] = 1

        # Add our metric values
        for col in metrics:
            key = 'brand.%s.%s' % (brand, col['name'])
            # If the metric didn't exist it may not exist. This is
            # only applicable in an early backfill.
            metric_row[col['name']] = row.get(key, None)

        yield metric_row


def filename_to_metadata(fn):
    # looks like $prefix/$region/$sector/$orignal name
    parts = fn.split('/')
    meta = {}

    # Grab the info from our name
    name = parts.pop().split('.')

    meta['sector'] = parts.pop()
    meta['region'] = parts.pop()
    meta['date'] = datetime.strptime(name[2], '%Y%m%d')

    # Use our metadata to construct a better filename
    meta['filename'] = 'brandindex-%s-metrics-%s-%s.csv.gz' % (
        meta['region'], meta['sector'], meta['date'].strftime('%Y%m%d')
    )

    return meta


def get_category_name(panoptic, cat):
    """Grab the category name from panoptic.

    If there is trouble, just return ''.
    """
    try:
        resp = requests.get(panoptic + '/brandindex/categories/%s/' % cat)
        return resp.json()['body']['name']
    except:
        return ""


def meta_to_pangaea_models(meta):
    return {
        'dataset_name': 'metrics-%s' % meta['sector'],
        'datasource_path': 'brandindex-%s' % meta['region'],
        'datasource_name': 'Brandindex-%s' % meta['region']
    }


def find_datafile_from_input(client, filename):
    meta = filename_to_metadata(filename)
    data_info = meta_to_pangaea_models(meta)
    s3_name = client.create_s3name(
        data_info['datasource_path'], data_info['dataset_name'], meta['filename']
    )

    try:
        return client.find(Datafile, {'file': s3_name})
    except:
        return False


def upload_and_update(client, panoptic_url, bucket, output, log):
    # Pull our info from our filename
    meta = filename_to_metadata(output)

    description = 'BrandIndex %s metrics, sector %s (%s)' % (
        meta['region'],
        meta['sector'],
        get_category_name(panoptic_url, meta['sector'])
    )
    dataset_name = 'metrics-%s' % meta['sector']
    datasource_path = 'brandindex-%s' % meta['region']
    datasource_name = 'Brandindex-%s' % meta['region']

    s3_name = client.create_s3name(
        datasource_path, dataset_name, meta['filename']
    )

    client.upload_file(output, bucket, s3_name)

    datafile = {
        'file': s3_name,
        'record_count': get_gzipped_record_count(output),
        'published_time': meta['date'].strftime('%Y-%m-%d 23:59:59Z'),
        'schema': SCHEMA,
        'dataset': {
            'name': dataset_name,
            'description': description,
            'owner': client.user['resource_uri'],
            'datasource': {
                'name': datasource_name,
                'path': datasource_path,
            },
        }
    }

    try:
        client.create(Datafile, datafile)
    except requests.HTTPError as e:
        if e.response.status_code == 409:
            log('%s already exists' % s3_name)
        else:
            msg = 'Headers:\n%s\n\nContent: %s' % (pformat(dict(e.response.headers)),
                                                   e.response.content)
            log(msg)
            raise


def convert_csv_to_metric(client,
                          config,
                          category_id,
                          region,
                          input_csv,
                          output_csv,
                          log):
    messages = []

    datafile_exists = find_datafile_from_input(client, input_csv)

    if datafile_exists:
        messages.append('Datafile for %s exists' % input_csv)
        return

    print('Reading from: %s' % input_csv)

    try:
        reader = csv_reader(input_csv)

        header = reader.next()
        brands = brands_from_columns(header)

        with gzip.open(output_csv, 'wb+') as output:
            print('Writing to: %s' % output_csv)
            writer = csv_writer(output)
            writer.writeheader()

            for row in reader:
                # Add values to the row that exist within the file path.
                row['category_id'] = category_id
                row['region'] = region
                for metric_row in convert_to_metric_rows(brands, row):
                    writer.writerow(metric_row)

        panoptic_url = config[config['datacenter']]['panoptic']
        bucket = config['AWS_STORAGE_BUCKET_NAME']
        upload_and_update(client, panoptic_url, bucket, output_csv, log)

    except Exception:
        messages.append('Error: %s %s' % (input_csv, output_csv))
        messages.append(traceback.format_exc())
        log('\n'.join(messages))
        raise

    messages.append('Finished: %s %s' % (input_csv, output_csv))
    log('\n'.join(messages))
