# create /usr/src/app/rel/test.txt
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") test.txt rel/
```

If destination doesn't exist, it's created, along with all missing directories in its path.
If the source is a file, and the destination doesn't end with a trailing slash, the source file will be written to the destination path as a file.
### [ADD --keep-git-dir](https://docs.docker.com/reference/dockerfile#add---keep-git-dir)
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") [--keep-git-dir=<boolean>] <src> ... <dir>
```

When `<src>` is the HTTP or SSH address of a remote Git repository, BuildKit adds the contents of the Git repository to the image excluding the `.git` directory by default.
The `--keep-git-dir=true` flag lets you preserve the `.git` directory.
```
# create /usr/src/app/rel/test.txt
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") test.txt rel/
```

If destination doesn't exist, it's created, along with all missing directories in its path.
If the source is a file, and the destination doesn't end with a trailing slash, the source file will be written to the destination path as a file.
### [COPY --from](https://docs.docker.com/reference/dockerfile#copy---from)
By default, the `COPY` instruction copies files from the build context. The `COPY --from` flag lets you copy files from an image, a build stage, or a named context instead.
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [--from=<image|stage|context>] <src> ... <dest>
```

To copy from a build stage in a [multi-stage build](https://docs.docker.com/build/building/multi-stage/), specify the name of the stage you want to copy from. You specify stage names using the `AS` keyword with the `FROM` instruction.
```
