## CMake support via Open Folder
Visual Studio 2017 introduces support for using CMake projects without converting to MSBuild project files (.vcxproj). For more information, see [CMake projects in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170). Opening CMake projects with **Open Folder** automatically configures the environment for C++ editing, building, and debugging.
  * C++ IntelliSense works without the need to create a CppProperties.json file in the root folder. We added a new dropdown to allow users to easily switch between configurations provided by CMake and CppProperties.json files.
  * Further configuration is supported via a CMakeSettings.json file that sits in the same folder as the CMakeLists.txt file.
![CMake Open Folder.](https://learn.microsoft.com/en-us/cpp/overview/media/cmake-cpp.png?view=msvc-170)


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-7)
##### Visual Studio 2017 version 15.3
  * Support added for the CMake Ninja generator.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-154)
##### Visual Studio 2017 version 15.4
  * Support added for importing existing CMake caches.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-8)
##### Visual Studio 2017 version 15.5
  * Support added for CMake 3.11, code analysis in CMake projects, Targets view in Solution Explorer, options for cache generation, and single file compilation. For more information, see [CMake Support in Visual Studio](https://devblogs.microsoft.com/cppblog/cmake-support-in-visual-studio-targets-view-single-file-compilation-and-cache-generation-settings/) and [CMake projects in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#windows-desktop-development)
