from invoke import task

@task
def build(c, docs=False):
    c.run("python setup.py build")
    if docs:
        c.run("something")