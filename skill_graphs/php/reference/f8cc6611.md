## [Running Vite](https://laravel.com/docs/12.x/vite#running-vite)
There are two ways you can run Vite. You may run the development server via the `dev` command, which is useful while developing locally. The development server will automatically detect changes to your files and instantly reflect them in any open browser windows.
Or, running the `build` command will version and bundle your application's assets and get them ready for you to deploy to production:
```


1# Run the Vite development server...




2npm run dev




3 



4# Build and version the assets for production...




5npm run build




# Run the Vite development server...
npm run dev

# Build and version the assets for production...
npm run build

```

If you are running the development server in [Sail](https://laravel.com/docs/12.x/sail) on WSL2, you may need some [additional configuration](https://laravel.com/docs/12.x/vite#configuring-hmr-in-sail-on-wsl2) options.
