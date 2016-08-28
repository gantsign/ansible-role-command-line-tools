import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('command,arg', [
    ('curl', '--version'),
    ('dos2unix', '--version'),
    ('glances', '--version'),
    ('grc', '--version'),
    ('htop', '--version'),
    ('mtr', '--version'),
    ('multitail', '-V'),
    ('ag', '--version'),
    ('tree', '--version'),
    ('wget', '--version')
])
def test_command_line_tools(Command, command, arg):
    cmd = Command(command + ' ' + arg)
    assert cmd.rc == 0
