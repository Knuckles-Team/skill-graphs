# End /etc/sysconfig/clock`
EOF`
```

A good hint explaining how to deal with time on LFS is available at `TZ` environment variable.
##  7.6. Configuring the Linux Console
This section discusses how to configure the **console** bootscript that sets up the keyboard map and the console font. If non-ASCII characters (e.g., the British pound sign and Euro character) will not be used and the keyboard is a U.S. one, skip this section. Without the configuration file, the **console** bootscript will do nothing.
The **console** script reads the `/etc/sysconfig/console` file for configuration information. Decide which keymap and screen font will be used. Various language-specific HOWTO's can also help with this (see [_http://www.tldp.org/HOWTO/HOWTO-INDEX/other-lang.html_](http://www.tldp.org/HOWTO/HOWTO-INDEX/other-lang.html). A pre-made `/etc/sysconfig/console` file with known settings for several countries was installed with the LFS-Bootscripts package, so the relevant section can be uncommented if the country is supported. If still in doubt, look in the `/usr/share/kbd` directory for valid keymaps and screen fonts. Read `loadkeys(1)` and `setfont(8)` to determine the correct arguments for these programs. Once decided, create the configuration file with the following command:
```
`cat >/etc/sysconfig/console <<"EOF"
`KEYMAP="_`[arguments for loadkeys]`_"
FONT="_`[arguments for setfont]`_"`
EOF`
```

For example, for Spanish users who also want to use the Euro character (accessible by pressing AltGr+E), the following settings are correct:
```
`cat >/etc/sysconfig/console <<"EOF"
`KEYMAP="es euro2"
FONT="lat9-16 -u iso01"`
EOF`
```

###  Note
The `FONT` line above is correct only for the ISO 8859-15 character set. If using ISO 8859-1 and, therefore, a pound sign instead of Euro, the correct `FONT` line would be:
```
`FONT="lat1-16"`
```

If the `KEYMAP` or `FONT` variable is not set, the **console** initscript will not run the corresponding program.
In some keymaps, the Backspace and Delete keys send characters different from ones in the default keymap built into the kernel. This confuses some applications. For example, Emacs displays its help (instead of erasing the character before the cursor) when Backspace is pressed. To check if the keymap in use is affected (this works only for i386 keymaps):
```
`zgrep '\W14\W' _`[/path/to/your/keymap]`_`
```

If the keycode 14 is Backspace instead of Delete, create the following keymap snippet to fix this issue:
```
`mkdir -pv /etc/kbd && cat > /etc/kbd/bs-sends-del <<"EOF"
`                  keycode  14 = Delete Delete Delete Delete
              alt keycode  14 = Meta_Delete
        altgr alt keycode  14 = Meta_Delete
                  keycode 111 = Remove
    altgr control keycode 111 = Boot
      control alt keycode 111 = Boot
altgr control alt keycode 111 = Boot`
EOF`
```

Tell the **console** script to load this snippet after the main keymap:
```
`cat >>/etc/sysconfig/console <<"EOF"
`KEYMAP_CORRECTIONS="/etc/kbd/bs-sends-del"`
EOF`
```

To compile the keymap directly into the kernel instead of setting it every time from the **console** bootscript, follow the instructions given in [Section 8.3, “Linux-2.6.11.12.”](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-bootable-kernel "8.3. Linux-2.6.11.12") Doing this ensures that the keyboard will always work as expected, even when booting into maintenance mode (by passing _`init=/bin/sh`_ to the kernel), because the **console** bootscript will not be run in that situation. Additionally, the kernel will not set the screen font automatically. This should not pose many problems because ASCII characters will be handled correctly, and it is unlikely that a user would need to rely on non-ASCII characters while in maintenance mode.
Since the kernel will set up the keymap, it is possible to omit the `KEYMAP` variable from the `/etc/sysconfig/console` configuration file. It can also be left in place, if desired, without consequence. Keeping it could be beneficial if running several different kernels where it is difficult to ensure that the keymap is compiled into every one of them.
##  7.7. Configuring the sysklogd script
The `sysklogd` script invokes the **syslogd** program with the _`-m 0`_ option. This option turns off the periodic timestamp mark that **syslogd** writes to the log files every 20 minutes by default. If you want to turn on this periodic timestamp mark, edit the `sysklogd` script and make the changes accordingly. See **`man syslogd`** for more information.
##  7.8. Creating the /etc/inputrc File
The `inputrc` file handles keyboard mapping for specific situations. This file is the startup file used by Readline — the input-related library — used by Bash and most other shells.
Most people do not need user-specific keyboard mappings so the command below creates a global `/etc/inputrc` used by everyone who logs in. If you later decide you need to override the defaults on a per-user basis, you can create a `.inputrc` file in the user's home directory with the modified mappings.
For more information on how to edit the `inputrc` file, see **info bash** under the _Readline Init File_ section. **info readline** is also a good source of information.
Below is a generic global `inputrc` along with comments to explain what the various options do. Note that comments cannot be on the same line as commands. Create the file using the following command:
```
`cat > /etc/inputrc << "EOF"
`# Begin /etc/inputrc
