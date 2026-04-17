## Code transformation tool[¶](https://docs.pydantic.dev/latest/migration/#code-transformation-tool)
We have created a tool to help you migrate your code. This tool is still in beta, but we hope it will help you to migrate your code more quickly.
You can install the tool from PyPI:
```
pip install bump-pydantic

```

The usage is simple. If your project structure is:
```
* repo_folder
    * my_package
        * <python source files> ...

```

Then you'll want to do:
```
cd /path/to/repo_folder
bump-pydantic my_package

```

See more about it on the
