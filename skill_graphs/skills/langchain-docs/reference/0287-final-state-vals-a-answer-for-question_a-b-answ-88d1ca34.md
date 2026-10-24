# Final state: {'vals': ['a:answer for question_a', 'b:answer for question_b']}
```

### Approve or reject

One of the most common uses of interrupts is to pause before a critical action and ask for approval. For example, you might want to ask a human to approve an API call, a database change, or any other important decision.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Literal
from langgraph.types import interrupt, Command

def approval_node(state: State) -> Command[Literal["proceed", "cancel"]]:
    # Pause execution; payload shows up on stream.interrupts (with stream_events) or result["__interrupt__"] (with invoke)
    is_approved = interrupt({
        "question": "Do you want to proceed with this action?",
        "details": state["action_details"]
    })

    # Route based on the response
    if is_approved:
        return Command(goto="proceed")  # Runs after the resume payload is provided
    else:
        return Command(goto="cancel")
```

When you resume the graph, pass `True` to approve or `False` to reject:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# To approve
graph.stream_events(Command(resume=True), config=config, version="v3").output

# To reject
graph.stream_events(Command(resume=False), config=config, version="v3").output
```

<Accordion title="Full example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import Literal, Optional, TypedDict

  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.graph import END, START, StateGraph
  from langgraph.types import Command, interrupt

  class ApprovalState(TypedDict):
      action_details: str
      status: Optional[Literal["pending", "approved", "rejected"]]

  def approval_node(state: ApprovalState) -> Command[Literal["proceed", "cancel"]]:
      # Expose details so the caller can render them in a UI
      decision = interrupt(
          {
              "question": "Approve this action?",
              "details": state["action_details"],
          }
      )

      # Route to the appropriate node after resume
      return Command(goto="proceed" if decision else "cancel")

  def proceed_node(state: ApprovalState):
      return {"status": "approved"}

  def cancel_node(state: ApprovalState):
      return {"status": "rejected"}

  builder = StateGraph(ApprovalState)
  builder.add_node("approval", approval_node)
  builder.add_node("proceed", proceed_node)
  builder.add_node("cancel", cancel_node)
  builder.add_edge(START, "approval")
  builder.add_edge("proceed", END)
  builder.add_edge("cancel", END)

  # Use a more durable checkpointer in production
  checkpointer = InMemorySaver()
  graph = builder.compile(checkpointer=checkpointer)

  config = {"configurable": {"thread_id": "approval-123"}}
  initial = graph.stream_events(
      {"action_details": "Transfer $500", "status": "pending"},
      config=config,
      version="v3",
  )
  _ = initial.output  # drive the stream to completion
  print(initial.interrupts)  # -> (Interrupt(value={'question': ..., 'details': ...}),)

  # Resume with the decision; True routes to proceed, False to cancel
  resumed = graph.stream_events(Command(resume=True), config=config, version="v3")
  print(resumed.output["status"])
  ```
</Accordion>

### Review and edit state

Sometimes you want to let a human review and edit part of the graph state before continuing. This is useful for correcting LLMs, adding missing information, or making adjustments.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import interrupt

def review_node(state: State):
    # Pause and show the current content for review (payload surfaces on stream.interrupts)
    edited_content = interrupt({
        "instruction": "Review and edit this content",
        "content": state["generated_text"]
    })

    # Update the state with the edited version
    return {"generated_text": edited_content}
```

When resuming, provide the edited content:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.stream_events(
    Command(resume="The edited and improved text"),  # Value becomes the return from interrupt()
    config=config,
    version="v3",
).output
```

