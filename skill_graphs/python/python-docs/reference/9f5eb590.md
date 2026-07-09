## Replacing Older Functions with the `subprocess` Module[¶](https://docs.python.org/3/library/subprocess.html#replacing-older-functions-with-the-subprocess-module "Link to this heading")
In this section, “a becomes b” means that b can be used as a replacement for a.
Note
All “a” functions in this section fail (more or less) silently if the executed program cannot be found; the “b” replacements raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead.
In addition, the replacements using [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output") will fail with a [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError") if the requested operation produces a non-zero return code. The output is still available as the [`output`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.output "subprocess.CalledProcessError.output") attribute of the raised exception.
In the following examples, we assume that the relevant functions have already been imported from the `subprocess` module.
### Replacing **/bin/sh** shell command substitution[¶](https://docs.python.org/3/library/subprocess.html#replacing-bin-sh-shell-command-substitution "Link to this heading")
Copy```
output=$(mycmd myarg)

```

becomes:
Copy```
output = check_output(["mycmd", "myarg"])

```

### Replacing shell pipeline[¶](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline "Link to this heading")
Copy```
output=$(dmesg | grep had)

```

becomes:
Copy```
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "had"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]

```

The `p1.stdout.close()` call after starting the p2 is important in order for p1 to receive a SIGPIPE if p2 exits before p1.
Alternatively, for trusted input, the shell’s own pipeline support may still be used directly:
Copy```
output=$(dmesg | grep had)

```

becomes:
Copy```
output = check_output("dmesg | grep had", shell=True)

```

### Replacing [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system")[¶](https://docs.python.org/3/library/subprocess.html#replacing-os-system "Link to this heading")
Copy```
sts = os.system("mycmd" + " myarg")
