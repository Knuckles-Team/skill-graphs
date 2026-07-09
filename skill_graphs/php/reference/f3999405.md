## VS Code Extension
### Test Runner Integration
Pull request by
Integrating with VS Code's built-in test runner makes it easier to run and iterate on your suite from within your IDE, shortening the edit-test loop and helping you stay in flow.
![Browsing tests in VS Code](https://github.com/user-attachments/assets/d819be37-93e5-4dc3-9f2d-a2afc5c44bde)
### Livewire Props
Pull request by
New support for hovering over Livewire 3 and 4 props means that you can see the relevant type and docblock information directly from the PHP class, reducing context switching in your Livewire and Blade components.
![Livewire prop hovering in VS Code](https://github.com/user-attachments/assets/40c0ba1a-6446-4dee-b03a-185c43f110e0)
## VS Code Extension
### Livewire 4 Support
Pull request by
First-class Livewire 4 support in the extension helps you stay in flow with better editor understanding as you build components: less context switching, more shipping.
### Docker Support
Pull request by
Improved Docker support makes Laravel development inside containers feel more natural in VS Code, helping teams standardize environments and reduce "works on my machine" friction.
### Add Markdown Hover Links for Scopes to the Implementation
Pull request by
Hover links turn query scopes into a navigable experience, jumping from usage to implementation faster, which is especially valuable in large codebases with lots of shared scopes.
### Support for Laravel Attributes
Pull request by
Better attribute support helps the editor understand modern Laravel patterns, improving navigation and reducing false positives. If your project leans on PHP attributes, this makes day-to-day editing noticeably smoother.
### Integration Artisan Make Commands with VS Code Explorer
Pull request by
Generate files where you're already working: integrating `artisan make:*` into the explorer and context menu cuts down on terminal hopping and keeps scaffolding close to your project structure.
### Support for Autocompletion Rules in `FormRequest`
Pull request by
Smarter autocomplete for `FormRequest` [validation rules](https://laravel.com/docs/validation#available-validation-rules) means fewer typos and faster validation authoring, which is particularly helpful when you're juggling complex rule sets.
### Add Scope Parameters to the Repository and Docblock Generator
Pull request by
Docblocks and repository hints that include scope parameters improve autocomplete accuracy and make "discoverability" better for teammates, so using existing scopes becomes as easy as reading the method signature.
## VS Code Extension
### Add Scope Parameters to the Repository and Docblock Generator
Pull request by
Model scope parameters now appear in model helper docblocks, making it clear to the user which parameters are required by the query scopes they are using.
### Add a Command That Generates Namespace
Pull request by
A new "Generate Namespace" command was added to the extension, allowing the user to quickly generate the correct namespace for a class.
## VS Code Extension
### Add Commands That Refactor Class Attributes in Blade Files
Pull request by
![Refactor class attributes](https://laravel.com/images/changelog/2025-09/vs-code-refactor-class-attributes.gif)
Commands are now available that refactor the selected or all class attributes to the `@class` directive.
### Add a Command That Wraps Selected Text With a Helper
Pull request by
![Wrap with helper](https://laravel.com/images/changelog/2025-09/vs-code-wrap-with-helper.gif)
Commands are now available that wrap the selected text with a helper, such as `dd`, `collect`, `dump`, and `str`.
### Pint Commands + Run Pint on Save
Pull request by
Commands are now available to "Run Pint", "Run Pint on Dirty Files", and "Run Pint on Current File". There is also now an optiont to run Pint on save for the current file.
## VS Code Extension
### Add DDEV Support
Pull request by
Adds proper support for DDEV, Docker-based PHP environments.
### Add Support for Custom View Extensions
Pull request by
The extension now recognizes custom registered view extensions such as `.blade.sh` or `.blade.ts` and will now autocomplete and link correctly to these files.
### Support for Configs in Subfolders
Pull request by
The extension now supports configs in nested subfolders (e.g. `config/foo/bar/baz.php`), providing better autocomplete and linking.
### Link Directly to Problem Files
Pull request by
Now, when the extension warns you about an invalid value, such as a config key, the warning will directly link you to the file where you can fix the issue.
### Autocompletion for `Route::is` and `routeIs` Methods
Pull request by
Full autocomplete and linking support for the `Route::is` and `routeIs` methods.
## VS Code Extension
![VS Code Performance Improvements](https://laravel.com/images/changelog/2025-06/vs-code-performance-improvements.png)
### Memory Improvements
Pull request by
We fixed a memory-leak issue in the extension’s background processes, reducing its long-term footprint and preventing slowdowns during extended coding sessions.
### Improved Startup Time
Pull request by
Initialization with the VS Code extension now completes in under one second (down from 5–7 seconds) by deferring heavy setup until it’s actually needed. You’ll notice the extension loads almost instantly so you can start building faster.
Get started with the