<Accordion title="Full example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict

  from langgraph.checkpoint.memory import MemorySaver
  from langgraph.graph import END, START, StateGraph
  from langgraph.types import Command, interrupt

  class ReviewState(TypedDict):
      generated_text: str

  def review_node(state: ReviewState):
      # Ask a reviewer to edit the generated content
      updated = interrupt(
          {
              "instruction": "Review and edit this content",
              "content": state["generated_text"],
          }
      )
      return {"generated_text": updated}

  builder = StateGraph(ReviewState)
  builder.add_node("review", review_node)
  builder.add_edge(START, "review")
  builder.add_edge("review", END)

  checkpointer = MemorySaver()
  graph = builder.compile(checkpointer=checkpointer)

  config = {"configurable": {"thread_id": "review-42"}}
  initial = graph.stream_events(
      {"generated_text": "Initial draft"}, config=config, version="v3"
  )
  _ = initial.output  # drive the stream to completion
  print(initial.interrupts)  # -> (Interrupt(value={'instruction': ..., 'content': ...}),)

  # Resume with the edited text from the reviewer
  final_state = graph.stream_events(
      Command(resume="Improved draft after review"),
      config=config,
      version="v3",
  )
  print(final_state.output["generated_text"])  # -> "Improved draft after review"
  ```
</Accordion>

### Interrupts in tools

You can also place interrupts directly inside tool functions. This makes the tool itself pause for approval whenever it's called, and allows for human review and editing of the tool call before it is executed.

First, define a tool that uses [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool
from langgraph.types import interrupt

@tool
def send_email(to: str, subject: str, body: str):
    """Send an email to a recipient."""

    # Pause before sending; payload surfaces on stream.interrupts when using event streaming
    response = interrupt({
        "action": "send_email",
        "to": to,
        "subject": subject,
        "body": body,
        "message": "Approve sending this email?"
    })

    if response.get("action") == "approve":
        # Resume value can override inputs before executing
        final_to = response.get("to", to)
        final_subject = response.get("subject", subject)
        final_body = response.get("body", body)
        return f"Email sent to {final_to} with subject '{final_subject}'"
    return "Email cancelled by user"
```

This approach is useful when you want the approval logic to live with the tool itself, making it reusable across different parts of your graph. The LLM can call the tool naturally, and the interrupt will pause execution whenever the tool is invoked, allowing you to approve, edit, or cancel the action.

