## Possible Ways to Fix It[](https://nextjs.org/docs/messages/conflicting-public-file-page#possible-ways-to-fix-it)
Rename either the public file or page file that is causing the conflict.
Example conflict between public file and page file
Folder structure
```
public/
  hello
pages/
  hello.js
```

Non-conflicting public file and page file
Folder structure
```
public/
  hello.txt
pages/
  hello.js
```
