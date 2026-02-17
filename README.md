# How to Build and Deploy Claude Code Agents

A reference repo for building reliable Claude Code agents and deploying them to DataGen.

## Quick Start

```bash
# Prerequisites (run in a regular terminal, not inside Claude Code)
brew install gh
npm install -g @anthropic-ai/claude-code
curl -fsSL https://cli.datagen.dev/install.sh | sh
gh auth login
datagen login
```

## Build (Steps 0-5)

### 0. Prepare the context layer

Identify reference docs the agent needs -- templates, scoring criteria, domain knowledge, edge cases. Store them in `context/` and reference via `@context/file.md` in the agent definition.

### 1. Look up the latest agent/skill `.md` format

Use the `claude-code-guide` subagent to check the current frontmatter and file structure before writing anything.

### 2. Register the agent

Run `/agent` in Claude Code, select the project, grant tools, and describe the scope.

### 3. Develop by doing

`/clear`, then manually walk through the task in normal mode. Capture the action trace -- real tool names, real parameters, real edge cases. **Do not skip this step.**

### 4. Update the agent definition

Distill the trace into indexed steps. Each step specifies input, tool(s), expected output, and error handling. Write intermediate results to `tmp/` files (RLM pattern).

### 5. Test and iterate

Restart Claude Code (`claude -r`), run the agent, observe, refine.

## Deploy (Steps 6-8)

### 6. Push to GitHub

```bash
git add .claude/agents/ .claude/skills/
git commit -m "Add agent definition"
git push
# Or create a new repo: gh repo create <owner>/<repo> --private --source=. --push
```

### 7. Connect to DataGen

```bash
datagen github connect-repo <owner>/<repo>
datagen github sync <owner>/<repo>
datagen agents list --repo <owner>/<repo>
```

### 8. Deploy, configure, run

```bash
datagen agents deploy <agent-id>
datagen agents config <agent-id> --set-prompt "Your prompt with {{payload.field}}"
datagen agents config <agent-id> --secrets KEY1,KEY2
datagen agents run <agent-id> --payload '{"key": "value"}'
# Or schedule: datagen agents schedule <agent-id> --cron "0 9 * * 1-5" --timezone "America/New_York"
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | A job-to-be-done -- orchestrates a specific workflow end-to-end |
| **Skill** | A reusable capability -- function library any agent can call |
| **Context layer** | Reference docs (templates, criteria, domain knowledge) the agent needs |
| **RLM pattern** | Write tool outputs to files instead of carrying them in context |

## Architecture Principles

1. **Agent = Job, Skill = Capability** -- compose skills inside agents
2. **Develop by doing** -- prototype first, codify second
3. **Context is the enemy** -- indexed steps + script-based outputs
4. **Plan before acting** -- task list with dependency graph upfront
5. **Validate with hooks** -- output schemas + hook enforcement
6. **Encoded expertise is the product** -- domain knowledge is the differentiator

## Repo Structure

```
.claude/agents/         # Agent definitions (auto-discovered by DataGen)
.claude/skills/         # Reusable skill definitions
agent.md                # DataGen SDK + MCP usage rules
linkedin-post/          # LinkedIn content about agent building
agent-demos/            # Demo agent walkthroughs
```
