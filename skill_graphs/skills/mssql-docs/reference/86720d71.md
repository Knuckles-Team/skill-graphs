## Syntax
Console
Copy
```
bcp [database_name.] schema.{table_name | view_name | "query"}
    {in data_file | out data_file | queryout data_file | format nul}

    [-a packet_size]
    [-b batch_size]
    [-c]
    [-C { ACP | OEM | RAW | code_page } ]
    [-d database_name]
    [-D]
    [-e err_file]
    [-E]
    [-f format_file]
    [-F first_row]
    [-G Microsoft Entra authentication]
    [-h"hint [,...n]"]
    [-i input_file]
    [-k]
    [-K application_intent]
    [-l login_timeout]
    [-L last_row]
    [-m max_errors]
    [-n]
    [-N]
    [-o output_file]
    [-P password]
    [-q]
    [-r row_term]
    [-R]
    [-S [server_name[\instance_name]]]
    [-t field_term]
    [-T]
    [-U login_id]
    [-u]
    [-v]
    [-V (80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170)]
    [-w]
    [-x]
    [-Y[s|m|o]]
    [-z]

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#considerations-and-limitations)
