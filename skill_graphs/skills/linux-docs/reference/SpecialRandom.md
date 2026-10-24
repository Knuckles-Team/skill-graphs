[](https://archlinux.org/)
  * [Home](https://archlinux.org/)
  * [Packages](https://archlinux.org/packages/)
  * [Forums](https://bbs.archlinux.org/)
  * [Wiki](https://wiki.archlinux.org/)
  * [GitLab](https://gitlab.archlinux.org/archlinux)
  * [Security](https://security.archlinux.org/)
  * [AUR](https://aur.archlinux.org/)
  * [Download](https://archlinux.org/download/)


[Jump to content](https://wiki.archlinux.org/title/Touchegg#bodyContent)
Main menu
Main menu
move to sidebar hide
Navigation
  * [Main page](https://wiki.archlinux.org/title/Main_page "Visit the main page \[alt-z\]")
  * [Table of contents](https://wiki.archlinux.org/title/Table_of_contents)
  * [Getting involved](https://wiki.archlinux.org/title/Getting_involved "Various ways Archers can contribute to the community")
  * [Wiki news](https://wiki.archlinux.org/title/ArchWiki:News "The latest lowdown on the wiki")
  * [Random page](https://wiki.archlinux.org/title/Special:Random "Load a random page \[alt-x\]")


Interaction
  * [Help](https://wiki.archlinux.org/title/Category:Help "Wiki navigation, reading, and editing help")
  * [Contributing](https://wiki.archlinux.org/title/ArchWiki:Contributing)
  * [Recent changes](https://wiki.archlinux.org/title/Special:RecentChanges "A list of recent changes in the wiki \[alt-r\]")
  * [Recent talks](https://wiki.archlinux.org/index.php?title=Special:RecentChanges&namespace=all-discussions)
  * [New pages](https://wiki.archlinux.org/title/Special:NewPages)
  * [Statistics](https://wiki.archlinux.org/title/ArchWiki:Statistics)
  * [Requests](https://wiki.archlinux.org/title/ArchWiki_talk:Requests)


[ **ArchWiki** ](https://wiki.archlinux.org/title/Main_page)
[Search ](https://wiki.archlinux.org/title/Special:Search "Search ArchWiki \[alt-f\]")
Search
Appearance
Appearance
move to sidebar hide
Text
  * Small
Standard
Large

This page always uses small font size
Width
  * Standard
Wide

The content is as wide as possible for your browser window.
Color (beta)
  * Automatic
Light
Dark

This page is always in light mode.
  * [Create account](https://wiki.archlinux.org/index.php?title=Special:CreateAccount&returnto=Touchegg "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://wiki.archlinux.org/index.php?title=Special:UserLogin&returnto=Touchegg "You are encouraged to log in; however, it is not mandatory \[alt-o\]")


Personal tools
  * [Create account](https://wiki.archlinux.org/index.php?title=Special:CreateAccount&returnto=Touchegg "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://wiki.archlinux.org/index.php?title=Special:UserLogin&returnto=Touchegg "You are encouraged to log in; however, it is not mandatory \[alt-o\]")


Toggle the table of contents
## Contents
move to sidebar hide
  * [ Beginning ](https://wiki.archlinux.org/title/Touchegg)
  * [ 1 Installation ](https://wiki.archlinux.org/title/Touchegg#Installation)
  * [ 2 Configuration ](https://wiki.archlinux.org/title/Touchegg#Configuration)
  * [ 3 Start on login ](https://wiki.archlinux.org/title/Touchegg#Start_on_login)


# Touchegg
1 language
  * [Page](https://wiki.archlinux.org/title/Touchegg "View the content page \[alt-c\]")
  * [Discussion](https://wiki.archlinux.org/title/Talk:Touchegg "Discussion about the content page \[alt-t\]")


English
  * [Read](https://wiki.archlinux.org/title/Touchegg)
  * [View source](https://wiki.archlinux.org/index.php?title=Touchegg&action=edit "This page is protected.
You can view its source \[alt-e\]")
  * [View history](https://wiki.archlinux.org/index.php?title=Touchegg&action=history "Past revisions of this page \[alt-h\]")


Tools
Tools
move to sidebar hide
Actions
  * [Read](https://wiki.archlinux.org/title/Touchegg)
  * [View source](https://wiki.archlinux.org/index.php?title=Touchegg&action=edit)
  * [View history](https://wiki.archlinux.org/index.php?title=Touchegg&action=history)


General
  * [What links here](https://wiki.archlinux.org/title/Special:WhatLinksHere/Touchegg "A list of all wiki pages that link here \[alt-j\]")
  * [Related changes](https://wiki.archlinux.org/title/Special:RecentChangesLinked/Touchegg "Recent changes in pages linked from this page \[alt-k\]")
  * [Permanent link](https://wiki.archlinux.org/index.php?title=Touchegg&oldid=847860 "Permanent link to this revision of this page")
  * [Page information](https://wiki.archlinux.org/index.php?title=Touchegg&action=info "More information about this page")


From ArchWiki
Touchegg is not compatible with Wayland.
## Installation
[Install](https://wiki.archlinux.org/title/Install "Install") the [touchegg](https://archlinux.org/packages/?name=touchegg) package. Install [touche](https://aur.archlinux.org/packages/touche/)AUR if you want a desktop application to configure touchegg.
For X11 GNOME, one can also install the extension
## Configuration
The default configuration can be found in `/usr/share/touchegg/touchegg.conf`.
To customize it, copy the default configuration to `~/.config/touchegg/touchegg.conf` and make your changes.
It is a basic XML file that defines various gestures. Please note that at this time, `TAP_AND_HOLD`, `PINCH`, and `ROTATE` do not appear to work.
See the
The two-fingers scrolling emulation [xdotool](https://archlinux.org/packages/?name=xdotool) and add the following to the configuration file:
```
<gesture type="SWIPE" fingers="2" direction="DOWN">
      <action type="RUN_COMMAND">
        <repeat>true</repeat>
        <command>xdotool click 4</command>
        <decreaseCommand>xdotool click 5</decreaseCommand>
      </action>
    </gesture>
    <gesture type="SWIPE" fingers="2" direction="UP">
      <action type="RUN_COMMAND">
        <repeat>true</repeat>
        <command>xdotool click 5</command>
        <decreaseCommand>xdotool click 4</decreaseCommand>
      </action>
    </gesture>
```

Note that on KDE, text gets selected while scrolling (see upstream
## Start on login
[Enable](https://wiki.archlinux.org/title/Enable "Enable") `touchegg.service`, the client can then be [autostarted](https://wiki.archlinux.org/title/Autostart "Autostart").
Retrieved from "[https://wiki.archlinux.org/index.php?title=Touchegg&oldid=847860](https://wiki.archlinux.org/index.php?title=Touchegg&oldid=847860)"
[Category](https://wiki.archlinux.org/title/Special:Categories "Special:Categories"):
  * [Input](https://wiki.archlinux.org/title/Category:Input "Category:Input")


  * This page was last edited on 2 October 2025, at 10:25.
  * Content is available under


  * [Privacy policy](https://terms.archlinux.org/docs/privacy-policy/)
  * [About ArchWiki](https://wiki.archlinux.org/title/ArchWiki:About)
  * [Disclaimers](https://wiki.archlinux.org/title/ArchWiki:General_disclaimer)
  * [Code of conduct](https://terms.archlinux.org/docs/code-of-conduct/ "archlinux-service-agreements:code-of-conduct")
  * [Terms of service](https://terms.archlinux.org/docs/terms-of-service/ "archlinux-service-agreements:terms-of-service")


  * ![](https://wiki.archlinux.org/resources/assets/mediawiki_compact.svg)


Search
Search
Toggle the table of contents
Touchegg
[](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg) [](https://wiki.archlinux.org/title/Touchegg)
[Add topic ](https://wiki.archlinux.org/title/Touchegg)
