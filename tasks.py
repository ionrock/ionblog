from invoke import task, run


@task
def release():
    run('rsync -r blog/html/ eric@162.243.34.8:htdocs/')
