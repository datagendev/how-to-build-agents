---
title: "Meeting Prep - Chehan Karunaratne"
description: "Claude Code 1:1 session prep with ABM signal agent for xGrowth GTM Engineer"
category: "research"
tags: ["meeting-prep", "claude-code-bootcamp", "agent-ideas", "abm", "xgrowth"]
created: 2026-02-16
updated: 2026-02-16
status: "active"
priority: "high"
---

# Chehan Karunaratne - Meeting Prep

## Meeting Details
- **Date:** 2026-02-17 5:00-5:30 PM CST
- **Google Meet:** https://meet.google.com/ajz-sccb-vfp
- **LinkedIn:** https://www.linkedin.com/in/chehan-karunaratne

## Profile
- **Title:** GTM Engineer - ABM & AI @ xGrowth
- **Location:** Sri Lanka
- **Followers:** 939 | Connections: 937
- **Bio:** "I have a lot of 'let me help you' energy, probably why I'm knee-deep in tech and customer service."

## Career History (career pivot in progress)
- GTM Engineer - ABM & AI @ xGrowth (2026 - present, VERY NEW)
  - "Build and iterate Clay workflows, building account-intel automations, and prototypes AI tools"
- Head of Sales and Operations @ Studyingermany.lk (2024 - present)
- Business Development Specialist @ Fit4Travel (2024 - 2026)
- Appointment Setter/Cold-calling @ LoviTech.lk (2023 - 2024)
- Customer Service Officer @ British Council, Sri Lanka (2022 - 2023)

## Skills & Certifications
- **Skills:** Anthropic Claude, Clay, ABM, Python, Automation, Data Scraping, Vibe Coding, HubSpot, CRM
- **Certs:** Clay Outbound Automation Certification, GTM Engineering (StackOptimise, Nov 2025)

## LinkedIn Activity Analysis

### Posts: Almost none (2 original posts)
- Clay certification announcement (34 reactions)
- New job announcement (51 reactions)
- Not building personal brand yet

### Comments: Aggressive resource collector (49 comments)
- "crashcourse" on Cody Schneider's Claude Code GTM guide (Feb 5)
- "dossier" on Tanay Mishra's AI Researcher tool (Feb 4)
- "APPLY" on Tanay Mishra's Claude Code workshop (Jan 30)
- "BOOK" on Sam Bhagwat's AI agent book (Jan 28)
- "CRASH" on Tim Yakubson's Clay crash course (Jan 27)
- "CRM Enrichment certification walkthrough" on Tim Yakubson (Jan 22)
- "SLACK" on Tim Yakubson's Slack scraping for leads (Jan 19)
- "AGENT" on Kirke Mannnik's GTM Claude + Gemini agents (Jan 11)
- "70" on Brigitta Ruha's outbound automation post (Dec 31)
- "COLD" on cold email design post (Dec 30)
- "REPLY RATE" on Hans Dekker's AI email scoring agent (Oct 8)
- "GTM" on Michael Edwards' GTM orchestration system with Sonnet (Oct 27)
- "LLM" on LLM-driven traffic growth (Oct 25)

**Pattern:** Consuming everything GTM engineering + Claude Code + Clay. In rapid learning mode for his new role at xGrowth.

## Conversation History (HeyReach)

**You:** Standard Claude Code bootcamp offer
**Chehan:** "Hi Yu-Sheng, Yes, I am very much interested"
**You:** Sent cal link
**Chehan:** "Thank you so much, I have booked some time for next Tuesday"
**You:** Asked if he's used Claude Code
**Chehan:** "Yes, I created a CRM using it recently"
**You:** Clarified this is about custom agent building, not vibe coding. Asked if he has an agent in mind.
**Chehan:** "Actually what i have in mind is creating some sort of agent to look for AI signals, like looking for signals in ABM marketing (basically using Signal Base or something like that). that's something i've been thinking about"

## Key Signals
- Brand new in GTM Engineer role - needs to deliver results fast
- His JOB DESCRIPTION is literally "building account-intel automations and prototypes AI tools"
- Has a specific agent idea ready (ABM signals)
- Built a CRM with Claude Code - has technical capability
- Clay certified - understands enrichment workflows
- Career pivoting from traditional sales into GTM engineering
- Most ready for a hands-on build session

## Agent Idea: ABM Account Pulse Monitor

### What He Asked For
"Creating some sort of agent to look for AI signals, like looking for signals in ABM marketing (basically using Signal Base or something like that)"

### The Agent

**Schedule:** Daily 6AM (ambient, per account)

For each target account on the ABM list, the agent builds and maintains a living dossier by running parallel research tasks.

### Architecture: Parallel Tasks Per Account

```
Agent receives: "Acme Corp" (one account)
    |
    +-- Task("Events research")         <- funding, launches, partnerships, conferences
    +-- Task("Job post research")       <- tech stack signals + pain language from jobs
    +-- Task("People research")         <- LinkedIn stakeholder map + their recent activity
    +-- Task("Competitor research")     <- what vendors they use/evaluate
    +-- Task("Pain signal research")    <- G2 reviews, complaints, forum posts
    |
    all run in parallel, each saves to:
    |
    tmp/abm-signals/acme-corp/
    ├── events.json
    ├── jobs.json
    ├── people.json
    ├── competitors.json
    └── pain.json
    |
    v
    Main thread reads all files
    -> Cross-domain reasoning + signal scoring
    -> Updates persistent account dossier
    -> Highlights what changed since last scan
```

