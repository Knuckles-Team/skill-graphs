## What's new for C++ in Visual Studio version 17.8
_Released Nov 2023_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's new for C++ Developers in Visual Studio 2022 17.8](https://devblogs.microsoft.com/cppblog/whats-new-for-cpp-developers-in-visual-studio-2022-17-8/)
Standard Library (STL) merged C++26, C++23 features, C++20 extensions, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.8 IDE | [Visual Studio 2022 version 17.8 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.8)
C++ language conformance improvements in Visual Studio 2022 17.8 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_178)
An overview of C++ improvements in Visual Studio, VS Code, and vcpkg during 2023 | [A year of C++ improvements](https://devblogs.microsoft.com/cppblog/a-year-of-cpp-improvements-in-visual-studio-vs-code-and-vcpkg)
A partial list of new features:
  * C++ structured diagnostics in the Output window and a new problem details window that provides more information about the error. For more information, see [Structured SARIF Output](https://learn.microsoft.com/en-us/cpp/build/reference/sarif-output?view=msvc-170) and [Problem Details Window](https://learn.microsoft.com/en-us/visualstudio/ide/reference/problem-details-window).
  * A feature that lets you visualize the size and alignment of your classes, structs, unions, base types, or enums even before the code is compiled. Hover over the identifier and a Quick Info displays the size and alignment information.
  * A feature that suggests when to mark member functions `const` because they don't modify the object's state. Hover over a member function and click the light bulb icon to mark the function as `const`.
  * Visual Studio now prompts you to mark global functions as static via a screwdriver icon that appears by the function name. Click the screwdriver icon to mark the function as static.
  * Unused #include directives are dimmed in the editor. You can hover over a dimmed include and use the light bulb menu to either remove that include or all unused includes. You can also add `#include` directives for entities that are indirectly included via other headers. For more information, see [Clean up C/C++ includes in Visual Studio](https://learn.microsoft.com/en-us/cpp/ide/include-cleanup-overview?view=msvc-170).
  * More Unreal Engine support:
    * Unreal Engine Test Adapter lets you discover, run, manage, and debug your Unreal Engine tests without leaving the Visual Studio IDE.
    * With Unreal Engine Code Snippets, you can find common Unreal Engine constructs as snippets in your member list.
    * Build Insights is now integrated with Visual Studio 2022 and works with MSBuild and CMake projects using MSVC. You can now see additional information about the compilation of a function such as how long it took to compile, the number of ForceInlines, and the impact of header files on build time. For more information, see [Tutorial: Troubleshoot function inlining on build time](https://learn.microsoft.com/en-us/cpp/build-insights/tutorials/build-insights-function-view?view=msvc-170) and [Tutorial: Troubleshoot header file impact on build time](https://learn.microsoft.com/en-us/cpp/build-insights/tutorials/build-insights-included-files-view?view=msvc-170).
  * Remote Linux unit test support now lets you run your CTest and GTest tests on your remote Linux machines from Visual Studio's Test Explorer, just like your local tests.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-177)
