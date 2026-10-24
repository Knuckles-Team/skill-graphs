# Add local tar without unpacking:
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") --unpack=false my-archive.tar.gz .
```

### [ADD --exclude](https://docs.docker.com/reference/dockerfile#add---exclude)
See [`COPY --exclude`](https://docs.docker.com/reference/dockerfile#copy---exclude).
## [COPY](https://docs.docker.com/reference/dockerfile#copy)
COPY has two forms. The latter form is required for paths containing whitespace.
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [OPTIONS] <src> ... <dest>
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [OPTIONS] ["<src>", ... "<dest>"]
```

The available `[OPTIONS]` are:
Option | Minimum Dockerfile version
---|---
[`--from`](https://docs.docker.com/reference/dockerfile#copy---from) |
[`--chmod`](https://docs.docker.com/reference/dockerfile#copy---chmod) | 1.2
[`--chown`](https://docs.docker.com/reference/dockerfile#copy---chown) |
[`--link`](https://docs.docker.com/reference/dockerfile#copy---link) | 1.4
[`--parents`](https://docs.docker.com/reference/dockerfile#copy---parents) | 1.20
[`--exclude`](https://docs.docker.com/reference/dockerfile#copy---exclude) | 1.19
The `COPY` instruction copies new files or directories from `<src>` and adds them to the filesystem of the image at the path `<dest>`. Files and directories can be copied from the build context, build stage, named context, or an image.
The `ADD` and `COPY` instructions are functionally similar, but serve slightly different purposes. Learn more about the [differences between `ADD` and `COPY`](https://docs.docker.com/build/building/best-practices/#add-or-copy).
### [Source](https://docs.docker.com/reference/dockerfile#source-1)
You can specify multiple source files or directories with `COPY`. The last argument must always be the destination. For example, to copy two files, `file1.txt` and `file2.txt`, from the build context to `/usr/src/things/` in the build container:
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") file1.txt file2.txt /usr/src/things/
```

If you specify multiple source files, either directly or using a wildcard, then the destination must be a directory (must end with a slash `/`).
`COPY` accepts a flag `--from=<name>` that lets you specify the source location to be a build stage, context, or image. The following example copies files from a stage named `build`:
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") golang AS build
[WORKDIR](https://docs.docker.com/reference/dockerfile/#workdir "Learn more about the WORKDIR instruction") /app
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=bind,target=. go build -o /myapp ./cmd

[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --from=build /myapp /usr/bin/
```

For more information about copying from named sources, see the [`--from` flag](https://docs.docker.com/reference/dockerfile#copy---from).
#### [Copying from the build context](https://docs.docker.com/reference/dockerfile#copying-from-the-build-context)
When copying source files from the build context, paths are interpreted as relative to the root of the context.
Specifying a source path with a leading slash or one that navigates outside the build context, such as `COPY ../something /something`, automatically removes any parent directory navigation (`../`). Trailing slashes in the source path are also disregarded, making `COPY something/ /something` equivalent to `COPY something /something`.
If the source is a directory, the contents of the directory are copied, including filesystem metadata. The directory itself isn't copied, only its contents. If it contains subdirectories, these are also copied, and merged with any existing directories at the destination. Any conflicts are resolved in favor of the content being added, on a file-by-file basis, except if you're trying to copy a directory onto an existing file, in which case an error is raised.
If the source is a file, the file and its metadata are copied to the destination. File permissions are preserved. If the source is a file and a directory with the same name exists at the destination, an error is raised.
If you pass a Dockerfile through stdin to the build (`docker build - < Dockerfile`), there is no build context. In this case, you can only use the `COPY` instruction to copy files from other stages, named contexts, or images, using the [`--from` flag](https://docs.docker.com/reference/dockerfile#copy---from). You can also pass a tar archive through stdin: (`docker build - < archive.tar`), the Dockerfile at the root of the archive and the rest of the archive will be used as the context of the build.
When using a Git repository as the build context, the permissions bits for copied files are 644. If a file in the repository has the executable bit set, it will have permissions set to 755. Directories have permissions set to 755.
##### [Pattern matching](https://docs.docker.com/reference/dockerfile#pattern-matching-1)
For local files, each `<src>` may contain wildcards and matching will be done using Go's
For example, to add all files and directories in the root of the build context ending with `.png`:
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") *.png /dest/
```

In the following example, `?` is a single-character wildcard, matching e.g. `index.js` and `index.ts`.
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") index.?s /dest/
```

When adding files or directories that contain special characters (such as `[` and `]`), you need to escape those paths following the Golang rules to prevent them from being treated as a matching pattern. For example, to add a file named `arr[0].txt`, use the following;
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") arr[[]0].txt /dest/
```

### [Destination](https://docs.docker.com/reference/dockerfile#destination-1)
If the destination path begins with a forward slash, it's interpreted as an absolute path, and the source files are copied into the specified destination relative to the root of the current build stage.
```
