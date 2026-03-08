## [Installation procedures for supported platforms](https://docs.docker.com/engine/install#installation-procedures-for-supported-platforms)
Click on a platform's link to view the relevant installation procedure.
Platform | x86_64 / amd64 | arm64 / aarch64 | arm (32-bit) | ppc64le | s390x
---|---|---|---|---|---
[CentOS](https://docs.docker.com/engine/install/centos/) | ✅ | ✅ |  | ✅ |
[Debian](https://docs.docker.com/engine/install/debian/) | ✅ | ✅ | ✅ | ✅ |
[Fedora](https://docs.docker.com/engine/install/fedora/) | ✅ | ✅ |  | ✅ |
[Raspberry Pi OS (32-bit)](https://docs.docker.com/engine/install/raspberry-pi-os/) |  |  | ⚠️ |  |
[RHEL](https://docs.docker.com/engine/install/rhel/) | ✅ | ✅ |  |  | ✅
[SLES](https://docs.docker.com/engine/install/sles/) |  |  |  |  | ❌
[Ubuntu](https://docs.docker.com/engine/install/ubuntu/) | ✅ | ✅ | ✅ | ✅ | ✅
[Binaries](https://docs.docker.com/engine/install/binaries/) | ✅ | ✅ | ✅ |  |
### [Other Linux distributions](https://docs.docker.com/engine/install#other-linux-distributions)
> Note
> While the following instructions may work, Docker doesn't test or verify installation on distribution derivatives.
  * If you use Debian derivatives such as "BunsenLabs Linux", "Kali Linux" or "LMDE" (Debian-based Mint) should follow the installation instructions for [Debian](https://docs.docker.com/engine/install/debian/), substitute the version of your distribution for the corresponding Debian release. Refer to the documentation of your distribution to find which Debian release corresponds with your derivative version.
  * Likewise, if you use Ubuntu derivatives such as "Kubuntu", "Lubuntu" or "Xubuntu" you should follow the installation instructions for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), substituting the version of your distribution for the corresponding Ubuntu release. Refer to the documentation of your distribution to find which Ubuntu release corresponds with your derivative version.
  * Some Linux distributions provide a package of Docker Engine through their package repositories. These packages are built and maintained by the Linux distribution's package maintainers and may have differences in configuration or are built from modified source code. Docker isn't involved in releasing these packages and you should report any bugs or issues involving these packages to your Linux distribution's issue tracker.


Docker provides [binaries](https://docs.docker.com/engine/install/binaries/) for manual installation of Docker Engine. These binaries are statically linked and you can use them on any Linux distribution.
