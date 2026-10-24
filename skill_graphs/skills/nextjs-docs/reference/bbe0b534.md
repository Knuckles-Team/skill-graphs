## How it Works[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output#how-it-works)
During `next build`, Next.js will use `import`, `require`, and `fs` usage to determine all files that a page might load.
Next.js' production server is also traced for its needed files and output at `.next/next-server.js.nft.json` which can be leveraged in production.
To leverage the `.nft.json` files emitted to the `.next` output directory, you can read the list of files in each trace that are relative to the `.nft.json` file and then copy them to your deployment location.
