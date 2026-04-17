
The EVMS Engine handles the creation, configuration, and management of
volumes, segments, and disks. The EVMS Engine is a programmatic interface to
the EVMS system. User interfaces and programs that use EVMS must go through
the Engine.

EVMS provides the capacity for plug-in modules to the Engine that allow EVMS
to perform specialized tasks without altering the core code. These plug-in
modules allow EVMS to be more extensible and customizable than other volume
management systems.
-----------------------------------------------------------------------------

1.5. Plug-in layer definitions

EVMS defines a layered architecture where plug-ins in each layer create
abstractions of the layer or layers below. EVMS also allows most plug-ins to
create abstractions of objects within the same layer. The following list
defines these layers from the bottom up.

Device managers
    The first (bottom) layer consists of device managers. These plug-ins
    communicate with hardware device drivers to create the first EVMS
    objects. Currently, all devices are handled by a single plug-in. Future
    releases of EVMS might need additional device managers for network device
    management (for example, to manage disks on a storage area network
    (SAN)).

Segment managers
    The second layer consists of segment managers. These plug-ins handle the
    segmenting, or partitioning, of disk drives. The Engine components can
    replace partitioning programs, such as fdisk and Disk Druid, and EVMS
    uses Device Mapper to replace the in-kernel disk partitioning code.
    Segment managers can also be "stacked," meaning that one segment manager
    can take as input the output from another segment manager.

    EVMS provides the following segment managers: DOS, GPT, System/390� (S/
    390), Cluster, BSD, Mac, and BBR. Other segment manager plug-ins can be
    added to support other partitioning schemes.

Region managers
    The third layer consists of region managers. This layer provides a place
    for plug-ins that ensure compatibility with existing volume management
    schemes in Linux and other operating systems. Region managers are
    intended to model systems that provide a logical abstraction above disks
    or partitions.

    Like segment managers, region managers can also be stacked. Therefore,
    the input object(s) to a region manager can be disks, segments, or other
    regions.

    There are currently three region manager plug-ins in EVMS: Linux LVM,
    LVM2, and Multi-Disk (MD).

    Linux LVM
        The Linux LVM plug-in provides compatibility with the Linux LVM and
        allows the creation of volume groups (known in EVMS as containers)
        and logical volumes (known in EVMS as regions).

    LVM2
          The LVM2 plug-in provides compatibility with the new volume format
        introduced by the LVM2 tools from Red Hat. This plug-in is very
        similar in functionality to the LVM plug-in. The primary difference
        is the new, improved metadata format.

    MD
        The Multi-Disk (MD) plug-in for RAID provides RAID levels linear, 0,
        1, 4, and 5 in software. MD is one plug-in that displays as four
        region managers that you can choose from.



EVMS features
    The next layer consists of EVMS features. This layer is where new
    EVMS-native functionality is implemented. EVMS features can be built on
    any object in the system, including disks, segments, regions, or other
    feature objects. All EVMS features share a common type of metadata, which
    makes discovery of feature objects much more efficient, and recovery of
    broken features objects much more reliable. There are three features
    currently available in EVMS: drive linking, Bad Block Relocation, and
    snapshotting.

    Drive Linking
        Drive linking allows any number of objects to be linearly
        concatenated together into a single object. A drive linked volume can
        be expanded by adding another storage object to the end or shrunk by
        removing the last object.

    Bad Block Relocation
        Bad Block Relocation (BBR) monitors its I/O path and detects write
        failures (which can be caused by a damaged disk). In the event of
        such a failure, the data from that request is stored in a new
        location. BBR keeps track of this remapping. Additional I/Os to that
        location are redirected to the new location.

    Snapshotting
        The Snapshotting feature provides a mechanism for creating a "frozen"
        copy of a volume at a single instant in time, without having to take
        that volume off-line. This is useful for performing backups on a live
        system. Snapshots work with any volume (EVMS or compatibility), and
        can use any other available object as a backing store. After a
        snapshot is created and made into an EVMS volume, writes to the
        "original" volume cause the original contents of that location to be
        copied to the snapshot's storage object. Reads to the snapshot volume
        look like they come from the original at the time the snapshot was
        created.



File System Interface Modules
    File System Interface Modules (FSIMs) provide coordination with the file
    systems during certain volume management operations. For instance, when
    expanding or shrinking a volume, the file system must also be expanded or
    shrunk to the appropriate size. Ordering in this example is also
    important; a file system cannot be expanded before the volume, and a
    volume cannot be shrunk before the file system. The FSIMs allow EVMS to
    ensure this coordination and ordering.

    FSIMs also perform file system operations from one of the EVMS user
    interfaces. For instance, a user can make new file systems and check
    existing file systems by interacting with the FSIM.

