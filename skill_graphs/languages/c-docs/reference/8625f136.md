## Non-MSBuild projects with Open Folder
Visual Studio 2017 introduces the **Open Folder** feature. It enables you to code, build, and debug in a folder containing source code without the need to create any solutions or projects. Now it's simpler to get started with Visual Studio, even if your project isn't an MSBuild-based project. **Open Folder** gives you access to powerful code understanding, editing, building, and debugging capabilities. They're the same ones that Visual Studio already provides for MSBuild projects. For more information, see [Open Folder projects for C++](https://learn.microsoft.com/en-us/cpp/build/open-folder-projects-cpp?view=msvc-170).
  * Improvements to the Open Folder experience. You can customize the experience through these .json files:
    * CppProperties.json to customize the IntelliSense and browsing experience.
    * Tasks.json to customize the build steps.
    * Launch.json to customize the debugging experience.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-6)
##### Visual Studio 2017 version 15.3
  * Improved support for alternative compilers and build environments such as MinGW and Cygwin. For more information, see [Using MinGW and Cygwin with Visual C++ and Open Folder](https://devblogs.microsoft.com/cppblog/using-mingw-and-cygwin-with-visual-cpp-and-open-folder/).
  * Added support to define global and configuration-specific environment variables in CppProperties.json and CMakeSettings.json. These environment variables can be consumed by debug configurations defined in launch.vs.json and tasks in tasks.vs.json. For more information, see [Customizing your Environment with Visual C++ and Open Folder](https://devblogs.microsoft.com/cppblog/customizing-your-environment-with-visual-c-and-open-folder/).
  * Improved support for CMake's Ninja generator, including the ability to easily target 64-bit platforms.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#cmake-support-via-open-folder)
