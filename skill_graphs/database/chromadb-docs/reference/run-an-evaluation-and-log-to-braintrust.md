# Run an evaluation and log to Braintrust
await Eval(
    PROJECT_NAME,
    # define your test cases
    data = lambda:[{"input": "What is my eye color?", "expected": "Brown"}],
    # define your retrieval pipeline w/ Chroma above
    task = pipeline_a,
    # use a prebuilt scoring function or define your own :)
    scores=[leven_evaluator],
)
```

Learn more: [docs](https://www.braintrustdata.com/docs).
