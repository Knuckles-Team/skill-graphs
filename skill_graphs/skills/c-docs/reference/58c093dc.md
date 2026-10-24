## What's new for C++ in Visual Studio version 17.9
_Released Feb 2024_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's new for C++ Developers in Visual Studio 2022 17.9](https://devblogs.microsoft.com/cppblog/whats-new-for-cpp-developers-in-visual-studio-2022-17-9/)
Standard Library (STL) merged C++23 features, performance improvements, enhanced behavior, Language Working Group (LWG) issue resolutions, and fixed bugs |
New features in the Visual Studio 17.9 IDE | [Visual Studio 2022 version 17.9 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.9)
C++ language conformance improvements in Visual Studio 2022 17.9 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_179)
Summary of C++ backend updates | [MSVC Backend updates since Visual Studio 2022 version 17.3](https://devblogs.microsoft.com/cppblog/msvc-backend-updates-since-visual-studio-2022-version-17-3/)
A partial list of new features:
  * `#include` diagnostics, which provides a detailed analysis of your `#include` directives. Activate this feature by right-clicking an `#include` and choosing **#include directives** > **Turn #include directive diagnostics on**. Above each `#include` is the number of times your code references that `#include` file. Click the **reference** link to navigate to where your code uses something from that header file. To view the build time of your `#include` directives, run Build Insights by navigating to **Build** > **Run Build Insights on Solution** > **Build**.
![Screenshot of #include diagnostics.](https://learn.microsoft.com/en-us/cpp/overview/media/include-diagnostics.png?view=msvc-170)
Above the # include is a **reference** link and many of the references to this # include file (in this case 1). The build time is also listed (in this case less than 1/2 a second).
  * Memory layout visualization, which shows how memory is arranged for your classes, structs, and unions. Hover over a type and choose the **Memory Layout** link in the **Quick Info** to open a dedicated window displaying the memory layout of the selected type. Hovering over individual data types within this window provides detailed information about their size and offset within the type.
![Screenshot of the memory layout window](https://learn.microsoft.com/en-us/cpp/overview/media/memory-layout-window.png?view=msvc-170)
The memory layout window shows the contents of the Snake class. It shows the memory offsets of the various fields of the class such as Point classes for the location of the head and body, the score, and so on.
  * You can now specify your own custom CMake executable. This feature is useful if you want to use a specific version of CMake that isn't shipped with Visual Studio. Navigate to **Tools** > **Options** and select **CMake** > **General**. Select **Enable custom CMake executable** and specify the directory path of your CMake executable.
![Screenshot of the CMake options dialog](https://learn.microsoft.com/en-us/cpp/overview/media/custom-cmake-option.png?view=msvc-170)
The CMake options dialog with the "Enable custom CMake executable" option and "CMake Executable Directory" field highlighted.
  * Improved IntelliSense for Unreal Engine projects.
  * Improved C++23 support: `std::format` and `std::span` `formattable`, `range_format`, `format_kind`, and `set_debug_format()` as part of `<mdspan>` per `format()` can format pointers per


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-178)
