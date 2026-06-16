# Workflow
@workflow.defn
class MultiModelWorkflow:
    def __init__(self) -> None:
        self.agent_a = TemporalAgent(
            model="claude",
            start_to_close_timeout=timedelta(seconds=60),
        )
        self.agent_b = TemporalAgent(
            model="bedrock",
            start_to_close_timeout=timedelta(seconds=60),
        )
