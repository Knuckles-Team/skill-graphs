[Environment Variables](https://vercel.com/docs/environment-variables)
Reserved Environment Variables
[Environment Variables](https://vercel.com/docs/environment-variables)
Reserved Environment Variables
# Reserved environment variables
Last updated December 10, 2025
The following [environment variable](https://vercel.com/docs/environment-variables) names are
  * `AWS_SECRET_KEY`
  * `AWS_EXECUTION_ENV`
  * `AWS_LAMBDA_LOG_GROUP_NAME`
  * `AWS_LAMBDA_LOG_STREAM_NAME`
  * `AWS_LAMBDA_FUNCTION_NAME`
  * `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
  * `AWS_LAMBDA_FUNCTION_VERSION`
  * `NOW_REGION`
  * `TZ`
  * `LAMBDA_TASK_ROOT`
  * `LAMBDA_RUNTIME_DIR`


##  [Allowed environment variables](https://vercel.com/docs/environment-variables/reserved-environment-variables#allowed-environment-variables)[](https://vercel.com/docs/environment-variables/reserved-environment-variables#allowed-environment-variables)
The following [environment variable](https://vercel.com/docs/environment-variables) names are [allowed](https://vercel.com/kb/guide/how-can-i-use-aws-sdk-environment-variables-on-vercel) by Vercel Vercel Function runtimes:
  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_SESSION_TOKEN`
  * `AWS_REGION`
  * `AWS_DEFAULT_REGION`


These variables may appear in your Vercel Functions even if you don't set them in your project explicitly. These values do not grant any AWS permissions and are not usable as AWS credentials. Configure your own AWS credentials using environment variables or set up [OIDC](https://vercel.com/docs/oidc/aws).
* * *
[ Previous Managing Environment Variables ](https://vercel.com/docs/environment-variables/managing-environment-variables)[ Next Rotating Environment Variables ](https://vercel.com/docs/environment-variables/rotating-secrets)
Was this helpful?
Send
