## What's new for C++ in Visual Studio version 16.10
For a summary of new features and bug fixes in Visual Studio version 16.10, see [What's New in Visual Studio 2019 version 16.10](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.10).
  * All C++20 features are now available under [`/std:c++latest`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170). While MSVC's implementation of the C++20 standards (as currently published by ISO) is feature complete, some key C++20 library features are expected to be amended by upcoming Defect Reports (ISO C++20 bug fixes) that may change them in an ABI-incompatible way. Please see
    * C++20 immediate functions & constinit support added in 16.10
    * The final pieces of `<chrono>`: new clocks, leap seconds, time zones, and parsing
    * Implementation of `<format>` for text formatting
  * [`/openmp:llvm`](https://learn.microsoft.com/en-us/cpp/build/reference/openmp-enable-openmp-2-0-support?view=msvc-170) is now available on x86 and ARM64, in addition to x64
  * Include directories can now be designated as external with customized compilation warning levels and code analysis settings.
  * Added the [`/await:strict`](https://learn.microsoft.com/en-us/cpp/build/reference/await-enable-coroutine-support?view=msvc-170) option to enable C++20-style coroutines in earlier language modes.
  * Debugger visualization of `std::coroutine_handle<T>` now displays the original coroutine function name and signature and the current suspend point.
  * Added support for
  * You're now required to accept or deny the host key fingerprint presented by the server when adding a new remote connection in Visual Studio.
  * Added an [`/external`](https://learn.microsoft.com/en-us/cpp/build/reference/external-external-headers-diagnostics?view=msvc-170) switch to MSVC for specifying headers which should be treated as external for warning purposes.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-169)
