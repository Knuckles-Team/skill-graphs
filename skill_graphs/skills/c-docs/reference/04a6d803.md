## What's new for C++ in Visual Studio version 16.3
For a summary of new features and bug fixes in Visual Studio version 16.3, see [What's New in Visual Studio 2019 version 16.3](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.3).
  * C++ developers can now toggle line comments using the keyboard shortcut **Ctrl+K** , **Ctrl+/**.
  * IntelliSense member lists are now filtered based on type qualifiers, for example, `const std::vector` now filters out methods such as `push_back`.
  * We added these C++20 Standard Library features (available under **`/std:c++latest`**, or**`/std:c++20`**starting in Visual Studio 2019 version 16.11):
    * `operator>>(basic_istream&, CharT*)`
    * `move()` In `<numeric>`
    * `is_nothrow_convertible`
  * [New C++ Core Guideline checks](https://devblogs.microsoft.com/cppblog/new-c-core-check-rules/), including the new "Enum Rules" rule set, and additional `const`, `enum`, and type rules.
  * A new default semantic colorization scheme allows users to better understand their code at a glance, the call-stack window can be configured to hide template arguments, and C++ IntelliCode is on-by-default.
  * Configure debug targets and custom tasks with environment variables using CMakeSettings.json or CppProperties.json or the new "env" tag on individual targets and tasks in launch.vs.json and tasks.vs.json.
  * Users can now use a quick action on missing vcpkg packages to automatically open a console and install to the default vcpkg installation.
  * The remote header copy done by Linux projects ([CMake](https://learn.microsoft.com/en-us/cpp/linux/cmake-linux-project?view=msvc-170) and [MSBuild](https://learn.microsoft.com/en-us/cpp/linux/configure-a-linux-project?view=msvc-170)) has been optimized and now runs in parallel.
  * Visual Studio's [native support for WSL](https://devblogs.microsoft.com/cppblog/c-with-visual-studio-2019-and-windows-subsystem-for-linux-wsl/) now supports parallel builds for MSBuild-based Linux projects.
  * Users can now specify a list of local build outputs to deploy to a remote system with Linux Makefile projects.
  * Setting descriptions in the [CMake Settings Editor](https://devblogs.microsoft.com/cppblog/introducing-the-new-cmake-project-settings-ui/) now contain more context and links to helpful documentation.
  * The C++ base model for IntelliCode is now enabled by default. You can change this setting by going to **Tools** > **Options** > **IntelliCode**.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-162)
