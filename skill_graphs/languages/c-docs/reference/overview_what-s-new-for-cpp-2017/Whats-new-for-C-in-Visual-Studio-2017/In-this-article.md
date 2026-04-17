##  In this article
  1. [Visual Studio 2017 C++ compiler](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-compiler)
  2. [C++ standard library](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#c-standard-library)
  3. [Other libraries](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#other-libraries)
  4. [Visual Studio 2017 C++ IDE](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-ide)
  5. [IntelliSense](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#intellisense)
  6. [Non-MSBuild projects with Open Folder](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#non-msbuild-projects-with-open-folder)
  7. [CMake support via Open Folder](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#cmake-support-via-open-folder)
  8. [Windows desktop development](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#windows-desktop-development)
  9. [Linux development with C++](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#linux-development-with-c)
  10. [Game development with C++](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#game-development-with-c)
  11. [Mobile development with C++ for Android and iOS](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#mobile-development-with-c-for-android-and-ios)
  12. [Universal Windows Apps](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#universal-windows-apps)
  13. [New options for C++ on Universal Windows Platform (UWP)](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#new-options-for-c-on-universal-windows-platform-uwp)
  14. [The Clang/C2 platform toolset](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#the-clangc2-platform-toolset)
  15. [C++ code analysis](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#c-code-analysis)
  16. [Unit testing in Visual Studio 2017](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#unit-testing-in-visual-studio-2017)
  17. [Visual Studio graphics diagnostics](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-graphics-diagnostics)

Show 13 more
Visual Studio 2017 brings many updates and fixes to the C++ environment. We've fixed over 250 bugs and reported issues in the compiler and tools. Many were submitted by customers through the [Report a Problem and Provide a Suggestion](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-report-a-problem-with-visual-studio?view=vs-2017&preserve-view=true) options under **Send Feedback**. Thank you for reporting bugs!
For more information on what's new in all of Visual Studio, see [What's new in Visual Studio 2017](https://learn.microsoft.com/en-us/visualstudio/ide/whats-new-visual-studio-2017?view=vs-2017&preserve-view=true). For information on what's new for C++ in Visual Studio 2019, see [What's new for C++ in Visual Studio 2019](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170&preserve-view=true&view=msvc-160). For information on what's new for C++ in Visual Studio 2015 and earlier versions, see [Visual C++ What's New 2003 through 2015](https://learn.microsoft.com/en-us/cpp/porting/visual-cpp-what-s-new-2003-through-2015?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-compiler)
##  In this article
  1. [Visual Studio 2017 C++ compiler](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-compiler)
  2. [C++ standard library](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#c-standard-library)
  3. [Other libraries](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#other-libraries)
  4. [Visual Studio 2017 C++ IDE](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-ide)
  5. [IntelliSense](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#intellisense)
  6. [Non-MSBuild projects with Open Folder](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#non-msbuild-projects-with-open-folder)
  7. [CMake support via Open Folder](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#cmake-support-via-open-folder)
  8. [Windows desktop development](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#windows-desktop-development)
  9. [Linux development with C++](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#linux-development-with-c)
  10. [Game development with C++](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#game-development-with-c)
  11. [Mobile development with C++ for Android and iOS](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#mobile-development-with-c-for-android-and-ios)
  12. [Universal Windows Apps](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#universal-windows-apps)
  13. [New options for C++ on Universal Windows Platform (UWP)](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#new-options-for-c-on-universal-windows-platform-uwp)
  14. [The Clang/C2 platform toolset](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#the-clangc2-platform-toolset)
  15. [C++ code analysis](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#c-code-analysis)
  16. [Unit testing in Visual Studio 2017](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#unit-testing-in-visual-studio-2017)
  17. [Visual Studio graphics diagnostics](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-graphics-diagnostics)

Show 8 more
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
