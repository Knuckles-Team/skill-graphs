## Introduction[¶](https://docs.python.org/3/library/optparse.html#introduction "Link to this heading")
`optparse` is a more convenient, flexible, and powerful library for parsing command-line options than the minimalist [`getopt`](https://docs.python.org/3/library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names.") module. `optparse` uses a more declarative style of command-line parsing: you create an instance of [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser"), populate it with options, and parse the command line. `optparse` allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
Here’s an example of using `optparse` in a simple script:
Copy```
from optparse import OptionParser
...
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

```

With these few lines of code, users of your script can now do the “usual thing” on the command-line, for example:
Copy```
<yourscript> --file=outfile -q

```

As it parses the command line, `optparse` sets attributes of the `options` object returned by [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") based on user-supplied command-line values. When `parse_args()` returns from parsing this command line, `options.filename` will be `"outfile"` and `options.verbose` will be `False`. `optparse` supports both long and short options, allows short options to be merged together, and allows options to be associated with their arguments in a variety of ways. Thus, the following command lines are all equivalent to the above example:
Copy```
<yourscript> -f outfile --quiet
<yourscript> --quiet --file outfile
<yourscript> -q -foutfile
<yourscript> -qfoutfile

```

Additionally, users can run one of the following
Copy```
<yourscript> -h
<yourscript> --help

```

and `optparse` will print out a brief summary of your script’s options:
```
Usage: <yourscript> [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  write report to FILE
  -q, --quiet           don't print status messages to stdout

```

where the value of _yourscript_ is determined at runtime (normally from `sys.argv[0]`).
