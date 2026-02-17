# The 6 Principles of Reliable Agent Building

## Principle 1: Agent = Job-to-be-done, Skill = Capability

### What it means
An agent is a main script that orchestrates a specific end-to-end job. A skill is a reusable capability that multiple agents can call. Think of agents as programs and skills as libraries.

### Why it works
Separating orchestration from capability creates natural boundaries. Each skill can be developed, tested, and iterated independently. When an agent breaks, you know whether the issue is in the orchestration logic or in a specific capability.

### How to apply it
- Define agents around outcomes: "enrich a company list", "generate a weekly report", "review outreach sequences"
- Define skills around capabilities: "analyze product metrics", "format data as CSV", "post to Slack"
- Compose skills inside agents using the `/skill` pattern
- Keep skills small enough to have a tight feedback loop -- if you can't test a skill in one `/clear` cycle, it's too big

## Principle 2: Develop by doing, not by prompting

### What it means
Don't write an agent definition from a description. Instead, manually walk through the task in normal Claude Code mode, capture the action trace, and then codify it into the agent.

### Why it works
When you auto-generate an agent from a prompt like "create an agent that enriches companies", the model guesses tool names, parameters, and workflows. These guesses are plausible but often wrong. When you prototype first, you capture:
- Real tool names and their exact parameter schemas
- The actual order of operations (which is often non-obvious)
- Edge cases and error recovery patterns
- Which outputs feed into which inputs

### How to apply it
1. Start a fresh session (`/clear`)
2. Do the task manually, step by step
3. Note every tool call, every parameter, every output
4. After completing the task, review your action trace
5. Distill the trace into the agent definition
6. Never skip this step, even for "simple" agents

## Principle 3: Context is the enemy (RLM pattern)

### What it means
The model's context window is a precious, finite resource. Every token of tool output, every inline reasoning chain, every repeated instruction eats into it. Use external storage (files, scripts, structured output) to keep context lean.

### Context layers: the input side
Before the agent even runs, prepare **context layer documents** -- reference files the agent can pull in via `@` links. These encode domain knowledge (guidelines, criteria, templates) outside the agent definition. The agent reads them when needed rather than carrying all domain knowledge inline. This is the input-side complement to script-based outputs (the output side).

### Why it works -- the RLM connection
MIT's Recursive Language Models (RLMs) formalize this insight. RLMs treat the prompt as an external environment and use a Python REPL to manage data:
- **Peek**: sample a subset of data to understand structure without loading everything
- **Grep**: filter data for relevant patterns instead of scanning inline
- **Partition + Map**: chunk large datasets and process each chunk independently
- **Variables**: store intermediate results as REPL variables, not in the prompt

This is exactly what the "write scripts that export tool results to tmp/ files" pattern achieves at the agent level. Instead of the model carrying all tool output in context, it writes results to files and reads only what it needs.

### How to apply it

**Use indexed step files:**
```
agent-definition/
  step-01-gather-inputs.md
  step-02-enrich-data.md
  step-03-validate-results.md
  step-04-generate-output.md
```
The agent reads only the current step, not the entire definition at once.

**Use script-based intermediate outputs:**
```python
# Script: enrich_company.py
# Calls MCP tools, saves results to tmp/
import json

results = call_tool("searchTools", {"query": company_name})
with open(f"tmp/{company_name}_enrichment.json", "w") as f:
    json.dump(results, f)
```

The model then peeks at the file (`head tmp/acme_enrichment.json`), greps for specific fields, or processes it in chunks -- without ever loading the full output into context.

**Partition large tasks:**
Instead of processing 100 companies in one context window, partition into batches:
```
tmp/batch_01.json  (companies 1-10)
tmp/batch_02.json  (companies 11-20)
...
```
Process each batch independently, then merge results.

## Principle 4: Make the model plan before it acts

### What it means
Before the agent executes any steps, it should generate an explicit task list with a dependency graph. This is the "think before you act" pattern at the workflow level.

### Why it works
Without a plan, the model executes steps greedily and often paints itself into a corner. With an explicit task list:
- Dependencies are visible, enabling parallel execution where possible
- The model can reason about the whole workflow before committing to any step
- Progress is trackable -- you can see what's done, what's in progress, and what's blocked
- Recovery is easier -- if a step fails, the plan shows what to retry

### How to apply it
- Start every agent run with a task list generation step
- Each task should specify: inputs, outputs, dependencies (what it blocks / what blocks it)
- Use the TaskCreate/TaskUpdate/TaskList tools to manage the plan
- The plan should be generated from the agent definition, not invented on the fly
- Allow the model to update the plan as it learns (some steps may spawn sub-tasks)

## Principle 5: Validate with hooks, not hope

### What it means
Don't trust that the model will produce correct output. Define expected output schemas for each step and use hooks to enforce them.

### Why it works
Models are probabilistic -- they can produce subtly wrong output that looks correct at a glance. Hooks provide deterministic validation:
- Schema validation catches structural errors (missing fields, wrong types)
- Content validation catches semantic errors (empty results, out-of-range values)
- Hooks run automatically, so validation is never skipped
- Failed validation forces the model to revisit and fix, creating a self-correcting loop

### How to apply it
- Define a JSON schema or validation function for each step's output
- Configure hooks that run after each step completes
- On validation failure, the hook should:
  1. Report which fields/constraints failed
  2. Provide the expected format
  3. Force the model to retry the step
- Common validations: non-empty results, required fields present, values within expected ranges, format matches template

## Principle 6: The real product is encoded expertise

### What it means
The value of an agent is not the code or the prompts -- it's the domain knowledge, judgment, and process encoded within. A domain expert using Claude Code produces better agents than a domain expert working with an engineer, because the expert's tacit knowledge gets directly encoded.

### Why it works
Traditional software development has a lossy translation layer: the domain expert explains requirements to the engineer, who interprets and implements them. Each translation loses nuance. With Claude Code:
- The domain expert encodes their knowledge directly
- Edge cases they know from experience get captured in the action trace
- Judgment calls ("when this happens, do X instead of Y") become explicit rules
- The resulting agent embodies the expert's full process, not a simplified version

### How to apply it
- Have the domain expert (not a developer) walk through the task in Step 2
- Capture their decision points: "I check this field because sometimes it's wrong"
- Encode heuristics as explicit rules in the agent definition
- Include error recovery knowledge: "If the API returns empty, try this alternative"
- The agent should make the same decisions the expert would make
