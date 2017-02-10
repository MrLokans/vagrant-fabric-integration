from fabric.api import env, task, run, local


def _read_vagrant_ssh_config():
    ssh_config_output = local('vagrant ssh-config', capture=True)
    config = dict(l.strip().split(' ')
                  for l in ssh_config_output.splitlines())
    return config


@task
def vagrant():
    config = _read_vagrant_ssh_config()
    env.hosts = ['{host}:{port}'.format(host=config['HostName'],
                                        port=config['Port'])]
    env.user = config['User']
    env.key_filename = [config['IdentityFile']]
    env.reject_unknown_hosts = False


@task
def uptime():
    """
    This taks is only used for demonstration purposes
    """
    run("uptime")
