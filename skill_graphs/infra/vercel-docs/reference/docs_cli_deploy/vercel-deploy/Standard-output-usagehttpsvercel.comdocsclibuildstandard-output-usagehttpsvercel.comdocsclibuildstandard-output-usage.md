##  [Standard output usage](https://vercel.com/docs/cli/build#standard-output-usage)[](https://vercel.com/docs/cli/build#standard-output-usage)
When deploying, `stdout` is always the Deployment URL.
terminal
```
vercel > deployment-url.txt
```

Using the `vercel` command to deploy and write `stdout` to a text file. When deploying, `stdout` is always the Deployment URL.
###  [Deploying to a custom domain](https://vercel.com/docs/cli/build#deploying-to-a-custom-domain)[](https://vercel.com/docs/cli/build#deploying-to-a-custom-domain)
In the following example, you create a bash script that you include in your CI/CD workflow. The goal is to have all preview deployments be aliased to a custom domain so that developers can bookmark the preview deployment URL. Note that you may need to [define the scope](https://vercel.com/docs/cli/global-options#scope) when using `vercel alias`
deployDomain.sh
```
# save stdout and stderr to files
vercel deploy >deployment-url.txt 2>error.txt

# check the exit code
code=$?
if [ $code -eq 0 ]; then
    # Now you can use the deployment url from stdout for the next step of your workflow
    deploymentUrl=`cat deployment-url.txt`
    vercel alias $deploymentUrl my-custom-domain.com
else
    # Handle the error
    errorMessage=`cat error.txt`
    echo "There was an error: $errorMessage"
fi
```

The script deploys your project and assigns the deployment URL saved in `stdout` to the custom domain using `vercel alias`.
