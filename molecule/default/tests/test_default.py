import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_crontab_file(File):
    c = File('/etc/resolv.conf').content
    assert 'nameserver 8.8.8.8' in c
    assert 'nameserver 8.8.4.4' in c
