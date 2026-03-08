##  [What happens when you archive](https://vercel.com/docs/flags/vercel-flags/quickstart#what-happens-when-you-archive)[](https://vercel.com/docs/flags/vercel-flags/quickstart#what-happens-when-you-archive)
When you archive a flag:
  1. Evaluation stops: The flag is no longer served by the SDK
  2. Your application falls back: It uses the default value defined in code
  3. Configuration is preserved: All variants, rules, and targeting settings are saved
  4. The flag moves to Archive: It no longer appears in the main flags list


If your code doesn't define a default value for the flag, evaluation will throw an error. Make sure your flag definitions include a `defaultValue` or handle missing flags gracefully.
flags.ts
```
export const archivedFeature = flag({
  key: 'archived-feature',
  adapter: vercelAdapter(),
  // This default is used when the flag is archived
  defaultValue: false,
});
```
