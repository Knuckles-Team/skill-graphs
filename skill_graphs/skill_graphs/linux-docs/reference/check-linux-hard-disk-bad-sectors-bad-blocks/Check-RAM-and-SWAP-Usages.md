# Check RAM and SWAP Usages
 free -m | grep -v "+\|You" > /tmp/ramcache
 echo -e '\E[32m'"Ram Usages :" $tecreset
 cat /tmp/ramcache | grep -v "Swap"
 echo -e '\E[32m'"Swap Usages :" $tecreset
 cat /tmp/ramcache | grep -v "Mem"

# Check RAM and SWAP Usages
free -h | grep -v + > /tmp/ramcache
i change >>
free -m | grep -v + > /tmp/ramcache
3)
df -h| grep ‘Filesystem\|/dev/sda*’ > /tmp/diskusage
i change>>
df -h| grep ‘Filesystem\|/dev/*’ > /tmp/diskusage
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868614)
  29. ![](https://secure.gravatar.com/avatar/d35bf998e4b5fbe49e7a97a368afd80524d4145e717e2ad3e7c7e6f38ec05422?s=50&d=blank&r=g)
Arash
[ February 17, 2017 at 2:03 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868579)
nice script
but how can i make it live and dynamic!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868579)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 17, 2017 at 2:57 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868589)
@Arash,
What you mean live? just simple download and execute the script to know the Server performance statistics..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868589)
  30. ![](https://secure.gravatar.com/avatar/8c3cd1b74945bd984b7d3b4f26402cd1fdf3ec6e71dfa21e3c301c99e5dfbeea?s=50&d=blank&r=g)
trash.80
[ February 17, 2017 at 1:21 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868561)
Give **inxi** a try:
It’s already in most distributions, including Ubuntu, just a simple apt-get.
inxi shows most everything you have here and has over 10 years development.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-868561)
  31. ![](https://secure.gravatar.com/avatar/858c823648ca5463509c0f7148451a9ecbcebdf998157028bcd50234b5bde0fb?s=50&d=blank&r=g)
Ariel
[ July 24, 2016 at 12:47 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801820)
Hi. I’m looking at the script and see ‘\E[32m’ before almost every echo string. Should it actually be there? What about support for other os types?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801820)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 25, 2016 at 11:16 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802043)
@Ariel,
The updated version of script is available at Github, the link can be found at the bottom of the article, and about compatibility, yes it works on almost all flavors of Linux distributions..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802043)
     * ![](https://secure.gravatar.com/avatar/a61b9424d142be37cb9cccd7ebc204d68a2a4fd21e42ed9aba5eea961e375a3f?s=50&d=blank&r=g)
Andres Tarallo
[ July 25, 2016 at 9:42 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802182)
@Ariel, those are scape codes that make certain messages appear in color. Making the script work on other UNIXES (*BSD, AIX or Solaris) is not my priority. When I have time I’ll be testing it on AIX, that I have availiable.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802182)
  32. ![](https://secure.gravatar.com/avatar/25feda3ef2224c33901e37d9bbb981f6cb1d3119ab19c37d2be8ffa3e48a9bbc?s=50&d=blank&r=g)
Immanuel
[ July 24, 2016 at 7:50 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801766)
Just tested the script. I made the following changes to get in working on Ubuntu and derivatives.
removed the use of su.
sudo cp $scriptname /usr/bin/monitor && echo “Congratulations! Script Installed, now run monitor Command” || echo “Installation failed”
Added virtual hard disk and multiple hard disk.
df -h| grep ‘Filesystem\|/dev/[s|v]d[a-z]*’ > /tmp/diskusage
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801766)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 25, 2016 at 11:11 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802042)
@Immanuel,
Thanks for making the script compatible for Ubuntu and its derivatives, hope it will help all Ubuntu users…
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802042)
  33. ![](https://secure.gravatar.com/avatar/53c5a163db9085d294f2af466b6ebd94509ded96787bbb79520cdac5b262bec0?s=50&d=blank&r=g)
ex_rat
[ July 23, 2016 at 4:23 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801609)
Hi, i like your script ! :)
