## Boost
### Added Support for Loading Guidelines and Skills Directly from Vendor Packages
Pull request by
Guidelines and skills can now be loaded directly from vendor packages, ensuring that guidelines always match the package version you are using and will never go stale.
### Add Support for Nightwatch MCP
Pull request by
Nightwatch MCP support improves the integration story for observability-driven workflows, so you can connect monitoring context to your tools more seamlessly.
### Enhance Database-Schema Tool with Full Column Metadata
Pull request by
The database schema tool now exposes richer column metadata, which improves the quality of schema-aware tooling and reduces incorrect assumptions (types, defaults, nullability).
This is particularly helpful when generating code, validating migrations, or building assistants that reason about your database structure.
## Boost
### Boost 2.0
We shipped Skills in Laravel
This update transitions many package guidelines into agent skills, enabling significantly better context management. By loading package-specific knowledge only when it is relevant, agents produce more accurate, higher-quality Laravel code with far less context noise. This is a must-have upgrade for getting the best results from AI agents when building Laravel applications.
As a result, existing guidelines are now roughly ~ 40 percent leaner, making agent responses more focused and much higher quality.
### Add Laravel Code Simplifier Prompt
Pull request by
A dedicated "code simplifier" prompt helps you quickly turn verbose or repetitive Laravel code into clean, idiomatic patterns, great for polishing PRs and accelerating refactors when you're moving fast.
### Add Livewire 4 Upgrade Prompt
Pull request by
Upgrading is easier when you have a focused guide. This prompt helps you identify the key changes for Livewire 4 and work through them systematically, reducing upgrade risk and cutting down on "why did this break?" time.
## Boost
### Add Resource and Prompts for Package Guidelines
Pull request by
Previously, all third-party package guidelines needed to be added to the global context, which could grow unbounded as more packages were integrated.
Boost is now reducing global context bloat by adding guidelines for only actively used packages that are loaded, thereby improving token efficiency and leaving room for more application-specific information.
## Boost
### Add Gemini
Pull request by
Google's
### Put User-Defined Guidelines at the Top
Pull request by
User guidelines now take precedence over the Boost presets while maintaining the overrides strategy, giving developers more control over how instructions are interpreted by agents.
### Add Sail Support in Guidelines
Pull request by
Sail now has first-class support across all guidelines. When a project installs Boost with Sail enabled, agent instructions now automatically switch to Sail-specific commands rather than native CLI commands.
### Remove Filament Guidelines
Pull request by
With the new
### Add OpenCode Support
Pull request by
Developers now have seamless integration of
## Boost
### Dynamic NPM Package Runner
Pull request by
Boost now detects which NPM package manager should be used to run any given script (`npm`, `pnpm`, `yarn` and `bun`). This assists the AI in using the correct CLI tools when running `npm` commands based on the project's existing dependencies.
### Add Support for Custom Code Environments
Pull request by
You can now create custom code environments (IDEs and AI agents) for Boost. Previously, Boost only supported a hardcoded list of environments, which made it difficult to add support for new IDEs or agents directly within the official Boost repository.
```


1use Laravel\Boost\Contracts\Agent;




2use Laravel\Boost\Contracts\McpClient;




3use Laravel\Boost\Install\CodeEnvironment\CodeEnvironment;




4 



5class MyCustomIDE extends CodeEnvironment implements Agent, McpClient




6{




7    // Implementation




8}




use Laravel\Boost\Contracts\Agent;
use Laravel\Boost\Contracts\McpClient;
use Laravel\Boost\Install\CodeEnvironment\CodeEnvironment;

class MyCustomIDE extends CodeEnvironment implements Agent, McpClient
{
    // Implementation
}

```

Registering your custom code environment:
```


1use Laravel\Boost\Boost;




2 



3Boost::registerCodeEnvironment('myide', MyCustomIDE::class);




use Laravel\Boost\Boost;

Boost::registerCodeEnvironment('myide', MyCustomIDE::class);

```

## Boost
### [1.x] Adds `boost:update` + Allows Package Authors to Publish Guidelines
Pull request by
Boost can now self-update with the new `boost:update` command. In addition, third-party packages can now auto-register their own guidelines by including a `resources/boost/guidelines/core.blade.php` file in their package.
### Allow Guideline Overriding
Pull request by
Users can now override guideline files, specifying that Boost should use their guidelines in specific instances instead of the default guidelines that come with Boost.
## Boost
### Add `enabled` Option to Config
Pull request by
Adds a `config('boost.enabled')` option to allows users to specifically enable/disable Boost in certain scenarios outside of environment constraints.
### Update Pint Guideline to Use `--dirty` Flag
Pull request by
Updates Boost guidelines to prefer the usage of Pint with the `--dirty` flag for cleaner diffs and PRs.