Cluster Manager Interface Modules
    Cluster Manager Interface Modules, also known as the EVMS Clustered
    Engine (ECE), interface with the local cluster manager installed on the
    system. The ECE provides a standardized ECE API to the Engine while
    hiding cluster manager details from the Engine.


-----------------------------------------------------------------------------
Chapter 2. Using the EVMS interfaces

This chapter explains how to use the EVMS GUI, Ncurses, and CLI interfaces.
This chapter also includes information about basic navigation and commands
available through the CLI.
-----------------------------------------------------------------------------

2.1. EVMS GUI

The EVMS GUI is a flexible and easy-to-use interface for administering
volumes and storage objects. Many users find the EVMS GUI easy to use because
it displays which storage objects, actions, and plug-ins are acceptable for a
particular task.
-----------------------------------------------------------------------------

2.1.1. Using context sensitive and action menus

The EVMS GUI lets you accomplish most tasks in one of two ways: context
sensitive menus or the Actions menu.

Context sensitive menus are available from any of the main "views." Each view
corresponds to a page in a notebook widget located on the EVMS GUI main
window. These views are made up of different trees or lists that visually
represent the organization of different object types, including volumes,
feature objects, regions, containers, segments, or disks.

You can view the context sensitive menu for an object by right-clicking on
that object. The actions that are available for that object display on the
screen. The GUI will only present actions that are acceptable for the
selected object at that point in the process. These actions are not always a
complete set.

To use the Actions menu, choose Action-><the action you want to accomplish>->
<options>. The Actions menu provides a more guided path for completing a task
than do context sensitive menus. The Actions option is similar to the wizard
or druid approach used by many GUI applications.

All of the operations you need to perform as an administrator are available
through the Actions menu.
-----------------------------------------------------------------------------

2.1.2. Saving changes

All of the changes that you make while in the EVMS GUI are only in memory
until you save the changes. In order to make your changes permanent, you must
save all changes before exiting. If you forget to save the changes and decide
to exit or close the EVMS GUI, you are reminded to save any pending changes.

To explicitly save all the changes you made, select Action->Save, and click
the Save button.
-----------------------------------------------------------------------------

2.1.3. Refreshing changes

The Refresh button updates the view and allows you to see changes, like mount
points, that might have changed outside of the GUI.
-----------------------------------------------------------------------------

2.1.4. Using the GUI "+"

Along the left hand side of the panel views in the GUI is a "+" that resides
beside each item. When you click the "+," the objects that are included in
the item are displayed. If any of the objects that display also have a "+"
beside them, you can expand them further by clicking on the "+" next to each
object name.
-----------------------------------------------------------------------------

2.1.5. Using the accelerator keys

You can avoid using a mouse for navigating the EVMS GUI by using a series of
key strokes, or "accelerator keys," instead. The following sections tell how
to use accelerator keys in the EVMS Main Window, the Selection Window, and
the Configuration Options Window.
-----------------------------------------------------------------------------

2.1.5.1. Main Window accelerator keys

In the Main Window view, use the following keys to navigate:


Table 2-1. Accelerator keys in the Main Window
+-------------------------------------+-------------------------------------+
|Left and right arrow keys            |Navigate between the notebook tabs of|
|                                     |the different views.                 |
+-------------------------------------+-------------------------------------+
|Down arrow and Spacebar              |Bring keyboard focus into the view.  |
+-------------------------------------+-------------------------------------+

 While in a view, use the following keys to navigate:


Table 2-2. Accelerator keys in the views
+-------------------------------------+-------------------------------------+
|up and down arrows                   |Allow movement around the window.    |
+-------------------------------------+-------------------------------------+
|"+"                                  |Opens an object tree.                |
+-------------------------------------+-------------------------------------+
|"-"                                  |Collapses an object tree.            |
+-------------------------------------+-------------------------------------+
|ENTER                                |Brings up the context menu (on a     |
|                                     |row).                                |
+-------------------------------------+-------------------------------------+
|Arrows                               |Navigate a context menu.             |
+-------------------------------------+-------------------------------------+
|ENTER                                |Activates an item.                   |
+-------------------------------------+-------------------------------------+
|ESC                                  |Dismisses the context menu.          |
+-------------------------------------+-------------------------------------+
|Tab                                  |Gets you out of the view and moves   |
|                                     |you back up to the notebook tab.     |
+-------------------------------------+-------------------------------------+

 To access the action bar menu, press Alt and then the underlined accelerator
key for the menu choice (for example, "A" for the Actions dropdown menu).

In a dropdown menu, you can use the up and down arrows to navigate. You could
also just type the accelerator key for the menu item, which is the character
with the underscore. For example, to initiate a command to delete a
container, type Alt + "A" + "D" + "C."

 Ctrl-S is a shortcut to initiate saving changes. Ctrl-Q is a shortcut to
