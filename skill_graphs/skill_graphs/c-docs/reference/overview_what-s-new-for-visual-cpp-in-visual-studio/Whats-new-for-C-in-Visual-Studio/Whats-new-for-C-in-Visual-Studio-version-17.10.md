## What's new for C++ in Visual Studio version 17.10
_Released May 2024_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's new for C++ Developers in Visual Studio 2022 17.10](https://devblogs.microsoft.com/cppblog/whats-new-for-c-developers-in-visual-studio-2022-17-10/)
Standard Library (STL) merged C++26 and C++23 features, C++20 defect reports, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.10 IDE | [Visual Studio 2022 version 17.10 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.10)
C++ language conformance improvements in Visual Studio 2022 17.10 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.10](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1710)
A partial list of new features:
  * **MSVC Toolset Update** : The MSVC toolset version is updated from 19.39 to 19.40. This may affect projects that have version assumptions. For more information about some ways in which this affects projects that assume that MSVC versions are all 19.3X for Visual Studio 2022 releases, see [MSVC Toolset Minor Version Number 14.40 in VS 2022 v17.10](https://devblogs.microsoft.com/cppblog/msvc-toolset-minor-version-number-14-40-in-vs-2022-v17-10/).
  * **Standard Library Enhancements** : The standard library added support for `std::format` more in line with those that already exist for integers. Improved the vectorized implementations of `std::min_element`, `std::ranges::min`, and friends.
  * **Build Insights** : Now provides template instantiation information. See [Templates View for Build Insights in Visual Studio](https://devblogs.microsoft.com/cppblog/templates-view-for-build-insights-in-visual-studio-2/) or the
  * **Unreal Engine Plugin** : There's a new opt-in feature for the Unreal Engine Plugin to run in the background, reducing startup costs. This is an opt-in feature that is activated via **Tools** > **Options** > **Unreal Engine**.
  * **New features for Linux** : See
  * **CMake Targets** : You can now pin targets in the **CMake Targets View**.
  * **Connection Manager UX** : The user experience provides a more seamless experience when connecting to remote systems. For more information, see [Usability Improvements in the Visual Studio Connection Manager](https://devblogs.microsoft.com/cppblog/usability-improvements-in-the-visual-studio-connection-manager/).
  * **Pull request comments** : You can now view GitHub and Azure DevOps comments directly in your working file. Enable the feature flag, **Pull Request Comments** in **Options** > **Environment** > **Preview Features** and checkout the pull request branch to get started.
  * **AI-Generated Content** : GitHub Copilot can now draft pull request descriptions. Requires an active GitHub Copilot subscription. Try it out by clicking the **Add AI Generated Pull Request Description** sparkle pen icon within the **Create a Pull Request** window.
  * **Image Preview** : Hover over an image path to see a preview with size details. The size is capped to 500 px wide and high.
![Screenshot of hover preview.](https://learn.microsoft.com/en-us/cpp/overview/media/hover-preview.png?view=msvc-170)
The mouse is hovering over the line std::filesystem::path vs_logo_path = "../images/vs_logo.png". Underneath appears a preview of the Visual Studio logo and the information that it's 251 x 500 pixels and 13.65 KB in size.
  * **Breakpoint/Tracepoint Creation** : You can now create conditional breakpoints or tracepoints directly from expressions in the source code from the right-click menu. This works on property or field names and values from autos, locals, watch windows, or DataTips.
  * **Attach to Process Dialog** : The functionality provided by the Attach to Process dialog is more user-friendly. You can now easily switch between tree and list views, organize processes better with collapsible sections, and select code types with a simplified combobox. Also, the "Select/Track Window" feature is now easier to use, allowing two-way tracking: selecting a process highlights its window, and clicking on a window selects its process.
  * **GitHub Copilot Integration** : GitHub Copilot and Copilot Chat extensions are now unified and ship directly in Visual Studio. To install it, install the **GitHub Copilot** component in the **Visual Studio Installer** :
[ ![Screenshot of the Visual Studio Installer GitHub Copilot installation option.](https://learn.microsoft.com/en-us/cpp/overview/media/github-copilot-install-option.png?view=msvc-170) ](https://learn.microsoft.com/en-us/cpp/overview/media/github-copilot-install-option-expanded.png?view=msvc-170#lightbox)
[ The Visual Studio installer is open to the Workloads tab. In the installation details pane, GitHub Copilot is shown as selected.](https://learn.microsoft.com/en-us/cpp/overview/media/github-copilot-install-option-expanded.png?view=msvc-170#lightbox)
[ ](https://learn.microsoft.com/en-us/cpp/overview/media/github-copilot-install-option-expanded.png?view=msvc-170#lightbox)
![Screenshot of GitHub Copilot button.](https://learn.microsoft.com/en-us/cpp/overview/media/unified-github-copilot-button.png?view=msvc-170)
The GitHub Copilot button is shown in the top-right corner of Visual Studio. It has options to open a chat window, GitHub Copilot settings, learn more, and manage copilot subscription.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-179)
