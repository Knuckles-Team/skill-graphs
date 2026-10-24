##  [Manually purging data cache](https://vercel.com/docs/routing#manually-purging-data-cache)[](https://vercel.com/docs/routing#manually-purging-data-cache)
You need to have a [member](https://vercel.com/docs/rbac/access-roles#member-role) role to perform this task.
In some circumstances, you may need to delete all cached data and force revalidation. You can do this by purging the data cache:
  1. Under your project, open Settings in the sidebar.
  2. In the left sidebar, select Caches.
  3. In the Data Cache section, click Purge Data Cache.
  4. In the dialog, confirm that you wish to delete and click the Continue & Purge Data Cache button.


Purging your data cache will create a temporary increase in request times for users as new data needs to be refetched.
