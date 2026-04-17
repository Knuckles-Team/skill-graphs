##  [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis#getting-started)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#getting-started)
  1. ###  [Create a new project](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-a-new-project)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-a-new-project)
First, create a new directory for your project:
terminal
```
mkdir litellm-ai-gateway
cd litellm-ai-gateway
```

  2. ###  [Install dependencies](https://vercel.com/docs/ai-gateway/sdks-and-apis#install-dependencies)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#install-dependencies)
Install the required LiteLLM Python package:
terminal
```
pip install litellm python-dotenv
```

  3. ###  [Configure environment variables](https://vercel.com/docs/ai-gateway/sdks-and-apis#configure-environment-variables)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#configure-environment-variables)
Create a `.env` file with your [Vercel AI Gateway API key](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key):
.env
```
VERCEL_AI_GATEWAY_API_KEY=your-api-key-here
```

If you're using the [AI Gateway from within a Vercel deployment](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-a-vercel-oidc-token), you can also use the `VERCEL_OIDC_TOKEN` environment variable which will be automatically provided.
  4. ###  [Create your LiteLLM application](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-your-litellm-application)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-your-litellm-application)
Create a new file called `main.py` with the following code:
main.py
```
import os
import litellm
from dotenv import load_dotenv

load_dotenv()

os.environ["VERCEL_AI_GATEWAY_API_KEY"] = os.getenv("VERCEL_AI_GATEWAY_API_KEY")

# Define messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me about the food scene in San Francisco."}
]

response = litellm.completion(
    model="vercel_ai_gateway/openai/gpt-4o",
    messages=messages
)

print(response.choices[0].message.content)
```

The following code:
     * Uses LiteLLM's `completion` function to make requests through Vercel AI Gateway
     * Specifies the model using the `vercel_ai_gateway/` prefix
     * Makes a chat completion request and prints the response
  5. ###  [Running the application](https://vercel.com/docs/ai-gateway/sdks-and-apis#running-the-application)[](https://vercel.com/docs/ai-gateway/sdks-and-apis#running-the-application)
Run your Python application:
terminal
```
python main.py
```

You should see a response from the AI model in your console.


* * *
[ Previous Capabilities ](https://vercel.com/docs/ai-gateway/capabilities)[ Next AI SDK ](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk)
Was this helpful?
Send
On this page
  * [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis#getting-started)
  * [Create a new project](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-a-new-project)
  * [Install dependencies](https://vercel.com/docs/ai-gateway/sdks-and-apis#install-dependencies)
  * [Configure environment variables](https://vercel.com/docs/ai-gateway/sdks-and-apis#configure-environment-variables)
  * [Create your LiteLLM application](https://vercel.com/docs/ai-gateway/sdks-and-apis#create-your-litellm-application)
  * [Running the application](https://vercel.com/docs/ai-gateway/sdks-and-apis#running-the-application)


Copy as MarkdownGive feedbackAsk AI about this page
