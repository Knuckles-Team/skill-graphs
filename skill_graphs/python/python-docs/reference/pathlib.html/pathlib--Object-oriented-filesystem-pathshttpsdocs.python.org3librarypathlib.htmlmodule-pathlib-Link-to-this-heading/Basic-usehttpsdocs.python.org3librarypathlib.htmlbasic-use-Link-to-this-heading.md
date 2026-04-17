## Basic use[¶](https://docs.python.org/3/library/pathlib.html#basic-use "Link to this heading")
Importing the main class:
Copy```
>>> from pathlib import Path

```

Listing subdirectories:
Copy```
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()]
[PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
 PosixPath('__pycache__'), PosixPath('build')]

```

Listing Python source files in this directory tree:
Copy```
>>> list(p.glob('**/*.py'))
[PosixPath('test_pathlib.py'), PosixPath('setup.py'),
 PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
 PosixPath('build/lib/pathlib.py')]

```

Navigating inside a directory tree:
Copy```
>>> p = Path('/etc')
>>> q = p / 'init.d' / 'reboot'
>>> q
PosixPath('/etc/init.d/reboot')
>>> q.resolve()
PosixPath('/etc/rc.d/init.d/halt')

```

Querying path properties:
Copy```
>>> q.exists()
True
>>> q.is_dir()
False

```

Opening a file:
Copy```
>>> with q.open() as f: f.readline()
...
'#!/bin/bash\n'

```
