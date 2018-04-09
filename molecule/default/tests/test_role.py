import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('command,arg', [
    ('curl', '--version'),
    ('dos2unix', '--version'),
    ('glances', '--version'),
    ('grc', '--version'),
    ('htop', '--version'),
    ('http', '--version'),
    ('mtr', '--version'),
    # Can test multitail due to: Error opening terminal: unknown.
    # ('multitail', '-V'),
    ('ag', '--version'),
    ('tree', '--version'),
    ('wget', '--version')
])
def test_command_line_tools(Command, command, arg):
    cmd = Command(command + ' ' + arg)
    assert cmd.rc == 0
