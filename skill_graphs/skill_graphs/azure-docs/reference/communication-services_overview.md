Search
Suggestions will filter as you type
  * [Azure Communication Services documentation](https://learn.microsoft.com/en-us/azure/communication-services/)
  *     * [What is Azure Communication Services?](https://learn.microsoft.com/en-us/azure/communication-services/overview)
    * [What's new](https://learn.microsoft.com/en-us/azure/communication-services/whats-new)
    * [Services](https://learn.microsoft.com/en-us/azure/communication-services/concepts/services)
    * [Pricing](https://azure.microsoft.com/pricing/details/communication-services/)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/)
  2. [ Azure ](https://learn.microsoft.com/en-us/azure/)
  3. [ Communication Services ](https://learn.microsoft.com/en-us/azure/communication-services/)


  1. [Learn](https://learn.microsoft.com/en-us/)
  2. [Azure](https://learn.microsoft.com/en-us/azure/)
  3. [Communication Services](https://learn.microsoft.com/en-us/azure/communication-services/)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/azure/communication-services/overview) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/communication-services/overview) or changing directories.
Access to this page requires authorization. You can try changing directories.
# What is Azure Communication Services?
Feedback
Summarize this article for me
##  In this article
  1. [Common scenarios](https://learn.microsoft.com/en-us/azure/communication-services/overview#common-scenarios)
  2. [Samples](https://learn.microsoft.com/en-us/azure/communication-services/overview#samples)
  3. [Platforms and SDK libraries](https://learn.microsoft.com/en-us/azure/communication-services/overview#platforms-and-sdk-libraries)
  4. [Design resources](https://learn.microsoft.com/en-us/azure/communication-services/overview#design-resources)
  5. [Other Microsoft Communication Services](https://learn.microsoft.com/en-us/azure/communication-services/overview#other-microsoft-communication-services)
  6. [Next steps](https://learn.microsoft.com/en-us/azure/communication-services/overview#next-steps)

Show 2 more
Azure Communication Services offers multichannel communication APIs for adding voice, video, chat, text messaging/SMS, email, and more to all your applications.
Azure Communication Services include REST APIs and client library SDKs, so you don't need to be an expert in the underlying technologies to add communication into your apps. Azure Communication Services is available in multiple [Azure geographies](https://learn.microsoft.com/en-us/azure/communication-services/concepts/privacy) and Azure for government.
Microsoft 365 Developer
42.6K subscribers
[](https://learn.microsoft.com/en-us/azure/communication-services/overview)
Microsoft 365 Developer
Search
Watch later
Share
Copy link
Info
Shopping
Tap to unmute
If playback doesn't begin shortly, try restarting your device.
More videos
## More videos
You're signed out
Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.
CancelConfirm
Share
Include playlist
An error occurred while retrieving sharing information. Please try again later.
0:00
0:00 / 13:13
•Live
•
Azure Communication Services supports various communication formats:
  * [Voice and Video Calling](https://learn.microsoft.com/en-us/azure/communication-services/concepts/voice-video-calling/calling-sdk-features)
  * [Rich Text Chat](https://learn.microsoft.com/en-us/azure/communication-services/concepts/chat/concepts)
  * [SMS](https://learn.microsoft.com/en-us/azure/communication-services/concepts/sms/concepts)
  * [Email](https://learn.microsoft.com/en-us/azure/communication-services/concepts/email/email-overview)
  * [Advanced Messaging for WhatsApp](https://learn.microsoft.com/en-us/azure/communication-services/concepts/advanced-messaging/whatsapp/whatsapp-overview)


You can connect custom client apps, custom services, and the publicly switched telephone network (PSTN) to your communications experience. You can acquire [phone numbers](https://learn.microsoft.com/en-us/azure/communication-services/concepts/telephony/plan-solution) directly through Azure Communication Services REST APIs, SDKs, or the Azure portal and use these numbers for SMS or calling applications.
You can also integrate email capabilities to your applications using production-ready email SDKs. Azure Communication Services [direct routing](https://learn.microsoft.com/en-us/azure/communication-services/concepts/telephony/plan-solution) enables you to use SIP and session border controllers to connect your own PSTN carriers and bring your own phone numbers.
In addition to REST APIs, [Azure Communication Services client libraries](https://learn.microsoft.com/en-us/azure/communication-services/concepts/sdk-options) are available for various platforms and languages, including Web browsers (JavaScript), iOS (Swift), Android (Java), Windows (.NET). Take advantage of the [UI library](https://learn.microsoft.com/en-us/azure/communication-services/concepts/ui-library/ui-library-overview) to accelerate development for Web, iOS, and Android apps. Azure Communication Services is identity agnostic, and you control how to identify and authenticate your customers.
Scenarios for Azure Communication Services include:
  * **Business to Consumer (B2C).** Employees and services engage external customers using voice, video, and text chat in browser and native apps. Your organization can send and receive SMS messages, or [operate an interactive voice response system (IVR)](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/call-automation) using Call Automation and a phone number you acquire through Azure. You can [Integrate with Microsoft Teams](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/get-started-teams-interop) to connect consumers to Teams meetings hosted by employees. This integration is ideal for remote healthcare, banking, and product support scenarios where employees might already be familiar with Teams.
  * **Consumer to Consumer (C2C).** Build engaging consumer-to-consumer interaction with voice, video, and rich text chat. You can build custom user interfaces on Azure Communication Services SDKs. You can also deploy complete application samples and an open-source UI toolkit to help you get started quickly.


To learn more, check out our
[](https://learn.microsoft.com/en-us/azure/communication-services/overview#common-scenarios)
## Common scenarios


Expand table
Resource | Description
---|---
**[Create a Communication Services resource](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource)** | Begin using Azure Communication Services through the Azure portal or Communication Services SDK to provision your first Communication Services resource. Once you have your Communication Services resource connection string, you can provide user access tokens.
**[Get a phone number](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/telephony/get-phone-number)** | Use Azure Communication Services to provision and release telephone numbers. Then use telephone numbers to initiate or receive phone calls and build SMS solutions.
**[Send an SMS from your app](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/sms/send)** | Use Azure Communication Services SMS REST APIs and SDKs to send and receive SMS messages from service applications.
**[Send an Email from your app](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/send-email)** | Use Azure Communication Services Email REST APIs and SDKs to send email messages from service applications.
After creating a Communication Services resource you can start building client scenarios, such as voice and video calling or text chat:
Expand table
Resource | Description
---|---
**[Create your first user access token](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/identity/access-tokens)** | User access tokens authenticate clients against your Azure Communication Services resource. These tokens are provisioned and reissued using Communication Services Identity APIs and SDKs.
**[Get started with voice and video calling](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/getting-started-with-calling)** | Azure Communication Services enable you to add voice and video calling to your browser or native apps using the Calling SDK.
**[Add telephony calling to your app](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/telephony/pstn-call)** | Use Azure Communication Services to add telephony calling capabilities to your application.
**[Make an outbound call from your app](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/call-automation/quickstart-make-an-outbound-call)** | Use Call Automation SDKs and REST APIs to make outbound calls with an interactive voice response system.
**[Join your calling app to a Teams meeting](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/get-started-teams-interop)** | Use Azure Communication Services to build custom meeting experiences that interact with Microsoft Teams. Users of your Communication Services solutions can interact with Teams participants over voice, video, chat, and screen sharing.
**[Get started with chat](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/chat/get-started)** | Use the Azure Communication Services Chat SDK to add rich real-time text chat into your applications.
| Telephony channel is a channel in Microsoft Bot Framework that enables the bot to interact with users over the phone. It uses the power of Microsoft Bot Framework combined with the Azure Communication Services and the Azure Speech Services.
| The UI Library for Azure Communication Services enables you to easily add rich, visual communication experiences to your applications for both calling and chat.
[](https://learn.microsoft.com/en-us/azure/communication-services/overview#samples)
## Samples
The following samples demonstrate end-to-end solutions using Azure Communication Services. Start with these samples to bootstrap your own Communication Services solutions.

Expand table
Sample name | Description
---|---
**[The Group Calling Hero Sample](https://learn.microsoft.com/en-us/azure/communication-services/samples/calling-hero-sample)** | Download a designed application sample for group calling via browsers, iOS, and Android devices.
**[The Group Chat Hero Sample](https://learn.microsoft.com/en-us/azure/communication-services/samples/chat-hero-sample)** | Download a designed application sample for group text chat in browsers.
**[The Web Calling Sample](https://learn.microsoft.com/en-us/azure/communication-services/samples/web-calling-sample)** | Download a designed web application for audio, video, and PSTN calling.
[](https://learn.microsoft.com/en-us/azure/communication-services/overview#platforms-and-sdk-libraries)
## Platforms and SDK libraries
To learn more about the Azure Communication Services SDKs, see the following resources. If you want to build your own clients or access the service over the Internet, REST APIs are available for most functions.
Expand table
Resource | Description
---|---
**[SDK libraries and REST APIs](https://learn.microsoft.com/en-us/azure/communication-services/concepts/sdk-options)** | Azure Communication Services capabilities are organized into six areas, each with an SDK. You can decide which SDK libraries to use based on your real-time communication needs.
**[Calling SDK overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/voice-video-calling/calling-sdk-features)** | See the Calling SDK for information about end-user browsers, apps, and services to drive voice and video communication.
**[Call Automation overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/call-automation)** | Review the Call Automation SDK for more about server-based intelligent call workflows and call recording for voice and PSTN channels.
**[Chat SDK overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/chat/sdk-features)** | See the Chat SDK for information about adding chat capabilities to your applications.
**[SMS SDK overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/sms/sdk-features)** | Review the SMS SDK to add SMS messaging to your applications.
**[Email SDK overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/email/sdk-features)** | See the Email SDK for information about adding transactional Email support to your applications.
**[UI Library overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/ui-library/ui-library-overview)** | Review the UI Library for more about production-ready UI components that you can drop into your applications.
[](https://learn.microsoft.com/en-us/azure/communication-services/overview#design-resources)
## Design resources
Find comprehensive components, composites, and UX guidance in the
[](https://learn.microsoft.com/en-us/azure/communication-services/overview#other-microsoft-communication-services)
## Other Microsoft Communication Services
Consider using two other Microsoft communication products that aren't directly interoperable with Azure Communication Services at this time:
  * [Microsoft Graph Cloud Communication APIs](https://learn.microsoft.com/en-us/graph/cloud-communications-concept-overview) enable organizations to build communication experiences tied to Microsoft Entra users with Microsoft 365 licenses. This workflow is ideal for applications tied to Microsoft Entra ID or where you want to extend productivity experiences in Microsoft Teams. There are also APIs to build applications and customization within the [Teams experience.](https://learn.microsoft.com/en-us/microsoftteams/platform/?preserve-view=true&view=msteams-client-js-latest)
  * [Azure PlayFab Party](https://learn.microsoft.com/en-us/gaming/playfab/features/multiplayer/networking/) simplifies adding low-latency chat and data communication to games. While you can power gaming chat and networking systems with Communication Services, PlayFab is a tailored option and free on Xbox.


[](https://learn.microsoft.com/en-us/azure/communication-services/overview#next-steps)
## Next steps
  * [Create a Communication Services resource](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource)


* * *
## Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
* * *
##  Additional resources
  * [ Create a Communication Services resource in Azure Communication Services - An Azure Communication Services article ](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource?source=recommendations)
This article describes how to create and manage your first Azure Communication Services resource.
  * [ Services available in Azure Communication Services ](https://learn.microsoft.com/en-us/azure/communication-services/concepts/services?source=recommendations)
Learn about the services provided by Azure Communication Services.
  * [ What's new in Azure Communication Services ](https://learn.microsoft.com/en-us/azure/communication-services/whats-new?source=recommendations)
Learn about the latest additions to Azure Communication Services.
  * [ Data residency and user privacy for Azure Communication Services - An Azure Communication Services article ](https://learn.microsoft.com/en-us/azure/communication-services/concepts/privacy?source=recommendations)
This article describes data residency and privacy related matters on Azure Communication Services.
  * [ SDKs and REST APIs for Azure Communication Services - An Azure Communication Services concept document ](https://learn.microsoft.com/en-us/azure/communication-services/concepts/sdk-options?source=recommendations)
Learn more about Azure Communication Services SDKs and REST APIs.
  * [ Azure managed applications - An Azure Communication Services article ](https://learn.microsoft.com/en-us/azure/communication-services/concepts/managed-apps?source=recommendations)
This article describes how to offer your customers cloud solutions using Azure managed applications for Azure Communication Services.
  * [ Reference documentation overview for Azure Communication Services - An Azure Communication Services concept document ](https://learn.microsoft.com/en-us/azure/communication-services/concepts/reference?source=recommendations)
Learn about Communication Services' reference documentation.


Show 4 more
Module
[ Introduction to Azure Communication Services - Training ](https://learn.microsoft.com/en-us/training/modules/intro-azure-communication-services/?source=recommendations)
Discover the key products and services that can help you create communication applications on Azure with Communication Services.
Certification
[ Microsoft 365 Certified: Collaboration Communications Systems Engineer Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/m365-collaboration-communications-systems-engineer/?source=recommendations)
Demonstrate skills to configure, deploy, monitor, and manage Microsoft Teams Phone, meetings, and certified devices.
* * *
  * Last updated on 05/09/2024


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/azure/communication-services/overview)
