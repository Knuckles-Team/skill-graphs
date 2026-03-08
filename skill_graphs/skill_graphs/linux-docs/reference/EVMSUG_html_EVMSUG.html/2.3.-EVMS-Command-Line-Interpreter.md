#  2.3. EVMS Command Line Interpreter
The EVMS Command Line Interpreter (EVMS CLI) provides a command-driven user interface for EVMS. The EVMS CLI helps automate volume management tasks and provides an interactive mode in situations where the EVMS GUI is not available.
Because the EVMS CLI is an interpreter, it operates differently than command line utilities for the operating system. The options you specify on the EVMS CLI command line to invoke the EVMS CLI control how the EVMS CLI operates. For example, the command line options tell the CLI where to go for commands to interpret and how often the EVMS CLI must save changes to disk. When invoked, the EVMS CLI prompts for commands.
The volume management commands the EVMS CLI understands are specified in the `/usr/src/evms-2.2.0/engine2/ui/cli/grammar.ps` file that accompanies the EVMS package. These commands are described in detail in the EVMS man page, and help on these commands is available from within the EVMS CLI.
* * *
