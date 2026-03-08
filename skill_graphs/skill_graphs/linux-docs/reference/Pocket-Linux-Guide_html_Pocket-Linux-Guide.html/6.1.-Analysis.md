#  6.1. Analysis
The root disk from the last chapter is looking pretty good. It has about seventy percent of the commands that the Filesystem Hierarchy Standard (FHS) document requires for the root filesystem. Plus it has commands for checking and mounting filesystems. But even with all of this the root disk is far from perfect. The list below outlines three things that could use some improvement if the Pocket Linux system is to stand up next to the more professional looking distributions.
  1. The system currently requires the kernel parameters to be typed at the `grub>` prompt in order to start properly. On any other GNU/Linux system this is only done in an emergency situation when the system is corrupted.
  2. Checking and mounting the root filesystem has to be done manually by running a script at a shell prompt. On most modern operating systems this function is handled automatically as part of the system start-up process.
  3. Using **CTRL** -**ALT** -**DELETE** for system shutdown is not very graceful. Filesystems should be unmounted and cached information should be flushed prior to shutdown. Again, this is something that most operating systems handle automatically.


Taking the above list into consideration, the goals for this phase are defined as follows:
  * Kernel loads without manual intervention.
  * Automated system start-up sequence.
  * Graceful shutdown capability.


* * *
