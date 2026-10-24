[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[Debugging and Profiling](https://docs.python.org/3/library/debug.html "previous chapter")
#### Next topic
[`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Audit+events+table&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Faudit_events.html&pagesource=library%2Faudit_events.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework") |
  * [previous](https://docs.python.org/3/library/debug.html "Debugging and Profiling") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [Audit events table](https://docs.python.org/3/library/audit_events.html)
  * |
  * Theme  Auto Light Dark |


# Audit events table[¶](https://docs.python.org/3/library/audit_events.html#audit-events-table "Link to this heading")
This table contains all events raised by [`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit") or [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit") calls throughout the CPython runtime and the standard library. These calls were added in 3.8 or later (see [**PEP 578**](https://peps.python.org/pep-0578/)).
See [`sys.addaudithook()`](https://docs.python.org/3/library/sys.html#sys.addaudithook "sys.addaudithook") and [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook") for information on handling these events.
**CPython implementation detail:** This table is generated from the CPython documentation, and may not represent events raised by other implementations. See your runtime specific documentation for actual events raised.
Audit event | Arguments | References
---|---|---
_thread.start_new_thread | `function`, `args`, `kwargs` | [[1]](https://docs.python.org/3/library/_thread.html#start_new_thread)
array.__new__ | `typecode`, `initializer` | [[1]](https://docs.python.org/3/library/array.html#array.array)
builtins.breakpoint | `breakpointhook` | [[1]](https://docs.python.org/3/library/functions.html#breakpoint)
builtins.id | `id` | [[1]](https://docs.python.org/3/library/functions.html#id)
builtins.input | `prompt` | [[1]](https://docs.python.org/3/library/functions.html#input)
builtins.input/result | `result` | [[1]](https://docs.python.org/3/library/functions.html#input)
code.__new__ | `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags` | [[1]](https://docs.python.org/3/library/types.html#types.CodeType)
compile | `source`, `filename` | [[1]](https://docs.python.org/3/library/functions.html#compile)
cpython.PyConfig_Set | `name`, `value` | [[1]](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Set)
cpython.PyInterpreterState_Clear |  | [[1]](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_Clear)
cpython.PyInterpreterState_New |  | [[1]](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_New)
cpython._PySys_ClearAuditHooks |  | [[1]](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx)
cpython.remote_debugger_script | `script_path` | [[1]](https://docs.python.org/3/library/sys.html#audit_event_cpython_remote_debugger_script_0)
cpython.run_command | `command` | [[1]](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
cpython.run_file | `filename` | [[1]](https://docs.python.org/3/using/cmdline.html#audit_event_cpython_run_file_0)
cpython.run_interactivehook | `hook` | [[1]](https://docs.python.org/3/library/sys.html#sys.__interactivehook__)
cpython.run_module | `module-name` | [[1]](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
cpython.run_startup | `filename` | [[1]](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)
cpython.run_stdin |  | [[1]](https://docs.python.org/3/library/asyncio.html#audit_event_cpython_run_stdin_2)[[2]](https://docs.python.org/3/using/cmdline.html#audit_event_cpython_run_stdin_0)[[3]](https://docs.python.org/3/using/cmdline.html#audit_event_cpython_run_stdin_1)
ctypes.addressof | `obj` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.addressof)
ctypes.call_function | `func_pointer`, `arguments` | [[1]](https://docs.python.org/3/library/ctypes.html#foreign-functions)
ctypes.cdata | `address` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address)
ctypes.cdata/buffer | `pointer`, `size`, `offset` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer)[[2]](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer_copy)
ctypes.create_string_buffer | `init`, `size` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer)
ctypes.create_unicode_buffer | `init`, `size` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.create_unicode_buffer)
ctypes.dlopen | `name` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader)
ctypes.dlsym | `library`, `name` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader)
ctypes.dlsym/handle | `handle`, `name` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader)
ctypes.get_errno |  | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno)
ctypes.get_last_error |  | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error)
ctypes.memoryview_at | `address`, `size`, `readonly` | [[1]](https://docs.python.org/3/library/ctypes.html#audit_event_ctypes_memoryview_at_0)
ctypes.set_errno | `errno` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno)
ctypes.set_exception | `code` | [[1]](https://docs.python.org/3/library/ctypes.html#foreign-functions)
ctypes.set_last_error | `error` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error)
ctypes.string_at | `ptr`, `size` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.string_at)
ctypes.wstring_at | `ptr`, `size` | [[1]](https://docs.python.org/3/library/ctypes.html#ctypes.wstring_at)
ensurepip.bootstrap | `root` | [[1]](https://docs.python.org/3/library/ensurepip.html#ensurepip.bootstrap)
exec | `code_object` | [[1]](https://docs.python.org/3/library/functions.html#eval)[[2]](https://docs.python.org/3/library/functions.html#exec)
fcntl.fcntl | `fd`, `cmd`, `arg` | [[1]](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl)
fcntl.flock | `fd`, `operation` | [[1]](https://docs.python.org/3/library/fcntl.html#fcntl.flock)
fcntl.ioctl | `fd`, `request`, `arg` | [[1]](https://docs.python.org/3/library/fcntl.html#fcntl.ioctl)
fcntl.lockf | `fd`, `cmd`, `len`, `start`, `whence` | [[1]](https://docs.python.org/3/library/fcntl.html#fcntl.lockf)
ftplib.connect | `self`, `host`, `port` | [[1]](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.connect)
ftplib.sendcmd | `self`, `cmd` | [[1]](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.sendcmd)[[2]](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.voidcmd)
function.__new__ | `code` | [[1]](https://docs.python.org/3/library/types.html#types.FunctionType)
gc.get_objects | `generation` | [[1]](https://docs.python.org/3/library/gc.html#gc.get_objects)
gc.get_referents | `objs` | [[1]](https://docs.python.org/3/library/gc.html#gc.get_referents)
gc.get_referrers | `objs` | [[1]](https://docs.python.org/3/library/gc.html#gc.get_referrers)
glob.glob | `pathname`, `recursive` | [[1]](https://docs.python.org/3/library/glob.html#glob.glob)[[2]](https://docs.python.org/3/library/glob.html#glob.iglob)
glob.glob/2 | `pathname`, `recursive`, `root_dir`, `dir_fd` | [[1]](https://docs.python.org/3/library/glob.html#glob.glob)[[2]](https://docs.python.org/3/library/glob.html#glob.iglob)
http.client.connect | `self`, `host`, `port` | [[1]](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.connect)
http.client.send | `self`, `data` | [[1]](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.send)
imaplib.open | `self`, `host`, `port` | [[1]](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.open)
imaplib.send | `self`, `data` | [[1]](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.send)
import | `module`, `filename`, `sys.path`, `sys.meta_path`, `sys.path_hooks` | [[1]](https://docs.python.org/3/reference/simple_stmts.html#import)
marshal.dumps | `value`, `version` | [[1]](https://docs.python.org/3/library/marshal.html#marshal.dump)
marshal.load |  | [[1]](https://docs.python.org/3/library/marshal.html#marshal.load)
marshal.loads | `bytes` | [[1]](https://docs.python.org/3/library/marshal.html#marshal.load)
mmap.__new__ | `fileno`, `length`, `access`, `offset` | [[1]](https://docs.python.org/3/library/mmap.html#mmap.mmap)
msvcrt.get_osfhandle | `fd` | [[1]](https://docs.python.org/3/library/msvcrt.html#msvcrt.get_osfhandle)
msvcrt.locking | `fd`, `mode`, `nbytes` | [[1]](https://docs.python.org/3/library/msvcrt.html#msvcrt.locking)
msvcrt.open_osfhandle | `handle`, `flags` | [[1]](https://docs.python.org/3/library/msvcrt.html#msvcrt.open_osfhandle)
object.__delattr__ | `obj`, `name` | [[1]](https://docs.python.org/3/reference/datamodel.html#object.__delattr__)
object.__getattr__ | `obj`, `name` | [[1]](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__)
object.__setattr__ | `obj`, `name`, `value` | [[1]](https://docs.python.org/3/reference/datamodel.html#object.__setattr__)
open | `path`, `mode`, `flags` | [[1]](https://docs.python.org/3/library/functions.html#open)[[2]](https://docs.python.org/3/library/io.html#io.open)[[3]](https://docs.python.org/3/library/os.html#os.open)
os.add_dll_directory | `path` | [[1]](https://docs.python.org/3/library/os.html#os.add_dll_directory)
os.chdir | `path` | [[1]](https://docs.python.org/3/library/os.html#os.chdir)[[2]](https://docs.python.org/3/library/os.html#os.fchdir)
os.chflags | `path`, `flags` | [[1]](https://docs.python.org/3/library/os.html#os.chflags)[[2]](https://docs.python.org/3/library/os.html#os.lchflags)
os.chmod | `path`, `mode`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.chmod)[[2]](https://docs.python.org/3/library/os.html#os.fchmod)[[3]](https://docs.python.org/3/library/os.html#os.lchmod)
os.chown | `path`, `uid`, `gid`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.chown)[[2]](https://docs.python.org/3/library/os.html#os.fchown)[[3]](https://docs.python.org/3/library/os.html#os.lchown)
os.exec | `path`, `args`, `env` | [[1]](https://docs.python.org/3/library/os.html#os.execl)
os.fork |  | [[1]](https://docs.python.org/3/library/os.html#os.fork)
os.forkpty |  | [[1]](https://docs.python.org/3/library/os.html#os.forkpty)
os.fwalk | `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.fwalk)
os.getxattr | `path`, `attribute` | [[1]](https://docs.python.org/3/library/os.html#os.getxattr)
os.kill | `pid`, `sig` | [[1]](https://docs.python.org/3/library/os.html#os.kill)
os.killpg | `pgid`, `sig` | [[1]](https://docs.python.org/3/library/os.html#os.killpg)
os.link | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.link)
os.listdir | `path` | [[1]](https://docs.python.org/3/library/os.html#os.listdir)
os.listdrives |  | [[1]](https://docs.python.org/3/library/os.html#os.listdrives)
os.listmounts | `volume` | [[1]](https://docs.python.org/3/library/os.html#os.listmounts)
os.listvolumes |  | [[1]](https://docs.python.org/3/library/os.html#os.listvolumes)
os.listxattr | `path` | [[1]](https://docs.python.org/3/library/os.html#os.listxattr)
os.lockf | `fd`, `cmd`, `len` | [[1]](https://docs.python.org/3/library/os.html#os.lockf)
os.mkdir | `path`, `mode`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.makedirs)[[2]](https://docs.python.org/3/library/os.html#os.mkdir)
os.posix_spawn | `path`, `argv`, `env` | [[1]](https://docs.python.org/3/library/os.html#os.posix_spawn)[[2]](https://docs.python.org/3/library/os.html#os.posix_spawnp)
os.putenv | `key`, `value` | [[1]](https://docs.python.org/3/library/os.html#os.putenv)
os.remove | `path`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.remove)[[2]](https://docs.python.org/3/library/os.html#os.removedirs)[[3]](https://docs.python.org/3/library/os.html#os.unlink)
os.removexattr | `path`, `attribute` | [[1]](https://docs.python.org/3/library/os.html#os.removexattr)
os.rename | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.rename)[[2]](https://docs.python.org/3/library/os.html#os.renames)[[3]](https://docs.python.org/3/library/os.html#os.replace)
os.rmdir | `path`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.rmdir)
os.scandir | `path` | [[1]](https://docs.python.org/3/library/os.html#os.scandir)
os.setxattr | `path`, `attribute`, `value`, `flags` | [[1]](https://docs.python.org/3/library/os.html#os.setxattr)
os.spawn | `mode`, `path`, `args`, `env` | [[1]](https://docs.python.org/3/library/os.html#os.spawnl)
os.startfile | `path`, `operation` | [[1]](https://docs.python.org/3/library/os.html#os.startfile)
os.startfile/2 | `path`, `operation`, `arguments`, `cwd`, `show_cmd` | [[1]](https://docs.python.org/3/library/os.html#os.startfile)
os.symlink | `src`, `dst`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.symlink)
os.system | `command` | [[1]](https://docs.python.org/3/library/os.html#os.system)
os.truncate | `fd`, `length` | [[1]](https://docs.python.org/3/library/os.html#os.ftruncate)[[2]](https://docs.python.org/3/library/os.html#os.truncate)
os.unsetenv | `key` | [[1]](https://docs.python.org/3/library/os.html#os.unsetenv)
os.utime | `path`, `times`, `ns`, `dir_fd` | [[1]](https://docs.python.org/3/library/os.html#os.utime)
os.walk | `top`, `topdown`, `onerror`, `followlinks` | [[1]](https://docs.python.org/3/library/os.html#os.walk)
pathlib.Path.glob | `self`, `pattern` | [[1]](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob)
pathlib.Path.rglob | `self`, `pattern` | [[1]](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob)
pdb.Pdb |  | [[1]](https://docs.python.org/3/library/pdb.html#pdb.Pdb)
pickle.find_class | `module`, `name` | [[1]](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.find_class)
poplib.connect | `self`, `host`, `port` | [[1]](https://docs.python.org/3/library/poplib.html#poplib.POP3)[[2]](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL)
poplib.putline | `self`, `line` | [[1]](https://docs.python.org/3/library/poplib.html#poplib.POP3)[[2]](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL)
pty.spawn | `argv` | [[1]](https://docs.python.org/3/library/pty.html#pty.spawn)
resource.prlimit | `pid`, `resource`, `limits` | [[1]](https://docs.python.org/3/library/resource.html#resource.prlimit)
resource.setrlimit | `resource`, `limits` | [[1]](https://docs.python.org/3/library/resource.html#resource.setrlimit)
setopencodehook |  | [[1]](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook)
shutil.chown | `path`, `user`, `group` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.chown)
shutil.copyfile | `src`, `dst` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.copy)[[2]](https://docs.python.org/3/library/shutil.html#shutil.copy2)[[3]](https://docs.python.org/3/library/shutil.html#shutil.copyfile)
shutil.copymode | `src`, `dst` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.copy)[[2]](https://docs.python.org/3/library/shutil.html#shutil.copymode)
shutil.copystat | `src`, `dst` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.copy2)[[2]](https://docs.python.org/3/library/shutil.html#shutil.copystat)
shutil.copytree | `src`, `dst` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.copytree)
shutil.make_archive | `base_name`, `format`, `root_dir`, `base_dir` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.make_archive)
shutil.move | `src`, `dst` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.move)
shutil.rmtree | `path`, `dir_fd` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.rmtree)
shutil.unpack_archive | `filename`, `extract_dir`, `format` | [[1]](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive)
signal.pthread_kill | `thread_id`, `signalnum` | [[1]](https://docs.python.org/3/library/signal.html#signal.pthread_kill)
smtplib.connect | `self`, `host`, `port` | [[1]](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.connect)
smtplib.send | `self`, `data` | [[1]](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP)
socket.__new__ | `self`, `family`, `type`, `protocol` | [[1]](https://docs.python.org/3/library/socket.html#socket.socket)
socket.bind | `self`, `address` | [[1]](https://docs.python.org/3/library/socket.html#socket.socket.bind)
socket.connect | `self`, `address` | [[1]](https://docs.python.org/3/library/socket.html#socket.socket.connect)[[2]](https://docs.python.org/3/library/socket.html#socket.socket.connect_ex)
socket.getaddrinfo | `host`, `port`, `family`, `type`, `protocol` | [[1]](https://docs.python.org/3/library/socket.html#socket.getaddrinfo)
socket.gethostbyaddr | `ip_address` | [[1]](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr)
socket.gethostbyname | `hostname` | [[1]](https://docs.python.org/3/library/socket.html#socket.gethostbyname)[[2]](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex)
socket.gethostname |  | [[1]](https://docs.python.org/3/library/socket.html#socket.gethostname)
socket.getnameinfo | `sockaddr` | [[1]](https://docs.python.org/3/library/socket.html#socket.getnameinfo)
socket.getservbyname | `servicename`, `protocolname` | [[1]](https://docs.python.org/3/library/socket.html#socket.getservbyname)
socket.getservbyport | `port`, `protocolname` | [[1]](https://docs.python.org/3/library/socket.html#socket.getservbyport)
socket.sendmsg | `self`, `address` | [[1]](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg)
socket.sendto | `self`, `address` | [[1]](https://docs.python.org/3/library/socket.html#socket.socket.sendto)
socket.sethostname | `name` | [[1]](https://docs.python.org/3/library/socket.html#socket.sethostname)
sqlite3.connect | `database` | [[1]](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)
sqlite3.connect/handle | `connection_handle` | [[1]](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)
sqlite3.enable_load_extension | `connection`, `enabled` | [[1]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension)
sqlite3.load_extension | `connection`, `path` | [[1]](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.load_extension)
subprocess.Popen | `executable`, `args`, `cwd`, `env` | [[1]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen)
sys._current_exceptions |  | [[1]](https://docs.python.org/3/library/sys.html#sys._current_exceptions)
sys._current_frames |  | [[1]](https://docs.python.org/3/library/sys.html#sys._current_frames)
sys._getframe | `frame` | [[1]](https://docs.python.org/3/library/sys.html#sys._getframe)
sys._getframemodulename | `depth` | [[1]](https://docs.python.org/3/library/sys.html#sys._getframemodulename)
sys.addaudithook |  | [[1]](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook)[[2]](https://docs.python.org/3/library/sys.html#sys.addaudithook)
sys.excepthook | `hook`, `type`, `value`, `traceback` | [[1]](https://docs.python.org/3/library/sys.html#sys.excepthook)
sys.monitoring.register_callback | `func` | [[1]](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.register_callback)
sys.remote_exec | `pid` | [[1]](https://docs.python.org/3/library/sys.html#script_path)
sys.set_asyncgen_hooks_finalizer |  | [[1]](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks)
sys.set_asyncgen_hooks_firstiter |  | [[1]](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks)
sys.setprofile |  | [[1]](https://docs.python.org/3/library/sys.html#sys.setprofile)
sys.settrace |  | [[1]](https://docs.python.org/3/library/sys.html#sys.settrace)
sys.unraisablehook | `hook`, `unraisable` | [[1]](https://docs.python.org/3/library/sys.html#sys.unraisablehook)
syslog.closelog |  | [[1]](https://docs.python.org/3/library/syslog.html#syslog.closelog)
syslog.openlog | `ident`, `logoption`, `facility` | [[1]](https://docs.python.org/3/library/syslog.html#syslog.openlog)
syslog.setlogmask | `maskpri` | [[1]](https://docs.python.org/3/library/syslog.html#syslog.setlogmask)
syslog.syslog | `priority`, `message` | [[1]](https://docs.python.org/3/library/syslog.html#syslog.syslog)
tempfile.mkdtemp | `fullpath` | [[1]](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory)[[2]](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp)
tempfile.mkstemp | `fullpath` | [[1]](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)[[2]](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile)[[3]](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp)
time.sleep | `secs` | [[1]](https://docs.python.org/3/library/time.html#audit_event_time_sleep_0)
urllib.Request | `fullurl`, `data`, `headers`, `method` | [[1]](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen)
webbrowser.open | `url` | [[1]](https://docs.python.org/3/library/webbrowser.html#webbrowser.open)
winreg.ConnectRegistry | `computer_name`, `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.ConnectRegistry)
winreg.CreateKey | `key`, `sub_key`, `access` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.CreateKey)[[2]](https://docs.python.org/3/library/winreg.html#winreg.CreateKeyEx)
winreg.DeleteKey | `key`, `sub_key`, `access` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.DeleteKey)[[2]](https://docs.python.org/3/library/winreg.html#winreg.DeleteKeyEx)
winreg.DeleteValue | `key`, `value` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.DeleteValue)
winreg.DisableReflectionKey | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.DisableReflectionKey)
winreg.EnableReflectionKey | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.EnableReflectionKey)
winreg.EnumKey | `key`, `index` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.EnumKey)
winreg.EnumValue | `key`, `index` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.EnumValue)
winreg.ExpandEnvironmentStrings | `str` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.ExpandEnvironmentStrings)
winreg.LoadKey | `key`, `sub_key`, `file_name` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.LoadKey)
winreg.OpenKey | `key`, `sub_key`, `access` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.OpenKey)
winreg.OpenKey/result | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.CreateKey)[[2]](https://docs.python.org/3/library/winreg.html#winreg.CreateKeyEx)[[3]](https://docs.python.org/3/library/winreg.html#winreg.OpenKey)
winreg.PyHKEY.Detach | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Detach)
winreg.QueryInfoKey | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.QueryInfoKey)
winreg.QueryReflectionKey | `key` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.QueryReflectionKey)
winreg.QueryValue | `key`, `sub_key`, `value_name` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.QueryValue)[[2]](https://docs.python.org/3/library/winreg.html#winreg.QueryValueEx)
winreg.SaveKey | `key`, `file_name` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.SaveKey)
winreg.SetValue | `key`, `sub_key`, `type`, `value` | [[1]](https://docs.python.org/3/library/winreg.html#winreg.SetValue)[[2]](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx)
The following events are raised internally and do not correspond to any public API of CPython:
Audit event | Arguments
---|---
_winapi.CreateFile | `file_name`, `desired_access`, `share_mode`, `creation_disposition`, `flags_and_attributes`
_winapi.CreateJunction | `src_path`, `dst_path`
_winapi.CreateNamedPipe | `name`, `open_mode`, `pipe_mode`
_winapi.CreatePipe |
_winapi.CreateProcess | `application_name`, `command_line`, `current_directory`
_winapi.OpenProcess | `process_id`, `desired_access`
_winapi.TerminateProcess | `handle`, `exit_code`
_posixsubprocess.fork_exec | `exec_list`, `args`, `env`
ctypes.PyObj_FromPtr | `obj`
Added in version 3.14: The `_posixsubprocess.fork_exec` internal audit event.
#### Previous topic
[Debugging and Profiling](https://docs.python.org/3/library/debug.html "previous chapter")
#### Next topic
[`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Audit+events+table&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Faudit_events.html&pagesource=library%2Faudit_events.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework") |
  * [previous](https://docs.python.org/3/library/debug.html "Debugging and Profiling") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [Audit events table](https://docs.python.org/3/library/audit_events.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
