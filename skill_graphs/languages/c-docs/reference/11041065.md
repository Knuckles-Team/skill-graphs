## What's new for C++ in Visual Studio version 16.1
For a summary of new features and bug fixes in Visual Studio version 16.1, see [What's New in Visual Studio 2019 version 16.1](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.1).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#c-compiler)
### C++ compiler
  * These C++20 features have been implemented in the C++ compiler, available under **`/std:c++latest`**(or**`/std:c++20`**starting in Visual Studio 2019 version 16.11):
    * Increased ability to find function templates via argument-dependent lookup for function call expressions with explicit template arguments (
    * Designated initialization (`Type t { .member = expr }` syntax.
  * Lambda support has been overhauled, addressing a large number of long-standing bugs. This change is enabled by default when using **`/std:c++20`**or**`/std:c++latest`**. In**`/std:c++17`**language mode and under the default (**`/std:c++14`**) mode, the new parser can be enabled by using[`/Zc:lambda`](https://learn.microsoft.com/en-us/cpp/build/reference/zc-lambda?view=msvc-170) in Visual Studio 2019 version 16.9 or later (previously available as **`/experimental:newLambdaProcessor`**beginning in Visual Studio 2019 version 16.3), for example,`/std:c++17 /Zc:lambda`.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#c-standard-library-improvements)
### C++ standard library improvements
  * These C++20 features have been added to our implementation of the C++ Standard Library, available under **`/std:c++latest`**:
    * `starts_with` and `ends_with` for `basic_string` and `basic_string_view`.
    * `contains` for associative containers.
    * `remove`, `remove_if`, and `unique` for `list` and `forward_list` now return `size_type`.
    * `shift_left` and `shift_right` added to `<algorithm>`.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#c-ide)
### C++ IDE
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#intellicode-for-c)
#### IntelliCode for C++
IntelliCode now ships as an optional component in the **Desktop Development with C++** workload. For more information, see [Improved C++ IntelliCode now Ships with Visual Studio 2019](https://devblogs.microsoft.com/cppblog/improved-c-intellicode-now-ships-with-visual-studio-2019/).
IntelliCode uses its own extensive training and your code context to put what you're most likely to use at the top of your completion list. It can often eliminate the need to scroll down through the list. For C++, IntelliCode offers the most help when using popular libraries such as the standard library.
The new IntelliCode features (Custom Models, C++ support, and EditorConfig inference) are disabled by default. To enable them, go to **Tools > Options > IntelliCode > General**. This version of IntelliCode has improved accuracy and includes support for free-functions. For more information, see [AI-Assisted Code Completion Suggestions Come to C++ via IntelliCode](https://devblogs.microsoft.com/cppblog/cppintellicode/).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#quick-info-improvements)
#### Quick Info improvements
  * The Quick Info tooltip now respects the semantic colorization of your editor. It also has a new **Search Online** link that will search online documentation for information about the hovered code construct. The link provided by Quick Info for red-squiggled code will search for the error online. That way you don't need to retype the message into your browser. For more information, see [Quick Info Improvements in Visual Studio 2019: Colorization and Search Online](https://devblogs.microsoft.com/cppblog/quick-info-improvements-in-visual-studio-2019-colorization-and-search-online/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#general-improvements)
#### General improvements
  * The Template Bar can populate the dropdown menu based on instantiations of that template in your codebase.
  * Lightbulbs for missing `#include` directives that vcpkg can install, and autocompletion of available packages for the CMake `find_package` directive.
  * The **General** Property Page for C++ projects has been revised. Some options are now listed under a new **Advanced** page. The **Advanced** page also includes new properties for your preferred toolset architecture, debug libraries, the MSVC toolset minor version, and Unity (jumbo) builds.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#cmake-support)
### CMake support
  * We updated the CMake version that ships with Visual Studio to 3.14. This version adds built-in support for MSBuild generators targeting Visual Studio 2019 projects as well as file-based IDE integration APIs.
  * We've added improvements to the CMake Settings Editor, including support for Windows Subsystem for Linux (WSL) and configurations from existing caches, changes to the default build and install roots, and support for environment variables in Linux CMake configurations.
  * Completions and quick info for built-in CMake commands, variables, and properties make it easier to edit your _`CMakeLists.txt`_files.
  * We've integrated support for editing, building, and debugging CMake projects with Clang/LLVM. For more information, see [Clang/LLVM Support in Visual Studio](https://devblogs.microsoft.com/cppblog/clang-llvm-support-in-visual-studio/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#linux-and-the-windows-subsystem-for-linux)
### Linux and the Windows Subsystem for Linux
  * We now support [AddressSanitizer (ASan) for the Linux Workload in Visual Studio 2019](https://devblogs.microsoft.com/cppblog/addresssanitizer-asan-for-the-linux-workload-in-visual-studio-2019/).
  * We've integrated Visual Studio support for using C++ with the Windows Subsystem for Linux (WSL). Now you can use your local Windows Subsystem for Linux (WSL) installation with C++ natively in Visual Studio without additional configuration or a SSH connection. For more information, see [C++ with Visual Studio 2019 and Windows Subsystem for Linux (WSL)](https://devblogs.microsoft.com/cppblog/c-with-visual-studio-2019-and-windows-subsystem-for-linux-wsl/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#code-analysis)
### Code Analysis
  * New quick fixes for uninitialized variable checks were added. Code Analysis warnings [C6001: using uninitialized memory `<variable>`](https://learn.microsoft.com/en-us/cpp/code-quality/c6001?view=msvc-170) and [C26494 VAR_USE_BEFORE_INIT](https://learn.microsoft.com/en-us/cpp/code-quality/c26494?view=msvc-170) are available in the lightbulb menu on relevant lines. They're enabled by default in the Microsoft Native Minimum ruleset and C++ Core Check Type rulesets, respectively. For more information, see [New code analysis quick fixes for uninitialized memory (C6001) and use before init (C26494) warnings](https://devblogs.microsoft.com/cppblog/new-code-analysis-quick-fixes-for-uninitialized-memory-c6001-and-use-before-init-c26494-warnings/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#remote-builds)
### Remote builds
  * Users can now separate remote build machines from remote debug machines when targeting Linux in both MSBuild and CMake projects.
  * The improved logging for remote connections makes it easier to diagnose issues in cross-platform development.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-160)
