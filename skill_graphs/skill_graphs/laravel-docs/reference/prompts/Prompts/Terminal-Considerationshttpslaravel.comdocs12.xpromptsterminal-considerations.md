## [Terminal Considerations](https://laravel.com/docs/12.x/prompts#terminal-considerations)
#### [Terminal Width](https://laravel.com/docs/12.x/prompts#terminal-width)
If the length of any label, option, or validation message exceeds the number of "columns" in the user's terminal, it will be automatically truncated to fit. Consider minimizing the length of these strings if your users may be using narrower terminals. A typically safe maximum length is 74 characters to support an 80-character terminal.
#### [Terminal Height](https://laravel.com/docs/12.x/prompts#terminal-height)
For any prompts that accept the `scroll` argument, the configured value will automatically be reduced to fit the height of the user's terminal, including space for a validation message.
