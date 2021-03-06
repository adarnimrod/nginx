import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_nginx_service(Service, Sudo):
    with Sudo():
        service = Service('nginx')
        assert service.is_running
        try:
            assert service.is_enabled
        except NotImplementedError:
            pass


include_directives = ['include /etc/nginx/sites-enabled/*;',
                      'include /etc/nginx/conf.d/*.conf;']


@pytest.mark.parametrize('directive', include_directives)
def test_nginx_include_directive(File, directive):
    assert directive in File('/etc/nginx/nginx.conf').content_string


def test_nginx_config(File, Command, Sudo):
    with Sudo():
        assert Command('nginx -t').rc == 0
    assert File('/etc/nginx/nginx.conf').exists
    assert File('/etc/nginx/conf.d').is_directory
    assert File('/etc/nginx/sites-enabled').is_directory


def test_nginx_alias(File, SystemInfo, User):
    if SystemInfo.type == 'openbsd':
        aliasfile = '/etc/mail/aliases'
        wwwuser = 'www'
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        aliasfile = '/etc/aliases'
        wwwuser = 'www-data'
    assert User(wwwuser).exists
    assert File(aliasfile).contains(wwwuser + ': root')


def test_nginx_dhparams(File):
    if File('/etc/ssl/dhparams.pem').is_file:
        assert 'ssl_dhparam /etc/ssl/dhparams.pem;' in File(
            '/etc/nginx/conf.d/dhparams.conf').content_string


def test_nginx_stub_status(File, Command):
    stub_status = File('/etc/nginx/sites-enabled/stub_status')
    assert stub_status.exists
    assert stub_status.contains('stub_status;')
    curl = Command(
        'curl --resolve stub_status:80:127.0.0.1 http://stub_status/')
    assert curl.rc == 0
    assert 'Active connections:' in curl.stdout


def test_nginx_socket(Socket):
    assert Socket('tcp://0.0.0.0:80').is_listening


def test_nginx_limit(File):
    assert File('/etc/nginx/conf.d/limit.conf').is_file
