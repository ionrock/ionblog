import os
import re
import subprocess

from datetime import datetime

from paver.easy import path

DEST = path('.')
SRC = path('../Ionrock Dot Org/src/')
FIND_DATE = re.compile('^:date: (\d{4})-(\d{2})-(\d{2})')
DATE_PATH = '%Y/%m/%d/'
OLD_DIRECTIVE = re.compile('^:(\w+): (.*)')


class BlogPost(object):

    def __init__(self, path):
        self.f = path

    @property
    def date(self):
        if not hasattr(self, '_date'):
            with open(self.f) as fh:
                for line in fh:
                    m = FIND_DATE.match(line)
                    if m:
                        self._date = datetime(*map(int, m.groups()))

        if not hasattr(self, '_date'):
            raise Exception('Invalid date: %s' % self.f)
        return self._date

    def create_directory(self):
        path = self.date.strftime(DATE_PATH)
        cmd = 'mkdir -p %s' % path
        subprocess.call(cmd.split())
        return path

    def fixup_directives(self):
        directives = {}
        content = []
        for line in open(self.f):
            m = OLD_DIRECTIVE.match(line)
            if m:
                k, v = m.groups()
                directives[k] = v
            else:
                content.append(line)

        # add a gap
        content.append('\n\n')

        # defaults
        content.append('.. author:: default\n')

        # add our adjusted directives
        for directive, value in directives.items():
            if directive == 'category':
                directive = 'categories'

            if directive != 'date':
                content.append('.. %s:: %s\n' % (directive, value))

        # add comments
        content.append('.. comments::\n')

        return ''.join(content)

    def write_file(self, dirname, content):
        path = os.path.join(dirname, os.path.basename(self.f))
        open(path, 'w+').write(content)
        return path

    def migrate(self):
        directory = self.create_directory()
        content = self.fixup_directives()
        path = self.write_file(directory, content)
        print('migrated %s' % self.f)

        return path


def run():
    paths = []
    for fn in SRC.listdir('*.rst'):
        post = BlogPost(fn)
        path = post.migrate()
        paths.append(path)

    paths.sort()
    paths.reverse()

    with open('master.rst', 'a') as master:
        master.write('\n')
        for path in paths:
            master.write('   %s\n' % path[:-4])


if __name__ == '__main__':
    run()
