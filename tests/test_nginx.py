import pytest


def test_nginx_service(Service):
    service = Service('nginx')
    assert service.is_running
    try:
        assert service.is_enabled
    except NotImplementedError:
        pass


def test_nginx_port(Socket):
    assert Socket('tcp://0.0.0.0:80/').is_listening


config_directives = ['include /etc/nginx/sites-enabled/*;',
                     'include /etc/nginx/conf.d/*.conf;',
                     'access_log syslog:localhost;',
                     'error_log syslog:locahost;']


@pytest.mark.parametrize('directive', config_directives)
def test_nginx_config_directive(File, directive):
    assert File('/etc/nginx/nginx.conf').contains(directive)


def test_nginx_config(File, Command, directive):
    assert Command('nginx -t').rc == 0
    assert File('/etc/nginx/nginx.conf').exists
    assert File('/etc/nginx/conf.d').is_directory
    assert File('/etc/nginx/sites-enabled').is_directory


def test_nginx_alias(File):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'Debian':
        assert File('/etc/aliases').contains('nginx: root')
    elif ansible_os_family == 'OpenBSD':
        assert File('/etc/mail/aliases').contains('nginx: root')
