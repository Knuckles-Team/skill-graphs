# directive=value
```

Treated as a comment because it appears after a comment that isn't a parser directive:
```
# directive=value
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") ImageName
```

The following `unknowndirective` is treated as a comment because it isn't recognized. The known `syntax` directive is treated as a comment because it appears after a comment that isn't a parser directive.
```
