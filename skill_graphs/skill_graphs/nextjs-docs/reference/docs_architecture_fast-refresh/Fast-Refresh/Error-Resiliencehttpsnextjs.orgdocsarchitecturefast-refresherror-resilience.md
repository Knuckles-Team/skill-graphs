## Error Resilience[](https://nextjs.org/docs/architecture/fast-refresh#error-resilience)
### Syntax Errors[](https://nextjs.org/docs/architecture/fast-refresh#syntax-errors)
If you make a syntax error during development, you can fix it and save the file again. The error will disappear automatically, so you won't need to reload the app. **You will not lose component state**.
### Runtime Errors[](https://nextjs.org/docs/architecture/fast-refresh#runtime-errors)
If you make a mistake that leads to a runtime error inside your component, you'll be greeted with a contextual overlay. Fixing the error will automatically dismiss the overlay, without reloading the app.
Component state will be retained if the error did not occur during rendering. If the error did occur during rendering, React will remount your application using the updated code.
If you have _too_ granular. They are used by React in production, and should always be designed intentionally.
