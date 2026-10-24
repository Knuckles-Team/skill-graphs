#  `test.support.script_helper` — Utilities for the Python execution tests[¶](https://docs.python.org/3/library/test.html#module-test.support.script_helper "Link to this heading")
The `test.support.script_helper` module provides support for Python’s script execution tests.

test.support.script_helper.interpreter_requires_environment()[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.interpreter_requires_environment "Link to this definition")

Return `True` if `sys.executable interpreter` requires environment variables in order to be able to run at all.
This is designed to be used with `@unittest.skipIf()` to annotate tests that need to use an `assert_python*()` function to launch an isolated mode (`-I`) or no environment mode (`-E`) sub-interpreter process.
A normal build & test does not run into this situation but it can happen when trying to run the standard library test suite from an interpreter that doesn’t have an obvious home with Python’s current home finding logic.
Setting [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME) is one way to get most of the testsuite to run in that situation. [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) or `PYTHONUSERSITE` are other common environment variables that might impact whether or not the interpreter can start.

test.support.script_helper.run_python_until_end(_* args_, _** env_vars_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.run_python_until_end "Link to this definition")

Set up the environment based on _env_vars_ for running the interpreter in a subprocess. The values can include `__isolated`, `__cleanenv`, `__cwd`, and `TERM`.
Changed in version 3.9: The function no longer strips whitespaces from _stderr_.

test.support.script_helper.assert_python_ok(_* args_, _** env_vars_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.assert_python_ok "Link to this definition")

Assert that running the interpreter with _args_ and optional environment variables _env_vars_ succeeds (`rc == 0`) and return a `(return code, stdout, stderr)` tuple.
If the ___cleanenv_ keyword-only parameter is set, _env_vars_ is used as a fresh environment.
Python is started in isolated mode (command line option `-I`), except if the ___isolated_ keyword-only parameter is set to `False`.
Changed in version 3.9: The function no longer strips whitespaces from _stderr_.

test.support.script_helper.assert_python_failure(_* args_, _** env_vars_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.assert_python_failure "Link to this definition")

Assert that running the interpreter with _args_ and optional environment variables _env_vars_ fails (`rc != 0`) and return a `(return code, stdout, stderr)` tuple.
See [`assert_python_ok()`](https://docs.python.org/3/library/test.html#test.support.script_helper.assert_python_ok "test.support.script_helper.assert_python_ok") for more options.
Changed in version 3.9: The function no longer strips whitespaces from _stderr_.

test.support.script_helper.spawn_python(_* args_, _stdout =subprocess.PIPE_, _stderr =subprocess.STDOUT_, _** kw_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.spawn_python "Link to this definition")

Run a Python subprocess with the given arguments.
_kw_ is extra keyword args to pass to [`subprocess.Popen()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen"). Returns a [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") object.

test.support.script_helper.kill_python(_p_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.kill_python "Link to this definition")

Run the given [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") process until completion and return stdout.

test.support.script_helper.make_script(_script_dir_ , _script_basename_ , _source_ , _omit_suffix =False_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.make_script "Link to this definition")

Create script containing _source_ in path _script_dir_ and _script_basename_. If _omit_suffix_ is `False`, append `.py` to the name. Return the full script path.

test.support.script_helper.make_zip_script(_zip_dir_ , _zip_basename_ , _script_name_ , _name_in_zip =None_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.make_zip_script "Link to this definition")

Create zip file at _zip_dir_ and _zip_basename_ with extension `zip` which contains the files in _script_name_. _name_in_zip_ is the archive name. Return a tuple containing `(full path, full path of archive name)`.

test.support.script_helper.make_pkg(_pkg_dir_ , _init_source =''_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.make_pkg "Link to this definition")

Create a directory named _pkg_dir_ containing an `__init__` file with _init_source_ as its contents.

test.support.script_helper.make_zip_pkg(_zip_dir_ , _zip_basename_ , _pkg_name_ , _script_basename_ , _source_ , _depth =1_, _compiled =False_)[¶](https://docs.python.org/3/library/test.html#test.support.script_helper.make_zip_pkg "Link to this definition")

Create a zip package directory with a path of _zip_dir_ and _zip_basename_ containing an empty `__init__` file and a file _script_basename_ containing the _source_. If _compiled_ is `True`, both source files will be compiled and added to the zip package. Return a tuple of the full zip path and the archive name for the zip file.
