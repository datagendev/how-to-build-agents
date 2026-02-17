---
name: how-to-create-agent
description: Step-by-step guide for building reliable Claude Code agents based on proven principles. Use when the user wants to create a new agent, improve an existing agent, or learn agent-building best practices.
---

# How to Create a Claude Code Agent

## When to use this skill

Use this skill when the user:
- Wants to create a new Claude Code agent
- Wants to improve or refactor an existing agent
- Asks about agent-building best practices
- Mentions "create agent", "build agent", "new agent", or "agent architecture"
- Wants to understand the difference between agents and skills

## Key distinction: Agent vs Skill

- **Agent** = a job-to-be-done. It is the main script that orchestrates a specific workflow end-to-end (e.g., "enrich a list of companies", "generate a daily activity report").
- **Skill** = a reusable capability. It is a function library that any agent can call (e.g., `/product-analysis`, `/report-generator`).
- Compose skills inside agents for modularity and tight feedback loops.

## Prerequisites

Before starting, ensure these CLI tools are installed:

1. **DataGen CLI** -- for deploying and managing agents
   ```bash
   curl -fsSL https://cli.datagen.dev/install.sh | sh
   ```

2. **GitHub CLI (`gh`)** -- for committing, pushing, and managing repos
   ```bash
   brew install gh
   ```

3. **Claude Code** -- the agent development environment
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

**One-time login (must be done in a regular terminal, not inside Claude Code):**
```bash
gh auth login        # opens browser for GitHub OAuth
datagen login        # opens browser for DataGen auth
```

These require interactive browser auth flows. Everything else in this workflow can be done inside Claude Code.

## The 9-step agent creation workflow

Steps 0-5: **Build** the agent locally
Steps 6-8: **Deploy** the agent to DataGen

### Step 0: Identify and prepare the context layer

Before writing any agent logic, help the user discover **what context the agent needs to do the job well**. This is a guided discovery process.

**Ask the user these questions:**

1. **What does "good" look like?** -- Is there a format, template, or example of the ideal output? If yes, capture it as a reference file (e.g., `output-template.md`, `example-report.md`).

2. **What rules or criteria drive decisions?** -- Does the task involve scoring, filtering, categorizing, or judging? If yes, document the criteria (e.g., `icp-criteria.md`, `review-checklist.md`, `grading-rubric.md`).

3. **What domain knowledge is assumed?** -- What would a new team member need to know to do this task? Glossaries, acronyms, product context, org structure -- capture it (e.g., `domain-context.md`, `team-structure.md`).

4. **Are there existing files, folders, or data sources the agent should know about?** -- Point the agent to relevant directories, config files, or data sources it will read from (e.g., `@src/components/`, `@data/customers.csv`).

5. **What are the edge cases and "watch out for" rules?** -- Things the user knows from experience that aren't written down anywhere (e.g., `edge-cases.md`, `known-issues.md`).

**Then organize the context:**

```
context/                              # or inside the agent's directory
  output-template.md                  # what good output looks like
  criteria.md                         # decision rules and scoring
  domain-context.md                   # background knowledge
  edge-cases.md                       # gotchas and special handling
```

The agent definition references these via `@` links:
```
Follow the format in @context/output-template.md.
Score companies using @context/criteria.md.
Watch for issues described in @context/edge-cases.md.
```

**Concrete examples of context layers:**

| Agent | Context files needed |
|-------|---------------------|
| Meeting summary | `summary-guideline.md` (format, what to include/exclude, tone), `example-summary.md` (a good example) |
| Company enrichment | `icp-criteria.md` (scoring rules, field definitions), `field-mapping.md` (CRM field names) |
| Outreach review | `review-checklist.md` (quality standards), `compliance-rules.md` (CAN-SPAM, LinkedIn ToS) |
| Daily report | `report-template.md` (sections, audience), `metric-definitions.md` (what each KPI means) |
| Code review | `style-guide.md` (conventions), `architecture.md` (system design decisions) |

**Why this matters**: Without context layers, the agent either guesses at domain knowledge (unreliable) or the user has to re-explain it every session (tedious). Context files make the expertise persistent, shareable, and updatable independently from the agent workflow.

### Step 1: Look up the latest .md file format for agents and skills

**This step is mandatory. Do not skip it.**

Before writing any agent or skill `.md` file, use the `claude-code-guide` subagent to research the current required format:

```
Task(subagent_type="claude-code-guide", prompt="Research the correct format for Claude Code custom agents defined in .claude/agents/ directory and skills defined in .claude/skills/ directory. What frontmatter fields are required/supported? What is the naming convention? How does discovery and invocation work?")
```

This ensures you use the correct frontmatter fields (`name`, `description`, `tools`, `model`, etc.) instead of guessing. The format may evolve -- always check before creating.

**Key findings to apply:**
- Agent `.md` files require YAML frontmatter with at minimum `name` (lowercase + hyphens) and `description`
- Skills live in `.claude/skills/<name>/skill.md` and are invoked via `/name`
- Agents live in `.claude/agents/<name>.md` and are invoked as subagents via the Task tool
- The `tools` field is an allowlist -- if omitted, the subagent inherits all tools from the parent
- Agents are loaded at session start; restart Claude Code or run `/agents` after adding new ones

### Step 2: Register

1. Run `/agent` to create a new agent
2. Select the project
3. Give the agent access to **all tools** it might need
4. Write a clear scope description -- what job does this agent do?

### Step 3: Develop (the critical step -- don't skip)

