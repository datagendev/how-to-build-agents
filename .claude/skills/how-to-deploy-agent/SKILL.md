---
name: how-to-deploy-agent
description: Step-by-step guide for deploying a Claude Code agent to DataGen. Use when the user wants to deploy, schedule, configure, or manage an agent on the DataGen platform.
---

# How to Deploy a Claude Code Agent

## When to use this skill

Use this skill when the user:
- Has a working agent and wants to deploy it
- Wants to push an agent to GitHub and connect it to DataGen
- Asks about scheduling, configuring, or managing deployed agents
- Mentions "deploy agent", "ship agent", "put agent in production", or "run agent on a schedule"

## Prerequisites (one-time setup in regular terminal)

These two commands require interactive browser auth and **must be run in a regular terminal, not inside Claude Code**:

```bash
gh auth login        # GitHub OAuth -- needed for push/repo creation
datagen login        # DataGen auth -- needed for deploy/manage
```

Everything else below can be run inside Claude Code via Bash.

Install the CLIs if not already present:
```bash
brew install gh                          # GitHub CLI
curl -fsSL https://cli.datagen.dev/install.sh | sh  # DataGen CLI
```

## The deployment workflow

### Step 1: Verify the agent exists locally

Check that the agent definition is in `.claude/agents/`:

```bash
ls .claude/agents/
```

DataGen discovers agents from `.md` files in this directory. If the agent file is elsewhere, move it here.

### Step 2: Push to GitHub

**If the repo has never been pushed to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit with agent definition"

# Create remote repo and push in one command
gh repo create <owner>/<repo-name> --private --source=. --push
```

**If the repo already exists on GitHub:**
```bash
git add .claude/agents/ .claude/skills/
git commit -m "Add agent definition"
git push
```

### Step 3: Connect repo to DataGen

```bash
# Check if GitHub App is already connected
datagen github status

# If not connected yet, install the GitHub App
datagen github connect

# If already connected, just add this specific repo
datagen github connect-repo <owner>/<repo-name>

# Verify it's connected
datagen github connected
```

### Step 4: Sync and discover agents

```bash
# Sync the repo to discover agents
datagen github sync <owner>/<repo-name>

# List discovered agents -- note the agent UUID
datagen agents list --repo <owner>/<repo-name>

# View agent details
datagen agents show <agent-id>
```

### Step 5: Push secrets (if the agent needs API keys)

```bash
# List existing secrets
datagen secrets list

# Push a secret with explicit value
datagen secrets set OPENAI_API_KEY=sk-abc123

# Or pull from your local environment variable
datagen secrets set OPENAI_API_KEY
```

### Step 6: Deploy

```bash
# Deploy the agent (creates a webhook endpoint)
datagen agents deploy <agent-id>
```

### Step 7: Configure

```bash
# Set the entry prompt (what the agent receives when triggered)
# Use {{payload.field_name}} to reference fields from the trigger payload
datagen agents config <agent-id> --set-prompt "Your task targeting {{payload.company}}, {{payload.domain}}"

# Attach secrets the agent needs at runtime
datagen agents config <agent-id> --secrets OPENAI_API_KEY,FIRECRAWL_API_KEY

# Configure PR behavior: create_pr | auto_merge | skip
datagen agents config <agent-id> --pr-mode create_pr

# Set up email notifications
datagen agents config <agent-id> --notify-success true --notify-failure true

# Add recipients
datagen agents config <agent-id> --add-recipient teammate@company.com:OWNER

# View current config
datagen agents config <agent-id>
```

### Step 8: Run or schedule

**Manual run:**
```bash
datagen agents run <agent-id>
datagen agents run <agent-id> --payload '{"companies": ["acme.com", "stripe.com"]}'
```

**Scheduled run (cron):**
```bash
# Every weekday at 9am ET
datagen agents schedule <agent-id> --cron "0 9 * * 1-5" --timezone "America/New_York" --name "weekday-morning"

# List schedules
datagen agents schedule <agent-id>

# Pause/resume/delete a schedule
datagen agents schedule <agent-id> --pause <schedule-id>
datagen agents schedule <agent-id> --resume <schedule-id>
datagen agents schedule <agent-id> --delete <schedule-id>
```

### Step 9: Monitor

```bash
# View recent execution logs
datagen agents logs <agent-id>
datagen agents logs <agent-id> --limit 20
```

## Quick reference (cheat sheet)

| Task | Command |
|------|---------|
| List agents | `datagen agents list` |
| Show agent details | `datagen agents show <id>` |
| Deploy | `datagen agents deploy <id>` |
| Undeploy | `datagen agents undeploy <id>` |
| Run manually | `datagen agents run <id>` |
| Run with payload | `datagen agents run <id> --payload '{...}'` |
| Set prompt | `datagen agents config <id> --set-prompt "..."` |
| Attach secrets | `datagen agents config <id> --secrets K1,K2` |
| Add schedule | `datagen agents schedule <id> --cron "..." --timezone "..."` |
| View logs | `datagen agents logs <id>` |
| Push secret | `datagen secrets set KEY=VALUE` |
| Connect repo | `datagen github connect-repo owner/repo` |
| Sync repo | `datagen github sync owner/repo` |
| Configure MCP | `datagen mcp` |

## Common issues

1. **"No agents found"** -- agent file must be a `.md` in `.claude/agents/`. Run `datagen github sync` after pushing.
2. **"Agent not deployed"** -- must run `datagen agents deploy <id>` before `run` or `schedule`.
3. **"Secret not found at runtime"** -- push the secret with `datagen secrets set`, then attach it with `datagen agents config <id> --secrets KEY_NAME`.
4. **Auth expired** -- re-run `datagen login` or `gh auth login` in a regular terminal.