### Account Context Layers (persistent dossier)

#### Events Timeline (`events.md`)
- Funding rounds, leadership changes, product launches
- Conferences (speaking, sponsoring, attending)
- Partnerships, acquisitions, office expansions/layoffs
- Creates outreach timing windows

#### Tech Stack (`stack.md`)
- CRM, marketing automation, outbound tools, data/analytics
- Scraped from job posts + website
- **Changes tracked over time:** "Snowflake appeared in job posts this month" = investing in data

#### People Map (`people.md`)
- Decision makers, champions, influencers
- Tenure tracking (new hire < 90 days = trigger)
- LinkedIn activity (what they post/comment about)

#### Pain Signals (`pain.md`)
- Job post language: "fix", "broken", "manual", "migrate", "replace"
- G2/Glassdoor reviews, Reddit/forum complaints
- Employee LinkedIn posts complaining about tools

#### Competitor Intel (`competitors.md`)
- Current vendors (from jobs, website, BuiltWith)
- Vendor engagement on LinkedIn (stakeholders liking competitor posts)
- Contract timing if available

#### Engagement History (`engagement.md`)
- Emails sent/replied (from outbound tools)
- Website visits, content consumed
- LinkedIn touches, meeting history

### Data Sources Per Task

| Task | API Sources |
|---|---|
| Events | Web search (funding, hires, news), LinkedIn company posts |
| Jobs | Web search (job postings), parse tech requirements + pain language |
| People | LinkedIn MCP: search_linkedin_person, get_linkedin_person_data, get_linkedin_person_posts |
| Competitors | Web search (vendor mentions), BuiltWith/Wappalyzer, job post tool requirements |
| Pain | Web search (G2 reviews, Glassdoor, Reddit), LinkedIn stakeholder posts |

All available now via DataGen: web_search, LinkedIn MCP, Firecrawl MCP.

### Cross-Domain Reasoning (the agent layer)

The main thread connects dots across tasks:

```
Existing context:
  - Using HubSpot (from stack, detected Dec)
  - VP Marketing "Sarah Chen" joined 45 days ago (from people)
  - Posted negative G2 review about HubSpot reporting (from pain, Jan)

Today's new signal:
  - Job post: "Marketing Operations Manager - Salesforce experience required"

Agent reasoning:
  "Acme Corp posted a Salesforce job while currently on HubSpot. Combined with
   their negative G2 review about HubSpot reporting (Jan) and new VP Marketing
   (joined 45 days ago, likely evaluating tools), this strongly suggests a
   CRM migration is underway. HIGH INTENT - reach out to Sarah Chen
   referencing migration support."
```

Without accumulated context, that job post is just a job post. **With context, it's a story.**

### Signal Scoring
- **Single signal** = noise, log and monitor
- **2 signals in a week** = warming, add to watch list
- **3+ signals in a week** = high intent, act today
- **Signal velocity** tracked over time: "went from 0 to 4 signals this week"

### Daily Digest Output
```
HIGH INTENT (act today):
  Acme Corp: New VP Marketing (45d) + Salesforce job post + negative HubSpot
  review. Likely CRM migration. Reach out to Sarah Chen.

WARMING (watch this week):
  Beta Inc: First hiring signal in 60 days (data engineer role). Monitor.

BASELINE (no change):
  43 accounts with no new signals
```

### Why Not 6sense/Bombora/SignalBase
- $30-50K/year enterprise tools - xGrowth probably can't justify for each client
- Black-box scoring - you don't see what triggered the signal
- This agent shows actual evidence: "here's the job post, here's the LinkedIn post"
- Transparent, customizable, fraction of the cost
- Chehan can build it himself and understand every piece

### Demo Plan for the Session

1. Pick one of xGrowth's actual target accounts
2. Show the parallel Task architecture in Claude Code:
   - Spawn 5 Tasks simultaneously (events, jobs, people, competitors, pain)
   - Each saves results to tmp/abm-signals/{company}/
3. Read the raw results together
4. Show AI synthesis: cross-domain reasoning, signal scoring
5. Build the account dossier live
6. "Now imagine this runs every morning at 6AM on all 50 accounts"

### The Pitch

"You told me you want ABM signals like SignalBase. Here's how we build it: an agent that watches each target account across 5 dimensions - events, jobs, people, competitors, and pain signals - all in parallel. It builds a living dossier that gets smarter over time. When it detects 3+ signals in a week, it alerts you with the evidence and a recommended outreach play. It's like having a 6sense that costs nothing and shows you its work."

## Session Strategy
1. He has the clearest agent idea - go straight into building
2. He's technical enough (built CRM, Clay certified) for hands-on
3. Show the parallel Task pattern in Claude Code - this teaches agent architecture
4. Use a real xGrowth target account for the demo
5. The dossier concept will resonate - his job is literally "account-intel automations"
6. Frame the transition: "Claude Code for prototyping -> DataGen for daily deployment"
7. Back-to-back with Saurabh at 5:30 - keep energy high, this session should be the most action-packed
