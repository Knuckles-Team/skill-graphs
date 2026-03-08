## What's new for C++ in Visual Studio version 17.3
_Released Aug 2022_
Expand table
For more information about | See
---|---
What's new for C++ developers | [C++ improvements in 17.3](https://devblogs.microsoft.com/visualstudio/visual-studio-2022-17-3-is-now-available/#c++-improvements)
Standard Library (STL) merged C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.3 IDE | [Visual Studio 2022 version 17.3 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.3)
C++ language conformance improvements in Visual Studio 2022 17.3 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_173)
A partial list of new features in 17.3:
  * The Arm64EC toolchain is no longer marked as experimental and is ready for production use.
  * The Visual Studio Terminal can now be used as an SSH client with your stored SSH connections. With the C++ for Linux Tools installed, open the Terminal tool window. The Terminal dropdown is populated with your stored connections. When you select a connection, a new Terminal window opens inside Visual Studio that shows a pseudo-terminal on your remote system. Control characters, colors, and cursor positional awareness are all supported.
  * Visual Studio can now add Unreal Engine class templates for your UE projects. To try this feature, ensure **IDE support for Unreal Engine** is selected in the **Game development with C++** workload in the Visual Studio Installer. When you're working on a UE project, right-click in the project or a folder/filter and select **Add** > **UE Class**.
  * **Go to Definition** now remembers the prior signature and navigates accordingly when a better match isn't available (for example, after you manually change the signature of one of the pair). The responsiveness of **Go To All** is improved. Previously, results appeared after you stopped typing. In the new experience, results show as you type.
  * In contexts requiring `enum` type completion (for example, assignments to `enum` variables, case labels, returning `enum` type, and so on), the autocompletion list is now filtered to just the matching enumerators and related constructs.
  * Added NuGet PackageReference support for C++/CLI MSBuild projects targeting .NET Core. This change was made to unblock mixed codebases from being able to adopt .NET Core. This support doesn't work for other C++ project types or any C++ project types targeting .NET Framework. There are no plans to extend PackageReference support to other C++ scenarios. The team is working on separate experiences involving vcpkg for non-MSBuild scenarios and to add greater functionality.
  * Added a Serial Monitor window for embedded development, available through **Debug** > **Windows** > **Serial Monitor**.
  * Improved C++ indexing by ~66% compared to 17.2.
  * Updated the version of CMake shipped with Visual Studio to version 3.23. See the
  * Upgraded the versions of LLVM tools shipped with Visual Studio to v14. For details of what is available, see the
  * Updated the side-by-side Dev 16.11 C++ Toolset to version 14.29.30145.00. The latest version of the Dev 16.11 C++ Toolset contains important bug fixes, including fixing all remaining C++20 defect reports. For more information about bug fixes, including C++20 defect reports in Dev 16.11, see [Visual Studio 2019 version 16.11.14 release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes#16.11.14).
  * Made various improvements to the in-editor experience of C++ modules. We're continuously working on improving the quality of the experience but encourage you to try them in 17.3. Report remaining issues through


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-172)
