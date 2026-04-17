## Permissions
A `bcp out` operation requires `SELECT` permission on the source table.
A `bcp in` operation minimally requires `SELECT`/`INSERT` permissions on the target table. In addition, `ALTER TABLE` permission is required if any of the following conditions are true:
  * Constraints exist and the `CHECK_CONSTRAINTS` hint isn't specified.
Disabling constraints is the default behavior. To enable constraints explicitly, use the `-h` option with the `CHECK_CONSTRAINTS` hint.
  * Triggers exist and the `FIRE_TRIGGER` hint isn't specified.
By default, triggers aren't fired. To fire triggers explicitly, use the `-h` option with the `FIRE_TRIGGERS` hint.
  * You use the `-E` option to import identity values from a data file.


Requiring `ALTER TABLE` permission on the target table was introduced in SQL Server 2005 (9.x). This requirement can cause **bcp** scripts that don't enforce triggers and constraint checks to fail if the user account lacks `ALTER TABLE` permissions for the target table.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#character-mode--c-and-native-mode--n-best-practices)
