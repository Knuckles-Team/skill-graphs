#  Linux From Scratch Editor's Manual
##  Version 20210713
###  Initial Version: Gerard Beekmans
###  Git Version: Pierre Labastie
Copyright © 2004-2021 Gerard Beekmans
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
  * Redistributions in any form must retain the above copyright notice, this list of conditions and the following disclaimer.
  * Neither the name of "Linux From Scratch" nor the names of its contributors may be used to endorse or promote products derived from this material without specific prior written permission.
  * Any material derived from Linux From Scratch must contain a reference to the "Linux From Scratch" project.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
**Abstract**
This manual teaches you how to properly edit the LFS Book.
* * *
#  Dedication
This book is dedicated to all the LFS editors, who have maintained the LFS project alive over all these years.
###  Table of Contents
  * ####  Welcome to the LFS Editor's Manual
  * ####  1. LFS Development
    * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch01-introduction)
    * [Changelog](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch-scatter-changelog)
  * ###  I. Basic Source Management
    * ####  2. Git Access
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch02-introduction)
      * [Anonymous Access](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch02-anongit)
      * [Git SSH Access (for editors)](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch02-gitssh)
    * ####  3. Basic Git Commands
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-introduction)
      * [git clone](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-clone)
      * [git pull](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-pull)
      * [git add](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-add)
      * [git rm and git mv](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-delmov)
      * [git status](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-status)
      * [git commit](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-commit)
      * [git log](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-log)
      * [git push](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-push)
      * [git checkout](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-checkout)
      * [git merge](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-merge)
      * [git rebase](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-rebase)
    * ####  4. Committing Changes - Policy
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-introduction)
      * [Test the instructions](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-test)
      * [Updating general.ent](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-updategeneralent)
      * [Update chapter01/changelog.xml](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-updatechangelog)
      * [Check All Relevant Files](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-checkfiles)
      * [Commenting something out](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-commenting)
      * [Commit it!](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-commit)
      * [Update Trac](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch04-trac)
    * ####  5. Using Trac
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch05-introduction)
      * [Adding comments](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch05-addingcomments)
      * [Enter a new bug](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch05-filingbug)
      * [Assigning Tickets](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch05-assignbug)
      * [Mark an Issue Fixed](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch05-fixbug)
    * ####  6. Package Upgrade Procedures
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch06-introduction)
      * [Updating Trac](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch06-updatetrac)
      * [Update the Book](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch06-updatebook)
      * [Render the Book and Check Links](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch06-renderchecklinks)
    * ####  7. Security Advisories
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch07-introduction)
      * [Consolidated.html](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch07-consolidated)
      * [Advisories since the last release.](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch07-since-last-release)
      * [What to do when we make a release.](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch07-when-we-release)
  * ###  II. Automatization
    * ####  8. Processes
      * [Introduction](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch08-introduction)
      * [Basics](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch08-basics)
      * [Specials](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch08-specials)
      * [Processes on the main server](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch08-server)


#  Welcome to the LFS Editor's Manual
This manual will teach you what you need to know in order to properly edit the LFS-Book. It will cover some basic issues like accessing Git over SSH and the Git commands you will use. It will also discuss the proper sequence of doing things like upgrading a package and how to work with the bug tracking database.

--
Gerard Beekmans
gerard@linuxfromscratch.org
Pierre Labastie
pierre@linuxfromscratch.org

