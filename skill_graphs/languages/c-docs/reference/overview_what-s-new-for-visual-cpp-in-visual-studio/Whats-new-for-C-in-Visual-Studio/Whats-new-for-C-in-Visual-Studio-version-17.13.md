## What's new for C++ in Visual Studio version 17.13
_Released February 2025_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.13](https://devblogs.microsoft.com/cppblog/whats-new-for-c-developers-in-visual-studio-2022-17-13/)
Standard Library (STL) C++26 and C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the IDE | [Visual Studio 2022 version 17.13 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.13)
C++ language updates | [MSVC compiler updates in Visual Studio 2022 17.13](https://devblogs.microsoft.com/cppblog/msvc-compiler-updates-in-visual-studio-2022-version-17-13/)
C++ language conformance improvements | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.13](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1713)
A quick highlight of some new features:
  * **C++ language enhancements**
    * Try out C++23 preview features by setting the C++ Language Standard to `/std:c++23preview`. This setting enables the latest C++23 features and bug fixes. For more information, see [/std (Specify Language Standard Version)](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170#stdc23preview).
    * Support for C++23’s `size_t` literal suffix, which helps avoid truncations or signed comparison mismatches--especially when writing loops. For example:
C++
Copy
```
// Infinite loop if v.size > max unsigned int
for (auto i = 0u; i < v.size(); ++i)
{
  ...
}

// Fixed because of uz literal
for (auto i = 0uz; i < v.size(); ++i)
{
  ...
}

```

    * Support for vector lengths for code generation on x86 and x64. For more information, see [/vlen](https://learn.microsoft.com/en-us/cpp/build/reference/vlen?view=msvc-170).
    * Support for Intel Advanced Vector Extensions 10 version 1. For more information about `/arch:AVX10.1`, see [/arch (x64)](https://learn.microsoft.com/en-us/cpp/build/reference/arch-x64?view=msvc-170).
  * **Standard Library enhancements**
    * Standard library support for coroutines. In this example from `fib` function is a coroutine. When the `co_yield` statement is executed, `fib` is suspended and the value is returned to the caller. You can resume the `fib` coroutine later to produce more values without requiring any manual state handling:
C++
Copy
```
std::generator<int> fib()
{
  auto a = 0, b = 1;

  while (true)
  {
      co_yield std::exchange(a, std::exchange(b, a + b));
  }
}

int answer_to_the_universe()
{
  auto rng = fib() | std::views::drop(6) | std::views::take(3);
  return std::ranges::fold_left(std::move(rng), 0, std::plus{});
}

```

  * Moved `system_clock`, `high_resolution_clock`, and `chrono_literals` from a commonly included internal header to `<chrono>`. If you see compiler errors that types like `system_clock` or user-defined literals like `1729ms` aren't recognized, include `<chrono>`.
  * Improved the vectorized implementations of `bitset` constructors from strings, `basic_string::find_last_of()`, `remove()`, `ranges::remove`, and the `minmax_element()` and `minmax()` algorithm families.
  * Added vectorized implementations of:
    * `find_end()` and `ranges::find_end` for 1-byte and 2-byte elements.
    * `basic_string::find()` and `basic_string::rfind()` for a substring.
    * `basic_string::rfind()` for a single character.
  * Merged C++23 Defect Reports:
    * `<print>`.
    * `std::print` More types faster with less memory.
  * **GitHub Copilot**
    * GitHub Copilot Free is now available. Get 2,000 code completions and 50 chat requests per month at no cost.
    * GitHub Copilot code completions provide autocomplete suggestions inline as you code. To enhance the experience of C++ developers, GitHub Copilot includes other relevant files as context. This reduces errors while offering more relevant and accurate suggestions.
    * You can now request a code review from GitHub Copilot from the Git Changes window:
![A screenshot of the Git Changes window with the GitHub Copilot Review button highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/vs2022-copilot-git-changes-review.png?view=msvc-170)
The Git Changes window is open with the GitHub Copilot Review button highlighted.
GitHub Copilot looks for potential issues and creates comments for them:
![A screenshot of the GitHub Copilot explaining an issue.](https://learn.microsoft.com/en-us/cpp/overview/media/vs2022-copilot-comment-example.png?view=msvc-170)
GitHub Copilot found an issue with the line if ( is_enabled_) new_site.disable(). It says it may be a mistake and should likely be if ( is_enabled_) new_site.enable() because the intention seem to be enabling the new site if the breakpoint is enabled.
To use this feature, ensure the following are turned on:
      * **Tools** > **Options** > **Preview Features** > **Pull Request Comments**
      * **Tools** > **Options** > **GitHub** > **Copilot** > **Source Control Integration** > **Enable Git preview features**.
    * GitHub Copilot Edits is a new feature that can make changes across multiple files in your project. To start a new Edits session, click **Create new edit session** at the top of the GitHub Copilot Chat window:
![A screenshot of the GitHub Copilot Chat window. The Create new edit session button is highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/vs2022-copilot-edit-session.png?view=msvc-170)
Describe the changes you want to make and Copilot suggests relevant edits. You can preview the edits one-by-one and accept the ones you want or make corrections:
![A screenshot of the GitHub Copilot Chat window displaying the files it edited.](https://learn.microsoft.com/en-us/cpp/overview/media/vs2022-copilot-edit-session-example.png?view=msvc-170)
GitHub Copilot is displaying a summary of the changes it made, such as 1. Create a new subclass range_breakpoint in include/libsdb/breakpoint.hpp" and 2. Implement the range_breakpoint class in src/breakpoint.cpp. An option to accept the changes is displayed.
For more information, see [Iterate across multiple files more efficiently with GitHub Copilot Edits](https://devblogs.microsoft.com/visualstudio/iterate-across-multiple-files-more-efficiently-with-github-copilot-edits-preview/).
  * **CMake**
    * Now supports CMake Presets v9. New macro expansions in a preset's include field. For more information, see


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-1712)
