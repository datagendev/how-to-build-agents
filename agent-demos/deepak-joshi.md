---
title: "Meeting Prep - Deepak Joshi"
description: "Claude Code 1:1 session prep with agent ideas for Scale Campaigns / Stamina GTM Engineer"
category: "research"
tags: ["meeting-prep", "claude-code-bootcamp", "agent-ideas", "cold-email", "instantly", "clay"]
created: 2026-02-16
updated: 2026-02-16
status: "active"
priority: "high"
---

# Deepak Joshi - Meeting Prep

## Meeting Details
- **Date:** 2026-02-17 2:30-3:00 PM CST
- **Google Meet:** https://meet.google.com/rfj-bqpa-ioy
- **LinkedIn:** https://www.linkedin.com/in/deepak--joshi

## Profile
- **Title:** Head of GTM @ Stamina | Founder @ Scale Campaigns | Claymaker @ Clay
- **Location:** India
- **Followers:** 2,968 | Connections: 2,822
- **Stack:** Apollo -> Clay -> Instantly (classic outbound)
- **Scale:** Sends 1M+ outbound emails per month across agencies, SaaS, marketplaces

## Career History
- Head of GTM @ Stamina (2025 - present)
- Founder @ Scale Campaigns (2024 - present) - his own outbound agency
- Claymaker @ Clay (2024 - present) - affiliate/partner with referral link
- Growth @ HireQuotient (2022)
- Marketing Manager @ Pixis (2021-2022) - led team of 5+
- Entrepreneur in Residence @ Zoutons.com (2021)
- Associate @ ZS (2020-2021) - healthcare product launch
- Interns at Udaan.com, Ramco Cements

## Skills
Cold Emails, Cold Outreach, Outbound Marketing, Email Infrastructure, LinkedIn, Demand Generation, Growth Hacking, Email List Building, Sales Prospecting, Lead Generation, Copywriting, SEO

## LinkedIn Activity Analysis

### His Posts: Practitioner content with case studies
- Writes about cold email frameworks, campaign metrics, prospecting techniques
- Gets 10-70 reactions on original posts
- Detailed tactical content (13 cold email rules, targeting via Slack/Facebook/LinkedIn groups)
- Key post (Jan 7, 2026): "I've been testing a bunch of these new AI cold email tools. They're not good. Like... not even close. But here's the thing nobody wants to admit - They COULD be." - Sees AI coming but hasn't found good solutions yet.

### His Comments: Resource collector
- Almost every comment is a keyword trigger to get free resources
- "APPLY", "Playbook", "Free", "Course", "Gem", "Intro", "email"
- Actively collecting cold email playbooks, tools, frameworks from other practitioners
- Follows: Tanay Mishra (Claude Code), Tomer Levi (email infrastructure), Taylor Haren (deliverability), Aamir Bajwa (outbound), Nathan Latka (founders)

## Conversation History (HeyReach)

**You:** Standard Claude Code bootcamp offer
**Deepak:** "What's the catch?"
**You:** Explained the platform angle - show people how to build agents, learn what agents are useful
**Deepak:** "Sure that works happy to chat"
**You:** Sent cal link + asked if he's used Claude Code
**Deepak:** (no reply to the Claude Code question)

## Key Signals
- Skeptical/evaluative - "What's the catch?" as first response
- Likely hasn't used Claude Code (didn't reply to that question)
- Deep expertise in cold email infrastructure at massive scale
- Clay partner - he won't leave Clay, agent must complement it
- His Jan 7 post shows he's thinking about AI in cold email but hasn't found the right approach
- Runs his own agency (Scale Campaigns) - efficiency = more clients = more revenue

## Agent Idea: Deliverability Drift Detector

### The Problem
At 1M emails/month with 30+ sending domains, deliverability degradation is the silent killer. A domain slowly dies over days before anyone notices. By the time open rates visibly drop, the damage is done - domain reputation burned, weeks of warmup needed for replacement.

Nobody checks 30 domains every 6 hours. Instantly shows current metrics but doesn't tell you WHY something is degrading.

### The Agent

**Schedule:** Every 6 hours (ambient, always running)

