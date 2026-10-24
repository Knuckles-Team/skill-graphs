# Good - deterministic across replays
value = workflow.random().randint(1, 100)
unique_id = workflow.uuid4()
