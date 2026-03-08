## Other libraries
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#open-source-library-support)
### Open-source library support
**Vcpkg** is an open-source command-line tool that greatly simplifies the process of acquiring and building open-source C++ static libs and DLLS in Visual Studio. For more information, see [vcpkg](https://learn.microsoft.com/en-us/vcpkg/).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#cpprest-sdk-290)
### CPPRest SDK 2.9.0
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-5)
##### Visual Studio 2017 version 15.5
The CPPRestSDK, a cross-platform web API for C++, is updated to version 2.9.0. For more information, see [CppRestSDK 2.9.0 is available on GitHub](https://devblogs.microsoft.com/cppblog/cpprestsdk-2-9-0-is-available-on-github/).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#atl)
### ATL
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-6)
##### Visual Studio 2017 version 15.5
  * Yet another set of name-lookup conformance fixes
  * Existing move constructors and move assignment operators are now properly marked as nonthrowing
  * Unsuppress valid warning C4640 about thread safe init of local statistics in atlstr.h
  * Thread-safe initialization of local statistics was automatically turned off in the XP toolset when using ATL to build a DLL. Now it's not. You can add **`/Zc:threadSafeInit-`**in your Project settings if you don't want thread-safe initialization.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-c-runtime)
### Visual C++ runtime
  * New header "cfguard.h" for Control Flow Guard symbols.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-c-ide)
