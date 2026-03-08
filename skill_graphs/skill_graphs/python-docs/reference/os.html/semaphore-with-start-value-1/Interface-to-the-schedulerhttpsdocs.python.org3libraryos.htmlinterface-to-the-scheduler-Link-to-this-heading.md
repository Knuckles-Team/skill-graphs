## Interface to the scheduler[¶](https://docs.python.org/3/library/os.html#interface-to-the-scheduler "Link to this heading")
These functions control how a process is allocated CPU time by the operating system. They are only available on some Unix platforms. For more detailed information, consult your Unix manpages.
Added in version 3.3.
The following scheduling policies are exposed if they are supported by the operating system.

os.SCHED_OTHER[¶](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "Link to this definition")

The default scheduling policy.

os.SCHED_BATCH[¶](https://docs.python.org/3/library/os.html#os.SCHED_BATCH "Link to this definition")

Scheduling policy for CPU-intensive processes that tries to preserve interactivity on the rest of the computer.

os.SCHED_DEADLINE[¶](https://docs.python.org/3/library/os.html#os.SCHED_DEADLINE "Link to this definition")

Scheduling policy for tasks with deadline constraints.
Added in version 3.14.

os.SCHED_IDLE[¶](https://docs.python.org/3/library/os.html#os.SCHED_IDLE "Link to this definition")

Scheduling policy for extremely low priority background tasks.

os.SCHED_NORMAL[¶](https://docs.python.org/3/library/os.html#os.SCHED_NORMAL "Link to this definition")

Alias for [`SCHED_OTHER`](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "os.SCHED_OTHER").
Added in version 3.14.

os.SCHED_SPORADIC[¶](https://docs.python.org/3/library/os.html#os.SCHED_SPORADIC "Link to this definition")

Scheduling policy for sporadic server programs.

os.SCHED_FIFO[¶](https://docs.python.org/3/library/os.html#os.SCHED_FIFO "Link to this definition")

A First In First Out scheduling policy.

os.SCHED_RR[¶](https://docs.python.org/3/library/os.html#os.SCHED_RR "Link to this definition")

A round-robin scheduling policy.

os.SCHED_RESET_ON_FORK[¶](https://docs.python.org/3/library/os.html#os.SCHED_RESET_ON_FORK "Link to this definition")

This flag can be OR’ed with any other scheduling policy. When a process with this flag set forks, its child’s scheduling policy and priority are reset to the default.

_class_ os.sched_param(_sched_priority_)[¶](https://docs.python.org/3/library/os.html#os.sched_param "Link to this definition")

This class represents tunable scheduling parameters used in [`sched_setparam()`](https://docs.python.org/3/library/os.html#os.sched_setparam "os.sched_setparam"), [`sched_setscheduler()`](https://docs.python.org/3/library/os.html#os.sched_setscheduler "os.sched_setscheduler"), and [`sched_getparam()`](https://docs.python.org/3/library/os.html#os.sched_getparam "os.sched_getparam"). It is immutable.
At the moment, there is only one possible parameter:

sched_priority[¶](https://docs.python.org/3/library/os.html#os.sched_param.sched_priority "Link to this definition")

The scheduling priority for a scheduling policy.

os.sched_get_priority_min(_policy_)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_min "Link to this definition")

Get the minimum priority value for _policy_. _policy_ is one of the scheduling policy constants above.

os.sched_get_priority_max(_policy_)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_max "Link to this definition")

Get the maximum priority value for _policy_. _policy_ is one of the scheduling policy constants above.

os.sched_setscheduler(_pid_ , _policy_ , _param_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setscheduler "Link to this definition")

Set the scheduling policy for the process with PID _pid_. A _pid_ of 0 means the calling process. _policy_ is one of the scheduling policy constants above. _param_ is a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param") instance.

os.sched_getscheduler(_pid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getscheduler "Link to this definition")

Return the scheduling policy for the process with PID _pid_. A _pid_ of 0 means the calling process. The result is one of the scheduling policy constants above.

os.sched_setparam(_pid_ , _param_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setparam "Link to this definition")

Set the scheduling parameters for the process with PID _pid_. A _pid_ of 0 means the calling process. _param_ is a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param") instance.

os.sched_getparam(_pid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getparam "Link to this definition")

Return the scheduling parameters as a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param") instance for the process with PID _pid_. A _pid_ of 0 means the calling process.

os.sched_rr_get_interval(_pid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_rr_get_interval "Link to this definition")

Return the round-robin quantum in seconds for the process with PID _pid_. A _pid_ of 0 means the calling process.

os.sched_yield()[¶](https://docs.python.org/3/library/os.html#os.sched_yield "Link to this definition")

Voluntarily relinquish the CPU. See

os.sched_setaffinity(_pid_ , _mask_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setaffinity "Link to this definition")

Restrict the process with PID _pid_ (or the current process if zero) to a set of CPUs. _mask_ is an iterable of integers representing the set of CPUs to which the process should be restricted.

os.sched_getaffinity(_pid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getaffinity "Link to this definition")

Return the set of CPUs the process with PID _pid_ is restricted to.
If _pid_ is zero, return the set of CPUs the calling thread of the current process is restricted to.
See also the [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") function.
