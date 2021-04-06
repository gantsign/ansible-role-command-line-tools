import pytest


@pytest.mark.parametrize('command,arg', [
    ('curl', '--version'),
    ('dos2unix', '--version'),
    ('glances', '--version'),
    ('grc', '--version'),
    ('htop', '--version'),
    ('http', '--version'),
    ('mtr', '--version'),
    # Can't test multitail due to: Error opening terminal: unknown.
    # ('multitail', '-V'),
    ('neofetch', ''),
    ('ag', '--version'),
    ('tree', '--version'),
    ('wget', '--version')
])
def test_command_line_tools(host, command, arg):
    cmd = host.run(command + ' ' + arg)
    assert cmd.rc == 0
