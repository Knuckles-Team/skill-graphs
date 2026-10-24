#  7.4. Summary
In this chapter we learned how to build conditions into our scripts so that different actions can be undertaken upon success or failure of a command. The actions can be determined using the **if** statement. This allows you to perform arithmetic and string comparisons, and testing of exit code, input and files needed by the script.
A simple **if/then/fi** test often preceeds commands in a shell script in order to prevent output generation, so that the script can easily be run in the background or through the cron facility. More complex definitions of conditions are usually put in a **case** statement.
Upon successful condition testing, the script can explicitly inform the parent using the **exit 0** status. Upon failure, any other number may be returned. Based on the return code, the parent program can take appropriate action.
* * *
