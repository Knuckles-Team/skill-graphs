## Environment Variable Load Order[](https://nextjs.org/docs/pages/guides/environment-variables#environment-variable-load-order)
Environment variables are looked up in the following places, in order, stopping once the variable is found.
  1. `process.env`
  2. `.env.$(NODE_ENV).local`
  3. `.env.local` (Not checked when `NODE_ENV` is `test`.)
  4. `.env.$(NODE_ENV)`
  5. `.env`


For example, if `NODE_ENV` is `development` and you define a variable in both `.env.development.local` and `.env`, the value in `.env.development.local` will be used.
> **Good to know** : The allowed values for `NODE_ENV` are `production`, `development` and `test`.
