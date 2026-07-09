# create /abs/test.txt
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") test.txt /abs/
```

Trailing slashes are significant. For example, `ADD test.txt /abs` creates a file at `/abs`, whereas `ADD test.txt /abs/` creates `/abs/test.txt`.
If the destination path doesn't begin with a leading slash, it's interpreted as relative to the working directory of the build container.
```
[WORKDIR](https://docs.docker.com/reference/dockerfile/#workdir "Learn more about the WORKDIR instruction") /usr/src/app
# create /abs/test.txt
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") test.txt /abs/
```

Trailing slashes are significant. For example, `COPY test.txt /abs` creates a file at `/abs`, whereas `COPY test.txt /abs/` creates `/abs/test.txt`.
If the destination path doesn't begin with a leading slash, it's interpreted as relative to the working directory of the build container.
```
[WORKDIR](https://docs.docker.com/reference/dockerfile/#workdir "Learn more about the WORKDIR instruction") /usr/src/app
