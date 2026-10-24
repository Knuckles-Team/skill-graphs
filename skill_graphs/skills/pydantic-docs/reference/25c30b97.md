# Run without subcommands
sys.argv = ['example.py']
cmd = Git()
assert cmd.model_dump() == {'clone': None, 'init': None}

try:
    # Will raise an error since no subcommand was provided
    get_subcommand(cmd).model_dump()
except SettingsError as err:
    assert str(err) == 'Error: CLI subcommand is required {clone, init}'