initiate quitting the EVMS GUI.
-----------------------------------------------------------------------------

2.1.5.2. Accelerator keys in the selection window

 A selection window typically contains a selection list, plus four to five
buttons below it. Use the following keys to navigate in the selection window:


Table 2-3. Accelerator keys in the selection window
+-------------------------------------+-------------------------------------+
|Tab                                  |Navigates (changes keyboard focus)   |
|                                     |between the list and the buttons.    |
+-------------------------------------+-------------------------------------+
|Up and down arrows                   |Navigates within the selection list. |
+-------------------------------------+-------------------------------------+
|Spacebar                             |Selects and deselects items in the   |
|                                     |selection list.                      |
+-------------------------------------+-------------------------------------+
|Enter on the button or type the      |Activates a button                   |
|accelerator character (if one exists)|                                     |
+-------------------------------------+-------------------------------------+
-----------------------------------------------------------------------------

2.1.5.3. Configuration options window accelerator keys

 Use the following keys to navigate in the configuration options window:


Table 2-4. Accelerator keys in the configuration options window
+-------------------------------------+-------------------------------------+
|Tab                                  |Cycles focus between fields and      |
|                                     |buttons                              |
+-------------------------------------+-------------------------------------+
|Left and right arrows                |Navigate the folder tabs if the      |
|                                     |window has a widget notebook.        |
+-------------------------------------+-------------------------------------+
|Spacebar or the down arrow           |Switches focus to a different        |
|                                     |notebook page.                       |
+-------------------------------------+-------------------------------------+
|Enter or type the accelerator        |Activates a button                   |
|character (if one exists)            |                                     |
+-------------------------------------+-------------------------------------+

For widgets, use the following keys to navigate:


Table 2-5. Widget navigation keys in the configuration options window
+-------------------------------------+-------------------------------------+
|Tab                                  |Cycles forward through a set of      |
|                                     |widgets                              |
+-------------------------------------+-------------------------------------+
|Shift-Tab                            |Cycles backward through a set of     |
|                                     |widgets.                             |
+-------------------------------------+-------------------------------------+

 The widget navigation, selection, and activation is the same in all dialog
windows.
-----------------------------------------------------------------------------

2.2. EVMS Ncurses interface

The EVMS Ncurses (evmsn) user interface is a menu-driven interface with
characteristics similar to those of the EVMS GUI. Like the EVMS GUI, evmsn
can accommodate new plug-ins and features without requiring any code changes.

The EVMS Ncurses user interface allows you to manage volumes on systems that
do not have the X and GTK+ libraries that are required by the EVMS GUI.
-----------------------------------------------------------------------------

2.2.1. Navigating through EVMS Ncurses

The EVMS Ncurses user interface initially displays a list of logical volumes
similar to the logical volumes view in the EVMS GUI. Ncurses also provides a
menu bar similar to the menu bar in the EVMS GUI.

A general guide to navigating through the layout of the Ncurses window is
listed below:

��*�Tab cycles you through the available views.

��*�Status messages and tips are displayed on the last line of the screen.

��*�Typing the accelerator character (the letter highlighted in red) for any
    menu item activates that item. For example, typing A in any view brings
    down the Actions menu.

��*�Typing A + Q in a view quits the application.

��*�Typing A + S in a view saves changes made during an evmsn session.

��*�Use the up and down arrows to highlight an object in a view. Pressing
    Enter while an object in a view is highlighted presents a context popup
    menu.

��*�Dismiss a context popup menu by pressing Esc or by selecting a menu item
    with the up and down arrows and pressing Enter to activate the menu item.


Dialog windows are similar in design to the EVMS GUI dialogs, which allow a
user to navigate forward and backward through a series of dialogs using Next
and Previous. A general guide to dialog windows is listed below:

��*�Tab cycles you through the available buttons. Note that some buttons
    might not be available until a valid selection is made.

��*�The left and right arrows can also be used to move to an available
    button.

��*�Navigate a selection list with the up and down arrows.

��*�Toggle the selection of an item in a list with spacebar.

��*�Activate a button that has the current focus with Enter. If the button
    has an accelerator character (highlighted in red), you can also activate
    the button by typing the accelerator character regardless of whether the
    button has the current focus.


The EVMS Ncurses user interface, like the EVMS GUI, provides context menus
for actions that are available only to the selected object in a view. Ncurses
also provides context menus for items that are available from the Actions
menu. These context menus present a list of commands available for a certain
object.
-----------------------------------------------------------------------------

2.2.2. Saving changes

All changes you make while in the EVMS Ncurses are only in memory until you
save the changes. In order to make the changes permanent, save all changes
before exiting. If you forget to save the changes and decide to exit the EVMS
Ncurses interface, you will be reminded of the unsaved changes and be given
the chance to save or discard the changes before exiting.

