1. [ Documentation ](https://go.dev/doc/)
  2. [ Download and install ](https://go.dev/doc/install)


# Download and install
Download and install Go quickly with the steps described here.
For other content on installing, you might be interested in:
  * [Managing Go installations](https://go.dev/doc/manage-install) -- How to install multiple versions and uninstall.
  * [Installing Go from source](https://go.dev/doc/install/source) -- How to check out the sources, build them on your own machine, and run them.


[ Download (1.26.1) ](https://go.dev/dl/)
## Go installation[¶](https://go.dev/doc/install#install)
Select the tab for your computer's operating system below, then follow its installation instructions.
Linux ![](https://go.dev/images/icons/underline.svg) Mac ![](https://go.dev/images/icons/underline.svg) Windows ![](https://go.dev/images/icons/underline.svg)
  1. **Remove any previous Go installation** by deleting the /usr/local/go folder (if it exists), then extract the archive you just downloaded into /usr/local, creating a fresh Go tree in /usr/local/go: ```
      $ rm -rf /usr/local/go && tar -C /usr/local -xzf go1.26.1.linux-amd64.tar.gz

        ![](https://go.dev/images/icons/copy-paste.svg)
        ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

(You may need to run each command separately with the necessary permissions, as root or through `sudo`.)
**Do not** untar the archive into an existing /usr/local/go tree. This is known to produce broken Go installations.
  2. Add /usr/local/go/bin to the `PATH` environment variable.
You can do this by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):
```
          export PATH=$PATH:/usr/local/go/bin

            ![](https://go.dev/images/icons/copy-paste.svg)
            ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

**Note:** Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as `source $HOME/.profile`.
  3. Verify that you've installed Go by opening a command prompt and typing the following command: ```
          $ go version

            ![](https://go.dev/images/icons/copy-paste.svg)
            ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

  4. Confirm that the command prints the installed version of Go.


  1. Open the package file you downloaded and follow the prompts to install Go.
The package installs the Go distribution to /usr/local/go. The package should put the /usr/local/go/bin directory in your `PATH` environment variable. You may need to restart any open Terminal sessions for the change to take effect.
  2. Verify that you've installed Go by opening a command prompt and typing the following command: ```
          $ go version

            ![](https://go.dev/images/icons/copy-paste.svg)
            ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

  3. Confirm that the command prints the installed version of Go.


  1. Open the MSI file you downloaded and follow the prompts to install Go.
By default, the installer will install Go to `Program Files` or `Program Files (x86)`. You can change the location as needed. After installing, you will need to close and reopen any open command prompts so that changes to the environment made by the installer are reflected at the command prompt.
  2. Verify that you've installed Go.
    1. In **Windows** , click the **Start** menu.
    2. In the menu's search box, type `cmd`, then press the **Enter** key.
    3. In the Command Prompt window that appears, type the following command: ```
              $ go version

                ![](https://go.dev/images/icons/copy-paste.svg)
                ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

    4. Confirm that the command prints the installed version of Go.


## You're all set![¶](https://go.dev/doc/install#code)
Visit the [Getting Started tutorial](https://go.dev/doc/tutorial/getting-started.html) to write some simple Go code. It takes about 10 minutes to complete.
go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.
Okay
