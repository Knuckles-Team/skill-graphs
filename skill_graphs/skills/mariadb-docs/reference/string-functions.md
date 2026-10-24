# String Functions

Explore MariaDB's built-in string functions for formatting, extracting, and manipulating text data within your queries.

MariaDB has many built-in functions that can be used to manipulate strings of data. With these functions, one can format data, extract certain characters, or use search expressions. Good developers should be aware of the string functions that are available. Therefore, in this article we will go through several string functions, grouping them by similar features, and provide examples of how they might be used.

#### Formatting

There are several string functions that are used to format text and numbers for nicer display. A popular and very useful function for pasting together the contents of data fields with text is the [CONCAT()](/docs/server/reference/sql-functions/string-functions/concat) function. As an example, suppose that a table called contacts has a column for each sales contact's first name and another for the last name. The following SQL statement would put them together:

```sql
SELECT CONCAT(name_first, ' ', name_last)
AS Name
FROM contacts;
```

This statement will display the first name, a space, and then the last name together in one column. The AS clause will change the column heading of the results to Name.

A less used concatenating function is [CONCAT\_WS()](/docs/server/reference/sql-functions/string-functions/concat_ws). It will put together columns with a separator between each. This can be useful when making data available for other programs. For instance, suppose we have a program that will import data, but it requires the fields to be separated by vertical bars. We could just export the data, or we could use a [SELECT](/docs/server/reference/sql-statements/data-manipulation/selecting-data/select) statement like the one that follows in conjunction with an interface written with an API language like Perl:

```sql
SELECT CONCAT_WS('|', col1, col2, col3)
FROM table1;
```

The first element above is the separator. The remaining elements are the columns to be strung together.

If we want to format a long number with commas every three digits and a period for the decimal point (e.g., 100,000.00), we can use the function [FORMAT()](/docs/server/reference/sql-functions/string-functions/format) like so:

```sql
SELECT CONCAT('$', FORMAT(col5, 2))
FROM table3;
```

In this statement, the [CONCAT()](/docs/server/reference/sql-functions/string-functions/concat) will place a dollar sign in front of the numbers found in the `col5` column, which are formatted with commas by [FORMAT()](/docs/server/reference/sql-functions/string-functions/format). The `2` within the [FORMAT()](/docs/server/reference/sql-functions/string-functions/format) stipulates two decimal places.

Occasionally, one will want to convert the text from a column to either all upper-case letters or all lower-case letters. In the example that follows, the output of the first column is converted to upper-case and the second to lower-case:

```sql
SELECT UCASE(col1),
LCASE(col2)
FROM table4;
```

When displaying data in forms, it's sometimes useful to pad the data displayed with zeros or dots or some other filler. This can be necessary when dealing with [VARCHAR](/docs/server/reference/data-types/string-data-types/varchar) columns where the width varies to help the user to see the column limits. There are two functions that may be used for padding: [LPAD()](/docs/server/reference/sql-functions/string-functions/lpad) and [RPAD()](/docs/server/reference/sql-functions/string-functions/rpad).

```sql
SELECT RPAD(part_nbr, 8, '.') AS 'Part Nbr.',
LPAD(description, 15, '_') AS Description
FROM catalog;
```

In this SQL statement, dots are added to the right end of each part number. So a part number of "H200" will display as "H200....", but without the quotes. Each part's description will have under-scores preceding it. A part with a description of "brass hinge" will display as "brass hinge".

If a column is a [CHAR](/docs/server/reference/data-types/string-data-types/char) data-type, a fixed width column, then it may be necessary to trim any leading or trailing spaces from displays. There are a few functions to accomplish this task. The [LTRIM()](/docs/server/reference/sql-functions/string-functions/ltrim) function will eliminate any leading spaces to the left. So "`H200`" becomes "`H200`". For columns with trailing spaces, spaces on the right, [RTRIM()](/docs/server/reference/sql-functions/string-functions/rtrim) will work: "`H500`" becomes "`H500`". A more versatile trimming function, though, is [TRIM()](/docs/server/reference/sql-functions/string-functions/trim). With it one can trim left, right or both. Below are a few examples:

```sql
SELECT TRIM(LEADING '.' FROM col1),
TRIM(TRAILING FROM col2),
TRIM(BOTH '_' FROM col3),
TRIM(col4)
FROM table5;
```

In the first [TRIM()](/docs/server/reference/sql-functions/string-functions/trim) clause, the padding component is specified; the leading dots are to be trimmed from the output of `col1`. The trailing spaces are trimmed off of `col2`—space is the default. Both leading and trailing under-scores are trimmed from `col3` above. Unless specified, BOTH is the default. So leading and trailing spaces are trimmed from `col4` in the statement here.

