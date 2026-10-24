# Set existing `parser` as the `root_parser` object for the user defined settings source
cli_settings = CliSettingsSource(Settings, root_parser=parser)
