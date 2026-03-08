## What's new for C++ in Visual Studio version 16.2
For a summary of new features and bug fixes in Visual Studio version 16.2, see [What's New in Visual Studio 2019 version 16.2](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.2).
  * For local CMake projects configured with Clang, Code Analysis now runs clang-tidy checks, appearing as part of background code analysis as in-editor warnings (squiggles) and in the Error List.
  * Updated the `<charconv>` header for C++17's
    * Added floating-point `to_chars()` overloads for `chars_format::fixed` and `chars_format::scientific` precision (`chars_format::general precision` is the only part not yet implemented)
    * Optimized `chars_format::fixed` shortest
  * Added these C++20 Standard Library features:
    * Available under **`/std:c++latest`**(or**`/std:c++20`**starting in Visual Studio 2019 version 16.11):
      * `atomic<floating-point>`
      * `char8_t` type for UTF-8 characters and strings
      * `to_address()` for converting a pointer to a raw pointer
    * Available under `/std:c++17` and `/std:c++latest` (or **`/std:c++20`**starting in Visual Studio 2019 version 16.11):
      * `[[nodiscard]]` in the library
    * Available unconditionally:
      * `<version>` header
      * `std::function` move constructor should be `noexcept`
  * Windows SDK is no longer a dependency for the CMake for Windows and CMake for Linux components.
  * Improvements to the **`/DEBUG:FAST`**and**`/INCREMENTAL`**times are on average twice as fast, and**`/DEBUG:FULL`**is now three to six times faster.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-161)
