# Parse and load CLI settings from the command line into the settings source.
sys.argv = ['example.py', '--food', 'kiwi', '--name', 'waldo']
s = CliApp.run(Settings, cli_settings_source=cli_settings)
print(s.model_dump())
#> {'name': 'waldo'}
