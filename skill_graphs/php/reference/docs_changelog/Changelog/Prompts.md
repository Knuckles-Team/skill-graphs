## Prompts
### Add `number` Prompt
Pull request by
A new `number` [prompt](https://laravel.com/docs/prompts) makes it easy to collect numeric input with validation baked in, perfect for CLI setup flows and interactive tooling. Features automatic clamping of the min/max values and adjusting the value via the up and down arrows.
```


1$retries = number('How many retries?', default: 3, min: 0, max: 10);




$retries = number('How many retries?', default: 3, min: 0, max: 10);

```

## Prompts
### Add Grid Component
Pull request by
The new `grid` component in [Prompts](https://laravel.com/docs/prompts) allows developers to easily create responsive grid-based layouts and present data clearly.
## Prompts
### Improve Display of Progress Bars With High Step Counts
Pull request by
![New progress display](https://laravel.com/images/changelog/2025-09/progress-after.png)
The display of the progress bar when using a large number of steps is improved by adding thousands separators and extra spacing.
