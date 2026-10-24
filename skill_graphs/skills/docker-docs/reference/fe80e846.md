# /parents/y/a.txt
```

This behavior is similar to the `--parents` or `--relative` flag.
As with Rsync, it is possible to limit which parent directories are preserved by inserting a dot and a slash (`./`) into the source path. If such point exists, only parent directories after it will be preserved. This may be especially useful copies between stages with `--from` where the source paths need to be absolute.
```
