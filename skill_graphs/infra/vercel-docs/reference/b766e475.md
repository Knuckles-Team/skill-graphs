##  [Understanding Deployment Checks](https://vercel.com/docs/deployment-checks#understanding-deployment-checks)[](https://vercel.com/docs/deployment-checks#understanding-deployment-checks)
Decoupling production builds and releases allows teams to move faster with higher confidence at scale.
  * Feature branches are worked on in isolation and merged to the default branch once the code passes required checks for merging.
  * Production deployments are created after new code is merged, but must pass a set of required checks before being released to end users.


By default, Vercel automatically promotes your most recent, successful production build to your custom production domains. This creates the following release workflow:
  1. Push or merge code to your default branch.
  2. Vercel creates a production build.
  3. Once the build is ready, release the build to production.


At scale, this can mean the set of code that is tested before merging is not the same as the code that would be released to end users. We want to maintain the safety of releases, while allowing developers and [agents](https://vercel.com/docs/agents) to continue authoring and merging code at high velocity.
With Deployment Checks, you introduce a new step that ensures the safety of the production deployment before it's released, with the following workflow:
  1. Push or merge code to your default branch.
  2. Vercel creates a production deployment.
  3. Run safety checks to ensure that the build is safe for release.
  4. Once Deployment Checks are passing, release the build to production.
