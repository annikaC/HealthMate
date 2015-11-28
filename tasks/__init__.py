
from invoke import Collection, ctask as task


@task
def runserver(ctx, port=8000, *args):
    """Run the server."""
    args = " ".join(args)
    if args:
        args = " " + args
    command = './manage.py runserver 0.0.0.0:{}{}'.format(port, args)
    ctx.run(command, pty=True)


@task
def freeze(ctx):
    """Freeze the current requirements."""
    ctx.run('pip-dump requirements/*.txt')


@task
def deploy(ctx, branch=None):
    """Deploy to production server."""
    cmd = ('ansible-playbook -i '
           'provisioning/inventory/production '
           'provisioning/production.yml')
    if branch:
        cmd += """ --extra-vars 'git_branch="{}"'""".format(branch)
    try:
        ctx.run(cmd)
    except:
        raise


ns = Collection(deploy, freeze, runserver)
