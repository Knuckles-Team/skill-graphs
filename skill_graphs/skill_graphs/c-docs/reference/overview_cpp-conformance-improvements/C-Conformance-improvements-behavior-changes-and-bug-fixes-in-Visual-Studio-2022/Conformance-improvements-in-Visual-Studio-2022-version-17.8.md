##  Conformance improvements in Visual Studio 2022 version 17.8
Visual Studio 2022 version 17.8 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#fu-issues-an-error)
###  `/FU` issues an error
The C compiler used to accept the `/FU` option, even though it hasn't support managed compilation for some time. It now issues an error. Projects that pass this option need to restrict it to C++/CLI projects only.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c-standard-library-1)
### C++ Standard Library
The C++23 named modules `std` and `std.compat` are now available when compiling with `/std:c++20`.
For a broader summary of changes made to the C++ Standard Library, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_177)
