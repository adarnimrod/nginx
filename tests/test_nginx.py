import pytest


def test_nginx_service(Service):
    service = Service('nginx')
    assert service.is_running
    try:
        assert service.is_enabled
    except NotImplementedError:
        pass


config_directives = ['include /etc/nginx/sites-enabled/*;',
                     'include /etc/nginx/conf.d/*.conf;',
                     'access_log syslog:server=127.0.0.1;',
                     'error_log syslog:server=127.0.0.1;']


@pytest.mark.parametrize('directive', config_directives)
def test_nginx_config_directive(File, directive):
    assert directive in File('/etc/nginx/nginx.conf').content_string


def test_nginx_config(File, Command):
    assert Command('nginx -t').rc == 0
    assert File('/etc/nginx/nginx.conf').exists
    assert File('/etc/nginx/conf.d').is_directory
    assert File('/etc/nginx/sites-enabled').is_directory


def test_nginx_alias(File, Ansible):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'Debian':
        assert File('/etc/aliases').contains('nginx: root')
    elif ansible_os_family == 'OpenBSD':
        assert File('/etc/mail/aliases').contains('www: root')
