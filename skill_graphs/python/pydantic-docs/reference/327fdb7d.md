# Run the clone subcommand
sys.argv = ['example.py', 'clone', 'repo', 'dest']
cmd = Git()
assert cmd.model_dump() == {
    'clone': {'repository': 'repo', 'directory': 'dest'},
    'init': None,
}
