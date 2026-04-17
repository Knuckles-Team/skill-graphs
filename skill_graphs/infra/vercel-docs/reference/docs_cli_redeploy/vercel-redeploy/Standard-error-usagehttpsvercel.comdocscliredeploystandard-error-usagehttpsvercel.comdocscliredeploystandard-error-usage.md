##  [Standard error usage](https://vercel.com/docs/cli/redeploy#standard-error-usage)[](https://vercel.com/docs/cli/redeploy#standard-error-usage)
If you need to check for errors when the command is executed such as in a CI/CD workflow, use `stderr`. If the exit code is anything other than `0`, an error has occurred. The following example demonstrates a script that checks if the exit code is not equal to 0:
check-redeploy.sh
```
# save stdout and stderr to files
vercel redeploy https://example-app-6vd6bhoqt.vercel.app >deployment-url.txt 2>error.txt

# check the exit code
code=$?
if [ $code -eq 0 ]; then
    # Now you can use the deployment url from stdout for the next step of your workflow
    deploymentUrl=`cat deployment-url.txt`
    echo $deploymentUrl
else
    # Handle the error
    errorMessage=`cat error.txt`
    echo "There was an error: $errorMessage"
fi
```
