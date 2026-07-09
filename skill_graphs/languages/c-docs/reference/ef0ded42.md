## Visual Studio graphics diagnostics
Visual Studio Graphics Diagnostics tools: You can use them to record and analyze rendering and performance problems in Direct3D apps. Use them on apps that run locally on your Windows PC, in a Windows device emulator, or on a remote PC or device.
  * **Input & Output for Vertex and Geometry shaders:** The ability to view input and output of vertex shaders and geometry shaders has been one of the most requested features. It's now supported in the tools. Select the VS or GS stage in the Pipeline Stages view to start inspecting its input and output in the table below.
![Input/Output for shaders.](https://learn.microsoft.com/en-us/cpp/overview/media/io-shaders.png?view=msvc-170)
  * **Search and filter in the object table:** Provides a quick and easy way to find the resources you're looking for.
![Screenshot of the Object Table section with the Type drop-down and Search text box called out.](https://learn.microsoft.com/en-us/cpp/overview/media/search.png?view=msvc-170)
  * **Resource History:** This new view provides a streamlined way of seeing the entire modification history of a resource as it was used during the rendering of a captured frame. To invoke the history for any resource, click the clock icon next to any resource hyperlink.
![Resource history.](https://learn.microsoft.com/en-us/cpp/overview/media/resource-history.png?view=msvc-170)
It displays the new **Resource History** tool window, populated with the change history of the resource.
![Resource history change.](https://learn.microsoft.com/en-us/cpp/overview/media/resource-history-change.png?view=msvc-170)
You can capture frames with full call stack capturing enabled. That lets you quickly deduce the context of each change event, and inspect it within your Visual Studio project. Set the full stack capture option in the Visual Studio **Tools > Options** dialog under **Graphics Diagnostics**.
  * **API Statistics:** View a high-level summary of API usage in your frame. It's handy for discovering calls you might not realize you're making at all, or calls you're making too often. This window is available via **View > API Statistics** in Visual Studio Graphics Analyzer.
![API stats.](https://learn.microsoft.com/en-us/cpp/overview/media/api-stats.png?view=msvc-170)
  * **Memory Statistics:** View how much memory the driver allocates for the resources you create in the frame. This window is available via **View > Memory Statistics** in **Visual Studio Graphics Analyzer**. To copy data to a CSV file for viewing in a spreadsheet, right-click and choose **Copy All**.
![Memory stats.](https://learn.microsoft.com/en-us/cpp/overview/media/memory-stats.png?view=msvc-170)
  * **Frame Validation:** The new errors and warnings list provides an easy way to navigate your event list based on potential issues detected by the Direct3D debug layer. Click **View > Frame Validation** in Visual Studio Graphics Analyzer to open the window. Then click **Run Validation** to start the analysis. It can take several minutes to complete, depending on the frame's complexity.
![Frame validation.](https://learn.microsoft.com/en-us/cpp/overview/media/frame-validation.png?view=msvc-170)
  * **Frame Analysis for D3D12:** Use Frame Analysis to analyze draw-call performance with directed "what-if" experiments. Switch to the Frame Analysis tab and run analysis to view the report.
![Frame analysis.](https://learn.microsoft.com/en-us/cpp/overview/media/frame-analysis.png?view=msvc-170)
  * **GPU Usage Improvements:** Open traces can be taken via the Visual Studio GPU Usage profiler with either GPUView or the Windows Performance Analyzer (WPA) tool for more detailed analysis. If you have the Windows Performance Toolkit installed, there are two hyperlinks: one for WPA and another for GPUView, at the bottom right of the session overview.
![GPU usage.](https://learn.microsoft.com/en-us/cpp/overview/media/gpu-usage.png?view=msvc-170)
Traces you open in GPUView via this link support synchronized VS and GPUView timeline zooming and panning. A checkbox in VS controls whether synchronization is enabled or not.
![GPUView.](https://learn.microsoft.com/en-us/cpp/overview/media/gpu-view.png?view=msvc-170)


* * *