#### Extracting

When there is a need to extract specific elements from a column, MariaDB has a few functions that can help. Suppose a column in the table contacts contains the telephone numbers of sales contacts, including the area-codes, but without any dashes or parentheses. The area-code of each could be extracted for sorting with the [LEFT()](/docs/server/reference/sql-functions/string-functions/left) and the telephone number with the [RIGHT()](/docs/server/reference/sql-functions/string-functions/right) function.

```sql
SELECT LEFT(telephone, 3) AS area_code,
RIGHT(telephone, 7) AS tel_nbr
FROM contacts
ORDER BY area_code;
```

In the [LEFT()](/docs/server/reference/sql-functions/string-functions/left) function above, the column telephone is given along with the number of characters to extract, starting from the first character on the left in the column. The [RIGHT()](/docs/server/reference/sql-functions/string-functions/right) function is similar, but it starts from the last character on the right, counting left to capture, in this statement, the last seven characters. In the SQL statement above, area\_code is reused to order the results set. To reformat the telephone number, it are necessary to use the [SUBSTRING()](/docs/server/reference/sql-functions/string-functions/substring) function.

```sql
SELECT CONCAT('(', LEFT(telephone, 3), ') ',
SUBSTRING(telephone, 4, 3), '-',
MID(telephone, 7)) AS 'Telephone Number'
FROM contacts
ORDER BY LEFT(telephone, 3);
```

In this SQL statement, the [CONCAT()](/docs/server/reference/sql-functions/string-functions/concat) function is employed to assemble some characters and extracted data to produce a common display for telephone numbers (e.g., (504) 555-1234). The first element of the [CONCAT()](/docs/server/reference/sql-functions/string-functions/concat) is an opening parenthesis. Next, a [LEFT()](/docs/server/reference/sql-functions/string-functions/left) is used to get the first three characters of telephone, the area-code. After that a closing parenthesis, along with a space is added to the output. The next element uses the [SUBSTRING()](/docs/server/reference/sql-functions/string-functions/substring) function to extract the telephone number's prefix, starting at the fourth position, for a total of three characters. Then a dash is inserted into the display. Finally, the function [MID()](/docs/server/reference/sql-functions/string-functions/mid) extracts the remainder of the telephone number, starting at the seventh position. The functions [MID()](/docs/server/reference/sql-functions/string-functions/mid) and [SUBSTRING()](/docs/server/reference/sql-functions/string-functions/substring) are interchangeable and their syntax are the same. By default, for both functions, if the number of characters to capture isn't specified, then it's assumed that the remaining ones are to be extracted.

#### Manipulating

There are a few functions in MariaDB that can help in manipulating text. One such function is [REPLACE()](/docs/server/reference/sql-functions/string-functions/replace-function). With it every occurrence of a search parameter in a string can be replaced. For example, suppose we wanted to replace the title *Mrs.* with *Ms.* in a column containing the person's title, but only in the output. The following SQL would do the trick:

```sql
SELECT CONCAT(REPLACE(title, 'Mrs.', 'Ms.'),
' ', name_first, ' ', name_last) AS Name
FROM contacts;
```

We're using the ever handy [CONCAT()](/docs/server/reference/sql-functions/string-functions/concat) function to put together the contact's name with spaces. The [REPLACE()](/docs/server/reference/sql-functions/string-functions/replace-function) function extracts each title and replaces *Mrs.* with *Ms.*, where applicable. Otherwise, for all other titles, it displays them unchanged.

If we want to insert or replace certain text from a column (but not all of its contents), we could use the [INSERT()](/docs/server/reference/sql-functions/string-functions/insert-function) function in conjunction with the [LOCATE()](/docs/server/reference/sql-functions/string-functions/locate) function. For example, suppose another contacts table has the contact's title and full name in one column. To change the occurrences of Mrs. to Ms., we could not use [REPLACE()](/docs/server/reference/sql-functions/string-functions/replace-function) since the title is embedded in this example. Instead, we would do the following:

```sql
SELECT INSERT(name, LOCATE(name, 'Mrs.'), 4, 'Ms.')
FROM contacts;
```

The first element of the [INSERT()](/docs/server/reference/sql-functions/string-functions/insert-function) function is the column. The second element which contains the [LOCATE()](/docs/server/reference/sql-functions/string-functions/locate) is the position in the string that text is to be inserted. The third element is optional; it states the number of characters to overwrite. In this case, Mrs. which is four characters is overwritten with Ms. (the final element), which is only three. Incidentally, if 0 is specified, then nothing is overwritten, text is inserted only. As for the [LOCATE()](/docs/server/reference/sql-functions/string-functions/locate) function, the first element is the column and the second the search text. It returns the position within the column where the text is found. If it's not found, then 0 is returned. A value of 0 for the position in the [INSERT()](/docs/server/reference/sql-functions/string-functions/insert-function) function negates it and returns the value of name unchanged.

On the odd chance that there is a need to reverse the content of a column, there's the [REVERSE()](/docs/server/reference/sql-functions/string-functions/reverse) function. You would just place the column name within the function. Another minor function is the [REPEAT()](/docs/server/reference/sql-functions/string-functions/repeat-function) function. With it a string may be repeated in the display:

```sql
SELECT REPEAT(col1, 2)
FROM table1;
```

The first component of the function above is the string or column to be repeated. The second component states the number of times it's to be repeated.

#### Expression Aids

The function [CHAR\_LENGTH()](/docs/server/reference/sql-functions/string-functions/char_length) is used to determine the number of characters in a string. This could be useful in a situation where a column contains different types of information of specific lengths. For instance, suppose a column in a table for a college contains identification numbers for students, faculty, and staff. If student identification numbers have eight characters while others have less, the following will count the number of student records:

```sql
SELECT COUNT(school_id)
AS 'Number of Students'
FROM table8
WHERE CHAR_LENGTH(school_id)=8;
```

The [COUNT()](/docs/server/reference/sql-functions/aggregate-functions/count) function above counts the number of rows that meet the condition of the `WHERE` clause.

In a [SELECT](/docs/server/reference/sql-statements/data-manipulation/selecting-data/select) statement, an [ORDER BY](/docs/server/reference/sql-statements/data-manipulation/selecting-data/select#order-by) clause can be used to sort a results set by a specific column. However, if the column contains IP addresses, a simple sort may not produce the desired results:

```sql
SELECT ip_address
FROM computers WHERE server='Y'
ORDER BY ip_address LIMIT 3;

+-------------+
| ip_address  |
+-------------+
| 10.0.1.1    |
| 10.0.11.1   |
| 10.0.2.1    |
+-------------+
```

In the limited results above, the IP address 10.0.2.1 should be second. This happens because the column is being sorted lexically and not numerically. The function [INET\_ATON()](/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/inet_aton) will solve this sorting problem.

```sql
SELECT ip_address
FROM computers WHERE server='Y'
ORDER BY INET_ATON(ip_address) LIMIT 3;
```

Basically, the [INET\_ATON()](/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/inet_aton) function will convert IP addresses to regular numbers for numeric sorting. For instance, if we were to use the function in the list of columns in a [SELECT](/docs/server/reference/sql-statements/data-manipulation/selecting-data/select) statement, instead of the `WHERE` clause, the address 10.0.1.1 would return 167772417, 10.0.11.1 will return 167774977, and 10.0.2.1 the number 167772673. As a complement to [INET\_ATON()](/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/inet_aton), the function [INET\_NTOA()](/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/inet_ntoa) will translate these numbers back to their original IP addresses.

MariaDB is fairly case insensitive, which usually is fine. However, to be able to check by case, the [STRCMP()](/docs/server/reference/sql-functions/string-functions/strcmp) function can be used. It converts the column examined to a string and makes a comparison to the search parameter.

```sql
SELECT col1, col2
FROM table6
WHERE STRCMP(col3, 'text')=0;
```

If there is an exact match, the function [STRCMP()](/docs/server/reference/sql-functions/string-functions/strcmp) returns 0. So if `col3` here contains "Text", it won't match. Incidentally, if `col3` alphabetically is before the string to which it's compared, a `-1` are returned. If it's after it, a `1` is returned.

When you have list of items in one string, the [SUBSTRING\_INDEX()](/docs/server/reference/sql-functions/string-functions/substring_index) can be used to pull out a sub-string of data. As an example, suppose we have a column which has five elements, but we want to retrieve just the first two elements. This SQL statement will return them:

```sql
SELECT SUBSTRING_INDEX(col4, '|', 2)
FROM table7;
```

The first component in the function above is the column or string to be picked apart. The second component is the delimiter. The third is the number of elements to return, counting from the left. If we want to grab the last two elements, we would use a negative two to instruct MariaDB to count from the right end.

#### Conclusion

There are more string functions available in MariaDB. A few of the functions mentioned here have aliases or close alternatives. There are also functions for converting between ASCII, binary, hexi-decimal, and octal strings. And there are also string functions related to text encryption and decryption that were not mentioned. However, this article has given you a good collection of common string functions that will assist you in building more powerful and accurate SQL statements.

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}
