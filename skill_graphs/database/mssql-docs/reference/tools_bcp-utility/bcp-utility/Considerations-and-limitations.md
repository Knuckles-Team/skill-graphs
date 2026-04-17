## Considerations and limitations
  * The **bcp** utility has a limitation that the error message shows only 512-byte characters. Only the first 512 bytes of the error message are displayed.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#considerations-for-bcp-on-linux-and-macos)
### Considerations for bcp on Linux and macOS
  * The field terminator is a tab (`\t`).
  * The line terminator is a newline (`\n`).
  * Character mode is the preferred format for **bcp** format files, and data files that don't contain extended characters.
  * A backslash (`\`) on a command-line argument must either be quoted or escaped. For example, to specify a newline as a custom row terminator, you must use one of the following mechanisms:
    * `-r\\n`
    * `-r"\n"`
    * `-r'\n'`


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#command-line-options)
