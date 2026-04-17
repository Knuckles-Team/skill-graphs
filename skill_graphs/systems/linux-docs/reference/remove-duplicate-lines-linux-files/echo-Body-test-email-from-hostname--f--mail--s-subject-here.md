# echo “Body test email from ‘hostname -f’ “| mail -s “subject here”
O/P : mail: cannot send message: Process exited with a non-zero status
can you please help me on this issue.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-942256)
  6. ![](https://secure.gravatar.com/avatar/ee6a0a0068d6e4e6f059133b88aa2accf00d12db66ccd7b00ee4c66573028d91?s=50&d=blank&r=g)
Mahboob Ali
[ September 25, 2017 at 12:20 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915902)
Hi,
I’m using Ubuntu and alertscript dir exists in **/usr/lib/zabbix/alertscripts/**. So I’ve make script file **zabbix-sendmail** in this location.
I’ve using my other smtp server instead of Gmail which is working fine.
I’ve completed step 3 and successfully able to send mail using **/usr/lib/zabbix/alertscripts/zabbix-sendmail** Mail-id “**Subject** ” “**Body** ” this command.
Now there is issue in setp 4. I’ve configured media for sending mail and also enable action. But now triggers changed in zabbix GUI but it not able to send mail even no any logs are coming.
So please suggest me what should I need to check ?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915902)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ September 25, 2017 at 1:20 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915910)
Consult zabbix docs …the mail script parh has been changed.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915910)
       * ![](https://secure.gravatar.com/avatar/ee6a0a0068d6e4e6f059133b88aa2accf00d12db66ccd7b00ee4c66573028d91?s=50&d=blank&r=g)
Mahboob Ali
[ September 25, 2017 at 2:21 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915918)
I’ve check in **/etc/zabbix/zabbix_server.conf** file and in file alert location mention as below:
```
AlertScriptsPath=/usr/lib/zabbix/alertscripts

```

It means script location is **/usr/lib/zabbix/alertscripts** and I’ve also create script in on same location but not get success.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-915918)
  7. ![](https://secure.gravatar.com/avatar/2c356a65dfbd67662d8feecf1c62c3c90db0df6f22ffc00f83c62de4990d7a4d?s=50&d=blank&r=g)
lucian
[ July 26, 2017 at 3:56 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-901907)
alertscripts folder name and location is in zabbix_server.conf, where zabbix_server.conf is in /etc/zabbix default location for alertscripts in Ubuntu is /etc/zabbix/alert.d everything else worked, thanks
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-901907)
  8. ![](https://secure.gravatar.com/avatar/79e0793d0f37dd76f02150a82932b542b56b3a6971da49b35a206e1c25f2c0cb?s=50&d=blank&r=g)
Jose
[ July 25, 2017 at 12:06 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-901577)
Hi, I follow the process up to allow access for less secure apps in my gmail account following your indications. However after apply changes and confirme it is turned on. I still receive the error ail: cannot send message: Process exited with a non-zero status.
Any Idea about what could be the problem?
thanks in advance.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-901577)
  9. ![](https://secure.gravatar.com/avatar/9bcb86a896645e573176dfd73ce2fc7b23c21db36b6ca58ccf85d28b38bf3961?s=50&d=blank&r=g)
Ted Miller
[ July 13, 2017 at 7:42 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-899592)
I found one thing missing: on Centos 7, ssmtp does not automatically activate itself as default mta when installed. I had to do command:
```
# alternatives --config mta

```

and then choose the number next to ssmtp. Before that postfix was grabbing my emails, so they weren’t being routed through gmail.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-899592)
  10. ![](https://secure.gravatar.com/avatar/e0ebfa2d38e4ec941a9363e1e9354ece773a75960fd463dfd756e04ae1a933e4?s=50&d=blank&r=g)
nokiamben
[ May 23, 2017 at 2:55 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-891513)
Hi, thank you!
It works perfectly for me `^^`
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-891513)
  11. ![](https://secure.gravatar.com/avatar/b1da1bb2aaec042049ca5c67e996b772fe651cda945388d41308b4b795ba044e?s=50&d=blank&r=g)
Muli
[ April 9, 2017 at 9:38 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-882483)
Hi,
I followed all the guides regarding sending mail using Gmail,
I manage to send test mails via script to Gmail accounts, but through zabbix mails are stuck in “in progress, 3 retries left” status.
Any help would be appreciated.
Muli
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-882483)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 15, 2017 at 10:59 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-883906)
In case you have issues with mail concerning different versions of Zabbix, please read their documentation at
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-883906)
     * ![](https://secure.gravatar.com/avatar/d4d4e3caef84a9fb06975bc70f3a40f4756ce4f83bf53972122efe84f3a44f75?s=50&d=blank&r=g)
Yuan
[ August 21, 2017 at 6:50 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-907544)
Same problem, please me on that problem
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-907544)
  12. ![](https://secure.gravatar.com/avatar/fe34353b1c7a5ab3129366877ae754de823d4e8f9284cdb8fc3a5629a6a54c45?s=50&d=blank&r=g)
Joseph John
[ March 5, 2017 at 1:53 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-872939)
Good article, but now Zabbix version is 3.2.X and setup they have given in
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-872939)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 6, 2017 at 11:55 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-873225)
@Joseph,
Thanks for notifying us about latest release of Zabbix 3.2.x, yes we will update the article to meet latest version, till then stay tuned to Tecmint.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-873225)
  13. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ March 1, 2017 at 1:57 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871958)
