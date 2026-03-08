## What's new for C++ in Visual Studio version 17.5
_Released Feb 2023_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.5](https://devblogs.microsoft.com/cppblog/visual-studio-17-5-for-cpp-devs/)
Standard Library (STL) merged C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.5 IDE | [Visual Studio 2022 version 17.5 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.5)
A partial list of new features includes:
  * `std::move`, `std::forward`, `std::move_if_noexcept`, and `std::forward_like` now don't produce function calls in generated code, even in debug mode. This change avoids named casts causing unnecessary overhead in debug builds. `/permissive-` (or an option that implies it, such as `/std:c++20` or `/std:c++latest`) is required.
  * Added [`[[msvc::intrinsic]]`](https://learn.microsoft.com/en-us/cpp/cpp/attributes?view=msvc-170#msvcintrinsic). You can apply this attribute to nonrecursive functions consisting of a single cast, which take only one parameter.
  * Added support for Linux Console in the Integrated Terminal, which allows for terminal I/O.
  * Added initial experimental support for C11 atomic primitives (`<stdatomic.h>`). You can enable this experimental feature with the `/experimental:c11atomics` option in `/std:c11` mode or later.
  * Added a new set of experimental high-confidence checks to the Lifetime Checker for reduced noise.
  * A new preview feature, Remote File Explorer, lets you view the file directory on your remote machines within VS, and upload and download files to it.
  * Changed versioning of CMake executables shipped with Visual Studio to match Kitware versions.
  * Added support for Hot Reload to the CMake Project template.
  * Go To Definition for C++ now uses a more subtle indicator of the operation taking more time, replacing the modal dialog from previous versions.
  * Started rollout of an experiment providing more smart results in the C++ autocompletion and member list. This functionality was previously known as Predictive IntelliSense but now uses a new presentation method.
  * We now ship a native Arm64 Clang toolset with our LLVM workload, allowing native compilation on Arm64 machines.
  * Added localization to the
  * Added support for opening a Terminal window into the currently running Developer Container.
  * Made several improvements to IntelliSense macro expansion. Notably, we enabled recursive expansion in more contexts, and we added options to the pop up to copy the expansion to the clipboard or expand the macro inline.
  * Concurrent monitoring is now supported in the Serial Monitor. Concurrent monitoring allows you to monitor multiple ports at the same time side by side. Press the plus button to open another Serial Monitor and get started.
  * You can now view properties from base classes modified in an Unreal Blueprint asset without leaving Visual Studio. Double-click in a Blueprint reference for a C++ class or property to open the UE Asset Inspector in Visual Studio.
  * Enabled running DevContainers on a remote Linux machine.
  * Enabled selection of multiple targets to build in the CMake Targets view.
  * Added support for CMakePresets.json version 5. See the
  * Enabled Test Explorer to build and test multiple CMake targets in parallel.
  * Added "Open container in terminal" option to Dev Containers.
  * Implemented standard library features:
    * `basic_format_string`, `format_string`, `wformat_string`
    * `ranges::fold_left`, `ranges::fold_right`, and so on.
    * `views::zip` (doesn't include `zip_transform`, `adjacent`, and `adjacent_transform`)


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-174)
