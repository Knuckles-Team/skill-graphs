[Skip to main content](https://docs.trychroma.com/guides/build/building-with-ai#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Build
Building with AI
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
##### Build
  * [Building with AI](https://docs.trychroma.com/guides/build/building-with-ai)
  * [Intro to Retrieval](https://docs.trychroma.com/guides/build/intro-to-retrieval)
  * [Look at Your Data](https://docs.trychroma.com/guides/build/look-at-your-data)
  * [Chunking](https://docs.trychroma.com/guides/build/chunking)
  * [Agentic Search](https://docs.trychroma.com/guides/build/agentic-search)
  * [Agentic Memory](https://docs.trychroma.com/guides/build/agentic-memory)


##### Deploy
  * [Client Server Mode](https://docs.trychroma.com/guides/deploy/client-server-mode)
  * [Python Thin Client](https://docs.trychroma.com/guides/deploy/python-thin-client)
  * [Performance](https://docs.trychroma.com/guides/deploy/performance)
  * [Observability](https://docs.trychroma.com/guides/deploy/observability)
  * [Docker](https://docs.trychroma.com/guides/deploy/docker)
  * [AWS](https://docs.trychroma.com/guides/deploy/aws)
  * [Azure](https://docs.trychroma.com/guides/deploy/azure)
  * [GCP](https://docs.trychroma.com/guides/deploy/gcp)


Build
# Building with AI
Copy page
Use LLMs to process unstructured data in your applications.
Copy page
AI is a new type of programming primitive. Large language models (LLMs) let us write software which can process **unstructured** information in a **common sense** way. Consider the task of writing a program to extract a list of people’s names from the following paragraph:
> Now the other princes of the Achaeans slept soundly the whole night through, but Agamemnon son of Atreus was troubled, so that he could get no rest. As when fair Hera’s lord flashes his lightning in token of great rain or hail or snow when the snow-flakes whiten the ground, or again as a sign that he will open the wide jaws of hungry war, even so did Agamemnon heave many a heavy sigh, for his soul trembled within him. When he looked upon the plain of Troy he marveled at the many watchfires burning in front of Ilion… - The Iliad, Scroll 10
Extracting names is easy for humans, but is very difficult using only traditional programming. Writing a general program to extract names from any paragraph is harder still. However, with an LLM the task becomes almost trivial. We can simply provide the following input to an LLM:
> List the names of people in the following paragraph, separated by commas: Now the other princes of the Achaeans slept soundly the whole night through, but Agamemnon son of Atreus was troubled, so that he could get no rest. As when fair Hera’s lord flashes his lightning in token of great rain or hail or snow when the snow-flakes whiten the ground, or again as a sign that he will open the wide jaws of hungry war, even so did Agamemnon heave many a heavy sigh, for his soul trembled within him. When he looked upon the plain of Troy he marveled at the many watchfires burning in front of Ilion… - The Iliad, Scroll 10
The output would correctly be:
> Agamemnon, Atreus, Hera
Integrating LLMs into software applications is as simple as calling an API. While the specifics of the API may vary between LLMs, most have converged on some common patterns:
  * Calls to the API typically consist of parameters including a `model` identifier, and a list of `messages`.
  * Each `message` has a `role` and `content`.
  * The `system` role can be thought of as the _instructions_ to the model.
  * The `user` role can be thought of as the _data_ to process.

For example, we can use AI to write a general purpose function that extracts names from input text.
  * OpenAI
  * Anthropic


Python
TypeScript
Report incorrect code
Copy
Ask AI
```
import json
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_names(text: str) -> list[str]:
    system_prompt = "You are a name extractor. The user will give you text, and you must return a JSON array of names mentioned in the text. Do not include any explanation or formatting."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    response = response.choices[0].message["content"]
    return json.loads(response)

```

Python
TypeScript
Report incorrect code
Copy
Ask AI
```
import json
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def extract_names(text: str) -> list[str]:
    system_prompt = "You are a name extractor. The user will give you text, and you must return a JSON array of names mentioned in the text. Do not include any explanation or formatting."

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": text}
        ]
    )

    response_text = response.content[0].text
    return json.loads(response_text)

```

Building with AI allows new type of work to be done by software. LLMs are capable of understanding abstract ideas and take action. Given access to retrieval systems and tools, LLMs can operate on tasks autonomously in ways that wasn’t possible with classical software.
Was this page helpful?
YesNo
[ Intro to Retrieval Next ](https://docs.trychroma.com/guides/build/intro-to-retrieval)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
