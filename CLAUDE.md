## Datagen Python SDK (how to use)

### Purpose

Use the Datagen Python SDK (`datagen-python-sdk`) when you need to run DataGen-connected tools from a local Python codebase (apps, scripts, cron jobs). Use Datagen MCP for interactive discovery/debugging of tool names and schemas.

### Prerequisites

- Install: `pip install datagen-python-sdk`
- Auth: set `DATAGEN_API_KEY` in the environment

### Mental model (critical)

- You execute tools by alias name: `client.execute_tool("<tool_alias>", params)`
- Tool aliases are commonly:
  - `mcp_<Provider>_<tool_name>` for connected MCP servers (Gmail/Linear/Neon/etc.)
  - First-party DataGen tools like `listTools`, `searchTools`, `getToolDetails`
- Always be schema-first: confirm params via `getToolDetails` before calling a tool from code.

### Recommended workflow (always follow)

1) Assume `DATAGEN_API_KEY` is not available until verified; then check if it exists (if missing, ask user to set it)
2) Import and create the SDK client:
   - `from datagen_sdk import DatagenClient`
   - `client = DatagenClient()`
3) Discover tool alias with `searchTools` (don't guess)
4) Confirm tool schema with `getToolDetails`
5) Execute with `client.execute_tool(tool_alias, params)`
6) Handle errors:
   - 401/403: missing/invalid API key OR the target MCP server isn't connected/authenticated in DataGen dashboard
   - 400/422: wrong params -> re-check `getToolDetails` and retry

### Minimal example

```python
import os
from datagen_sdk import DatagenClient

if not os.getenv("DATAGEN_API_KEY"):
    raise RuntimeError("DATAGEN_API_KEY not set")

client = DatagenClient()
result = client.execute_tool(
    "mcp_Gmail_gmail_send_email",
    {
        "to": "user@example.com",
        "subject": "Hello",
        "body": "Hi from DataGen!",
    },
)
print(result)
```

### Discovery examples (don't skip)

```python
from datagen_sdk import DatagenClient

client = DatagenClient()

# List all tools
tools = client.execute_tool("listTools")

# Search by intent
matches = client.execute_tool("searchTools", {"query": "send email"})

# Get schema for a tool alias
details = client.execute_tool("getToolDetails", {"tool_name": "mcp_Gmail_gmail_send_email"})
```

## Agent-Building Philosophy

### Core principles

1. **Agent = Job-to-be-done, Skill = Capability** -- agents are the main script for a specific job; skills are reusable function libraries. Compose skills inside agents for modularity and tight feedback loops.
2. **Develop by doing, not by prompting** -- walk through the task manually in normal CC mode first, capture the action trace, then distill it into the agent definition. Prototype first, codify second.
3. **Context is the enemy (RLM pattern)** -- use indexed step files (not everything inline) and script-based intermediate outputs. Write scripts that export MCP tool results to tmp/ files instead of digesting output inline. This follows the Recursive Language Model pattern: treat context as an external environment, use code to peek/grep/partition/map over it, and let the model revisit data without carrying it all in context.
4. **Make the model plan before it acts** -- require explicit task list generation upfront with dependency graph before execution. This enables parallel work while respecting step dependencies.
5. **Validate with hooks, not hope** -- pre-define expected output schemas for each step. Use hooks to validate output files and force revisits on errors.
6. **The real product is encoded expertise** -- the differentiator is how well you encode domain knowledge, judgment, and process into the agent. Domain Expert + Claude Code > Domain Expert + Engineer.

### 8-step agent creation workflow

**Build (local):**
0. **Context layer**: identify and prepare reference docs (guidelines, criteria, templates)
1. **Register**: `/agent` -> project -> all tools -> describe scope -> create
2. **Develop**: `/clear`, manually walk through the task in normal mode, capture action trace
3. **Update**: summarize trace, update agent .md in step-by-step manner
4. **Test**: `/clear` again, run agent on task, iterate

**Deploy (prerequisite: `gh auth login` and `datagen login` in a regular terminal first):**
5. **Push**: commit agent to git, create GitHub repo if needed (`gh repo create`), push
6. **Connect**: `datagen github connect-repo <owner>/<repo>`, then `datagen agents list`
7. **Deploy**: `datagen agents deploy <id>`, configure prompt/secrets/schedule

### Script-based output pattern (RLM-aligned)

Instead of asking the model to reason over large tool outputs inline:
- Write scripts that call MCP tools and save results to `tmp/` files
- The model can peek at file contents, grep for patterns, or partition data
- This prevents context bloat and provides persistent results for recovery
- Formally backed by MIT's Recursive Language Models research

### Context layer preparation

Before building an agent, prepare the **context layer** -- reference documents that encode domain expertise the agent needs. For example:
- A meeting summary agent needs a `summary-guideline.md` with formatting rules, what to include/exclude, tone, and structure
- An enrichment agent needs an `icp-criteria.md` with scoring rules and field definitions
- A review agent needs a `review-checklist.md` with quality standards

These context files go in the agent's directory and are referenced via `@` in the agent definition. They separate domain knowledge from orchestration logic, making both easier to maintain.
