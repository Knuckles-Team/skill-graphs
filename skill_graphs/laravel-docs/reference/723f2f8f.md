## [Supervisor Configuration](https://laravel.com/docs/12.x/queues#supervisor-configuration)
In production, you need a way to keep your `queue:work` processes running. A `queue:work` process may stop running for a variety of reasons, such as an exceeded worker timeout or the execution of the `queue:restart` command.
For this reason, you need to configure a process monitor that can detect when your `queue:work` processes exit and automatically restart them. In addition, process monitors can allow you to specify how many `queue:work` processes you would like to run concurrently. Supervisor is a process monitor commonly used in Linux environments and we will discuss how to configure it in the following documentation.
#### [Installing Supervisor](https://laravel.com/docs/12.x/queues#installing-supervisor)
Supervisor is a process monitor for the Linux operating system, and will automatically restart your `queue:work` processes if they fail. To install Supervisor on Ubuntu, you may use the following command:
```


1sudo apt-get install supervisor




sudo apt-get install supervisor

```

If configuring and managing Supervisor yourself sounds overwhelming, consider using [Laravel Cloud](https://cloud.laravel.com), which provides a fully-managed platform for running Laravel queue workers.
#### [Configuring Supervisor](https://laravel.com/docs/12.x/queues#configuring-supervisor)
Supervisor configuration files are typically stored in the `/etc/supervisor/conf.d` directory. Within this directory, you may create any number of configuration files that instruct supervisor how your processes should be monitored. For example, let's create a `laravel-worker.conf` file that starts and monitors `queue:work` processes:
```


 1[program:laravel-worker]




 2process_name=%(program_name)s_%(process_num)02d




 3command=php /home/forge/app.com/artisan queue:work --sleep=3 --tries=3 --max-time=3600




 4autostart=true




 5autorestart=true




 6stopasgroup=true




 7killasgroup=true




 8user=forge




 9numprocs=8




10redirect_stderr=true




11stdout_logfile=/home/forge/app.com/worker.log




12stopwaitsecs=3600




[program:laravel-worker]
process_name=%(program_name)s_%(process_num)02d
command=php /home/forge/app.com/artisan queue:work --sleep=3 --tries=3 --max-time=3600
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
user=forge
numprocs=8
redirect_stderr=true
stdout_logfile=/home/forge/app.com/worker.log
stopwaitsecs=3600

```

In this example, the `numprocs` directive will instruct Supervisor to run eight `queue:work` processes and monitor all of them, automatically restarting them if they fail. You should change the `command` directive of the configuration to reflect your desired queue connection and worker options.
You should ensure that the value of `stopwaitsecs` is greater than the number of seconds consumed by your longest running job. Otherwise, Supervisor may kill the job before it is finished processing.
#### [Starting Supervisor](https://laravel.com/docs/12.x/queues#starting-supervisor)
Once the configuration file has been created, you may update the Supervisor configuration and start the processes using the following commands:
```


1sudo supervisorctl reread




2 



3sudo supervisorctl update




4 



5sudo supervisorctl start "laravel-worker:*"




sudo supervisorctl reread

sudo supervisorctl update

sudo supervisorctl start "laravel-worker:*"

```

For more information on Supervisor, consult the
