## What's new for C++ in Visual Studio version 17.12
_Released November 2024_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.12](https://devblogs.microsoft.com/cppblog/whats-new-for-c-developers-in-visual-studio-2022-17-12/)
Standard Library (STL) merged C++26 and C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.12 IDE | [Visual Studio 2022 version 17.12 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.12)
C++ language conformance improvements in Visual Studio 2022 17.12 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.12](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1712)
A quick highlight of some of the new features:
  * **Standard Library Enhancements**
    * C++23 Formatting ranges (`stack`, `queue`, and `priority_queue`.
    * Added multidimensional subscript operators, which also support `<mdspan>`. For example: `print("m[{}, {}]: '{}'; ", i, j, m[i, j])`.
  * **Game development in C++**
    * Directly open Unreal Engine projects in Visual Studio without having to generate a Visual Studio solution file wrapping the Unreal Engine project. For more information, see [Work with Unreal Engine projects in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-quickstart).
    * You can specify the command line arguments to pass when debugging directly from the toolbar. For more information, see [Set command line arguments for Unreal Engine projects](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-quickstart#set-command-line-arguments).  ![A screenshot of the command-line argument dropdown. It contains one command line argument: -graphicsadaptor=0.](https://learn.microsoft.com/en-us/cpp/overview/media/command-line-argument-dropdown.png?view=msvc-170)
  * **Build Insights**
    * You can run Build Insights on selected files. Select the files you want in the **Solution Explorer** , right-click, and choose **Run Build Insights on Selected Files** :  ![A screenshot of files in the Solution Explorer. The context menu is open and the option to Run Build Insights on Selected Files is highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/build-insights-run-on-selected-files.png?view=msvc-170)
    * You can filter Build Insights results by project. Click the filter button on the filter column header and select the projects you want to see results for:  ![A screenshot of the Build Insights window with the Included Files tab open. The filter button was selected and a list of projects appears. Checkboxes next to Two projects are checked.](https://learn.microsoft.com/en-us/cpp/overview/media/build-insights-filter-by-project.png?view=msvc-170)
    * Clicking the question mark icon in the Build Insights window to see a short description for the tabs in the Build Insights window, and a link to the documentation for a detailed explanation:  ![A screenshot of the Build Insights window with the view explanations button \(a question mark in a circle\) highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/build-insights-view-explanations.png?view=msvc-170)
  * **GitHub Copilot**
    * You can click **Ask Copilot** next to the value of a variable to get AI-driven insights into what led to its current state. For example, the following program has an off-by-one error in its loop condition:
![A screenshot of the Autos window. The variable named it is NULL. The Ask Copilot icon next to it is highlighted.](https://learn.microsoft.com/en-us/cpp/overview/media/copilot-smart-variable-inspection.png?view=msvc-170)
The code that caused this problem is: for (auto it = h.animals_.begin(); it <= h.animals_.end(); it++).
`it` variable, it tells you why it is `<NULL>`:
![A screenshot of a GitHub Copilot window.](https://learn.microsoft.com/en-us/cpp/overview/media/copilot-smart-variable-explanation.png?view=msvc-170)
This error is inside a function defined as int calculate_number_of_cats(const house& h). The GitHub Copilot message says: "The value of the expression it is NULL, which means that the iterator is not pointing to any valid element in the vector animals_. In the context of your program, it is supposed to iterate over the animals_ vector in the house object to count the number of cat objects. Why it is null. Based on the locals and call stack context: the house object h has an empty animals_ vector (size=0). The loop condition it <= h.animals_.end() is incorrect. It should be it != h.animals_.end()."
    * You can click **Ask Copilot** about errors in the Visual Studio **Error List** to get help on the error and a suggested fix. For example:
![A screenshot of the Error List window.](https://learn.microsoft.com/en-us/cpp/overview/media/copilot-fix-my-code.png?view=msvc-170)
The Ask Copilot icon is highlighted next to an error that unique_ptr is attempting to reference a deleted function.
![A screenshot of the GitHub Copilot explanation for the error.](https://learn.microsoft.com/en-us/cpp/overview/media/copilot-fix-my-code-suggestion.png?view=msvc-170)
The Copilot message says: "The error occurs because the range-based for loop was attempting to copy std::unique_ptr objects, which is not allowed since std::unique_ptr cannot be copied. To fix this, I changed the loop to use a reference to avoid copying the std::unique_ptr objects. This way, the loop iterates over references to the std::unique_ptr objects, which is allowed."
  * **Debugging**
    * New debug visualizers for `mutex`, `recursive_mutex`, and `move_iterator`.
    * The debugger now displays return values inline:  ![A screenshot of a tooltip showing the value 8.25. It's the result of the expression following the return statement that was stepped over.](https://learn.microsoft.com/en-us/cpp/overview/media/debugger-inline-return-values.png?view=msvc-170)


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-1711)
