# Will not raise an error since subcommand is not required
assert get_subcommand(cmd, is_required=False) is None
