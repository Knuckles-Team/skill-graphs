![](https://www.docker.com/app/uploads/2024/01/icon-new.svg)
[Insights on the state of AI agents from 800+ builders and leaders. Join our 3/25 webinar](https://www.docker.com/events/the-state-of-ai-agents-webinar/)
✕
[](https://docs.docker.com/ "Docker Docs home page")
  * [Get started](https://docs.docker.com/get-started/)
  * [Guides](https://docs.docker.com/guides/)
  * [Manuals](https://docs.docker.com/manuals/)
  * [Reference](https://docs.docker.com/reference/)


Ask AI
Search
### Ask me about Docker
Get instant answers to your Docker questions. I can help with commands, concepts, troubleshooting, and best practices.
Try asking:
How do Docker Hardened Images work?  What is MCP Toolkit?  How do I create an org?
### Ask me about Docker
Get instant answers to your Docker questions. I can help with commands, concepts, troubleshooting, and best practices.
Try asking:
How do Docker Hardened Images work?  What is MCP Toolkit?  How do I create an org?
Was this helpful?
Helpful Not quite
Copy
You've reached the maximum of
Start a new thread
Context
When enabled, Gordon considers the current page you're viewing to provide more relevant answers.
Answers are generated based on the documentation.
[](https://docs.docker.com/get-started/)
  * [](https://docs.docker.com/guides/)
  * [](https://docs.docker.com/manuals/)
  * [](https://docs.docker.com/reference/)


  * [Get Docker](https://docs.docker.com/get-started/get-docker/ "Get Docker")
  * [What is Docker?](https://docs.docker.com/get-started/docker-overview/ "What is Docker?")
  * [Introduction](https://docs.docker.com/get-started/introduction/)
    * [Get Docker Desktop](https://docs.docker.com/get-started/introduction/get-docker-desktop/ "Get Docker Desktop")
    * [Develop with containers](https://docs.docker.com/get-started/introduction/develop-with-containers/ "Develop with containers")
    * [Build and push your first image](https://docs.docker.com/get-started/introduction/build-and-push-first-image/ "Build and push your first image")
    * [What's next](https://docs.docker.com/get-started/introduction/whats-next/ "What's next")
  * Docker concepts
    * The basics
      * [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/ "What is a container?")
      * [What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/ "What is an image?")
      * [What is a registry?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/ "What is a registry?")
      * [What is Docker Compose?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/ "What is Docker Compose?")
    * [Building images](https://docs.docker.com/get-started/docker-concepts/building-images/)
      * [Understanding the image layers](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/ "Understanding the image layers")
      * [Writing a Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/ "Writing a Dockerfile")
      * [Build, tag, and publish an image](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/ "Build, tag, and publish an image")
      * [Using the build cache](https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/ "Using the build cache")
      * [Multi-stage builds](https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/ "Multi-stage builds")
    * Running containers
      * [Publishing and exposing ports](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/ "Publishing and exposing ports")
      * [Overriding container defaults](https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults/ "Overriding container defaults")
      * [Persisting container data](https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/ "Persisting container data")
      * [Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/ "Sharing local files with containers")
      * [Multi-container applications](https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/ "Multi-container applications")
  * [Docker workshop](https://docs.docker.com/get-started/workshop/)
    * [Part 1: Containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/ "Part 1: Containerize an application")
    * [Part 2: Update the application](https://docs.docker.com/get-started/workshop/03_updating_app/ "Part 2: Update the application")
    * [Part 3: Share the application](https://docs.docker.com/get-started/workshop/04_sharing_app/ "Part 3: Share the application")
    * [Part 4: Persist the DB](https://docs.docker.com/get-started/workshop/05_persisting_data/ "Part 4: Persist the DB")
    * [Part 5: Use bind mounts](https://docs.docker.com/get-started/workshop/06_bind_mounts/ "Part 5: Use bind mounts")
    * [Part 6: Multi-container apps](https://docs.docker.com/get-started/workshop/07_multi_container/ "Part 6: Multi-container apps")
    * [Part 7: Use Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/ "Part 7: Use Docker Compose")
    * [Part 8: Image-building best practices](https://docs.docker.com/get-started/workshop/09_image_best/ "Part 8: Image-building best practices")
    * [Part 9: What next](https://docs.docker.com/get-started/workshop/10_what_next/ "Part 9: What next")
  * [Educational resources](https://docs.docker.com/get-started/resources/ "Educational resources")


[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / Docker workshop
# Overview of the Docker workshop
Copy as Markdown
Open Markdown Ask Docs AI Claude Open in Claude
Table of contents
  * [What is a container?](https://docs.docker.com/get-started/workshop/#what-is-a-container)
  * [What is an image?](https://docs.docker.com/get-started/workshop/#what-is-an-image)
  * [Next steps](https://docs.docker.com/get-started/workshop/#next-steps)


* * *
This 45-minute workshop contains step-by-step instructions on how to get started with Docker. This workshop shows you how to:
  * Build and run an image as a container.
  * Share images using Docker Hub.
  * Deploy Docker applications using multiple containers with a database.
  * Run applications using Docker Compose.


> Note
> For a quick introduction to Docker and the benefits of containerizing your applications, see [Getting started](https://docs.docker.com/get-started/introduction/).
## [What is a container?](https://docs.docker.com/get-started/workshop/#what-is-a-container)
A container is a sandboxed process running on a host machine that is isolated from all other processes running on that host machine. That isolation leverages
  * Is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI.
  * Can be run on local machines, virtual machines, or deployed to the cloud.
  * Is portable (and can be run on any OS).
  * Is isolated from other containers and runs its own software, binaries, configurations, etc.


If you're familiar with `chroot`, then think of a container as an extended version of `chroot`. The filesystem comes from the image. However, a container adds additional isolation not available when using chroot.
## [What is an image?](https://docs.docker.com/get-started/workshop/#what-is-an-image)
A running container uses an isolated filesystem. This isolated filesystem is provided by an image, and the image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.
## [Next steps](https://docs.docker.com/get-started/workshop/#next-steps)
In this section, you learned about containers and images.
Next, you'll containerize a simple application and get hands-on with the concepts.
[Containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/)
Table of contents
  * [What is a container?](https://docs.docker.com/get-started/workshop/#what-is-a-container)
  * [What is an image?](https://docs.docker.com/get-started/workshop/#what-is-an-image)
  * [Next steps](https://docs.docker.com/get-started/workshop/#next-steps)


[Product offerings](https://www.docker.com/) [Pricing](https://www.docker.com/pricing/) [About us](https://www.docker.com/company/) [llms.txt](https://docs.docker.com/llms.txt)
Cookies Settings | [Terms of Service](https://www.docker.com/legal/docker-terms-service "Docker Terms of Service") | | [Legal](https://www.docker.com/legal "Docker Legal Terms")
Copyright © 2013-2026 Docker Inc. All rights reserved.
Search this siteResults will appear as you typeClear
Start typing to search the documentation
By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.
Cookies Settings Reject All Accept All Cookies
![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.

Allow All
###  Manage Consent Preferences
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Reject All Confirm My Choices
Give feedback
## Was this page useful?
HateLove
Next
