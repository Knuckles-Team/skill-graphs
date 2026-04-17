##  [Setting up your local environment](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-local-environment)[](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-local-environment)
  1. ###  [Set up your workspace](https://vercel.com/docs/getting-started-with-vercel#set-up-your-workspace)[](https://vercel.com/docs/getting-started-with-vercel#set-up-your-workspace)
If you're the first person on your team to use Vercel's private registry, you'll need to set up your workspace to fetch packages from the private registry.
Execute the following command to configure your package manager to fetch packages with the `@vercel-private` scope from the private registry. If you're using modern Yarn (v2 or newer) see the [Using modern versions of Yarn](https://vercel.com/docs/getting-started-with-vercel#setting-registry-server-using-modern-versions-of-yarn) section below.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm config set --location=project @vercel-private:registry "https://vercel-private-registry.vercel.sh/registry"
```

```
npm config set --location=project @vercel-private:registry "https://vercel-private-registry.vercel.sh/registry"
```

```
npm config set --location=project @vercel-private:registry "https://vercel-private-registry.vercel.sh/registry"
```

```
npm config set --location=project @vercel-private:registry "https://vercel-private-registry.vercel.sh/registry"
```

This command creates an `.npmrc` file (or updates one if it exists) at the root of your workspace. We recommend committing this file to your repository, as it will help other engineers get on board faster.
  2. ###  [Setting registry server using modern versions of Yarn](https://vercel.com/docs/getting-started-with-vercel#setting-registry-server-using-modern-versions-of-yarn)[](https://vercel.com/docs/getting-started-with-vercel#setting-registry-server-using-modern-versions-of-yarn)
Yarn version 2 or newer ignores the `.npmrc` config file so you will need to use this command instead to add the registry to your project's `.yarnrc.yml` file:
```
yarn config set npmScopes.vercel-private.npmRegistryServer "https://vercel-private-registry.vercel.sh/registry"
```

  3. ###  [Log in to the private registry](https://vercel.com/docs/getting-started-with-vercel#log-in-to-the-private-registry)[](https://vercel.com/docs/getting-started-with-vercel#log-in-to-the-private-registry)
Each team member will need to complete this step. It may be helpful to summarize this step in your team's onboarding documentation.
To log in, use the following command and follow the prompts:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm login --scope=@vercel-private
```

```
npm login --scope=@vercel-private
```

```
npm login --scope=@vercel-private
```

```
npm login --scope=@vercel-private
```

The minimum required version of npm to log into the registry is 8.14.0. For pnpm, version 7.0.0 or higher is required.
During this process, you will be asked to log in to your Vercel account. Ensure that the account that you log in to has access to the Vercel product(s) that you're trying to install.
You should now have a `.npmrc` file in your home directory that contains the authentication token for the private registry.
  4. ####  [Setting token using modern versions of Yarn](https://vercel.com/docs/getting-started-with-vercel#setting-token-using-modern-versions-of-yarn)[](https://vercel.com/docs/getting-started-with-vercel#setting-token-using-modern-versions-of-yarn)
Yarn version 2 or newer requires the authentication token to be saved in a `.yarnrc.yml` file. After running the above command, you can copy the token from the `.npmrc` file with:
```
auth_token=$(awk -F'=' '/vercel-private-registry.vercel.sh\/:_authToken/ {print $2}' $(npm config get userconfig)) \
&& yarn config set --home 'npmRegistries["https://vercel-private-registry.vercel.sh/registry"].npmAuthToken' $auth_token
```

Note the `--home` flag, which ensures the token is saved in the global `.yarnrc.yml` rather then in your project so that it isn't committed.
  5. ###  [Verify your setup](https://vercel.com/docs/getting-started-with-vercel#verify-your-setup)[](https://vercel.com/docs/getting-started-with-vercel#verify-your-setup)
Verify your login status by executing:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm whoami --registry=https://vercel-private-registry.vercel.sh/registry
```

```
yarn npm whoami --scope=vercel-private
```

```
npm whoami --registry=https://vercel-private-registry.vercel.sh/registry
```

```
bun pm whoami --registry=https://vercel-private-registry.vercel.sh/registry
```

The Yarn command only works with Yarn version 2 or newer, use the npm command if using Yarn v1.
You should see your Vercel username returned if everything is set up correctly.
  6. ###  [Optionally set up a pre-install message for missing credentials](https://vercel.com/docs/getting-started-with-vercel#optionally-set-up-a-pre-install-message-for-missing-credentials)[](https://vercel.com/docs/getting-started-with-vercel#optionally-set-up-a-pre-install-message-for-missing-credentials)
When a user tries to install a package from the private registry without first logging in, the error message might be unclear. To help, we suggest adding a pre-install message that provides instructions to those unauthenticated users.
Create a `preinstall.mjs` file with your error message:
preinstall.mjs
```
import { exec } from 'node:child_process';
import { promisify } from 'node:util';

const execPromise = promisify(exec);

// Detect which package manager is being used
const userAgent = process.env.npm_config_user_agent || '';
const isYarn = userAgent.includes('yarn');
const isPnpm = userAgent.includes('pnpm');
const isBun = userAgent.includes('bun');

let checkCommand;
let loginCommand;

if (isPnpm) {
  checkCommand =
    'pnpm whoami --registry=https://vercel-private-registry.vercel.sh/registry';
  loginCommand = 'pnpm login --scope=@vercel-private';
} else if (isYarn) {
  checkCommand = 'yarn npm whoami --scope=vercel-private';
  loginCommand = 'npm login --scope=@vercel-private';
} else {
  // npm or bun
  checkCommand =
    'npm whoami --registry=https://vercel-private-registry.vercel.sh/registry';
  loginCommand = 'npm login --scope=@vercel-private';
}

try {
  await execPromise(checkCommand);
} catch (error) {
  throw new Error(
    `Please log in to the Vercel private registry to install \`@vercel-private\`-scoped packages:\n\`${loginCommand}\``,
  );
}
```

Then add the following script to the `scripts` field in your `package.json`:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
{  "scripts": {    "pnpm:devPreinstall": "node preinstall.mjs"  }}
```

```
{  "scripts": {    "preinstall": "node preinstall.mjs"  }}
```

```
{  "scripts": {    "preinstall": "node preinstall.mjs"  }}
```

```
{  "scripts": {    "preinstall": "node preinstall.mjs"  }}
```