To explicitly save all changes, press A + S and confirm that you want to save
changes.
-----------------------------------------------------------------------------

2.3. EVMS Command Line Interpreter

The EVMS Command Line Interpreter (EVMS CLI) provides a command-driven user
interface for EVMS. The EVMS CLI helps automate volume management tasks and
provides an interactive mode in situations where the EVMS GUI is not
available.

Because the EVMS CLI is an interpreter, it operates differently than command
line utilities for the operating system. The options you specify on the EVMS
CLI command line to invoke the EVMS CLI control how the EVMS CLI operates.
For example, the command line options tell the CLI where to go for commands
to interpret and how often the EVMS CLI must save changes to disk. When
invoked, the EVMS CLI prompts for commands.

The volume management commands the EVMS CLI understands are specified in the
/usr/src/evms-2.2.0/engine2/ui/cli/grammar.ps file that accompanies the EVMS
package. These commands are described in detail in the EVMS man page, and
help on these commands is available from within the EVMS CLI.
-----------------------------------------------------------------------------

2.3.1. Using the EVMS CLI

Use the evms command to start the EVMS CLI. If you do not enter an option
with evms, the EVMS CLI starts in interactive mode. In interactive mode, the
EVMS CLI prompts you for commands. The result of each command is immediately
saved to disk. The EVMS CLI exits when you type exit. You can modify this
behavior by using the following options with evms:

-b
    This option indicates that you are running in batch mode and anytime
    there is a prompt for input from the user, the default value is accepted
    automatically. This is the default behavior with the -f option.

-c
    This option saves changes to disk only when EVMS CLI exits, not after
    each command.

-f filename
    This option tells the EVMS CLI to use filename as the source of commands.
    The EVMS CLI exits when it reaches the end of filename.

-p
    This option only parses commands; it does not execute them. When combined
    with the -f option, the -p option detects syntax errors in command files.

-h
    This option displays help information for options used with the evms
    command.

-rl
    This option tells the CLI that all remaining items on the command line
    are replacement parameters for use with EVMS commands.

    Note NOTE
    �    Replacement parameters are accessed in EVMS commands using the $(x)
         notation, where x is the number identifying which replacement
         parameter to use. Replacement parameters are assigned numbers
         (starting with 1) as they are encountered on the command line.
         Substitutions are not made within comments or quoted strings.

         An example would be:
         evms -c -f testcase -rl sda sdb

         sda is the replacement for parameter1 and sdb is the replacement for
         parameter2


Note NOTE
�    Information on less commonly used options is available in the EVMS man
     page.
-----------------------------------------------------------------------------

2.3.2. Notes on commands and command files

The EVMS CLI allows multiple commands to be displayed on a command line. When
you specify multiple commands on a single command line, separate the commands
with a colon ( : ). This is important for command files because the EVMS CLI
sees a command file as a single long command line. The EVMS CLI has no
concept of lines in the file and ignores spaces. These features allow a
command in a command file to span several lines and use whatever indentation
or margins that are convenient. The only requirement is that the command
separator (the colon) be present between commands.

The EVMS CLI ignores spaces unless they occur within quote marks. Place in
quotation marks a name that contains spaces or other non-printable or control
characters. If the name contains a quotation mark as part of the name, the
quotation mark must be "doubled," as shown in the following example:
"This is a name containing ""embedded"" quote marks."

EVMS CLI keywords are not case sensitive, but EVMS names are case sensitive.
Sizes can be input in any units with a unit label, such as KB, MB, GB, or TB.

Finally, C programming language style comments are supported by the EVMS CLI.
Comments can begin and end anywhere except within a quoted string, as shown
in the following example:
/* This is a comment */
Create:Vo/*This is a silly place for a comment, but it is
allowed.*/lume,"lvm/Sample Container/My LVM
Volume",compatibility
-----------------------------------------------------------------------------

Chapter 3. The EVMS log file and error data collection

This chapter discusses the EVMS information and error log file and the
various logging levels. It also explains how to change the logging level.
-----------------------------------------------------------------------------

3.1. About the EVMS log file

The EVMS Engine creates a log file called /var/log/evmsEngine.log every time
the Engine is opened. The Engine also saves copies of up to nine previous
Engine sessions in the files /var/log/evmsEngine.n.log, where n is the number
of the session between 1 and 9.
-----------------------------------------------------------------------------

3.2. Log file logging levels

There are several possible logging levels that you can choose to be collected
in /var/log/evmsEngine.log. The "lowest" logging level, critical, collects
only messages about serious system problems, whereas the "highest" level,
everything, collects all logging related messages. When you specify a
