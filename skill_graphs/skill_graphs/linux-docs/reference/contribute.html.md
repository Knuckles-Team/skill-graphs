[ ![Linux From Scratch | Your Distro, Your Rules](https://www.linuxfromscratch.org/images/linux-from-scratch.png) ](https://www.linuxfromscratch.org/index.html)
Web LFS
  * [Patches](https://www.linuxfromscratch.org/patches/)
  * [Hints](https://www.linuxfromscratch.org/hints/)
  * [SLFS](https://www.linuxfromscratch.org/slfs/)
  * [GLFS](https://www.linuxfromscratch.org/glfs/)
  * [MLFS](https://www.linuxfromscratch.org/mlfs/)
  * [ALFS](https://www.linuxfromscratch.org/alfs/)
  * [BLFS](https://www.linuxfromscratch.org/blfs/)
  * [LFS](https://www.linuxfromscratch.org/lfs/)


  * [Home](https://www.linuxfromscratch.org/)
  * [News](https://www.linuxfromscratch.org/news.html)
  * [Support](https://www.linuxfromscratch.org/support.html)
  * [General FAQ](https://www.linuxfromscratch.org/faq)
  * [Mailing Lists](https://www.linuxfromscratch.org/mail.html)
  * [Wiki](https://wiki.linuxfromscratch.org/lfs/)
  * [Search](https://www.linuxfromscratch.org/search.html)
  * [Credits](https://www.linuxfromscratch.org/credits.html)
  * [Contribute](https://www.linuxfromscratch.org/contribute.html)
  * [Website Mirrors](https://www.linuxfromscratch.org/mirrors.html)
  * [Site Map](https://www.linuxfromscratch.org/sitemap.html)


# How to Contribute
## Become a mirror
You can assist the LFS project by providing an HTTP or FTP mirror. The HTTP mirrors provide the LFS website, books, patches and hints. The FTP mirrors can provide a number of services including LFS packages and BLFS packages. The requirements for the various mirrors are listed below. If you would like to become a mirror, please set it up and send an email with the data requested below to the website maintainer,
### Requirements
Here is a list of requirements for the various mirrors. All mirrors require that you use [rsync](https://www.linuxfromscratch.org/blfs/view/stable/basicnet/rsync.html) to sync your mirrors with our main servers, and a [cron](https://www.linuxfromscratch.org/blfs/view/stable/general/fcron.html) program to schedule it for you.
You can find inexpensive
#### HTTP Mirror
  * At least 5 GB of disk space.
  * [Apache Webserver](https://www.linuxfromscratch.org/blfs/view/stable/server/majorservers.html#apache) or equivalent with the following options enabled:
    * Indexes
    * FollowSymlinks
    * IncludesNOEXEC (requires mod_include.so)
  * If you want to use Nginx instead of Apache, the following options should be used:
    * ssi on; (requires ngx_http_ssi_module)
    * disable_symlinks off;
    * autoindex on;


To set up the mirror, use the following rsync instruction in a cron script:
`/usr/bin/rsync -lprt --delete www.linuxfromscratch.org::lfs-website /srv/www/lfs`
#### LFS and BLFS FTP Mirrors
  * At least 800 GB of disk space.
  * The path to the mirror being "/pub/lfs/" and "/pub/blfs/" if possible.


To set up the ftp mirrors, use the rsync instructions in a cron script:
`/usr/bin/rsync -lprt --delete rsync.osuosl.org::lfs  /srv/ftp/LFS
      /usr/bin/rsync -lprt --delete rsync2.osuosl.org::blfs /srv/ftp/BLFS`
#### Still interested?
If you are still interested in becoming a mirror, please email the following information to the appropriate list or the webmaster.
  * Location (City and Country)
  * Hostname and IP Address
  * Bandwidth
  * Contact Name and Valid E-mail Address


## Make a donation
One of the ways to help the Linux From Scratch project is by making donations.
Financial donations can be made through
USD $
If you'd like to donate but can't use PayPal, please contact
All proceeds of donations will be used to pay the monthly server hosting bills.


© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