1. Run `/clear` to start with a fresh context
2. **Manually walk through the task** in normal Claude Code mode, step by step
3. As you work, pay attention to:
   - Which tools you call and in what order
   - What inputs each step needs
   - What outputs each step produces
   - Where you hit errors and how you recover
4. This produces an **action trace** -- the ground truth for your agent

> This is the most important step. Auto-generating agent definitions from a description produces hallucinated prompts. Prototyping the workflow first captures real tool names, real parameters, and real edge cases.

### Step 4: Update

1. Summarize the action trace from Step 2
2. Structure the agent definition as **indexed step files**:
   - Each step gets a numbered description (Step 1, Step 2, ...)
   - Each step specifies: input, tool(s) to call, expected output, error handling
3. Apply the architecture principles from @.claude/skills/how-to-create-agent/principles.md:
   - Use script-based intermediate outputs (write to `tmp/` files)
   - Define output schemas for validation
   - Set up hooks for quality gates
4. Update the agent `.md` file with the step-by-step definition

### Step 5: Test

> **Important:** If you just created or modified an agent `.md` file, you must restart Claude Code before the agent will be discoverable. Agents are loaded at session start -- changes to `.claude/agents/` are not picked up mid-session.

1. Exit Claude Code and restart with `claude -r` to resume the conversation with the new agent loaded
2. Run the agent on the target task
3. Observe:
   - Does it follow the steps in order?
   - Does it handle errors gracefully?
   - Does it produce the expected output format?
4. Iterate: go back to Step 3 and refine the agent definition

---

### Step 6: Push to GitHub

Once the agent works locally, push it to GitHub so DataGen can discover it.

**If the repo has never been pushed to GitHub:**
```bash
# Initialize git if not already
git init
git add .
git commit -m "Initial commit with agent definition"

# Create a remote repo and push (gh CLI handles everything)
gh repo create <owner>/<repo-name> --private --source=. --push
```

**If the repo already exists on GitHub:**
```bash
git add .claude/agents/ .claude/skills/
git commit -m "Add agent definition"
git push
```

The agent definition lives in `.claude/agents/` -- DataGen auto-discovers any `.md` files in that directory.

### Step 7: Connect repo to DataGen

```bash
# If GitHub App is not installed yet (first time)
datagen github connect

# If GitHub App is already installed, just add the repo
datagen github connect-repo <owner>/<repo-name>

# Verify connection
datagen github status

# Sync to discover agents
datagen github sync <owner>/<repo-name>

# List discovered agents to get the agent UUID
datagen agents list --repo <owner>/<repo-name>
```

### Step 8: Deploy and configure

```bash
# Deploy the agent (creates a webhook endpoint)
datagen agents deploy <agent-id>

# Configure entry prompt, secrets, and notifications
datagen agents config <agent-id> --set-prompt "Your task prompt"
datagen agents config <agent-id> --secrets KEY1,KEY2
datagen agents config <agent-id> --notify-success true

# Run manually to verify
datagen agents run <agent-id> --payload '{"key": "value"}'

# Or set up a cron schedule
datagen agents schedule <agent-id> --cron "0 9 * * *" --timezone "America/New_York"
```

## Architecture principles (summary)

See @.claude/skills/how-to-create-agent/principles.md for the full deep-dive.

1. **Agent = Job-to-be-done, Skill = Capability** -- compose skills inside agents
2. **Develop by doing, not by prompting** -- prototype first, codify second
3. **Context is the enemy (RLM pattern)** -- indexed steps + script-based outputs
4. **Make the model plan before it acts** -- task list with dependency graph upfront
5. **Validate with hooks, not hope** -- output schemas + hook enforcement
6. **The real product is encoded expertise** -- domain knowledge is the differentiator

## Skill composition pattern

For complex agents, break capabilities into skills and compose them:

```
Agent: daily-activity-report
  Uses: /product-analysis (skill)
  Uses: /report-generator (skill)
  Uses: /slack-poster (skill)
```

Each skill handles one capability with a tight feedback loop. The agent orchestrates the skills in sequence, passing outputs between them.

## Script-based output pattern

Instead of asking the model to reason over large tool outputs inline:

```bash
# Bad: tool output floods the context window
result = call_mcp_tool("searchTools", {"query": "gmail"})
# model now carries all of this in context...

# Good: script saves to file, model peeks as needed
python3 scripts/search_tools.py --query "gmail" > tmp/search_results.json
# model reads only what it needs from the file
```

This follows the Recursive Language Model (RLM) pattern: treat context as an external environment, use code to peek/grep/partition/map over data.

## Common pitfalls

1. **Context bloat** -- putting all step definitions inline instead of using indexed step files. The model loses focus when the agent definition is too long.
2. **Hallucinated prompts** -- auto-generating agent definitions from a description without prototyping first. You get plausible-sounding but wrong tool names and parameters.
3. **Skipping the trace step** -- jumping straight to writing the agent definition without manually walking through the task. This is the #1 cause of brittle agents.
4. **Monolithic agents** -- building one massive agent instead of composing smaller skills. Harder to debug, harder to reuse.
5. **No validation** -- hoping the model produces correct output instead of defining schemas and using hooks to enforce them.
6. **Missing frontmatter** -- creating agent/skill `.md` files without the required YAML frontmatter (`name`, `description`, `tools`, etc.). Always run the `claude-code-guide` lookup in Step 1 to get the current format before writing any `.md` files.

## Examples

See @.claude/skills/how-to-create-agent/examples.md for concrete agent examples including:
- 12-step company enrichment agent
- HeyReach review agent
- Daily activity report agent with skill composition
