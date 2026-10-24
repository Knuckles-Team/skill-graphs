## Test CLI Runner[¶](https://flask.palletsprojects.com/en/stable/api/#test-cli-runner "Link to this heading")

_class_ flask.testing.FlaskCliRunner(_app_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner "Link to this definition")

A [`CliRunner`](https://click.palletsprojects.com/en/stable/api/#click.testing.CliRunner "\(in Click v8.3.x\)") for testing a Flask app’s CLI commands. Typically created using [`test_cli_runner()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner "flask.Flask.test_cli_runner"). See [Running Commands with the CLI Runner](https://flask.palletsprojects.com/en/stable/testing/#testing-cli).

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **kwargs** (_t.Any_)



invoke(_cli =None_, _args =None_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner.invoke "Link to this definition")

Invokes a CLI command in an isolated environment. See [`CliRunner.invoke`](https://click.palletsprojects.com/en/stable/api/#click.testing.CliRunner.invoke "\(in Click v8.3.x\)") for full method documentation. See [Running Commands with the CLI Runner](https://flask.palletsprojects.com/en/stable/testing/#testing-cli) for examples.
If the `obj` argument is not given, passes an instance of [`ScriptInfo`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo "flask.cli.ScriptInfo") that knows how to load the Flask app being tested.

Parameters:

  * **cli** (`cli` group.
  * **args** (
  * **kwargs** (



Returns:

a [`Result`](https://click.palletsprojects.com/en/stable/api/#click.testing.Result "\(in Click v8.3.x\)") object.

Return type:

[_Result_](https://click.palletsprojects.com/en/stable/api/#click.testing.Result "\(in Click v8.3.x\)")
