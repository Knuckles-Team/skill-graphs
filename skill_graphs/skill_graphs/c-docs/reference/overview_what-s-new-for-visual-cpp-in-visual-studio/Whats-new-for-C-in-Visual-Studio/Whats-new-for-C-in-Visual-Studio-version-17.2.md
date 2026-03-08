## What's new for C++ in Visual Studio version 17.2
_Released May 2022_
Expand table
For more information about | See
---|---
What's new for C++ developers | [Visual Studio 2022 17.2 is now available](https://devblogs.microsoft.com/visualstudio/visual-studio-2022-17-2-is-now-available/)
Standard Library (STL) merged C++20 defect reports, C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.2 IDE | [Visual Studio 2022 version 17.2 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.2)
C++ language conformance improvements in Visual Studio 2022 17.2 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_172)
A partial list of new features in 17.2:
  * Added compiler support for C++23 feature **`/std:c++latest`**option.
  * Added IntelliSense support for C++23 features
  * Added inline parameter name and type hint support, toggled by pressing **Alt+F1** or double-tapping **Ctrl**. This behavior can be customized under **Tools > Options > Text Editors > C/C++ > IntelliSense**.
  * Added experimental support for C++20 modules in CMake projects. This support is currently only available with the Visual Studio (MSBuild) generator.
  * In 17.1, we introduced peripheral register and RTOS views for embedded developers. We continue to improve the capabilities of those views with usability improvements in 17.2:
    * The RTOS tool window is now hidden by default. It prevents showing a tool window with error messages that aren't relevant when you're not using an RTOS.
    * When you double-click an RTOS object in the tool window, it adds a watch for the object.
    * When you select the start and end values for the stack pointer in the RTOS tool window, it opens in the memory window.
    * Added thread awareness for device targets to the call stack window.
    * Users can now select a pin icon next to peripherals, registers, or fields to pin them to the top of the Peripheral View.
  * Added implementations of the remaining C++20 defect reports (also known as _backports_). All C++20 features are now available under the **`/std:c++20`**option. For more information about the implemented backports, see the[MSVC's STL Completes `/std:c++20`](https://devblogs.microsoft.com/cppblog/msvcs-stl-completes-stdc20/) blog post.
  * We added various C++23 Library features, available under the **`/std:c++latest`**option. For more information about the new features, see the
  * Improved performance of the initial C++ indexing by up to 20%, depending on the depth of the include graph.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-171)
