# Agent Examples

Concrete examples of agents built following the 6 principles.

## Example 1: 12-Step Company Enrichment Agent

A production agent that takes a list of company domains and produces enriched company profiles ready for CRM import.

### Job-to-be-done
Given a CSV of company domains, produce enriched profiles with firmographics, tech stack, key contacts, and scoring.

### Step structure

```
Step 1:  Parse input CSV, validate domains, create tmp/input_companies.json
Step 2:  For each company, run Firecrawl scrape -> tmp/scrape_{domain}.json
Step 3:  Extract firmographics (industry, size, revenue) from scrape results
Step 4:  Run LinkedIn company search -> tmp/linkedin_{domain}.json
Step 5:  Extract key contacts (title, role) from LinkedIn results
Step 6:  Run tech stack detection via BuiltWith -> tmp/techstack_{domain}.json
Step 7:  Score each company based on ICP criteria -> tmp/scores.json
Step 8:  Validate all enrichment fields against schema
Step 9:  Merge all data into unified profile per company
Step 10: Generate summary statistics (coverage rates, score distribution)
Step 11: Format output as CRM-ready CSV
Step 12: Post summary to Slack channel
```

### Key patterns demonstrated

- **Script-based outputs**: Each step writes to `tmp/` files. The model never holds all scrape results in context simultaneously.
- **Partitioned processing**: Companies are processed in batches of 10 to avoid context bloat.
- **Schema validation**: Step 8 validates every enrichment field against a predefined schema before proceeding.
- **Skill composition**: Steps 2, 4, and 6 each use dedicated tool-calling skills.

### Agent definition excerpt

```markdown
## Step 2: Scrape company websites

For each company in tmp/input_companies.json:
1. Read the domain from the company record
2. Run: python3 scripts/scrape_company.py --domain {domain} --output tmp/scrape_{domain}.json
3. The script calls Firecrawl MCP tool and saves the full scrape result
4. Verify the output file exists and is valid JSON
5. If scrape fails (timeout, 404), log to tmp/scrape_errors.json and continue

Expected output: tmp/scrape_{domain}.json for each company
Error handling: Log failures, don't block the pipeline
```

## Example 2: HeyReach Review Agent

An agent that reviews HeyReach outreach sequences for quality, personalization, and compliance.

### Job-to-be-done
Given a HeyReach campaign export, review each sequence for quality issues and produce an actionable report.

### How it was developed (the action trace method)

1. **Manual walkthrough**: Opened a HeyReach export, reviewed 5 sequences manually in Claude Code
2. **Captured patterns**: Noticed recurring issues -- generic openers, missing personalization tokens, too-long messages, compliance gaps
3. **Codified rules**: Turned observations into explicit review criteria:
   - Message length < 300 chars for InMails, < 500 for emails
   - Personalization tokens present in first sentence
   - No spam trigger words
   - CAN-SPAM compliance (unsubscribe link present in emails)
   - Follow-up spacing >= 3 days
4. **Built the agent**: Structured as a 6-step review pipeline

### Step structure

```
Step 1: Parse HeyReach export -> tmp/sequences.json
Step 2: For each sequence, extract messages and metadata
Step 3: Run quality checks (length, personalization, spacing)
Step 4: Run compliance checks (CAN-SPAM, LinkedIn ToS)
Step 5: Score each sequence (0-100) with breakdown
Step 6: Generate review report with specific fix recommendations
```

### Key patterns demonstrated

- **Develop by doing**: The review criteria came from actually reviewing sequences, not from a description of what a reviewer should check.
- **Encoded expertise**: The length limits, spacing rules, and compliance checks encode domain knowledge that a sales ops expert knows but rarely documents.
- **Hook validation**: Each sequence review is validated against a schema ensuring all required fields are scored.

## Example 3: Daily Activity Report Agent with Skill Composition

An agent that generates a daily activity report by composing two skills: `/product-analysis` and `/report-generator`.

### Job-to-be-done
Every morning, pull the previous day's product metrics (from PostHog), analyze trends, and generate a formatted report posted to Slack.

### Skill decomposition

**Skill: /product-analysis**
- Pulls metrics from PostHog API
- Computes day-over-day and week-over-week changes
- Identifies anomalies (> 2 standard deviations from 30-day mean)
- Outputs: `tmp/metrics_analysis.json`

**Skill: /report-generator**
- Takes a metrics analysis JSON
- Formats it into a structured report (summary, highlights, concerns, action items)
- Supports multiple output formats (Slack blocks, HTML, Markdown)
- Outputs: `tmp/report.{format}`

### Agent orchestration

```
Step 1: Call /product-analysis with date range = yesterday
        -> produces tmp/metrics_analysis.json
Step 2: Peek at tmp/metrics_analysis.json to check for anomalies
Step 3: If anomalies found, add to high-priority section
Step 4: Call /report-generator with input = tmp/metrics_analysis.json, format = slack
        -> produces tmp/report.slack
Step 5: Post tmp/report.slack to #daily-metrics channel
Step 6: If anomalies found, also post to #alerts channel
```

### Key patterns demonstrated

- **Skill composition**: The agent doesn't do analysis or formatting itself -- it delegates to focused skills.
- **Tight feedback loops**: Each skill can be tested independently. If the report format is wrong, you fix `/report-generator` without touching the agent.
- **Context management**: The metrics analysis is saved to a file. The agent peeks at it to make routing decisions (anomaly check) without loading the full analysis into context.
- **Plan before act**: The agent generates a task list at the start, including conditional steps (anomaly alerting) that may or may not execute.

## Structural Patterns Across Examples

### File organization
All three agents follow the same pattern:
```
tmp/                          # Intermediate outputs (gitignored)
scripts/                      # Helper scripts for tool calls
agent-definition/             # Step files (or inline in agent .md)
```

### Error handling
Every step specifies:
- What success looks like (expected output file, schema)
- What failure looks like (missing file, invalid JSON, empty results)
- How to recover (retry, skip, fallback)

### Testing cycle
All agents were built using the 4-step workflow:
1. Register the agent
2. Manually walk through the task (capture action trace)
3. Codify the trace into the agent definition
4. Test with `/clear` and iterate