**Agent workflow:**
1. Pulls sending metrics from Instantly across all domains/campaigns (open rate, bounce rate, spam complaints)
2. Compares against each domain's own 7-day rolling baseline (not industry benchmarks - its own history)
3. Detects **drift** before it becomes a crisis
4. When drift detected, runs diagnostic investigation tree
5. Pushes to Slack with diagnosis + recommendation

### The Investigation Tree (Why This Is Agent-Worthy)

When drift is detected on a domain, the agent runs a conditional diagnostic:

```
Domain X open rate dropping
|
+-- Step 1: Volume check (Instantly API)
|   "Did sending volume change on this domain in last 7 days?"
|   -> Volume spiked 30%+ = likely warmup threshold exceeded
|
+-- Step 2: Campaign isolation (Instantly API)
|   "Which campaigns run on this domain? Is one dragging it down?"
|   -> Per-campaign metrics on this domain
|   -> Campaign ABC bouncing 8% while others at 1% = bad list
|
+-- Step 3: Content change detection (Instantly API)
|   "Did any campaign copy change around when drift started?"
|   -> Copy changed 2 days before drift = spam filter trigger
|
+-- Step 4: List source correlation
|   "Were new leads added to campaigns on this domain recently?"
|   -> New batch + bounce rate climb = bad list source
|
+-- Step 5: Cross-domain comparison
|   "Are OTHER domains also drifting?"
|   -> All drifting = system-wide (content, list, ESP)
|   -> Only this domain = domain-specific (reputation, blacklist)
|
+-- Step 6: Infrastructure check (DNS/blacklist API)
|   Check SPF, DKIM, DMARC, Spamhaus, Barracuda
|
+-- Step 7: Synthesize diagnosis
    Multi-factor root cause analysis with confidence level
```

### Example Output

"Domain acme3.com started drifting Tuesday. Most likely cause: Campaign 'Healthcare CIOs' added 2,400 new leads Monday from Apollo list. That campaign's bounce rate is 6.2% vs 1.1% average across other campaigns on this domain. Recommendation: pause that campaign on this domain, verify the list, redistribute to a healthier domain while acme3.com recovers."

### Why Not n8n/Clay/Instantly

- **Instantly** shows metrics but doesn't track drift patterns or correlate causes
- **n8n** could poll metrics but can't reason about "what changed that caused this"
- **Clay** enriches contacts, not infrastructure health
- The investigation path is **conditional** - depends on what you find at each step
- Multi-factor reasoning: "Volume up 20% AND new list AND one campaign bouncing" = agent weighs together
- Natural language diagnosis with recommendations, not just threshold alerts

### Data Sources

| Check | Source | What we pull |
|---|---|---|
| Volume history | Instantly API | Daily sends per domain, 14-day window |
| Campaign metrics | Instantly API | Per-campaign open/bounce/reply per domain |
| Content changes | Instantly API | Sequence versions + timestamps |
| Lead additions | Instantly API | When leads added to campaigns |
| Cross-domain health | Instantly API | All domains' metrics for comparison |
| Blacklist status | MXToolbox / web scrape | Domain listed? |
| DNS records | DNS lookup | SPF, DKIM, DMARC valid? |

### Why He'd Want This
- Each dead domain costs real money (new domain + 2-4 weeks warmup)
- His Jan 7 post about Gmail AI spam filters = deliverability is top of mind
- At 30+ domains, manual monitoring is impossible
- Insurance that runs silently, only alerts when something needs attention
- Complements Clay (list building) + Instantly (sending) - fills the intelligence gap

### The Pitch

"Clay is your enrichment engine. Instantly is your sending engine. This agent is your intelligence engine. It watches all 30 domains 24/7 and tells you not just WHAT is degrading, but WHY - and what to do about it. Before you even notice the open rate drop."

## Session Strategy
1. Expect skepticism - he asked "what's the catch?" upfront
2. He may not have Claude Code installed - be ready for a demo-only session
3. Lead with his pain: "You send 1M emails/month. How do you monitor domain health today?"
4. Show the investigation tree concept - the conditional reasoning is what differentiates from dashboards
5. Position as complementary to Clay + Instantly, not a replacement
6. If he pushes back: "When was the last time a domain died before you caught it?"
