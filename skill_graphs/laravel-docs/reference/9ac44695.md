## Pint
### Adds an `agent` Format
Pull request by
A new `--format agent` flag was added that gets automatically used when [Pint](https://laravel.com/docs/pint) is executed within OpenCode or Claude Code.
The default Pint output is designed for humans: colorful, with progress dots and formatted summaries. AI agents need something different: structured JSON they can reliably parse, unambiguous status values like `"status":"pass"` instead of inferring from formatted text, minimal output that saves context window and reduces token cost, and deterministic results without ANSI colors or formatting noise.
## Pint
### Added `--parallel` Option
Pull request by
```


1./vendor/bin/pint --parallel




./vendor/bin/pint --parallel

```

By leveraging PHP CS Fixer’s parallel runner, [Pint](https://laravel.com/docs/12.x/pint) now formats files concurrently. On large codebases that once took minutes, you’ll see results in seconds, speeding up both local workflows and CI pipelines for a clear quality of life win.
