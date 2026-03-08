# escape=\
```

Or
```
# escape=`
```

The `escape` directive sets the character used to escape characters in a Dockerfile. If not specified, the default escape character is `\`.
The escape character is used both to escape characters in a line, and to escape a newline. This allows a Dockerfile instruction to span multiple lines. Note that regardless of whether the `escape` parser directive is included in a Dockerfile, escaping is not performed in a `RUN` command, except at the end of a line.
Setting the escape character to ``` is especially useful on `Windows`, where `\` is the directory path separator. ``` is consistent with
Consider the following example which would fail in a non-obvious way on Windows. The second `\` at the end of the second line would be interpreted as an escape for the newline, instead of a target of the escape from the first `\`. Similarly, the `\` at the end of the third line would, assuming it was actually handled as an instruction, cause it be treated as a line continuation. The result of this Dockerfile is that second and third lines are considered a single instruction:
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") microsoft/nanoserver
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") testfile.txt c:\\
RUN dir c:\
```

Results in:
```
PS E:\myproject> docker build -t cmd .

Sending build context to Docker daemon 3.072 kB
Step 1/2 : FROM microsoft/nanoserver
 ---> 22738ff49c6d
Step 2/2 : COPY testfile.txt c:\RUN dir c:
GetFileAttributesEx c:RUN: The system cannot find the file specified.
PS E:\myproject>

```

One solution to the above would be to use `/` as the target of both the `COPY` instruction, and `dir`. However, this syntax is, at best, confusing as it is not natural for paths on Windows, and at worst, error prone as not all commands on Windows support `/` as the path separator.
By adding the `escape` parser directive, the following Dockerfile succeeds as expected with the use of natural platform semantics for file paths on Windows:
```
# escape=`

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") microsoft/nanoserver
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") testfile.txt c:\
RUN dir c:\
```

Results in:
```
PS E:\myproject> docker build -t succeeds --no-cache=true .

Sending build context to Docker daemon 3.072 kB
Step 1/3 : FROM microsoft/nanoserver
 ---> 22738ff49c6d
Step 2/3 : COPY testfile.txt c:\
 ---> 96655de338de
Removing intermediate container 4db9acbb1682
Step 3/3 : RUN dir c:\
 ---> Running in a2c157f842f5
 Volume in drive C has no label.
 Volume Serial Number is 7E6D-E0F7

 Directory of c:\

10/05/2016  05:04 PM             1,894 License.txt
10/05/2016  02:22 PM    DIR          Program Files
10/05/2016  02:14 PM    DIR          Program Files (x86)
10/28/2016  11:18 AM                62 testfile.txt
10/28/2016  11:20 AM    DIR          Users
10/28/2016  11:20 AM    DIR          Windows
           2 File(s)          1,956 bytes
           4 Dir(s)  21,259,096,064 bytes free
 ---> 01c7f3bef04f
Removing intermediate container a2c157f842f5
Successfully built 01c7f3bef04f
PS E:\myproject>

```

### [check](https://docs.docker.com/reference/dockerfile#check)
```
