## Step 7: Configure Cacti Cron Job
Now open the crontab file to schedule polling intervals for **Cacti**.
```
sudo vi /etc/cron.d/cacti

```

Remove the comment from the following line. The **poller.php** script runs every 5 minutes to gather data from known hosts, which **Cacti** uses to create graphs.
```
*/5 * * * *    cacti   /usr/bin/php /usr/share/cacti/poller.php > /dev/null 2>&1

```
