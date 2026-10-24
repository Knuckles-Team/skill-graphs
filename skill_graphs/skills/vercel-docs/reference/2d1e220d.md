##  [CLI examples](https://vercel.com/docs/cron-jobs#cli-examples)[](https://vercel.com/docs/cron-jobs#cli-examples)
###  [Your first sandbox](https://vercel.com/docs/cron-jobs#your-first-sandbox)[](https://vercel.com/docs/cron-jobs#your-first-sandbox)
Create a sandbox and run a command in one step:
```
sandbox run echo "Hello Sandbox!"
```

You'll see output like:
`Creating sandbox... ✓ Running command... Hello Sandbox! Sandbox stopped. `
###  [Create a long-running sandbox](https://vercel.com/docs/cron-jobs#create-a-long-running-sandbox)[](https://vercel.com/docs/cron-jobs#create-a-long-running-sandbox)
For interactive work, create a sandbox that stays running:
```
sandbox create --timeout 30m
```

This returns a sandbox ID like `sb_abc123xyz`. Save this ID to interact with the sandbox.
###  [Execute commands in your sandbox](https://vercel.com/docs/cron-jobs#execute-commands-in-your-sandbox)[](https://vercel.com/docs/cron-jobs#execute-commands-in-your-sandbox)
Run commands using the sandbox ID:
```
# Check the environment
sandbox exec sb_abc123xyz node --version

# Install packages
sandbox exec sb_abc123xyz npm init -y
sandbox exec sb_abc123xyz npm install express

# Create files
sandbox exec sb_abc123xyz touch server.js
```

###  [Copy files to/from sandbox](https://vercel.com/docs/cron-jobs#copy-files-to/from-sandbox)[](https://vercel.com/docs/cron-jobs#copy-files-to/from-sandbox)
Test local code in the sandbox:
```
# Copy your code to the sandbox
sandbox copy ./my-app.js sb_abc123xyz:/home/sandbox/

# Run it
sandbox exec sb_abc123xyz node /home/sandbox/my-app.js

# Copy results back
sandbox copy sb_abc123xyz:/home/sandbox/output.json ./results.json
```

###  [Interactive shell access](https://vercel.com/docs/cron-jobs#interactive-shell-access)[](https://vercel.com/docs/cron-jobs#interactive-shell-access)
Work inside the sandbox like it's your machine:
```
sandbox exec --interactive --tty sb_abc123xyz bash
```

Now you're inside the sandbox! Try:
```
pwd                    # See where you are
ls -la                 # List files
node -e "console.log('Inside!')"  # Run Node.js
exit                   # Leave when done
```

###  [Stop your sandbox](https://vercel.com/docs/cron-jobs#stop-your-sandbox)[](https://vercel.com/docs/cron-jobs#stop-your-sandbox)
When finished:
```
sandbox stop sb_abc123xyz
```

###  [Test AI-generated code interactively](https://vercel.com/docs/cron-jobs#test-ai-generated-code-interactively)[](https://vercel.com/docs/cron-jobs#test-ai-generated-code-interactively)
```
# Create sandbox
SANDBOX_ID=$(sandbox create --timeout 15m --silent)

# Copy AI-generated code
sandbox copy ./ai-generated.js $SANDBOX_ID:/app/

# Test it interactively
sandbox exec --interactive --tty $SANDBOX_ID bash
# Now inside: cd /app && node ai-generated.js

# Clean up
sandbox stop $SANDBOX_ID
```

###  [Debug a failing build](https://vercel.com/docs/cron-jobs#debug-a-failing-build)[](https://vercel.com/docs/cron-jobs#debug-a-failing-build)
```
# Create sandbox with more time
sandbox create --timeout 1h

# Copy your project
sandbox copy ./my-project/ sb_abc123xyz:/app/

# Try building
sandbox exec sb_abc123xyz --workdir /app npm run build

# If it fails, debug interactively
sandbox exec -it sb_abc123xyz bash
```