#  Chapter 1. LFS Development
##  1.1. Introduction
LFS development takes place using three main systems. First, the mailing lists `<`, `<` and (to a lesser extent) `<`. Second the Trac bug tracking system, and third the Git server where the book itself is stored. All of these services are provided by the server **`linuxfromscratch.org`**also known as**`rivendell.linuxfromscratch.org`**or more usually,**`rivendell`**. This single server provides mailing lists, web hosting, Git hosting, Trac and basically everything we use to work on the LFS project.
The LFS book is written using Docbook-XML 4.5 and is split into a number of XML files. The directories in the source tree represent the chapters of the book and each XML file within a directory typically contains the text for a section within that chapter. This structure is designed to enable a contributor to quickly locate the particular area of the book they want to edit.
The Trac ticketing system for LFS can be found at <https://wiki.linuxfromscratch.org/lfs>. In order to be able to add, remove and edit tickets, you need to add an account and make sure you are logged in whenever you wish to perform such an action. You can query and read the Trac database without logging in or having a user created. Note that all ticket messages are copied to the `<` mailing list and that all editors should be subscribed to this and the `<` list at a minimum.
See [Using Trac](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#chapter05 "Chapter 5. Using Trac") for information on how to get a user created with the appropriate update permissions for the Trac system.
Finally, there is the Git server which will be discussed in the following chapters.
##  1.2. Changelog
This is version 20210713 of the Linux From Scratch Editor's Manual, dated July 13th 2021.
Below is a list of changes made since the Last Git version of the book, first a summary, then a detailed log.
  * Added:
    * Added Current LFS Stylesheets.
    * Added entry for git log.
    * Added entry for git status.
    * Added entry for git push.
    * Added entry for git clone.
    * Added entry for git pull.
  * Removed:
    * Removed the entry for svn diff.
    * Removed the entry for svn update.
    * Renamed all the other svn xxx entries to git xxx.
    * Removed Old stylesheets.
  * Changelog Entries:
    * July 13, 2021
      * [thomas] Add chapter 8: Processes to build the books.
    * April 29, 2021
      * [ken] Add chapter 7: Security Advisories.
    * March 31, 2021
      * [bdubbs] Wording changes.
    * January 10, 2021
      * [pierre] chapter01/introduction: A few more fixes in the server name and the version of DocBook we are using.
      * [pierre] stylesheets: remove $LastChangedBy and $Date annotations that are useless in git.
      * [pierre] Chapter 4: adapt "commit it!" for git.
    * January 9, 2021
      * [pierre] Chapter 4: adapt "check relevant files" for git.
      * [pierre] Chapter 4 updating changelog: show how to have a changelog entry corresponding to only one revision of the book.
      * [pierre] Chapter 4: adapt the introduction for git.
      * [pierre] Chapter 3: rewrite the push command for git.
    * January 8, 2021
      * [bdubbs] Chapter 3: copy stylesheets and images from the lfs book.
      * [pierre] Chapter 3: rewrite the status command for git.
      * [pierre] Chapter 2 and 3: remove references to master branch and replace with trunk.
      * [pierre] Chapter 3: remove diff.xml. Add log.xml and status.xml.
      * [pierre] Chapter 3: Add xreflabel attributes for git commands, rewrite the introduction using xref.
      * [pierre] Chapter 3: rewrite the diff, merge, pull, push, rebase commands for git.
    * January 7, 2021
      * [pierre] Chapter 3: add push.xml.
      * [pierre] Chapter 3: rewrite the add, checkout, clone, commit, rm, mv commands for git.
    * January 5, 2021
      * [pierre] Chapter 3: Rewrite the introduction for git.
      * [pierre] Chapter 3: Remove update.xml, moving.xml, delete.xml. Add clone.xml, pull.xml, delmov.xml, rebase.xml (templates).
      * [pierre] Stylesheets: Remove and use those of the lfs book.
      * [pierre] Makefile: Create variables so that using a local layout is easier. Fix some obsolete commands.
      * [pierre] Chapter 2: Change filenames, rewrite things so that the commands refer to git instead of svn. Fix hostnames.
    * January 4, 2021
      * [pierre] introduction: Fix hostnames. change subversion to git. Change XML coding style.
      * [pierre] prologue: slight rewrite. Change XML coding style to what we have in the other books.
      * [pierre] tag Last_SVN_Version.


#  Part I. Basic Source Management
##  Chapter 2. Git Access
##  2.1. Introduction
The rivendell Git server provides repositories for all of the *LFS projects (and some others). The repository which we are interested in for LFS editing is (unsurprisingly) the LFS repository. A complete list of the modules which are available can be found using the Trac source browser interface at <https://wiki.linuxfromscratch.org/lfs/browser>.
There are two types of Git access to the LFS tree. First, there is anonymous read-only access which anyone can use. Second, there is read-write access granted to active editors.
###  Note to Subversion Users
Subversion is a centralized version control system, which means there is a unique repository on the server, and that users can _check out_ that repository to a working directory on their local machine. Users with write access can then _commit_ their modifications to the repository on the server.
Git is a distributed version control system, which means that all users have their own repository. The repository on the server is nothing more than the others, except that a public access is granted to it. The action of copying the repository from the server to the local machine is named _cloning_. Checking out and committing thus only occur locally. The action of synchronizing the public repository with the local one is named _pull_ (public to local) or _push_ (local to public for users with write access).
##  2.2. Anonymous Access
To get anonymous access, simply use the following command (note that this assumes you are using bash or a similar shell:
```
`git clone https://git.linuxfromscratch.org/lfs.git lfs-git`
```

This will copy the public repository to a subdirectory named `.git` in the directory `lfs-git` and then checkout the default branch to that directory. It will also set the local repository to track the default branch of the public repository so that you can update your local repository by simply running (after changing to directory `lfs-git`):
```
`git pull`
```

Note that for the LFS book, the default branch is named _trunk_.
##  2.3. Git SSH Access (for editors)
For editors, access is slightly more complicated. You first need to generate an ssh key-pair. To generate the keys run:
```
`ssh-keygen -t ed25519`
```

###  Note
Editors are not required to have an account on the server, but it may be helpful.
When prompted where to save them, it's probably best to leave them in .ssh (as `id_ed25519` and `id_ed25519.pub`). When prompted for a passphrase just press enter unless you want to give the phrase _every_ time you synchronize to the server. However, since the same passphrase will be used when you log in to _rivendell_ over ssh, it may be advisable to have some security in place.
Having generated your keys, send the `~/.ssh/id_ed25519.pub` to an LFS administrator in order to have it added to `~git/.ssh/authorized_keys` _on rivendell_. If you will be obtaining a login account on the server, the administrator will use the same key to allow you ssh access.
Your local copy of `id_ed25519` and `id_ed25519.pub` should remain untouched by this process.
Once this process is set up, try to checkout the latest LFS book revision by running (from your local machine):
```
`git clone git@git.linuxfromscratch.org:lfs.git lfsbook`
```

If all goes well you will download a copy of the current repository to `lfsbook/.git` and you will check out the default branch, which is named _trunk_. You will also have write access so from now on be extra careful. Note that _no_ changes will be made until you issue a **`git               push`**command.
The above is fine for getting the default branch, but you may want to work on a different public branch. To set up a local branch that tracks a public branch named _new_branch_ , just issue:
```
`git checkout --track origin/_<new_branch>_`
```

###  Note to Subversion Users
Contrary to Subversion, where you need to check out a new working copy of the remote branch, with Git almost nothing is downloaded. The local directory now reflects the new branch, but the old branch directory does not exist anymore.
If you need to work on the default branch named _trunk_ , just commit your changes (if any) to the new branch (the commit is local), and switch back to trunk with:
```
`git checkout trunk`
```

Since the new branch is already set up, if you want again to work on the new branch, just do:
```
`git checkout _<new_branch>_`
```

As with anonymous access, you can update your local repository by simply **cd** 'ing into the LFS directory and running:
```
`git pull`
```

##  Chapter 3. Basic Git Commands
##  3.1. Introduction
Let's get familiar with the basic set of commands which all editors will use on an almost daily basis. There are many more options available than the ones listed here, so you will want to read the Git documentation (**git`help`** also provides a useful quick reference for Git commands. Sometimes **git status** shows a couple of commands that an user might want to run in the current state of the repository.
###  Note to Subversion Users
As already said, the Git repository is on the local machine. More precisely, the directory holds a working copy of some branch of the repository, and the repository itself is stored under the `.git` directory along with various configuration settings. The command [git checkout](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-checkout "3.10. git checkout") is used to switch branches.
In addition to the local repository, git maintains a staging area that is known as the index. The command [git add](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-add "3.4. git add") populates that staging area and [git commit](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-commit "3.7. git commit") is used transfer the content of the index to the repository. This allows for a fine control of what is committed, but several shortcuts can be taken. Contrary to subversion, **git add** is not only be used to add files, but also to store modifications to the existing files.
##  3.2. git clone
**`git clone`**. This command is used to copy a public repository to the local machine and checkout the default (_trunk_ for LFS) branch. You should only need to do this once. Various options allow creation of a “shallow” repository that does not contain the full history or all the branches. See **git help clone**.
#####  Examples
To clone the LFS repository with only read access:
```
`git clone https://git.linuxfromscratch.org/lfs.git lfsbook`
```

To clone with read/write access:
```
`git clone git@git.linuxfromscratch.org:lfs.git lfsbook`
```

##  3.3. git pull
**`git pull`**. This command synchronizes your local repository. If you have made local changes, Git will try to merge any changes on the server with the changes you have committed _on your machine_. If the changes on the server overlap with local uncommitted changes, the merge is cancelled, and the work tree will remain untouched.
Unlike **svn`up`** , when Git merges your local commits with the changes on the server, it will produce a merge commit. Too many merge commits may cause the history to be confusing. As an alternative, one can pass `--rebase` to **git`pull`** , telling Git to rebase your local commits onto the changes on the server. Read [git rebase](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-rebase "3.12. git rebase") for the details about rebasing.
To make a clean history, editors should use rebasing instead of merging for synchronizing the changes on the server if you have some local commits. To make `--rebase` the default for **git pull** , issue: **git config pull.rebase true**.
You should always do a manual **git`pull`** before trying to push changes in order to ensure that there are no conflicts with changes that have been made since you started your work. Note that **git`push`** will warn you if there is a conflict and you forget to perform a **git`pull`**.
##  3.4. git add
**`git add [_`modified-files`_]`**. This stages the modifications to all the `modified-files` (including newly created files) to the index. If you specify a directory in `modified-files`, all the files modified in this directory or its subdirectories are staged. The change is not in the local repository until you do a **`git commit`**. We will touch on this more as we continue in the chapter.
This command can be used in a very flexible way by using the `-p` option. You can select each hunk of the diff that is staged into the index. This allows testing a full change and then divides commits into small “atomic” pieces that are easier to review and understand.
##  3.5. git rm and git mv
**`git rm`**. This removes a file and lets Git know about it. Various options allow selecting whether the file is only deleted in the index or both in the index and the working directory. Note that you need to commit (and possibly push) for the removal to appear in the repository.
**`git mv`**. This renames or moves a file and lets Git know about it. Again, you need to commit (and possibly push) for the change to appear in the repository.
##  3.6. git status
**`git status`**. This is probably the command you'll be using most often. It prints the files that have been modified in the working directory, and that are not in the index, or that are in the index and not committed yet. It also outputs the state of the local repository respective to the remote one.
A very handy feature is that it outputs a list of commands that can be used in the current context.
##  3.7. git commit
**git`commit`**. This command stores your changes to the _local_ repository. Normally it commits changes staged in the index, but various options allow you to bypass staging. Note that nothing is changed on the server until you issue **`git               push`**. The`-m` and `-F` options can be used to pass a log message to the command. If you don't specify a _-m "MESSAGE"_ or _-F "Filename"_ option, Git will open the default editor and ask you to type in a log message. The default editor is specified by the environment variables, `GIT_EDITOR` or `VISUAL` or `EDITOR` (checked in that order) or by a configuration parameter in `~/.git/config`. For example, to set your default editor to vim, run:
```
`export GIT_EDITOR=vim`
```

or:
```
`git config --global core.editor vim`
```

Do not use empty log messages (see later in this document on the policy which governs them).
##  3.8. git log
**`git log`**. Outputs the commit log of the branch currently in the working directory. Various options allow customizing the level of information given for each commit. Editors are strongly advised to run this command before pushing to the remote repository or merging. If the history is too convoluted, it may be necessary to run[git rebase](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html#ch03-rebase "3.12. git rebase") in order to simplify it. Your co-editors will hate you if you change the history after pushing it.
###  Note to Subversion Users
The output is automatically passed to a pager so that it is not necessary to pipe it to **less**. Furthermore, no access to the remote repository is needed, so it is usually much faster to get a long log.
##  3.9. git push
**`git push`**. This command synchronizes the public repository on the server with your local one. You should make sure you want to publish all the commits you have made. Sometimes it may be useful to run**`git rebase -i`**in order to simplify the history. Also, to prevent conflicts when pushing, it is better to first use**`git pull`**prior to pushing and resolve any conflicts locally.
##  3.10. git checkout
**`git checkout`**. This command is used to make a branch of the local repository visible in the working directory.
###  Note to Subversion Users
**`git checkout`**is sometimes confusing to subversion users because it is very different from**`svn                 checkout`**. The former is closer to**`svn switch`**. When using Git, you will find yourself creating branches rather often, and using**`git                 checkout`**to switch between them is a rather common command.
##  3.11. git merge
**`git merge`**. This is useful to apply changes from another branch (or several branches) to the current one. By default the resulting changes are committed. This can be prevented with the`--no-commit` option, which gives you a chance to inspect and further tweak the merge result before committing.
In some cases, merging results in conflicts that have to be manually resolved. Note that edits should merge only to a clean branch, that is, after committing all changes.
###  Note to Subversion Users
Contrary to subversion, there is no `--dry-run` option to **`git merge`**. But a repository can always be reset to a previous state with**`git reset --hard                 <commit-id>`**.
##  3.12. git rebase
**`git rebase`**This is useful to have the current branch start from another point in the history. For example if you have:
```
                              B1---B2---B3    my_branch
                             /
                            A---C1---C2       trunk

```

rebasing my_branch onto trunk will produce:
```
                              B'1---B'2---B'3 my_branch
                             /
                   A---C1---C2                trunk

```

where the state reached after commit B'3 is the same as it was at B3.
But the most useful command is **`git rebase -i`**that allows you to rewrite history when you have made messy commits.
##  Chapter 4. Committing Changes - Policy
##  4.1. Introduction
Here is a summary list of things to do before committing changes:
  * Test the instructions you are adding.
  * Update `general.ent` with the new date.
  * Update `chapter01/changelog.xml.`
  * Check that all relevant files have been **`git add`**'d or**`git rm`**'d.
  * Check the validity of the XML.
  * Check that the book renders properly.
  * Commit; go back to the beginning if you have another set of changes you want to make.
  * Push once you are done with all your changes.
  * Update Trac to reflect the changes.


You should normally restrict a commit to one set of changes, so if you are updating the versions of three packages you will usually do that in three separate commits. Clearly, what forms a "set" is a matter for your judgement. Always think that a set will have to be merged to (at least) the multilib branch. Pushing is not mandatory after each change if you plan to soon make another one. Once again, editors should run **`git pull`**before pushing in order to resolve any conflict locally.
The editors of the LFS book prefer that changes to the date in general.ent are made as part of a _real_ change.
##  4.2. Test the instructions
This may seem _really_ obvious but it's very easy to make a typo in installation command changes which causes the installation to break. We've all done it, you'll probably do it too eventually. But double check to minimize the chance.
##  4.3. Updating general.ent
The following elements should be uncommented and updated in the `general.ent` file when a release (including -rc releases) is made, and the two lines about `version.ent` should be commented out:
```
<!ENTITY version         "10.2-rc1">
<!ENTITY versiond        "10.2-rc1">
<!ENTITY releasedate     "August 26th, 2021">
<!ENTITY copyrightdate   "1999-2021">
```

For development snapshots, these entities are automatically generated from the Git commit info. So `general.ent` does not need to be updated.
##  4.4. Update chapter01/changelog.xml
Changelog updates should _always_ be provided with the exception of small typo fixes. You don't need to add "fixed small typo in XXX" to the changelog otherwise it will grow too much.
Changelog updates need to be in the following format:
```
<listitem>
  <para>Month Day, Year</para>
  <itemizedlist>
    <listitem>
      <para>[username] - What you changed.</para>
    </listitem>
<!-- if it only applies to the sysv version (adapt for systemd) -->
    <listitem revision="sysv">
      <para>[username] - What you changed only for sysv version.</para>
    </listitem>
    <listitem>
      <para>[username] - Previous changelog entry from the same day,
      by you or another editor.</para>
    </listitem>
  <itemizedlist>
</listitem>
```

Example:
```
<listitem>
  <para>March 3, 2006</para>
  <itemizedlist>
    <listitem>
      <para>[renodr] - Update to attr-2.5.1. Fixes
      <ulink url="&lfs-ticket-root;4833">#4833</ulink>.</para>
    </listitem>
  </itemizedlist>
</listitem>
```

Changelog entries are always on top of the previously added changelog entry.
##  4.5. Check All Relevant Files
If you are adding files, you need to run a **git add** command on each of them. When you remove files, you should always do that with **git rm**. Moving or renaming files is done with **git mv**. Adding a directory and all its children is done with **git add <dirname>**.
If you think you're ready to commit, run **git status** to see the state of the working copy. The normal process is to first **git add** the files that are modified to the index, then run **git commit** to store the set of changes into the local repository. The output of git status looks like this:
```
On branch trunk
Your branch is up to date with 'origin/trunk'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   TODO
```

where the "Changes to be committed" appear in green, while the "Changes not staged for commit" appear in red.
##  4.6. Commenting something out
Sometimes, a change will make something no longer appropriate, but you think that it might be needed in the future. If you comment it out in the normal way, and start the comment with a `FIXME:` marker, that will be highlighted whenever the file is edited, at least if you use vim.
If you encounter a _FIXME:_ in a comment, do not automatically assume that it can be deleted because the following instructions have now been commented out.
Note that there is no example here - the rendering of html strips out comments, and an empty box looks silly. As always, render your local copy after you comment something out, so that you can see the result!
##  4.7. Commit it!
Once you are sure that everything renders and that you know which files you wish to commit, you're ready. First commit locally:
  * Normal Procedure: allows to only commit what you want
    * Run **git add _`<file1>                           <file2> ...`_**
    * After verifying that all has been correctly staged (use **git status** and/or **git diff --staged**), run **git commit** and fill up the log message in the editor window. Or for a short log message, run **git commit -m "_`log                           message`_"**.
  * Shortcut to commit all modified files in one go:
    * Run **git commit -a** and write the log message in the editor window. As above, you can use the `-m` option for short log messages.


Now push your work: **git push**. A transaction log of all the commits that make up the push will be emailed to the `<` mailinglist so other editors can see right away what you did. The commit emails contain some basic info (log, changes to which files) including a _diff -u_ format output.
_About log messages:_ Due to the way **git log** displays log messages, please keep the size of each line below 72 characters. A good commit message is composed of a short summary (not more than fifty characters), a blank line, then details, reasons, etc on less than 72 characters lines. Log messages should _never_ be empty. Even if the message is just 'small typo fix', that'll do. Other usual messages are 'update to package-x.y.z' or 'fixed installation instructions of package foo'. That last one usually needs also explanation lines as said above.
_Example_ : If you have modified `general.ent`, the changelog, and fixed a typo in chapter 6 bash installation, the workflow could be:
```
`git add general.ent chapter01/changelog.xml chapter06/bash.xml
git commit -m 'fixed a typo in chapter 6 bash'`
```

##  4.8. Update Trac
The final part of updating the book is to update the ticket. This is usually as easy as going to the wiki (<https://wiki.linuxfromscratch.org/lfs>), going to the ticket and choosing resolve, changing resolution to fixed.
##  Chapter 5. Using Trac
##  5.1. Introduction
This chapter covers the things you need to do when you are using Trac for entering new bugs into the system and fixing/updating outstanding bugs.
We assume you have already logged into Trac before doing anything outlined in the following sections.
##  5.2. Adding comments
  * Go to the ticket you want to add comments to
  * Add your additional information in the _Comment_ box.
  * As the last step, click on the _Submit changes_ button to commit your changes to the database. A log of this will be sent to the lfs-book mailinglist.


##  5.3. Enter a new bug
You found a bug, or somebody else found a bug and you decided to add it to Trac. Or you want to log a request for a feature that somebody has asked for or a task of some other type.
  * Go to <https://wiki.linuxfromscratch.org/lfs/newticket>
  * Select the ticket type (defect for bugs, or enhancement, or task).
  * The _Short summary_ and _Full Description_ are mandatory.
  * Select the _Priority_. Use your own judgement on how important fixing this bug is. If you're not sure just leave the default. Priorities are periodically re-evaluated and changed anyway.
  * Select the _Component_ - the only options are Book or Bootscripts.
  * Select the _Severity_ as appropriate, anything from trivial to critical or blocker.
  * If you don't want to assign yourself to it right away, leave the _Assign To_ field blank. It will be assigned to `<` until an editor changes that to himself.
  * If you wish, select a _Milestone_ , either the next version, or future.
  * Select the proper _Version_. You most always will choose the _SVN_ version. It doesn't make sense to report a bug against an old version if it's no longer in Subversion. If it is, then SVN is newer than a previously released stable book version. The versions are basically there only for people who don't edit the book and who want to report a bug against the book version they have.
  * Fill in the _Keywords_ and _Cc:_ fields if you wish.
  * If you are using any formatting in the Full description field, you may wish to click on the _Preview_ button.
  * As the last step, click on the _Submit ticket_ button to commit your changes to the database. A log of this will be sent to the `<` mailinglist.


##  5.4. Assigning Tickets
When you are ready to start working on an issue that is in Trac, step one is to assign it to yourself. This informs all the editors that you are working on the issue.
  * Go to the issue you want to work on.
  * Select the _Accept ticket_ radio button.
  * Click on the _Submit changes_ button.
  * While working on the issue, sometimes you may want to add comments to it. Feel free to do so.


##  5.5. Mark an Issue Fixed
Once you have fixed an issue and have committed the relevant changes into the Subversion repository, you need to mark the ticket fixed in Trac.
  * Go to the ticket you fixed and which is assigned to you.
  * Select the “resolve as” radio button. Then select the proper resolution. Usually you'll select _fixed_ here, but there are times when you select other ones like cases where a reported issue is (_invalid_), or we know about it but won't fix it (_wontfix_) and so on.
  * Click on the _Submit changes_ button to commit the changes to the database.


##  Chapter 6. Package Upgrade Procedures
##  6.1. Introduction
Updating a package in the LFS-Book consists of the following:
  * Updating Trac to announce the availability of a new version of a package.
  * Updating the book to reflect the new version of the package.


##  6.2. Updating Trac
When a new package is released by its maintainers, we mark this in Trac. You don't need to update the book right after a package is released, but at least announce it.
  * Go to Trac's query page at <https://wiki.linuxfromscratch.org/lfs/report>
  * Choose Active Tickets and look for the name of the package.
  * Create a new ticket for the new version (as previously discussed under entering a new bug). Mark it as an enhancement. Add any interesting information, e.g. from the release notes. When you have put in all the information you wish to record, click on _Submit ticket_ in the normal way.
  * If there is an existing open ticket for a prior version of the package, resolve that as _wontfix_ with a note that it has been superseded by the new ticket. Alternatively, select _Modify Ticket_ and update the Summary and Description to reflect the new version.


##  6.3. Update the Book
When you're going to update the book by adding a new package to it, here's how you do it:
  * Assign yourself to the ticket for this new package.
  * Test build an LFS system to make sure this package compiles properly in an LFS environment. Don't use your regular workstation's environment - it may be sufficiently different for to affect the build procedures. A package may depend on something that you have installed but which doesn't come with the LFS-Book. Also keep in mind that some packages are used more than once in the LFS build process.
  * Update the installation instructions in the book, if necessary.
  * When the package compiles properly and the package works too (doesn't seg fault or show other errors when trying to execute programs from it), then open the `packages.ent` in an editor.
  * Find the _package-version_ entity and update its value to the new version.
  * Update the list of files installed by the new version of the package. This can be trivially gathered by using **find** immediately prior to and immediately after installing the new version and **diff** ing the output.


##  6.4. Render the Book and Check Links
Now that you're done, make sure the book renders properly and check the links in _Chapter 3_ to make sure the new package links are valid.
If this checks out, then you're done with the package update. For more information about how to build the HTML files from the book sources, refer to _Chapter 8_.
Commit your changes to the Git repository.
##  Chapter 7. Security Advisories
##  7.1. Introduction
In both LFS and BLFS we try to advise our users of security vulnerabilities. Sometimes vulnerabilities are mentioned in a release announcement, at other times they are noticed later.
The current advisories point to the development books, with past advisories pointing to the numbered books (rather than to'stable' ). You will probably need to create some symlinks in wherever you render the books so that both versions of the current LFS and BLFS books point to your local copies so that you can check them before pushing. If you have local renders of the current released books you can also link to those. Because `consolidated.html` is located in the BLFS book, you will need to make a special symlink to get to that from your local LFS advisories.
For historical reasons, the links at rivendell point to 'svn' and 'systemd' for the current books.
Normally we will raise a security advisory once we have a tested fix in the appropriate book (LFS or BLFS), i.e. a newer version, or a patch. However sometimes a vulnerability remains open for a long time and we may choose to suggest a workaround such as "do not use this feature of the package".
We try to provide enough details to enable users to decide if they need to update as soon as possible, including a vulnerability assessment and any details we can find. If upstream provides an assessment of the severity we will normally use that. Otherwise we must search around for details. If details of a CVE are publicly visible there might be a rating at
In theory, a user of a recent past version of the book can look at our current and previous vulnerabilities and see every fixed vulnerability which affects a package. In practice it is not always clear that a newer version has fixed a vulnerability - if that comes to light after we have made a release with a newer version of the package such items might be ignored on the grounds that most users have already looked at the previous vulnerabilities and are unlikely to notice new additions - for example a vulenrability in flac-3.2 was fixed in flac-3.3 but not publicly mentioned. In such cases we can add a 'Late Advisories' section between the advisories for the current book and the previous advisories - see 10.0-102 in `consolidated.html` and the corresponding entry in `10.0.html`. In these cases, the best way to alert users is to announce the advisory on the lfs-support and blfs-support lists.
From time to time we may become aware that the details of an advisory should be changed, e.g. it might be that it is invalid for some reason (e.g. never in a released version, or only applicable to windows). When this happens we can modify the existing item and change the 'Date' entry to 'Updated' with the current date.
For day to day updates to advisories the files are organized into:
  * `blfs/advisories/consolidated.html` (shared between LFS and BLFS).
  * `lfs/advisories/NN.N.html` (for any LFS advisories since the current (NN.N) release).
  * `bfs/advisories/NN.N.html` (for any BLFS advisories since the current (NN.N) release).


There are two parts to creating an advisory:
  * Taking the next available number to create an entry in `consolidated.html` containing the necessary details.
  * Adding summary advisory details for this version of LFS or BLFS.


_Much of any new item will be copied from a template or from an earlier advisory. It is important to take your time when reviewing what you have created, to see that it reads and links correctly._
##  7.2. Consolidated.html
The consolidated page provides a list of our advisories since we began to create them. They are numbered within releases, in each case newest first. This page lives in `blfs/advisories` but it is common to both LFS and BLFS.
Create the details for the next available advisory number. The top part of the page contains a lot of commented items which can be used as a template, but if there are previous advisories for this package it may be easier to copy details from one of those.
As well as the number, and the sa-NN.N-nnn link, each entry has a date and a severity. Where upstream has assigned a severity we normally go with that. If a source such as NVD has assigned a severity, consider if it is appropriate (our default is 'High' even for Denial of Service on non-server programs).
Where one or more CVEs have been issued, it may be useful to link to NVD if that provides details, or else to any other reliable source which explains the vulnerability (i.e. google for it). If the details are not public, you might not be able to find a suitable external link. But for packages which provide their own advisories it is good to link to those.
Render the page, check that the links (external to applications, and internal to the sysv and systemd books) work correctly and that what you have written and pasted makes sense.
It might be beneficial to commit the change to consolidated.html at this point, so that you own the advisory number (e.g. if you think other people may also be updating advisories). In that case it is probably best to do only one if you have several, and to then update the page for the current release.
##  7.3. Advisories since the last release.
There are separate pages for LFS and BLFS where we list our advisories since our last release. These pages are in alphabetical order, with newer advisories coming before older ones for the same package.
In both LFS and BLFS the page is labelled with the number of our current release, so 10.1.html from March 2021 until we release our next version.
You will see there is a commented <h3>PackageName<h3> as a guide. The <h4> line should be copied from the entry you created in `consolidated.html`. Follow that with a short paragraph summarising the problem and how to fix it (or in exceptional cases other actions to work around the problem). Add a sentence linking to the advisory in `consolidated.html`.
Some packages get extra information, e.g. Thunderbird has an italic paragraph explaining how the vulnerabilities are in a browser-like context. If this is the first advisory for Thunderbird in this release, copy that part from the previous advisories. Similarly, in LFS glibc gets different information because the only supported upgrade path in LFS is to build a new LFS: give information to let users decide how serious the vulnerabilit{y,ies} is/are for their use-case (many are quite old).
##  7.4. What to do when we make a release.
When a new release of the books is ready (i.e. the new book directories for this version have been populated), there are notes in the `Notes-re-release.txt` files:
As well as updating `index.html` for the new release, and creating a new page for the new version - initially stating "There are no known security vulnerabilities" - the advisories for what is now the previous release need to be amended.
That is because the packages in that release have been tested up to the versions and packages in that release, and from time to time packages will later drop out, or be replaced by forked versions, or even move to a different part of the book. So the links should be changed so that instead of pointing to the development book, they now point to the version we have just released.
#  Part II. Automatization
##  Chapter 8. Processes
##  8.1. Introduction
This chapter describes the processes on how to convert the DocBook XML sources to HTML which are presented to the users on the website. The processes are basically same on a local machine when the user clones the XMLs to a local repository and wants to create the HTML files there.
Prerequisites are a small set of tools, namly [ make](https://www.linuxfromscratch.org/lfs/view/development/chapter08/make.html), [ DocBook XML](https://www.linuxfromscratch.org/blfs/view/svn/pst/docbook.html), [ DocBook XSLT](https://www.linuxfromscratch.org/blfs/view/svn/pst/docbook-xsl.html) and the [ xsltproc](https://www.linuxfromscratch.org/blfs/view/svn/general/libxslt.html) tools. This tools are used to convert DocBook XML to other formats, most used target format is HTML which can be used to present the books in a nicely formatted way to the user. Other formats might be PDF, but this is not part of this chapter.
This chapter is divided in following parts:
  * Basics on conversion
Describe the basic steps to convert the XMLs to HTML which are common to LFS and BLFS.
  * Specials in LFS or BLFS
Notes on specials to keep in mind when converting the LFS or the BLFS book.
  * Processes on the server
Notes for editors and admins maintaining the book conversion on the main LFS server.


##  8.2. Basics
###  8.2.1. Rendering books
When a book has been checked out (cloned), change into the top level directory of the book. The creation of the HTML files is started with following command:
```
`make`
```

By default, the sysv version of the book will be rendered. To create the systemd version issue:
```
`make REV=systemd`
```

The only allowed values for REV are `sysv` or `systemd`. Any other value - while sysv is the default when nothing is specified - will cause an error.
The output location is depending on the type of the book, it will be different when building the LFS, the BLFS or any other book. Usually, the output is a drectory in the HOME directory of the current user. As time of writing, the directories are
_Type_ |  _Directory_
---|---
LFS (sysv) |  ~/lfs-book
LFS (systemd) |  ~/lfs-systemd
BLFS (sysv) |  ~/public_html/blfs-book
BLFS (systemd) |  ~/public_html/blfs-systemd
Editors guide (this book) |  ~/lfs-editors-guide-output
To specify a different output directory, use the BASEDIR parameter:
```
`make BASEDIR=<path/to/put/the/htmls>`
```

Of course, a combination of REV and BASEDIR is allowed.
####  8.2.1.1. Other common parameters
To control whether the build process should show all executed commands in detail, use a non-empty parameter V:
```
`make V=1`
```

The build process of LFS or BLFS books requires the production of some temporary data. Parameter RENDERTMP defines where to store such temporary files. The default is `$HOME/tmp` and can be set to any other directory but it should be different to BASEDIR:
```
`make RENDERTMP=<path/to/put/temp/files>`
```

###  8.2.2. Bootscripts / Service files
TODO: Describe what to do when bootscripts has been changed. Edit chglog, update general.ent in LFS, ..., copy over to anduin, ...
##  8.3. Specials
###  8.3.1. Specials
This section describes some extensions and variations available for some type of books.
####  8.3.1.1. LFS - Multilib version
There is a special branch of the LFS book which includes additional instructions for those users who like to build a system which supports 32bit binaries and not only 64bit. For more details about how and why, refer to that book, here only the parameters required to build the ML book are discussed.
In order to use the multilib version of the book, the repository must be switched to the branch `multilib` by using git:
```
`git checkout multilib`
```

To control if and which multilib version of the book will be created, use the ARCH parameter.
```
`make ARCH=ml_32`
```

Possible values for ARCH are `ml_32` to include instructions to support the m32 binaries or `ml_x32` for the mx32 architecture. `ml_default` which is used when ARCH is not given, includes none of the additional instructions and the resulting book is nearly identical to the book when the `trunk` branch is used. `ml_all` includes both `ml_32` and `ml_x32` instructions.
##  8.4. Processes on the main server
###  8.4.1. Scripts
Useful scripts to automate the daily rendering of the books are located in `/usr/local/bin`.
Following a list of scripts which might be of interest for rendering and installing the books on the main server:
  * build-lfs-edguide.sh
(no parameters)
This script creates the Editors Guide as a "one-pager" - meaning the whole guide is in one HTML page.
The result can be viewed at [ https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html](https://www.linuxfromscratch.org/lfs/LFS-EDITORS-GUIDE.html).
  * check-blfs-files.sh
...
  * render-blfs-book-systemd.sh
...
  * render-blfs-book.sh
...
  * render-lfs-book-dev.sh
...
  * render-lfs-book-systemd.sh
...
  * update-hints.sh
...
  * update-patches.sh
...
  * update-website.sh
...


###  8.4.2. Cronjobs
There are several cronjobs (tasks executed automatically at a specific time). Those tasks automated the rendering of the books as well as the handling of files like patches, bootscripts and so on.
Following a list of cronjobs defined on the main server:
...
