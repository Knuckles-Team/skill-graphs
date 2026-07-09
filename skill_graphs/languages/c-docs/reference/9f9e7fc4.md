## What's new for C++ in Visual Studio version 17.11
_Released August 2024_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.11](https://devblogs.microsoft.com/cppblog/whats-new-for-c-developers-in-visual-studio-2022-17-11/)
Standard Library (STL) merged C++26 and C++23 features, C++20 defect reports, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.11 IDE | [Visual Studio 2022 version 17.11 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.11)
C++ language conformance improvements in Visual Studio 2022 17.11 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.11](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1711)
A partial list of new features:
  * **Standard Library Enhancements**
    * The formatted output implementation now includes `std::range_formatter` and formatters for `std::pair` and `std::tuple`.
    * Added support for `std::println()` with no arguments. This prints a blank line as proposed in
    * Improved vectorization for several algorithms including `replace_copy()`, `replace_copy_if()`, `ranges::replace_copy`, `ranges::replace_copy_if`, `find_first_of()` and `ranges::find_first_of`, for 8-bit and 16-bit elements, `mismatch()`, `ranges::mismatch`, `count()`, `ranges::count`, `find()`, `ranges::find`, `ranges::find_last`, and `ranges::iota`.
  * **Game development in C++**
    * You can now add common Unreal Engine class templates, modules, and plugins from within Visual Studio. For more information, see [Add Unreal Engine classes, modules, and plugins in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-add-class-module-plugin).
    * The new Unreal Engine toolbar provides quick access to Unreal Engine related actions from within Visual Studio. The toolbar allows you to quickly attach to Unreal Engine processes, rescan the Blueprints cache, quickly access the Unreal Engine Log, and provides quick access to the Unreal Engine Configuration Page for Visual Studio. For more information, see [Unreal Engine Toolbar](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-quickstart#unreal-engine-toolbar).
    * You can now filter trace results by project. Also, results in each row show the relative path and file name instead of the full path. Results grouping in the **Included Files** view is also improved:
![A screenshot of the improved Included Files diagnostics results.](https://learn.microsoft.com/en-us/cpp/overview/media/include-diagnostics-improved.png?view=msvc-170)
The Included Files view has a new column for the project. The Project column is selected and projects such as (Select All), CompilerIdC, OpenAL, common, and so on, are selected. The included files are listed by relative path and file name and grouped together.
  * **CMake debugging**
    * You can now debug your CMake scripts and `CMakeLists.txt` files in the Visual Studio debugger for CMake projects that target Linux via Windows Subsystem for Linux (WSL) or SSH. To start a CMake debugging session in Visual Studio, set a breakpoint in your `CMakeLists.txt` file and then navigate to **Project** > **Configure Cache with CMake Debugging**.
  * **GitHub Copilot**
    * When you hover over symbols in the code editor, click the Copilot **Tell me more** button in the Quick Info dialog to learn more about a given symbol:
![A screenshot of the Quick Info window.](https://learn.microsoft.com/en-us/cpp/overview/media/github-copilot-quick-info.png?view=msvc-170)
The Quick Info window is shown above a function. The Tell me more link is highlighted.
    * GitHub Copilot can generate naming suggestions for your identifiers (variables, methods, or classes) based on how your identifier is used and the style of your code.
![A screenshot of the GitHub Copilot Rename dialog.](https://learn.microsoft.com/en-us/cpp/overview/media/copilot-rename.png?view=msvc-170)
The Rename dialog has a New name field with a dropdown list that shows these choices: text_color, font_color, display_color, console_color, and menu_text_color.
You need an active [GitHub Copilot subscription](https://visualstudio.microsoft.com/github-copilot/). Right-click the variable you wish to rename, and choose **Rename** (`Ctrl+R`, `Ctrl+R`). Select the GitHub Copilot sparkle icon to generate naming suggestions.
  * **Debugging**
    * Conditional breakpoints in C++ are faster.
  * **Diagnostics improvements**
    * Improved diagnostics when calling `std::get<T>` on a `std::tuple` that has multiple instances of `T` in its template arguments. MSVC used to report:
`error C2338: static_assert failed: 'duplicate type T in get<T>(tuple)'`.
Now it reports:
`error C2338: static_assert failed: 'get<T>(tuple<Types...>&) requires T to occur exactly once in Types.(N4971 [tuple.elemm]/5)'`
    * Improved diagnostics when `std::ranges::to` is unable to construct the requested result. MSVC used to report:
`error C2338: static_assert failed: 'the program is ill-formed per N4950 [range.utility.conv.to]/2.3'`
Now it reports:
`error C2338: static_assert failed: 'ranges::to requires the result to be constructible from the source range, either by using a suitable constructor, or by inserting each element of the range into the default-constructed object. (N4981 [range.utility.conv.to]/2.1.5)'`


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-1710)
