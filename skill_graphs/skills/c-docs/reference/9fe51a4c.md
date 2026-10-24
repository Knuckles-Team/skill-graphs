## What's new for C++ in Visual Studio version 17.14
_Released May 2025_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.14](https://devblogs.microsoft.com/cppblog/whats-new-for-c-developers-in-visual-studio-2022-17-14/)
Standard Library (STL) merged C++26 and C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the IDE | [Visual Studio 2022 version 17.14 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes)
C++ language updates | [C++ Language Updates in MSVC in Visual Studio 2022 17.14](https://devblogs.microsoft.com/cppblog/c-language-updates-in-msvc-in-visual-studio-2022-17-14/)
C++ language conformance improvements | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.14](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1714)
A quick highlight of some of the new features:
  * C++ Dynamic Debugging allows you to debug optimized code without impacting performance. For more information, see [C++ Dynamic Debugging](https://learn.microsoft.com/en-us/visualstudio/debugger/cpp-dynamic-debugging).
  * Implemented C++23 features (requires `/std:c++latest` or `/std:c++23preview`):
  * Automatically generate documentation comments with GitHub Copilot. For more information, see [Introducing automatic documentation comment generation in Visual Studio](https://devblogs.microsoft.com/visualstudio/introducing-automatic-documentation-comment-generation-in-visual-studio/).
  * Use the Model Picker in Visual Studio to select your AI model for GitHub Copilot. For more information, see
![A screenshot of the GitHub Copilot chat window with the Model Picker dropdown highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/model-picker.png?view=msvc-170)
The dropdown for the Model Picker is open. The options include: GPT-4o, o3-mini, Claude 3.7 Sonnet Thinking, and others.
  * Unreal Engine integration improvements:
    * The Visual Studio C++ debugger now supports Unreal Engine Blueprints.
    * Commands for building files, modules, and plugins are available natively in Visual Studio.
  * New compiler flag [/forceInterlockedFunctions](https://learn.microsoft.com/en-us/cpp/build/reference/force-interlocked-functions?view=msvc-170) dynamically selects between Armv8.0 load, store exclusive instructions or Armv8.1 Large System Extension (LSE) atomic instructions based on CPU capability at runtime.
  * Added support for IntelliSense-based completions and quick info for CMake modules in Visual Studio. You can view all available CMake modules and when you hover over a referenced CMake module, IntelliSense provides more info about the selected module:
![A screenshot of intellisense explaining C Make Print Helpers.](https://learn.microsoft.com/en-us/cpp/overview/media/cmake-module-intellisense.png?view=msvc-170)
The screenshot is of an edit in the C Make Lists .txt file. The cursor is on include ( CMakePrintHelpers ). Intellisense says: Convenience functions for printing properties and variables, useful for debugging.
When you start typing a CMake module name in your `CMakeLists.txt` or other CMake script files, IntelliSense provides a list of available modules to choose from:
![A screenshot of intellisense for a include statement.](https://learn.microsoft.com/en-us/cpp/overview/media/cmake-intellisense.png?view=msvc-170)
The screenshot is of an edit in the C Make Lists .txt file. The cursor is on include ( C Make. The Intellisense dropdown contains entries for C Make Add Fortran Subdirectory, C Make Dependent Option, and more.
  * Guidelines Support Library (GSL) 4.2.0: This release includes performance improvements for `gsl::span`, new features, and better alignment with C++ standards. For more information, see [Announcing Guidelines Support Library v4.2.0](https://devblogs.microsoft.com/cppblog/announcing-guidelines-support-library-v4-2-0/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-1713)