###  [Run a development server](https://vercel.com/docs/cron-jobs#run-a-development-server)[](https://vercel.com/docs/cron-jobs#run-a-development-server)
```
# Create with port exposure
sandbox create --timeout 30m --publish-port 3000

# Start your dev server
sandbox exec --workdir /app sb_abc123xyz npm run dev

# Access at the provided URL
# Visit: https://sb-abc123xyz.vercel.app
```

* * *
[ Previous Routing Middleware ](https://vercel.com/docs/routing-middleware)[ Next Getting Started ](https://vercel.com/docs/cron-jobs/quickstart)
Was this helpful?
Send
On this page
  * [Installation](https://vercel.com/docs/cron-jobs#installation)
  * [Authentication](https://vercel.com/docs/cron-jobs#authentication)
  * [sandbox --help](https://vercel.com/docs/cron-jobs#sandbox---help)
  * [sandbox list](https://vercel.com/docs/cron-jobs#sandbox-list)
  * [Sandbox list example](https://vercel.com/docs/cron-jobs#sandbox-list-example)
  * [Sandbox list options](https://vercel.com/docs/cron-jobs#sandbox-list-options)
  * [Sandbox list flags](https://vercel.com/docs/cron-jobs#sandbox-list-flags)
  * [sandbox create](https://vercel.com/docs/cron-jobs#sandbox-create)
  * [Sandbox create example](https://vercel.com/docs/cron-jobs#sandbox-create-example)
  * [Sandbox create options](https://vercel.com/docs/cron-jobs#sandbox-create-options)
  * [Sandbox create flags](https://vercel.com/docs/cron-jobs#sandbox-create-flags)
  * [sandbox config](https://vercel.com/docs/cron-jobs#sandbox-config)
  * [Sandbox config example](https://vercel.com/docs/cron-jobs#sandbox-config-example)
  * [Sandbox config network-policy options](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-options)
  * [Sandbox config network-policy flags](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-flags)
  * [Sandbox config network-policy arguments](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-arguments)
  * [sandbox copy](https://vercel.com/docs/cron-jobs#sandbox-copy)
  * [Sandbox copy example](https://vercel.com/docs/cron-jobs#sandbox-copy-example)
  * [Sandbox copy options](https://vercel.com/docs/cron-jobs#sandbox-copy-options)
  * [Sandbox copy flags](https://vercel.com/docs/cron-jobs#sandbox-copy-flags)
  * [Sandbox copy arguments](https://vercel.com/docs/cron-jobs#sandbox-copy-arguments)
  * [sandbox exec](https://vercel.com/docs/cron-jobs#sandbox-exec)
  * [Sandbox exec example](https://vercel.com/docs/cron-jobs#sandbox-exec-example)
  * [Sandbox exec options](https://vercel.com/docs/cron-jobs#sandbox-exec-options)
  * [Sandbox exec flags](https://vercel.com/docs/cron-jobs#sandbox-exec-flags)
  * [Sandbox exec arguments](https://vercel.com/docs/cron-jobs#sandbox-exec-arguments)
  * [sandbox connect](https://vercel.com/docs/cron-jobs#sandbox-connect)
  * [Sandbox connect example](https://vercel.com/docs/cron-jobs#sandbox-connect-example)
  * [Sandbox connect options](https://vercel.com/docs/cron-jobs#sandbox-connect-options)
  * [Sandbox connect flags](https://vercel.com/docs/cron-jobs#sandbox-connect-flags)
  * [Sandbox connect arguments](https://vercel.com/docs/cron-jobs#sandbox-connect-arguments)
  * [sandbox stop](https://vercel.com/docs/cron-jobs#sandbox-stop)
  * [Sandbox stop example](https://vercel.com/docs/cron-jobs#sandbox-stop-example)
  * [Sandbox stop options](https://vercel.com/docs/cron-jobs#sandbox-stop-options)
  * [Sandbox stop flags](https://vercel.com/docs/cron-jobs#sandbox-stop-flags)
  * [Sandbox stop arguments](https://vercel.com/docs/cron-jobs#sandbox-stop-arguments)
  * [sandbox run](https://vercel.com/docs/cron-jobs#sandbox-run)
  * [Sandbox run example](https://vercel.com/docs/cron-jobs#sandbox-run-example)
  * [Sandbox run options](https://vercel.com/docs/cron-jobs#sandbox-run-options)
  * [Sandbox run flags](https://vercel.com/docs/cron-jobs#sandbox-run-flags)
  * [Sandbox run arguments](https://vercel.com/docs/cron-jobs#sandbox-run-arguments)
  * [sandbox snapshot](https://vercel.com/docs/cron-jobs#sandbox-snapshot)
  * [Sandbox snapshot example](https://vercel.com/docs/cron-jobs#sandbox-snapshot-example)
  * [Sandbox snapshot options](https://vercel.com/docs/cron-jobs#sandbox-snapshot-options)
  * [Sandbox snapshot flags](https://vercel.com/docs/cron-jobs#sandbox-snapshot-flags)
  * [Sandbox snapshot arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshot-arguments)
  * [sandbox snapshots](https://vercel.com/docs/cron-jobs#sandbox-snapshots)
  * [Sandbox snapshots subcommands](https://vercel.com/docs/cron-jobs#sandbox-snapshots-subcommands)
  * [sandbox snapshots list](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list)
  * [Sandbox snapshots list example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-example)
  * [Sandbox snapshots list options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-options)
  * [Sandbox snapshots list flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-flags)
  * [sandbox snapshots get](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get)
  * [Sandbox snapshots get example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-example)
  * [Sandbox snapshots get options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-options)
  * [Sandbox snapshots get flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-flags)
  * [Sandbox snapshots get arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-arguments)
  * [sandbox snapshots delete](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete)
  * [Sandbox snapshots delete example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-example)
  * [Sandbox snapshots delete options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-options)
  * [Sandbox snapshots delete flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-flags)
  * [Sandbox snapshots delete arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-arguments)
  * [sandbox login](https://vercel.com/docs/cron-jobs#sandbox-login)
  * [Sandbox login example](https://vercel.com/docs/cron-jobs#sandbox-login-example)
  * [Sandbox login flags](https://vercel.com/docs/cron-jobs#sandbox-login-flags)
  * [sandbox logout](https://vercel.com/docs/cron-jobs#sandbox-logout)
  * [Sandbox logout example](https://vercel.com/docs/cron-jobs#sandbox-logout-example)
  * [Sandbox logout flags](https://vercel.com/docs/cron-jobs#sandbox-logout-flags)
  * [CLI examples](https://vercel.com/docs/cron-jobs#cli-examples)
  * [Your first sandbox](https://vercel.com/docs/cron-jobs#your-first-sandbox)
  * [Create a long-running sandbox](https://vercel.com/docs/cron-jobs#create-a-long-running-sandbox)
  * [Execute commands in your sandbox](https://vercel.com/docs/cron-jobs#execute-commands-in-your-sandbox)
  * [Copy files to/from sandbox](https://vercel.com/docs/cron-jobs#copy-files-to/from-sandbox)
  * [Interactive shell access](https://vercel.com/docs/cron-jobs#interactive-shell-access)
  * [Stop your sandbox](https://vercel.com/docs/cron-jobs#stop-your-sandbox)
  * [Test AI-generated code interactively](https://vercel.com/docs/cron-jobs#test-ai-generated-code-interactively)
  * [Debug a failing build](https://vercel.com/docs/cron-jobs#debug-a-failing-build)
  * [Run a development server](https://vercel.com/docs/cron-jobs#run-a-development-server)


Copy as MarkdownGive feedbackAsk AI about this page
