## Visual Studio 2017 C++ IDE
  * Configuration change performance is now better for C++ native projects and much better for C++/CLI projects. When a solution configuration is activated for the first time, it is faster, and all later activations of this solution configuration is almost instantaneous.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-5)
##### Visual Studio 2017 version 15.3
  * Several project and code wizards have been rewritten in the signature dialog style.
  * **Add Class** now launches the Add Class wizard directly. All of the other items that were previously here are now available under **Add > New Item**.
  * Win32 projects are now under the **Windows Desktop** category in the **New Project** dialog.
  * The **Windows Console** and **Desktop Application** templates now create the projects without displaying a wizard. There's a new **Windows Desktop Wizard** under the same category that displays the same options as the old **Win32 Console Application** wizard.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-7)
##### Visual Studio 2017 version 15.5
Several C++ operations that use the IntelliSense engine for refactoring and code navigation run much faster. The following numbers are based on the Visual Studio Chromium solution with 3500 projects:
Expand table
Feature | Performance Improvement
---|---
Rename | 5.3x
Change Signature | 4.5x
Find All References | 4.7x
C++ now supports Ctrl+Click **Go To Definition** , making mouse navigation to definitions easy. The Structure Visualizer from the Productivity Power Tools pack is now also included in the product by default.
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#intellisense)
