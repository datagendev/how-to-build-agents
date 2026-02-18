---
layout: default
title: How I'd Sell HR Software to SMBs Using Clay
---

# How I'd Sell HR Software to SMBs Using Clay

*The Glassdoor signal your competitors can't see.*

---

Every HR software rep works the same playbook: pull a list of companies by size and industry, blast them with "streamline your HR operations" emails, and hope someone bites. The problem? So does every other rep selling Rippling, Gusto, BambooHR, and Zenefits. Same list. Same message. Same inbox graveyard.

What if you could find the companies whose employees are *already complaining* about their HR systems -- publicly, on Glassdoor -- and reach out with a message that references the exact pain they're experiencing?

That's GTM alpha. And here's how to build it in Clay.

## The Signal: Glassdoor Pain Reviews

Most intent data vendors track funding rounds and job changes. Everyone sees those signals. They're table stakes now -- a "congrats on the funding" email is background noise.

But Glassdoor reviews? Nobody's systematically mining those for sales signals. When an employee at a 200-person company writes "payroll is always late" or "our benefits portal looks like it was built in 2003," that's a buying signal hiding in plain sight.

The insight: **the company doesn't know they're broadcasting their HR pain to the world. You do.**

## The Enrichment Chain

Here's how to stack signals from "could buy" to "needs it now":

**Layer 1 -- Base list (who could buy)**

Import companies from LinkedIn: software companies, 50-500 employees, United States. This is your TAM. Thousands of companies. Too many to work manually, too broad to email blindly.

**Layer 2 -- Fit signal (who matches your ICP)**

Enrich with firmographics: filter to companies that recently raised Series A or B (they're scaling fast, HR pain increases with headcount). Use Clay's waterfall enrichment to pull funding data from multiple providers -- if Clearbit misses it, Owler catches it, then Crunchbase fills gaps.

**Layer 3 -- Timing signal (who needs it *right now*)**

This is where it gets interesting. Add a Claygent column with this prompt:

> "Search Glassdoor for this company. Find employee reviews from the last 12 months that mention HR systems, payroll, benefits, onboarding, or time tracking. Return any negative mentions with the review date and a one-sentence summary."

Clay's AI agent scrapes Glassdoor, reads the reviews, and returns structured data. Companies with 3+ negative HR-related reviews in the past year? Those are your hot accounts.

**Layer 4 -- Context signal (what to say to them)**

For each hot account, add another AI column:

> "Based on these Glassdoor review excerpts, identify the specific HR pain point (payroll accuracy, benefits access, onboarding speed, or time tracking). Output the pain category and a one-sentence summary I can reference in an email."

Now you don't just know *who* to email -- you know *what* to say.

## The Email That Writes Itself

With four layers of enrichment, the personalized email practically assembles itself:

> {% raw %}{{First Name}}{% endraw %} -- I was looking into {% raw %}{{Company}}{% endraw %} and noticed some of your team has mentioned challenges with {% raw %}{{pain category}}{% endraw %} on public review sites.
>
> This is actually one of the most common issues we see at companies going through the growth phase you're in ({% raw %}{{employee count}}{% endraw %} people, Series {% raw %}{{funding round}}{% endraw %}). When {% raw %}{{specific pain summary}}{% endraw %}, it usually means the HR stack hasn't scaled with the team.
>
> We've helped companies like [similar customer] fix this in under two weeks. Worth a 15-minute look?

That's not a cold email. That's a warm email to someone who doesn't know you've been listening.

## The ROI Math

Let's compare the two approaches:

**Manual research:**
- Find a company on LinkedIn: 2 min
- Check their Glassdoor page: 5 min
- Read through reviews for HR mentions: 5 min
- Write a personalized email: 5 min
- **Total: ~17 minutes per prospect**
- In a full day, you work maybe 25 accounts

**With Clay:**
- Import 500 companies: 2 min
- Run enrichment chain (all four layers): 15 min
- Filter to hot accounts with HR pain: instant
- Generate personalized email drafts: 5 min
- **Total: ~22 minutes for 500 accounts, producing 30-50 qualified hot leads**

That's roughly **40 hours per month** of manual research eliminated per rep -- the same number Oyster reported after implementing Clay for their intent-based outbound.

And the quality is higher. You're not guessing who has HR pain. You're finding companies that are publicly broadcasting it.

## Why This Signal Has a Shelf Life

Here's the thing about GTM alpha: it expires. Right now, almost nobody is systematically mining Glassdoor for outbound signals. That means you have a window.

Once more reps figure this out -- and they will -- the "I noticed on Glassdoor" email will become as generic as "congrats on the new role." The advantage goes to whoever builds the system first and starts compounding their signal library.

Clay calls this the "expiration date" problem. Every tactic that works today gets copied and commoditized. The companies that win long-term aren't the ones who find one good signal -- they're the ones who build a *system* for continuously discovering new ones.

## Bottom Line

Stop competing on the same intent signals everyone else is watching. The companies whose employees are complaining about HR on Glassdoor don't show up in any intent data platform. They show up in Clay, if you know where to look.

The playbook: import your TAM, enrich for fit, mine Glassdoor for pain signals, and let AI draft the outreach. 22 minutes instead of a full day. Better targeting, better personalization, better results.

---

*[Clay](https://www.clay.com) gives you access to 100+ data providers and AI-powered enrichment in one platform. Try it free and build your first signal chain.*

---

[Back to Clay Playbooks](/how-to-build-agents/clay/)