In case you have issues with mail concerning different versions of Zabbix, please read their documentation at
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871958)
  14. ![](https://secure.gravatar.com/avatar/5c6e52530a0b632e2e144923935d7c20be871bb973d86b11df689efe6f0820d6?s=50&d=blank&r=g)
syam
[ March 1, 2017 at 10:57 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871928)
Hi i am using 2.4.8 version till step: 3, I able to see the mail notifications to my gmail account. In step:4 I have done the same steps but i unable to receive the mails. Zabbix not sending emails reporting msg “status: not sent. Can some one please help me.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871928)
  15. ![](https://secure.gravatar.com/avatar/0d7d6d2664402c6b22d0d75740bf3ed4132d0dedebd26f60cb6639f168818d34?s=50&d=blank&r=g)
Hamilton Jimenez
[ February 9, 2017 at 10:34 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-865965)
Since Zabbix 3.0 you must configure the Media Type to pass the parameters manually, they are not passed automatically as $1, $2 and $3 anymore so you need to add three parameters to the Media Type manually:
```
{ALERT.SENDTO}
{ALERT.SUBJECT}
{ALERT.MESSAGE}

```

if you don’t fix the media type like this, the script won't do anything.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-865965)
  16. ![](https://secure.gravatar.com/avatar/67280601f778d4d06e9c402a0644c760ae6561c277e2214ca7ca2bfc06405e08?s=50&d=blank&r=g)
anoop vijayan maniankara
[ September 23, 2016 at 5:29 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-820261)
This is awesome post! thanks !
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-820261)
  17. ![](https://secure.gravatar.com/avatar/2ac96bbc21b59c53b429a691779dab5b0e9c26a9698f46c716d7c48f56d14cb1?s=50&d=blank&r=g)
mana
[ June 28, 2016 at 4:01 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-796058)
I have installed zabbix and done your configuration to send email, but when in your instruction you pass the $1, $2 and $3 parameters to the mail script?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-796058)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ June 28, 2016 at 6:11 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-796086)
Just create the script from step 6 and use it to send mail from zabbix settings. You don;t have to pass anything manual to the script
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-796086)
       * ![](https://secure.gravatar.com/avatar/b8ed0876644d168934079ae69c3c02a9ec03bb5761ef73b8de87fd5242c70ed9?s=50&d=blank&r=g)
Ailbert Riksen
[ July 19, 2016 at 5:12 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800552)
Hi Matei,
I just tried to send email via your sendmail script, but I do nog get any $1, $2 and $3 parameter. I checked this bij adding a log output of thes parameters in the zabbix-sendmail script.
My dialog for creating a new mediatype also gives me the opportunity to define script parameters. I’m using Zabbix 3.0.0. You are using 2.4.5, as I can see from your screenshots.
Any idea how to define these parameters?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800552)
       * ![](https://secure.gravatar.com/avatar/b8ed0876644d168934079ae69c3c02a9ec03bb5761ef73b8de87fd5242c70ed9?s=50&d=blank&r=g)
Ailbert Riksen
[ July 19, 2016 at 5:45 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800558)
In Zabbix 3.0.0 you have to define the parameters. see
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800558)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 20, 2016 at 10:52 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800744)
@Ailbert,
Thanks for notifying us, we will update this article for Zabbix 3.0 support..
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-800744)
  18. ![](https://secure.gravatar.com/avatar/5811ee326f07de1838333112c2b62370a47cfa4c631bca226b085bdd67bf3a8d?s=50&d=blank&r=g)
Balaraju
[ May 31, 2016 at 10:55 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-785284)
Hi team
Can we do sms alerts using http API.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-785284)
  19. ![](https://secure.gravatar.com/avatar/0e5413e991f821bbecde14c52e8b375dec6f0a23f3112aadae05770cb957c5de?s=50&d=blank&r=g)
Daniel
[ May 18, 2016 at 1:47 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-781496)
I have the same error.
My Zabbix tell sending emails reporting msg “status: sent”.
but i can't see the mail
Can u help me?
sorry for my english.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-781496)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ May 18, 2016 at 1:15 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-781679)
It looks like your mail server is not configured propery to send or forward mails. Invastigate this issue further.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-781679)
  20. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 26, 2016 at 11:21 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-774287)
