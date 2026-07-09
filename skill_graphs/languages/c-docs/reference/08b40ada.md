##  Conformance improvements in Visual Studio 2022 version 17.11
Visual Studio 2022 version 17.11 includes the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
For an in-depth summary of changes made to the Standard Template Library, including conformance changes, bug fixes, and performance improvements, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#print-blank-lines-with-println)
### Print blank lines with `println`
Per `println`. This feature is available when compiling with `/std:c++latest`. Before this change, you wrote: `println("");` Now you write: `println();`.
  * `println();` is equivalent to `println(stdout);`
  * `println(FILE* stream);` is equivalent to `println(stream, "\n");`


[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#implemented-range_formatter)
### Implemented `range_formatter`
Per `range_formatter` is now implemented. This feature is available when compiling with `/std:c++latest`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1710)
