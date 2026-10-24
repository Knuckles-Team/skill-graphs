## What's new for C++ in Visual Studio version 16.5
For a summary of new features and bug fixes in Visual Studio version 16.5, see [What's New in Visual Studio 2019 version 16.5](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.5).
  * **IntelliCode Team Completions model and member variables support:** C++ developers can now train IntelliCode models on their own codebases. We call this a Team Completions model because you benefit from your team's practices. Additionally, we've improved IntelliCode suggestions for member variables.
  * **IntelliSense improvements:**
    * IntelliSense now displays more readable type names when dealing with the Standard Library.
    * We've added the ability to toggle whether **Enter** , **Space** , and **Tab** function as commit characters, and to toggle whether **Tab** is used to Insert Snippet. Find these settings under **Tools > Options > Text Editor > C/C++ > Advanced > IntelliSense**.
  * **Connection Manager over the command line:** You can now interact with your stored remote connections over the command line. It's useful for tasks such as provisioning a new development machine or setting up Visual Studio in continuous integration.
  * **Debug and deploy for WSL:** Use Visual Studio's native support for WSL to separate your build system from your remote deploy system. Now you can build natively on WSL and deploy the build artifacts to a second remote system for debugging. This workflow is supported by both CMake projects and MSBuild-based Linux projects.
  * **Support for FIPS 140-2 compliance mode:** Visual Studio now supports FIPS 140-2 compliance mode when developing C++ applications that target a remote Linux system.
  * **Language services for CMake Language files and better CMake project manipulation:**
    * The source file copy for CMake projects targeting a remote Linux system has been optimized. Visual Studio now keeps a "fingerprint file" of the last set of sources copied remotely and optimizes behavior based on the number of files that have changed.
    * Code navigation features such as Go To Definition and Find All References are now supported for functions, variables, and targets in CMake script files.
    * Add, remove, and rename source files and targets in your CMake projects from the IDE without manually editing your CMake scripts. When you add or remove files with the Solution Explorer, Visual Studio will automatically edit your CMake project. You can also add, remove, and rename the project's targets from the Solution Explorer's Targets View.
  * **Linux project improvements:** Visual Studio Linux projects now have more accurate IntelliSense and allow you to control remote header synchronization on a project-by-project basis.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-164)
