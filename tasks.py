from invoke import task, run


@task
def build():
    run('tinker -b')


@task
def release():
    run('rsync -r blog/html/ eric@ionrock.org:htdocs/')
