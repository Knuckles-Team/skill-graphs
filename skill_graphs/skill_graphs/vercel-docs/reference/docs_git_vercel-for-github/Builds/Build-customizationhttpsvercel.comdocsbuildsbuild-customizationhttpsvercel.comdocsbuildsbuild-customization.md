##  [Build customization](https://vercel.com/docs/builds#build-customization)[](https://vercel.com/docs/builds#build-customization)
Depending on your framework, Vercel automatically sets the Build Command, Install Command, and Output Directory. If needed, you can customize these in your project's Settings:
  1. Build Command: Override the default (`npm run build`, `next build`, etc.) for custom workflows.
  2. Output Directory: Specify the folder containing your final build output (e.g., `dist` or `build`).
  3. Install Command: Control how dependencies are installed (e.g., `pnpm install`, `yarn install`) or skip installing dev dependencies if needed.


To learn more, see [Configuring a Build](https://vercel.com/docs/deployments/configure-a-build).
