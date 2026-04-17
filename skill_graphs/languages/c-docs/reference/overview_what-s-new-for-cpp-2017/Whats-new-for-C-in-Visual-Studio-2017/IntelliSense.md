## IntelliSense
  * The new SQLite-based database engine is now being used by default. The new engine speeds up database operations like **Go To Definition** and **Find All References**. It significantly improves initial solution parse time. The setting moved to **Tools > Options > Text Editor > C/C++ > Advanced**. (It was formerly under ...C/C++ > Experimental.)
  * We've improved IntelliSense performance on projects and files not using precompiled headers - an Automatic Precompiled Header is created for headers in the current file.
  * We've added error filtering and help for IntelliSense errors in the error list. Clicking on the error column now allows for filtering. Also, clicking on the specific errors or pressing F1 launches an online search for the error message.
![Error List.](https://learn.microsoft.com/en-us/cpp/overview/media/errorlist1.png?view=msvc-170)
![Error List Filtered.](https://learn.microsoft.com/en-us/cpp/overview/media/errorlist2.png?view=msvc-170)
  * Added the ability to filter Member List items by kind.
![Member List Filtering.](https://learn.microsoft.com/en-us/cpp/overview/media/mlfiltering.png?view=msvc-170)
  * Added a new experimental Predictive IntelliSense feature that provides contextually aware filtering of what appears in the Member List. For more information, see [C++ IntelliSense Improvements - Predictive IntelliSense & Filtering](https://devblogs.microsoft.com/cppblog/c-intellisense-improvements-predictive-intellisense-filtering/).
  * **Find All References** (Shift+F12) now helps you get around easily, even in complex codebases. It provides advanced grouping, filtering, sorting, searching within results, and (for some languages) colorization, so you can get a clear understanding of your references. For C++, the new UI includes information about whether we're reading from or writing to a variable.
  * The Dot-to-Arrow IntelliSense feature moved from experimental to advanced, and is now enabled by default. The editor features **Expand Scopes** and **Expand Precedence** moved from experimental to advanced.
  * The experimental refactoring features **Change Signature** and **Extract Function** are now available by default.
  * Added an experimental 'Faster project load' feature for C++ projects. The next time you open a C++ project it will load faster, and the time after that it will load _much_ faster!
  * Some of these features are common to other languages, and some are specific to C++. For more information about these new features, see [Announcing Visual Studio "15" Preview 5](https://devblogs.microsoft.com/visualstudio/announcing-visual-studio-15-preview-5/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-157-3)
##### Visual Studio 2017 version 15.7
  * Support added for ClangFormat. For more information, see [ClangFormat Support in Visual Studio 2017](https://devblogs.microsoft.com/cppblog/clangformat-support-in-visual-studio-2017-15-7-preview-1/).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#non-msbuild-projects-with-open-folder)
