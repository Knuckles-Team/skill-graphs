##  2.3.4. Periodic command execution: **cron** and **at**
Both users and system administrators often need to run commands periodically. For example, the system administrator might want to run a command to clean the directories with temporary files (`/tmp` and `/var/tmp`) from old files, to keep the disks from filling up, since not all programs clean up after themselves correctly.
The **cron** service is set up to do this. Each user can have a `crontab` file, where she lists the commands she wishes to execute and the times they should be executed. The **cron** daemon takes care of starting the commands when specified.
The **at** service is similar to **cron** , but it is once only: the command is executed at the given time, but it is not repeated.
We will go more into this later. See the manual pages cron(1), crontab(1), crontab(5), at(1) and atd(8) for more in depth information.
[Chapter 13](https://tldp.org/LDP/sag/html/sag.html#TASK-AUTOMATION) will cover this.
* * *
