def test_example(Service, Command, Ansible):
    assert Service('nginx').is_running
    if not Ansible('setup')['ansible_facts']['ansible_os_family'] == 'OpenBSD':
        assert Service('nginx').is_enabled
    assert Command('nginx -t')
