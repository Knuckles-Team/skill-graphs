# make
gcc -std=gnu99 -c -I. -DBINDIR=\”/usr/local/bin\” -DSYSCONFDIR=\”/usr/local/etc\” -DFONTDIR=\”/usr/local/share/sarg/fonts\” -DIMAGEDIR=\”/usr/local/share/sarg/images\” -DSARGPHPDIR=\”/var/www/html\” -DLOCALEDIR=\”/usr/local/share/locale\” -DPACKAGE_NAME=\”sarg\” -DPACKAGE_TARNAME=\”sarg\” -DPACKAGE_VERSION=\”2.3.8\” -DPACKAGE_STRING=\”sarg\ 2.3.8\” -DPACKAGE_BUGREPORT=\”\” -DPACKAGE_URL=\”\” -DHAVE_DIRENT_H=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDIO_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_SYS_TIME_H=1 -DHAVE_TIME_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DIRENT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_SOCKET_H=1 -DHAVE_NETDB_H=1 -DHAVE_ARPA_INET_H=1 -DHAVE_NETINET_IN_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_CTYPE_H=1 -DHAVE_ERRNO_H=1 -DHAVE_SYS_RESOURCE_H=1 -DHAVE_SYS_WAIT_H=1 -DHAVE_STDARG_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_LIMITS_H=1 -DHAVE_LOCALE_H=1 -DHAVE_EXECINFO_H=1 -DHAVE_MATH_H=1 -DHAVE_LIBINTL_H=1 -DHAVE_LIBGEN_H=1 -DHAVE_STDBOOL_H=1 -DHAVE_GETOPT_H=1 -DHAVE_FCNTL_H=1 -DHAVE_GD_H=1 -DHAVE_GDFONTL_H=1 -DHAVE_GDFONTT_H=1 -DHAVE_GDFONTS_H=1 -DHAVE_GDFONTMB_H=1 -DHAVE_GDFONTG_H=1 -DHAVE_ICONV=1 -DICONV_CONST= -DHAVE_ICONV_H=1 -DENABLE_NLS=1 -DHAVE_GETTEXT=1 -DHAVE_DCGETTEXT=1 -DHAVE_FOPEN64=1 -D_LARGEFILE64_SOURCE=1 -DHAVE_BZERO=1 -DHAVE_BACKTRACE=1 -DHAVE_SYMLINK=1 -DHAVE_LSTAT=1 -DHAVE_GETNAMEINFO=1 -DHAVE_GETADDRINFO=1 -DHAVE_MKSTEMP=1 -DSIZEOF_RLIM_T=8 -DRLIM_STRING=\”%lli\” -g -O2 -Wall -Wno-sign-compare -Wextra -Wno-unused-parameter -Werror=implicit-function-declaration -Werror=format util.c
gcc -std=gnu99 -c -I. -DBINDIR=\”/usr/local/bin\” -DSYSCONFDIR=\”/usr/local/etc\” -DFONTDIR=\”/usr/local/share/sarg/fonts\” -DIMAGEDIR=\”/usr/local/share/sarg/images\” -DSARGPHPDIR=\”/var/www/html\” -DLOCALEDIR=\”/usr/local/share/locale\” -DPACKAGE_NAME=\”sarg\” -DPACKAGE_TARNAME=\”sarg\” -DPACKAGE_VERSION=\”2.3.8\” -DPACKAGE_STRING=\”sarg\ 2.3.8\” -DPACKAGE_BUGREPORT=\”\” -DPACKAGE_URL=\”\” -DHAVE_DIRENT_H=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDIO_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_SYS_TIME_H=1 -DHAVE_TIME_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DIRENT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_SOCKET_H=1 -DHAVE_NETDB_H=1 -DHAVE_ARPA_INET_H=1 -DHAVE_NETINET_IN_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_CTYPE_H=1 -DHAVE_ERRNO_H=1 -DHAVE_SYS_RESOURCE_H=1 -DHAVE_SYS_WAIT_H=1 -DHAVE_STDARG_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_LIMITS_H=1 -DHAVE_LOCALE_H=1 -DHAVE_EXECINFO_H=1 -DHAVE_MATH_H=1 -DHAVE_LIBINTL_H=1 -DHAVE_LIBGEN_H=1 -DHAVE_STDBOOL_H=1 -DHAVE_GETOPT_H=1 -DHAVE_FCNTL_H=1 -DHAVE_GD_H=1 -DHAVE_GDFONTL_H=1 -DHAVE_GDFONTT_H=1 -DHAVE_GDFONTS_H=1 -DHAVE_GDFONTMB_H=1 -DHAVE_GDFONTG_H=1 -DHAVE_ICONV=1 -DICONV_CONST= -DHAVE_ICONV_H=1 -DENABLE_NLS=1 -DHAVE_GETTEXT=1 -DHAVE_DCGETTEXT=1 -DHAVE_FOPEN64=1 -D_LARGEFILE64_SOURCE=1 -DHAVE_BZERO=1 -DHAVE_BACKTRACE=1 -DHAVE_SYMLINK=1 -DHAVE_LSTAT=1 -DHAVE_GETNAMEINFO=1 -DHAVE_GETADDRINFO=1 -DHAVE_MKSTEMP=1 -DSIZEOF_RLIM_T=8 -DRLIM_STRING=\”%lli\” -g -O2 -Wall -Wno-sign-compare -Wextra -Wno-unused-parameter -Werror=implicit-function-declaration -Werror=format log.c
log.c: En la funciÃ³n âmainâ:
log.c:1506: error: el formato â%liâ espera el tipo âlong intâ, pero el argumento 7 es de tipo âlong long intâ
log.c:1513: error: el formato â%liâ espera el tipo âlong intâ, pero el argumento 8 es de tipo âlong long intâ
log.c:1564: error: el formato â%liâ espera el tipo âlong intâ, pero el argumento 2 es de tipo âlong long intâ
make: *** [log.o] Error 1
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-134367)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 12, 2014 at 3:03 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-134733)
install pcre package using yum command.
```
# yum install pcre

```
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-134733)
  57. ![](https://secure.gravatar.com/avatar/269eeab623b20dbdf287ae3d0afd15b3f7d16b543dcb7c5f9a830ba66eaa934a?s=50&d=blank&r=g)
magesh
[ March 5, 2014 at 8:33 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-130197)
Hi ravi,
Everything went well, But i can’t view the reports through my browser. Whenever i type
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-130197)
     * ![](https://secure.gravatar.com/avatar/3dddb368c53dbfa507ce4064f5626ffc4f6acc5a02ffa3cc4a5067783d9d1fd5?s=50&d=blank&r=g)
kiran
[ October 13, 2014 at 5:15 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-331783)
Flush ur iptables
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-331783)
  58. ![](https://secure.gravatar.com/avatar/7998bc571b181f3dd11b7d9259ef8f2c156c89a70c0ff0a839b0e57f8b1373da?s=50&d=blank&r=g)
Mau
[ March 5, 2014 at 8:47 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-129969)
Thank you for this tutorial. This is actually a great tool for IT professional, however, after entering the “sarg -x” command I am getting this error.
SARG: sarg version: 2.3.8 Feb-07-2014
SARG: Reading access log file: /var/log/squid/access.log
SARG: getword loop detected after 256 bytes.0%
SARG: Line=”04/Mar/2014:11:25:53 +0800 140157 172.16.0.176 TCP_MISS/302 438 GET”
SARG: Record=”http://ads.cnn.com/event.ng/Type=adxmiss&ClientType=2&ASeg=&AMod=&AOpt=0&AdID=797605&FlightID=560907&TargetID=183732&SiteID=1590&EntityDefResetFlag=0&Segments=DECBHHicHY3JEQBBCAIT4uGJmn9iy-ynq6VUeIZwLiJKyDB4uUktggjmHeLGGunxs7vEsUSytlDazMd1aLZA196guXIy3cXSH7LtOb3BnVRy3g59Z2O8JzFRMz_3cZXHtfKc859yxks239WeetdOjZtD-wAnOCnz&Targets=DECBHHicLZDJFQAhCEMb8sAe6L-xYZnTf0oSogwh18dkovU4A4oGyPJxiUctQIMQOcQAZgdf4C6xPiQGJeNTmuhSZj_EwnSBH3Y4yYap1PqU8nAnpgMPzKaSuq4EuWGo3g42a0kQqDOzPNdA-6I27D7PH3HoWdT0RNUs18D0y3SPV5FTT4jnPSAaMzLnV8JDWhip2U2SKWYmxnpoCdx9ZgqVDxQBSwQ.&Values=DECBHHicJZDJAQAhCAMb4kGQI_Tf2Eb3wQBy224zRhjcDeXWPJKStEShDkPIQE0Je9OWF2toVcXUCJOWWbCclJ8MHKtYJVR7UeSE1bjXY4tckfLEcUVJ-CNMk3rEvJm72kDDKkSQYiracK6IZ6P1juhzyRTVQsvHztG-Z_NewfOOIe_-xUW-q9RZqvK8o44-pFWSv6oP70M6xw..&RawValues=NGUSERID%252C5313de170652160a3c8ef72b2401f964%252CKXID%252Cnqjy664yj%252CTID%252C13939029942996432425196198%252CTIL%252C8363992093935&random=dgAhwyA,bjrkrnNwpWAd&Params.tag.transactionid=13939029942996432425196198&Params.User.UserID=5313de170652160a3c8ef72b2401f964 danilo DIRECT/157.166.224.71 text/html”
SARG: searching for ‘x20’
SARG: getword backtrace:
SARG: 1:sarg() [0x804e57c]
SARG: 2:sarg() [0x804effe]
SARG: 3:sarg() [0x80548a3]
SARG: 4:/lib/libc.so.6(__libc_start_main+0xe6) [0x3fad26]
SARG: 5:sarg() [0x80499c1]
SARG: Maybe you have a broken user ID in your /var/log/squid/access.log file
Can you tell me where did I go wrong? I have followed each and every step in tutorial and it was installed successfully. Until this error came out.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-129969)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 5, 2014 at 6:06 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-130159)
It seems a bug in sarg that failed to read log file, due to some http read warning that cannot be parsed. Which sarg version you using?
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-130159)
  59. ![](https://secure.gravatar.com/avatar/25fa2d087c7a9543c12415c715f7b1564513e360c901ec7b16e712041f7c9b05?s=50&d=blank&r=g)
Umesh
[ February 19, 2014 at 9:47 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-124061)
Hi ,
I have installed and configured sarg , when try to access i’m getting following error message.
While trying to process the request:
GET /squid-reports/ HTTP/1.0
Host: 192.168.30.6
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8
Via: 1.1 localhost.localdomain:80 (squid/2.6.STABLE21)
X-Forwarded-For: 192.168.30.15
Cache-Control: max-age=259200
Connection: keep-alive
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-124061)
  60. ![](https://secure.gravatar.com/avatar/626eeb1604315ab1fda09d43a5ae90871b497ae709d49f9e1570e63450407171?s=50&d=blank&r=g)
Raymond Chong
[ February 13, 2014 at 3:41 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-122284)
Hi!
After i enter “#sudo sarg -x” and it generate the report, but at last sentence it show..
“SARG: Maybe you have a broken time in your /var/www/sarg/ONE-SHOT/sarg-date file”
Is there any problem with my access.log?
And also i can’t find any index.html report inside ONE-SHOT folder, just have IP Address Folder. Is there my sarg option set to wrong way? Please help me, thanks!
Regards,
Raymond Chong
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-122284)
  61. ![](https://secure.gravatar.com/avatar/3519fb3b8c54b2574869db2908a3b7838372fd0874cd0c08af3285c8a54eda13?s=50&d=blank&r=g)
Konstantin
[ January 29, 2014 at 11:27 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-115879)
I use also “Lightsquid” – very easy and simple tool for squid log analylize.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-115879)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 30, 2014 at 11:47 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-116132)
Yeah thanks, never heard of such tool ‘Lightsquid’ will surely try it and will provide a detailed article soon.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-116132)
  62. ![](https://secure.gravatar.com/avatar/627b7573e53519748b51a39ce97c3e8e8532a5c1c6d924de980503a2832ec0b8?s=50&d=blank&r=g)
Jo
[ January 23, 2014 at 10:08 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-111768)
Hi Ravi
Thanks for your reply. I searched the entire system for the path where the log files for SARG is created. I could not find it.
I have even re-compiled the SARG from source again and installed it. It is still showing me the same error that “SARG: File not found: /var/log/squid/access.log”.
I am installing this service using the root ID. I am not sure on where I am going wrong. Could you please shed some light on this issue and assist to fix it for me.
Looking forward to hearing from you.
Jos
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-111768)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 24, 2014 at 3:12 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-112221)
Is squid is installed on the system? and logs are generating at /var/log/squid/access.log? Please check this first, the log file must exist to process SARG to generate reports.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-112221)
       * ![](https://secure.gravatar.com/avatar/94335e0f51fcef10a47fcd6304b5e92b57d3c91e5aa75e6d2f94171fb7728bc5?s=50&d=blank&r=g)
pablo
[ January 28, 2014 at 12:19 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-114486)
Hi!
Check if it is not in the directory “var/log/squid3/access.log” this depends on the squid package that you installed on your system.
you can run
