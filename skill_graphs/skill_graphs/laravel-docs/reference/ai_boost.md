Not sure when to use AI SDK, Boost, or MCP?[Read the breakdown](https://laravel.com/blog/laravel-ai-sdk-boost-or-mcp-which-tool-do-you-need)
Dismiss
[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * Events
  * [Docs](https://laravel.com/docs)


Sign in
[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * [Events](https://laravel.com/community)
  * [Docs](https://laravel.com/docs)


  * [Overview](https://laravel.com/)
  * [Starter Kits](https://laravel.com/starter-kits)
  * [Release Notes](https://laravel.com/docs/releases)
  * [Documentation](https://laravel.com/docs)
  * [Laravel Learn](https://laravel.com/learn)


  * [Laravel Cloud](https://cloud.laravel.com)
  * [Forge](https://forge.laravel.com)
  * [Nightwatch](https://nightwatch.laravel.com)
  * [Nova](https://nova.laravel.com)


  * [Blog](https://laravel.com/blog)
  * [Careers](https://laravel.com/careers)
  * [Trust](https://trust.laravel.com)
  * [Legal](https://laravel.com/legal)
  * [Status](https://status.laravel.com)


Search docs
Search`K`
`⌘K`
AI Tools
[ AI SDK  ](https://laravel.com/ai) [ Boost  ](https://laravel.com/ai/boost) [ MCP  ](https://laravel.com/ai/mcp)
#  Boost your development with Laravel’s AI assistant
Laravel Boost accelerates AI-assisted development by providing the essential context and structure
that AI needs to generate high-quality, Laravel-specific code using any agent.
[ View documentation ](https://laravel.com/docs/12.x/boost)
  * UserController.php
  * users.tsx


```


 1class UserController




 2{




 3    public function index()




 4    {




 5        $users = User::active()




 6            ->orderByName()




 7            ->get(['id', 'name', 'email']);




 8 




 9        return Inertia::render('Users', [




10            'users' => $users,




11        ]);




12    }




13}




class UserController
{
    public function index()
    {
        $users = User::active()
            ->orderByName()
            ->get(['id', 'name', 'email']);

        return Inertia::render('Users', [
            'users' => $users,
        ]);
    }
}

```
```


 1export default ({ users }) => {




 2    return (




 3        <div>




 4            <h1>Users</h1>




 5            <ul>




 6                {users.map((user) => (




 7                    <li key={user.id}>{user.name}</li>




 8                ))}




 9            </ul>




10        </div>




11    );




12};




export default ({ users }) => {
    return (
        <div>
            <h1>Users</h1>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
};

```

  * UserController.php
  * users.tsx


```


 1class UserController




 2{




 3    public function index()




 4    {




 5        $users = User::active()




 6            ->orderByName()




 7            ->get(['id', 'name', 'email']);




 8 




 9        return Inertia::render('Users', [




10            'users' => $users,




11        ]);




12    }




13}




class UserController
{
    public function index()
    {
        $users = User::active()
            ->orderByName()
            ->get(['id', 'name', 'email']);

        return Inertia::render('Users', [
            'users' => $users,
        ]);
    }
}

```
```


 1export default ({ users }) => {




 2    return (




 3        <div>




 4            <h1>Users</h1>




 5            <ul>




 6                {users.map((user) => (




 7                    <li key={user.id}>{user.name}</li>




 8                ))}




 9            </ul>




10        </div>




11    );




12};




export default ({ users }) => {
    return (
        <div>
            <h1>Users</h1>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
};

```

White screen issue when listing users
I get a white screen in the browser when listing users
I'll help you debug the white screen issue when listing users. Let me first understand the current state of your application and then investigate what might be causing this problem.
To-Dos 5
Investigate white screen issue when listing users
Check routes configuration for user listing
Examine controllers and views for user listing
Check browser logs for JavaScript errors
Check Laravel application logs for errors
Called application-info
Called list-routes
Called browser-logs
Read UserController.php
Called application-info
Laravel Boost By Numbers
v2.2.3
1 day ago
72
Contributors
3320
GitHub Stars
7
Open PRs
Accurate AI development
Boost powers 15 specialized tools to scan your codebase, read logs, run queries, extract configs, perform commands and much more.
![Accurate AI development](https://laravel.com/images/ai/boost/ai-tools.svg) ![Accurate AI development](https://laravel.com/images/ai/boost/ai-tools-dark.svg)
Powerful Documentation API
Boost searches both the Laravel documentation and package knowledge bases to deliver the most current best practices and up-to-date information.
![Powerful Documentation API](https://laravel.com/images/ai/boost/documentation-api.png) ![Powerful Documentation API](https://laravel.com/images/ai/boost/documentation-api-dark.webp)
##  Powerful tools at your fingertips
###  Application Info
Reads PHP & Laravel versions, database engine, ecosystem packages, and Eloquent models
###  Database Schema
Inspects and reads your complete database schema with intelligent analysis
###  Database Queries
Executes queries against your database directly from your AI assistant
###  Route Inspector
Inspects and analyzes your application's routes for better navigation
###  Artisan Commands
Lists and inspects available Artisan commands for streamlined development
###  Tinker Integration
Executes suggested code within the context of your Laravel application
###  Configuration Access
Gets configuration values and available keys for more accurate code generation
###  Documentation Search
Queries Laravel's hosted documentation API fine-tuned to your installed packages
###  Error Tracking
Reads application logs, browser errors, and tracks the last encountered issues
##  Setup your editor and start using Boost today
Step 1
$ composer require laravel/boost --dev
Copied
Step 2
$ php artisan boost:install
Copied
Step 3
PhpStorm GithubCopilot Copilot (VS Code) Cursor Claude Code Codex CLI Gemini CLI Manual Install
  1. Press shift twice to open the command palette
  2. Search "MCP Settings" and press enter
  3. Check the box next to laravel-boost
  4. Click 'Apply' at the bottom right
  5. If you see a green checkmark, you're ready to go!


  1. Open the Command Palette Cmd+Shift+P or Ctrl+Shift+P
  2. Press enter on "MCP: List Servers"
  3. Arrow to laravel-boost and press enter
  4. Choose 'Start server' and you're good to go!


  1. Open the Command Palette Cmd+Shift+P or Ctrl+Shift+P
  2. Press enter on "/open MCP Settings"
  3. Turn the toggle on for laravel-boost


  1. Claude is enabled automatically, but if you find it isn't
  2. Open a shell in the project's directory
  3. Run claude mcp add -s local -t stdio laravel-boost php artisan boost:mcp


  1. Codex support is typically enabled automatically, but if you find it isn't
  2. Open a shell in the project's directory
  3. Run codex mcp add -- php artisan boost:mcp


  1. Gemini support is typically enabled automatically, but if you find it isn't
  2. Open a shell in the project's directory
  3. Run gemini mcp add -s project -t stdio laravel-boost php artisan boost:mcp


  1. Run php artisan boost:mcp


Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