Go to Configuration — > Action and check if email setting are Enable and properly configured.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-774287)
  21. ![](https://secure.gravatar.com/avatar/7c5483dfa8b4df8e95a725863f763087be077ab8f2b9fd1b16a9fae0158c63ef?s=50&d=blank&r=g)
Andrews
[ April 25, 2016 at 7:54 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-774183)
Hi,
I’m testing using command line and its works fine.
But my Zabbix not sending emails reporting msg “status: not sent”.
Can u help me?
Tnx
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-774183)
     * ![](https://secure.gravatar.com/avatar/dc2b54b5316266ab6d59575898a3eac83903c60d7da3158b49b3466360ea2c1d?s=50&d=blank&r=g)
Mike A.
[ May 31, 2016 at 2:16 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-785327)
It’s the same problem I have now. Sending email via command line works but not in Zabbix. Did you come up with a solution or a way to trace where the problem is?
Thanks!
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-785327)
       * ![](https://secure.gravatar.com/avatar/d797d0171f5b64624754dee5ba8cd53119cf83d666140cd43921bd346726a83a?s=50&d=blank&r=g)
tomas
[ June 9, 2016 at 8:31 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-789840)
may the problem be that in command line i need to add “./” before “zabbix-sendmail
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-789840)
         * ![](https://secure.gravatar.com/avatar/5c6e52530a0b632e2e144923935d7c20be871bb973d86b11df689efe6f0820d6?s=50&d=blank&r=g)
syam
[ March 1, 2017 at 10:59 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871929)
hi does your problem got fixed.. can you pls help me.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-871929)
  22. ![](https://secure.gravatar.com/avatar/2f7861543f131878aa9b978b7a4a9d4084965fdf5ab6940181cc31f5028c3692?s=50&d=blank&r=g)
Mamadou Lamine Diallo
[ April 15, 2016 at 9:45 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-772692)
thank you for this post helpful
please can you help me to integrate zabbix with request tracker or OTRS or other like this
thank u in advance
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-772692)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 19, 2016 at 11:10 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-773131)
For this subject you should consult zabbix documentation.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-773131)
  23. ![](https://secure.gravatar.com/avatar/a20d17d2fa62ebc41d339c2862a152879efb84ef1b211820c290fee09c9ed49c?s=50&d=blank&r=g)
Laurenz
[ April 11, 2016 at 8:50 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-772115)
One error that i got was the path of the script, to get it working on my zabbix 3.0, i had to change the path from /usr/local/share/zabbix/alerscripts/zabbix-sedmail to /usr/lib/zabbix/alertscripts/zabbix-sendmail.
Hope it helps!
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-772115)
     * ![](https://secure.gravatar.com/avatar/db3d3ea17c4ce3a36565695a6d407bcf01d3572a564ddb90bb8d24b08de5f8d4?s=50&d=blank&r=g)
Ram Pal
[ July 7, 2016 at 1:41 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-797876)
I installed zabbix 3.0 on centos7, i also created zabbix-sendmail file in **/usr/lib/zabbix/alertscripts/** because **/usr/local/share/zabbix/alerscripts/** path does not exist.
I configured ssmtp according this documentation, now i am getting mail by command line but zabbix not sending reports. Action and internal are all enable.
Please help
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-797876)
  24. ![](https://secure.gravatar.com/avatar/7c5483dfa8b4df8e95a725863f763087be077ab8f2b9fd1b16a9fae0158c63ef?s=50&d=blank&r=g)
Andrews
[ April 7, 2016 at 12:03 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770417)
Thnx
I solved my problem.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770417)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 7, 2016 at 10:54 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770568)
@Andrews,
How you solved problem yourself? it would be great if you could mention those instructions so that its will beneficial to others, who face similar problem…
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770568)
  25. ![](https://secure.gravatar.com/avatar/7c5483dfa8b4df8e95a725863f763087be077ab8f2b9fd1b16a9fae0158c63ef?s=50&d=blank&r=g)
Andrews
[ April 6, 2016 at 11:57 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770416)
Good article, Thx.
I’m having a problem when trying to send an email using /etc/zabbix/scripts/sendemail.sh a*******a@gmail.com.br “Test” “Msg Test”.
/etc/zabbix/scripts/sendemail.sh: line 2: /usr/bin/mail: No such file or directory
Can u help me?
Cheers
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-770416)
  26. ![](https://secure.gravatar.com/avatar/210333f263be7017470ba66e555fa3c1905990166a1445d106b98f40dc3c0da3?s=50&d=blank&r=g)
strato
[ March 19, 2016 at 9:54 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-761815)
Worked like a charm. Thanks for the detail write-up!
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-761815)
  27. ![](https://secure.gravatar.com/avatar/12763b39c44cacc05c0be8177fe5363be8d8277aef3e32e7bf57fca6396da11b?s=50&d=blank&r=g)
itai
[ February 4, 2016 at 1:00 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-747644)
Hi
After running “yum install ssmtp mailx” on centos 7
I can’t find /etc/ssmtp/ssmtp.conf
the file does not exist.
can you please help?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-747644)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 4, 2016 at 12:07 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-747816)
@Itai,
That means both the packages ssmtp and mailx are not installed on the system, if you think you’ve managed to install them successfully, could you check them using following command, if installed below command will show output as shown.
```
# rpm -q ssmtp mailx

ssmtp-2.64-14.el7.x86_64
mailx-12.5-12.el7_0.x86_64

```
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-747816)
  28. ![](https://secure.gravatar.com/avatar/a4b65a460a7bed873a20b54d581ac308b782f5d312e7949ee2614ba7e26b42fc?s=50&d=blank&r=g)
swap
[ January 21, 2016 at 11:41 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-742350)
Very good article.. Thanks a lott.! it Works for me..
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-742350)
  29. ![](https://secure.gravatar.com/avatar/7e86b0243acbf7a4f97812d576806efa8e64cb8d064e41222c8301c26113a194?s=50&d=blank&r=g)
Steve
[ November 4, 2015 at 9:58 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-701041)
Thanks for the walkthrough! When I configure SSMTP and run it by itself to test, it works fine. When I run the script listed in step seven (zabbix-sendmail), it fails with “mail: cannot send message: Process exited with a non-zero status”. /var/log/mail.err gives the error “Client does not have permissions to send as this sender”. I have given chmod +x to the script, and have ran it using sudo and without. Any idea what is going on?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-701041)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ November 5, 2015 at 1:03 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-701477)
It seems to be a problem with client permissions on the mail server side. What kind of mail server are you using? Your own mail server or a public mail domain?
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-701477)
       * ![](https://secure.gravatar.com/avatar/7e86b0243acbf7a4f97812d576806efa8e64cb8d064e41222c8301c26113a194?s=50&d=blank&r=g)
Steve
[ November 6, 2015 at 6:47 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-702240)
We are using Exchange Online.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-702240)
         * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ November 7, 2015 at 8:45 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-702780)
I’ve no experience with Office 365, but a good starting point can be found here
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-702780)
  30. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ October 10, 2015 at 4:04 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-683309)
You’re right! If you install Zabbix from repositories using binary packages the path for scripts would be /usr/lib/zabbix/alertscripts/, else, if you compile and install it from sources, the path is /usr/local/share/zabbix/alertscripts/. Once again… this tutorial covers only Zabbix installation from sources, but your remark is welcome for users who tend to install zabbix server using distribution repositories.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-683309)
  31. ![](https://secure.gravatar.com/avatar/00d3844c397623ccdecf7eb866dc776d39eedded9f1b805b8c75621b491183c5?s=50&d=blank&r=g)
Igor Murta
[ October 10, 2015 at 12:22 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-682875)
Very good article. It works for me!!! Thx a lot!!
Just a small comment/question.
The path to create the script “zabbix-sendmail” I suppose that might be same path set in zabbix_server.conf with the parameter “AlertScriptsPath”
For the standard install of zabbix server, this parameter is set to AlertScriptsPath=/usr/lib/zabbix/alertscripts
Instead of /usr/local/share/zabbix/alertscripts/
Cheers
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-682875)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[PhotoRec – Recover Deleted or Lost Files in Linux](https://www.tecmint.com/photorec-recover-deleted-lost-files-in-linux/)
[How to Use the Cat Command in Linux [22 Useful Examples]](https://www.tecmint.com/cat-command-linux/)
[How to Find Linux OS Name and Kernel Version You Are Running](https://www.tecmint.com/check-linux-os-version/)
[15 Tips On How to Use ‘Curl’ Command in Linux](https://www.tecmint.com/linux-curl-command-examples/)
[12 Tcpdump Commands – A Network Sniffer Tool](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/)
[Gdu – A Pretty Fast Disk Usage Analyzer for Linux](https://www.tecmint.com/gdu-disk-usage-analyzer-for-linux/)
## Linux Server Monitoring Tools
[ngrep – A Network Packet Analyzer for Linux](https://www.tecmint.com/ngrep-network-packet-analyzer-for-linux/)
[How to Limit Time and Memory Usage of Processes in Linux](https://www.tecmint.com/limit-time-and-memory-usage-of-linux-process/)
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[Mytop – A Useful Tool for Monitoring MySQL/MariaDB Performance in Linux](https://www.tecmint.com/mytop-mysql-mariadb-database-performance-monitoring-in-linux/)
[iPerf3 – Test Network Speed/Throughput in Linux](https://www.tecmint.com/test-network-throughput-in-linux/)
[4 Useful Tools to Monitor CPU and GPU Temperature in Ubuntu](https://www.tecmint.com/monitor-cpu-and-gpu-temperature-in-ubuntu/)
## Learn Linux Tricks & Tips
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
[10 Practical Examples Using Wildcards to Match Filenames in Linux](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/)
[How to Set Limits on User Running Processes in Linux](https://www.tecmint.com/set-limits-on-user-processes-using-ulimit-in-linux/)
[6 Useful Tools to Remember Linux Commands Forever](https://www.tecmint.com/remember-linux-commands/)
[How to Manage User Password Expiration and Aging in Linux](https://www.tecmint.com/manage-user-password-expiration-and-aging-in-linux/)
[Use ‘pushd’ and ‘popd’ for Efficient Filesystem Navigation in Linux](https://www.tecmint.com/pushd-and-popd-linux-filesystem-navigation/)
## Best Linux Tools
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[5 Best PDF Page Cropping Tools For Linux](https://www.tecmint.com/best-pdf-page-cropping-tools-for-linux/)
[Top 5 Diagram Tools for Linux Users in 2025 (Free & Open-Source)](https://www.tecmint.com/best-diagram-viewer-linux/)
[5 Best Mathematical Equation and Formula Writing Tools for Linux](https://www.tecmint.com/mathematical-equation-tools-linux/)
[23 Best Open Source Text Editors for Linux in 2024](https://www.tecmint.com/best-open-source-linux-text-editors/)
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/ "Scroll back to top")
Search for:
