## Azure Pipelines[](https://nextjs.org/docs/app/guides/ci-build-caching#azure-pipelines)
Using Azure Pipelines' `next build`:
```
- task: Cache@2
  displayName: 'Cache .next/cache'
  inputs:
    key: next | $(Agent.OS) | yarn.lock
    path: '$(System.DefaultWorkingDirectory)/.next/cache'
```
