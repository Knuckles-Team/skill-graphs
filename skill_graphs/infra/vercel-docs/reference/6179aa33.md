##  [Managing items in the store](https://vercel.com/docs/edge-config/edge-config-dashboard#managing-items-in-the-store)[](https://vercel.com/docs/edge-config/edge-config-dashboard#managing-items-in-the-store)
The default view of the Edge Config's detail page shows the list of all items in the store. You will see an open accordion titled Learn how to use this in code if the Edge Config is connected to at least one project. This accordion provides the steps with a code example on how to read your store items.
To add, edit or delete any item in your store, edit the `json` object in the right panel and click Save Items.
###  [Restoring Edge Config backups](https://vercel.com/docs/edge-config/edge-config-dashboard#restoring-edge-config-backups)[](https://vercel.com/docs/edge-config/edge-config-dashboard#restoring-edge-config-backups)
Backups of your Edge Config are automatically created when you make changes, and are stored for a [length of time](https://vercel.com/docs/edge-config/edge-config-limits#backup-retention) determined by your plan. To restore one:
  1. From your [dashboard](https://vercel.com/dashboard), open [Storage](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fstores&title=Go+to+Storage) in the sidebar and then select your Edge Config
  2. From the left section, open Backups in the sidebar
  3. From the list, select the backup that you would like to view. You'll be taken to the Items section in the sidebar to view a comparison of the backup version and current version
  4. To restore the backup, select the Restore button and confirm the action


To learn more about backups, see [Edge Config backups](https://vercel.com/docs/edge-config/using-edge-config#edge-config-backups).
When protected by a JSON schema, the backup must pass schema validation to be restored.
