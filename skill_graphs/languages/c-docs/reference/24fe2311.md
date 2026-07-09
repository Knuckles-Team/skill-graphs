## What's new for C++ in Visual Studio version 17.1
_Released Feb 2022_
Expand table
For more information about | See
---|---
What's new for C++ developers | [Visual Studio 2022 17.1 is now available!](https://devblogs.microsoft.com/visualstudio/visual-studio-2022-17-1-is-now-available/)
Standard Library (STL) merged C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.1 IDE | [Visual Studio 2022 version 17.1 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.1)
C++ language conformance improvements in Visual Studio 2022 17.1 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_171)
A partial list of new features in 17.1:
  * A new **Configure Preset** template is added to configure and build CMake projects on a remote macOS system with _`CMakePresets.json`_. You can also launch CMake targets on a remote macOS system, and then debug remotely in the Visual Studio debugger backed by GDB or LLDB.
  * You can now debug core dumps on a remote macOS system from Visual Studio with LLDB or GDB.
  * The versions of
  * Visual Studio's CMake integration is only active when a _`CMakeLists.txt`_is identified at the root of the open workspace. If a _`CMakeLists.txt`_is identified at another level of the workspace, then you're prompted to activate Visual Studio's CMake integration with a notification.
  * New views that enable you to inspect and interact with peripheral registers on microcontrollers and real time operating systems (RTOS) objects, available through **Debug** > **Windows** > **Embedded Registers**
  * Added a new thread view for RTOS projects, available through **Debug** > **Windows** > **RTOS Objects**. For more information, see [Embedded Software Development in Visual Studio](https://devblogs.microsoft.com/cppblog/visual-studio-embedded-development/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-170)
