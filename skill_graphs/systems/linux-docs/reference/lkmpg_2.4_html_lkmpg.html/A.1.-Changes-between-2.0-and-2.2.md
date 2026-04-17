#  A.1. Changes between 2.0 and 2.2
* * *
##  A.1.1. Changes between 2.0 and 2.2
I don't know the entire kernel well enough do document all of the changes. In the course of converting the examples (or actually, adapting Emmanuel Papirakis's changes) I came across the following differences. I listed all of them here together to help module programmers, especially those who learned from previous versions of this book and are most familiar with the techniques I use, convert to the new version.
An additional resource for people who wish to convert to 2.2 is located on

`asm/uaccess.h`

If you need `put_user` or `get_user` you have to `**#include**` it.

`get_user`

In version 2.2, `get_user` receives both the pointer into user memory and the variable in kernel memory to fill with the information. The reason for this is that `get_user` can now read two or four bytes at a time if the variable we read is two or four bytes long.

file_operations

This structure now has a flush function between the `open` and `close` functions.

`close` in file_operations

In version 2.2, the `close` function returns an integer, so it's allowed to fail.

`read`,`write` in file_operations

The headers for these functions changed. They now return `**ssize_t**` instead of an integer, and their parameter list is different. The inode is no longer a parameter, and on the other hand the offset into the file is.

`proc_register_dynamic`

This function no longer exists. Instead, you call the regular `proc_register` and put zero in the inode field of the structure.

Signals

The signals in the task structure are no longer a 32 bit integer, but an array of `__NSIG_WORDS_` integers.

`queue_task_irq`

Even if you want to schedule a task to happen from inside an interrupt handler, you use `queue_task`, not `queue_task_irq`.

Module Parameters

You no longer just declare module parameters as global variables. In 2.2 you have to also use `_MODULE_PARM_` to declare their type. This is a big improvement, because it allows the module to receive string parameters which start with a digits, for example, without getting confused.

Symmetrical Multi-Processing

The kernel is no longer inside one huge spinlock, which means that kernel modules have to be aware of SMP.
* * *