<Accordion title="Full example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import sqlite3
  import operator
  from typing import TypedDict, Annotated, Literal
  from langchain.tools import tool
  from langchain_anthropic import ChatAnthropic
  from langgraph.checkpoint.sqlite import SqliteSaver
  from langgraph.graph import StateGraph, START, END
  from langgraph.types import Command, interrupt
  from langchain.messages import AnyMessage, SystemMessage, ToolMessage

  class AgentState(TypedDict):
      messages: Annotated[list[AnyMessage], operator.add]

  @tool
  def send_email(to: str, subject: str, body: str):
      """Send an email to a recipient."""

      # Pause before sending; payload surfaces on stream.interrupts when using event streaming
      response = interrupt({
          "action": "send_email",
          "to": to,
          "subject": subject,
          "body": body,
          "message": "Approve sending this email?",
      })

      if response.get("action") == "approve":
          final_to = response.get("to", to)
          final_subject = response.get("subject", subject)
          final_body = response.get("body", body)

          # Actually send the email (your implementation here)
          print(f"[send_email] to={final_to} subject={final_subject} body={final_body}")
          return f"Email sent to {final_to}"

      return "Email cancelled by user"

  model = ChatAnthropic(model="claude-sonnet-4-6").bind_tools([send_email])
  tools_by_name = {"send_email": send_email}

  def agent_node(state: AgentState):
      # LLM may decide to call the tool; interrupt pauses before sending
      result = model.invoke(state["messages"])
      return {"messages": [result]}

  def tool_node(state: AgentState):
      """Performs the tool call"""
      result = []
      for tool_call in state["messages"][-1].tool_calls:
          tool = tools_by_name[tool_call["name"]]
          observation = tool.invoke(tool_call["args"])
          result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
      return {"messages": result}

  def should_continue(state: AgentState) -> Literal["tool_node", END]:
      """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""
      messages = state["messages"]
      last_message = messages[-1]

      if last_message.tool_calls:
          return "tool_node"
      return END

  builder = StateGraph(AgentState)
  builder.add_node("agent", agent_node)
  builder.add_node("tool_node", tool_node)

  builder.add_edge(START, "agent")
  builder.add_conditional_edges("agent", should_continue, ["tool_node", END])  # Routes to "tools" or END
  builder.add_edge("tool_node", "agent")  # Loop back after tools

  checkpointer = SqliteSaver(
      sqlite3.connect("tool-approval.db", check_same_thread=False)
  )
  graph = builder.compile(checkpointer=checkpointer)

  config = {"configurable": {"thread_id": "email-workflow"}}
  initial = graph.stream_events(
      {
          "messages": [
              {"role": "user", "content": "Send an email to alice@example.com about the meeting"}
          ]
      },
      config=config,
      version="v3",
  )
  initial.output  # drive the stream to completion
  print(initial.interrupts)  # -> (Interrupt(value={'action': 'send_email', ...}),)

  # Resume with approval and optionally edited arguments
  resumed = graph.stream_events(
      Command(resume={"action": "approve", "subject": "Updated subject"}),
      config=config,
      version="v3",
  )
  print(resumed.output["messages"][-1])  # -> Tool result returned by send_email
  ```
</Accordion>

### Validating human input

Sometimes you need to validate input from humans and ask again if it's invalid. You can do this using multiple [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls in a loop.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import interrupt

def get_age_node(state: State):
    prompt = "What is your age?"

    while True:
        answer = interrupt(prompt)  # payload surfaces on stream.interrupts when using event streaming

        # Validate the input
        if isinstance(answer, int) and answer > 0:
            # Valid input - continue
            break
        else:
            # Invalid input - ask again with a more specific prompt
            prompt = f"'{answer}' is not a valid age. Please enter a positive number."

    return {"age": answer}
```

Each time you resume the graph with invalid input, it will ask again with a clearer message. Once valid input is provided, the node completes and the graph continues.

<Accordion title="Full example">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import sqlite3
  from typing import TypedDict

  from langgraph.checkpoint.sqlite import SqliteSaver
  from langgraph.graph import END, START, StateGraph
  from langgraph.types import Command, interrupt

  class FormState(TypedDict):
      age: int | None

  def get_age_node(state: FormState):
      prompt = "What is your age?"

      while True:
          answer = interrupt(prompt)

          if isinstance(answer, int) and answer > 0:
              return {"age": answer}

          prompt = f"'{answer}' is not a valid age. Please enter a positive number."

  builder = StateGraph(FormState)
  builder.add_node("collect_age", get_age_node)
  builder.add_edge(START, "collect_age")
  builder.add_edge("collect_age", END)

  checkpointer = SqliteSaver(sqlite3.connect("forms.db"))
  graph = builder.compile(checkpointer=checkpointer)

  config = {"configurable": {"thread_id": "form-1"}}
  first = graph.stream_events({"age": None}, config=config, version="v3")
  _ = first.output  # drive the stream to completion
  print(first.interrupts)  # -> (Interrupt(value='What is your age?', ...),)

  # Provide invalid data; the node re-prompts
  retry = graph.stream_events(Command(resume="thirty"), config=config, version="v3")
  _ = retry.output  # drive the stream to completion
  print(retry.interrupts)  # -> (Interrupt(value="'thirty' is not a valid age...", ...),)

  # Provide valid data; loop exits and state updates
  final = graph.stream_events(Command(resume=30), config=config, version="v3")
  print(final.output["age"])  # -> 30
  ```
</Accordion>

## Rules of interrupts

When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) within a node, LangGraph suspends execution by raising an exception that signals the runtime to pause. This exception propagates up through the call stack and is caught by the runtime, which notifies the graph to save the current state and wait for external input.

When execution resumes (after you provide the requested input), the runtime restarts the entire node from the beginning—it does not resume from the exact line where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called. This means any code that ran before the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) will execute again. Because of this, there's a few important rules to follow when working with interrupts to ensure they behave as expected.

### Do not wrap `interrupt` calls in try/except

The way that [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) pauses execution at the point of the call is by throwing a special exception. If you wrap the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) call in a try/except block, you will catch this exception and the interrupt will not be passed back to the graph.

* ✅ Separate [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls from error-prone code
* ✅ Use specific exception types in try/except blocks

<CodeGroup>
  ```python Separating logic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: interrupting first, then handling
      # error conditions separately
      interrupt("What's your name?")
      try:
          fetch_data()  # This can fail
      except Exception as e:
          print(e)
      return state
  ```

  ```python Explicit exception handling theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: catching specific exception types
      # will not catch the interrupt exception
      try:
          name = interrupt("What's your name?")
          fetch_data()  # This can fail
      except NetworkException as e:
          print(e)
      return state
  ```
</CodeGroup>

* 🔴 Do not wrap [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls in bare try/except blocks

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def node_a(state: State):
    # ❌ Bad: wrapping interrupt in bare try/except
    # will catch the interrupt exception
    try:
        interrupt("What's your name?")
    except Exception as e:
        print(e)
    return state
```

### Do not reorder `interrupt` calls within a node

It's common to use multiple interrupts in a single node, however this can lead to unexpected behavior if not handled carefully.

When a node contains multiple interrupt calls, LangGraph keeps a list of resume values specific to the task executing the node. Whenever execution resumes, it starts at the beginning of the node. For each interrupt encountered, LangGraph checks if a matching value exists in the task's resume list. Matching is **strictly index-based**, so the order of interrupt calls within the node is important.

* ✅ Keep [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls consistent across node executions

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def node_a(state: State):
    # ✅ Good: interrupt calls happen in the same order every time
    name = interrupt("What's your name?")
    age = interrupt("What's your age?")
    city = interrupt("What's your city?")

    return {
        "name": name,
        "age": age,
        "city": city
    }
```

* 🔴 Do not conditionally skip [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls within a node
* 🔴 Do not loop [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls using logic that isn't deterministic across executions

<CodeGroup>
  ```python Skipping interrupts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ❌ Bad: conditionally skipping interrupts changes the order
      name = interrupt("What's your name?")

      # On first run, this might skip the interrupt
      # On resume, it might not skip it - causing index mismatch
      if state.get("needs_age"):
          age = interrupt("What's your age?")

      city = interrupt("What's your city?")

      return {"name": name, "city": city}
  ```

  ```python Looping interrupts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ❌ Bad: looping based on non-deterministic data
      # The number of interrupts changes between executions
      results = []
      for item in state.get("dynamic_list", []):  # List might change between runs
          result = interrupt(f"Approve {item}?")
          results.append(result)

      return {"results": results}
  ```
</CodeGroup>

### Do not return complex values in `interrupt` calls

Depending on which checkpointer is used, complex values may not be serializable (e.g. you can't serialize a function). To make your graphs adaptable to any deployment, it's best practice to only use values that can be reasonably serialized.

* ✅ Pass simple, JSON-serializable types to [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
* ✅ Pass dictionaries/objects with simple values

<CodeGroup>
  ```python Simple values theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: passing simple types that are serializable
      name = interrupt("What's your name?")
      count = interrupt(42)
      approved = interrupt(True)

      return {"name": name, "count": count, "approved": approved}
  ```

  ```python Structured data theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: passing dictionaries with simple values
      response = interrupt({
          "question": "Enter user details",
          "fields": ["name", "email", "age"],
          "current_values": state.get("user", {})
      })

      return {"user": response}
  ```
</CodeGroup>

* 🔴 Do not pass functions, class instances, or other complex objects to [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)

<CodeGroup>
  ```python Functions theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def validate_input(value):
      return len(value) > 0

  def node_a(state: State):
      # ❌ Bad: passing a function to interrupt
      # The function cannot be serialized
      response = interrupt({
          "question": "What's your name?",
          "validator": validate_input  # This will fail
      })
      return {"name": response}
  ```

  ```python Class instances theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  class DataProcessor:
      def __init__(self, config):
          self.config = config

  def node_a(state: State):
      processor = DataProcessor({"mode": "strict"})

      # ❌ Bad: passing a class instance to interrupt
      # The instance cannot be serialized
      response = interrupt({
          "question": "Enter data to process",
          "processor": processor  # This will fail
      })
      return {"result": response}
  ```
</CodeGroup>

### Side effects called before `interrupt` must be idempotent

Because interrupts work by re-running the nodes they were called from, side effects called before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) should (ideally) be idempotent. For context, idempotency means that the same operation can be applied multiple times without changing the result beyond the initial execution.

As an example, you might have an API call to update a record inside of a node. If [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) is called after that call is made, it will be re-run multiple times when the node is resumed, potentially overwriting the initial update or creating duplicate records.

* ✅ Use idempotent operations before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
* ✅ Place side effects after [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls
* ✅ Separate side effects into separate nodes when possible

<CodeGroup>
  ```python Idempotent operations theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: using upsert operation which is idempotent
      # Running this multiple times will have the same result
      db.upsert_user(
          user_id=state["user_id"],
          status="pending_approval"
      )

      approved = interrupt("Approve this change?")

      return {"approved": approved}
  ```

  ```python Side effects after interrupt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ✅ Good: placing side effect after the interrupt
      # This ensures it only runs once after approval is received
      approved = interrupt("Approve this change?")

      if approved:
          db.create_audit_log(
              user_id=state["user_id"],
              action="approved"
          )

      return {"approved": approved}
  ```

  ```python Separating into different nodes theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def approval_node(state: State):
      # ✅ Good: only handling the interrupt in this node
      approved = interrupt("Approve this change?")

      return {"approved": approved}

  def notification_node(state: State):
      # ✅ Good: side effect happens in a separate node
      # This runs after approval, so it only executes once
      if (state.approved):
          send_notification(
              user_id=state["user_id"],
              status="approved"
          )

      return state
  ```
</CodeGroup>

* 🔴 Do not perform non-idempotent operations before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
* 🔴 Do not create new records without checking if they exist

<CodeGroup>
  ```python Creating records theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ❌ Bad: creating a new record before interrupt
      # This will create duplicate records on each resume
      audit_id = db.create_audit_log({
          "user_id": state["user_id"],
          "action": "pending_approval",
          "timestamp": datetime.now()
      })

      approved = interrupt("Approve this change?")

      return {"approved": approved, "audit_id": audit_id}
  ```

  ```python Appending to lists theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  def node_a(state: State):
      # ❌ Bad: appending to a list before interrupt
      # This will add duplicate entries on each resume
      db.append_to_history(state["user_id"], "approval_requested")

      approved = interrupt("Approve this change?")

      return {"approved": approved}
  ```
</CodeGroup>

## Using with subgraphs called as functions

When invoking a subgraph within a node, the parent graph will resume execution from the **beginning of the node** where the subgraph was invoked and the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was triggered. Similarly, the **subgraph** will also resume from the beginning of the node where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def node_in_parent_graph(state: State):
    some_code()  # <-- This will re-execute when resumed
    # Invoke a subgraph as a function.
    # The subgraph contains an `interrupt` call.
    subgraph_result = subgraph.invoke(some_input)
    # ...

def node_in_subgraph(state: State):
    some_other_code()  # <-- This will also re-execute when resumed
    result = interrupt("What's your name?")
    # ...
```

## Debugging with interrupts

To debug and test a graph, you can use static interrupts as breakpoints to step through the graph execution one node at a time. Static interrupts are triggered at defined points either before or after a node executes. You can set these by specifying `interrupt_before` and `interrupt_after` when compiling the graph.

<Note>
  Static interrupts are **not** recommended for human-in-the-loop workflows. Use the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function instead.
</Note>

<Tabs>
  <Tab title="At compile time">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    graph = builder.compile(
        interrupt_before=["node_a"],  # [!code highlight]
        interrupt_after=["node_b", "node_c"],  # [!code highlight]
        checkpointer=checkpointer,
    )

    # Pass a thread ID to the graph
    config = {
        "configurable": {
            "thread_id": "some_thread"
        }
    }

    # Run the graph until the breakpoint
    graph.invoke(inputs, config=config)  # [!code highlight]

    # Resume the graph
    graph.invoke(None, config=config)  # [!code highlight]
    ```

    1. The breakpoints are set during `compile` time.
    2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
    3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
    4. A checkpointer is required to enable breakpoints.
    5. The graph is run until the first breakpoint is hit.
    6. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>

  <Tab title="At run time">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {
        "configurable": {
            "thread_id": "some_thread"
        }
    }

    # Run the graph until the breakpoint
    graph.invoke(
        inputs,
        interrupt_before=["node_a"],  # [!code highlight]
        interrupt_after=["node_b", "node_c"],  # [!code highlight]
        config=config,
    )

    # Resume the graph
    graph.invoke(None, config=config)  # [!code highlight]
    ```

    1. `graph.invoke` is called with the `interrupt_before` and `interrupt_after` parameters. This is a run-time configuration and can be changed for every invocation.
    2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
    3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
    4. The graph is run until the first breakpoint is hit.
    5. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>
</Tabs>

<Tip>
  To debug your interrupts, use [LangSmith](/langsmith/observability).
</Tip>

### Using LangSmith Studio

You can use [LangSmith Studio](/langsmith/studio) to set static interrupts in your graph in the UI before running the graph. You can also use the UI to inspect the graph state at any point in the execution.

<img alt="image" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/interrupts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run a local server
Source: https://docs.langchain.com/oss/python/langgraph/local-server

This guide shows you how to run a LangGraph application locally.

## Prerequisites

Before you begin, ensure you have the following:

* An API key for [LangSmith](https://smith.langchain.com/settings) - free to sign up

## 1. Install the LangGraph CLI

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Python >= 3.11 is required.
  pip install -U "langgraph-cli[inmem]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Python >= 3.11 is required.
  uv add "langgraph-cli[inmem]"
  ```
</CodeGroup>

## 2. Create a LangGraph app

Create a new app from the [`new-langgraph-project-python` template](https://github.com/langchain-ai/new-langgraph-project). This template demonstrates a single-node application you can extend with your own logic.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph new path/to/your/app --template new-langgraph-project-python
```

<Tip>
  **Additional templates**
  If you use `langgraph new` without specifying a template, you will be presented with an interactive menu that will allow you to choose from a list of available templates.
</Tip>

## 3. Install dependencies

In the root of your new LangGraph app, install the dependencies in `edit` mode so your local changes are used by the server:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  cd path/to/your/app
  pip install -e .
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  cd path/to/your/app
  uv sync
  ```
</CodeGroup>

## 4. Create a `.env` file

You will find a `.env.example` in the root of your new LangGraph app. Create a `.env` file in the root of your new LangGraph app and copy the contents of the `.env.example` file into it, filling in the necessary API keys:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2...
```

## 5. Launch Agent server

Start the LangGraph API server locally:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev
```

Sample output:

```
INFO:langgraph_api.cli:

        Welcome to

╦  ┌─┐┌┐┌┌─┐╔═╗┬─┐┌─┐┌─┐┬ ┬
║  ├─┤││││ ┬║ ╦├┬┘├─┤├─┘├─┤
╩═╝┴ ┴┘└┘└─┘╚═╝┴└─┴ ┴┴  ┴ ┴

- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

This in-memory server is designed for development and testing.
For production use, please use LangSmith Deployment.
```

The `langgraph dev` command starts Agent Server in an in-memory mode. This mode is suitable for development and testing purposes. For production use, deploy Agent Server with access to a persistent storage backend. For more information, see the [Platform setup overview](/langsmith/platform-setup).

## 6. Test your application in Studio

[Studio](/langsmith/studio) is a specialized UI that you can connect to LangGraph API server to visualize, interact with, and debug your application locally. Test your graph in Studio by visiting the URL provided in the output of the `langgraph dev` command:

```
>    - LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

For an Agent Server running on a custom host/port, update the `baseUrl` query parameter in the URL. For example, if your server is running on `http://myhost:3000`:

```
https://smith.langchain.com/studio/?baseUrl=http://myhost:3000
```

<Accordion title="Safari compatibility">
  Use the `--tunnel` flag with your command to create a secure tunnel, as Safari has limitations when connecting to localhost servers:

  ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  langgraph dev --tunnel
  ```
</Accordion>

## 7. Test the API

<Tabs>
  <Tab title="Python SDK (async)">
    1. Install the LangGraph Python SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       pip install langgraph-sdk
       ```
    2. Send a message to the assistant (threadless run):
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph_sdk import get_client
       import asyncio

       client = get_client(url="http://localhost:2024")

       async def main():
           async for chunk in client.runs.stream(
               None,  # Threadless run
               "agent", # Name of assistant. Defined in langgraph.json.
               input={
               "messages": [{
                   "role": "human",
                   "content": "What is LangGraph?",
                   }],
               },
           ):
               print(f"Receiving new event of type: {chunk.event}...")
               print(chunk.data)
               print("\n\n")

       asyncio.run(main())
       ```
  </Tab>

  <Tab title="Python SDK (sync)">
    1. Install the LangGraph Python SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       pip install langgraph-sdk
       ```
    2. Send a message to the assistant (threadless run):
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph_sdk import get_sync_client

       client = get_sync_client(url="http://localhost:2024")

       for chunk in client.runs.stream(
           None,  # Threadless run
           "agent", # Name of assistant. Defined in langgraph.json.
           input={
               "messages": [{
                   "role": "human",
                   "content": "What is LangGraph?",
               }],
           },
           stream_mode="messages-tuple",
       ):
           print(f"Receiving new event of type: {chunk.event}...")
           print(chunk.data)
           print("\n\n")
       ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url "http://localhost:2024/runs/stream" \
        --header 'Content-Type: application/json' \
        --data "{
            \"assistant_id\": \"agent\",
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"messages-tuple\"
        }"
    ```
  </Tab>
</Tabs>

## Next steps

Now that you have a LangGraph app running locally, take your journey further by exploring deployment and advanced features:

* [Deployment quickstart](/langsmith/deployment-quickstart): Deploy your LangGraph app using LangSmith.

* [LangSmith](/langsmith/observability): Learn about foundational LangSmith concepts.

* [SDK Reference](https://reference.langchain.com/python/langsmith/deployment/sdk/): Explore the SDK API Reference.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/local-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Observability
Source: https://docs.langchain.com/oss/python/langgraph/observability

Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability) to visualize these execution steps. To use it, [enable tracing for your application](/langsmith/trace-with-langgraph). This enables you to do the following:

* [Debug a locally running application](/langsmith/observability-studio#debug-langsmith-traces).
* [Evaluate the application performance](/oss/python/langchain/test/evals).
* [Monitor the application](/langsmith/dashboards).

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.

## Enable tracing

To enable tracing for your application, set the following environment variables:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](#log-to-a-project).

For more information, see [Trace with LangGraph](/langsmith/trace-with-langgraph).

## Trace selectively

You may opt to trace specific invocations or parts of your application using LangSmith's `tracing_context` context manager:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import langsmith as ls

# This WILL be traced
with ls.tracing_context(enabled=True):
    agent.invoke({"messages": [{"role": "user", "content": "Send a test email to alice@example.com"}]})

# This will NOT be traced (if LANGSMITH_TRACING is not set)
agent.invoke({"messages": [{"role": "user", "content": "Send another email"}]})
```

## Log to a project

<Accordion title="Statically">
  You can set a custom project name for your entire application by setting the `LANGSMITH_PROJECT` environment variable:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_PROJECT=my-agent-project
  ```
</Accordion>

<Accordion title="Dynamically">
  You can set the project name programmatically for specific operations:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import langsmith as ls

  with ls.tracing_context(project_name="email-agent-test", enabled=True):
      response = agent.invoke({
          "messages": [{"role": "user", "content": "Send a welcome email"}]
      })
  ```
</Accordion>

## Add metadata to traces

You can annotate your traces with custom metadata and tags:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
response = agent.invoke(
    {"messages": [{"role": "user", "content": "Send a welcome email"}]},
    config={
        "tags": ["production", "email-assistant", "v1.0"],
        "metadata": {
            "user_id": "user_123",
            "session_id": "session_456",
            "environment": "production"
        }
    }
)
```

`tracing_context` also accepts tags and metadata for fine-grained control:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
with ls.tracing_context(
    project_name="email-agent-test",
    enabled=True,
    tags=["production", "email-assistant", "v1.0"],
    metadata={"user_id": "user_123", "session_id": "session_456", "environment": "production"}):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Send a welcome email"}]}
    )
```

This custom metadata and tags will be attached to the trace in LangSmith.

<Tip>
  To learn more about how to use traces to debug, evaluate, and monitor your agents, see the [LangSmith documentation](/langsmith/observability).
</Tip>

## Use anonymizers to prevent logging of sensitive data in traces

You may want to mask sensitive data to prevent it from being logged to LangSmith. You can create [anonymizers](/langsmith/mask-inputs-outputs#rule-based-masking-of-inputs-and-outputs) and apply them to
your graph using configuration. This example will redact anything matching the Social Security Number format XXX-XX-XXXX from traces sent to LangSmith.

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.tracers.langchain import LangChainTracer
from langgraph.graph import StateGraph, MessagesState
from langsmith import Client
from langsmith.anonymizer import create_anonymizer

anonymizer = create_anonymizer([
    # Matches SSNs
    { "pattern": r"\b\d{3}-?\d{2}-?\d{4}\b", "replace": "<ssn>" }
])

tracer_client = Client(anonymizer=anonymizer)
tracer = LangChainTracer(client=tracer_client)

# Define the graph
graph = (
    StateGraph(MessagesState)
    ...
    .compile()
    .with_config({'callbacks': [tracer]})
)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
