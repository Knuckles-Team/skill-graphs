# Braintrust
Source: https://docs.trychroma.com/integrations/frameworks/braintrust

[Braintrust](https://www.braintrustdata.com) is an enterprise-grade stack for building AI products including: evaluations, prompt playground, dataset management, tracing, etc.

Braintrust provides a Typescript and Python library to run and log evaluations and integrates well with Chroma.

* [Tutorial: Evaluate Chroma Retrieval app w/ Braintrust](https://www.braintrustdata.com/docs/examples/rag)

Example evaluation script in Python:
(refer to the tutorial above to get the full implementation)

```python theme={null}
from autoevals.llm import *
from braintrust import Eval

PROJECT_NAME="Chroma_Eval"

from openai import OpenAI

client = OpenAI()
leven_evaluator = LevenshteinScorer()

async def pipeline_a(input, hooks=None):
    # Get a relevant fact from Chroma
    relevant = collection.query(
        query_texts=[input],
        n_results=1,
    )
    relevant_text = ','.join(relevant["documents"][0])
    prompt = """
        You are an assistant called BT. Help the user.
        Relevant information: {relevant}
        Question: {question}
        Answer:
        """.format(question=input, relevant=relevant_text)
    messages = [{"role": "system", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    result = response.choices[0].message.content
    return result
