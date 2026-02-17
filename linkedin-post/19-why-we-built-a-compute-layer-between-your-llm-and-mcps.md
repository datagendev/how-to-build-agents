# LinkedIn Post

- **Date**: 2025-09-15T22:56:06.011Z
- **Reactions**: 12
- **Comments**: 3
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7373489820448260096

---

# Why We Built a Compute Layer Between Your LLM and MCPs

MCPs make observability so easy. Connect to HeyReach, get reply rates. Connect to Supabase, get usage stats. The demos look great.

## Issues with MCPs
But here's where it gets flimsy : What if I want to see which campaign actually brings the most active users?

Now I need data from both MCPs. MCPs don't talk to each other. So Claude ends up copying data between MCP calls, 

Typical Claude + MCPs:
- Call HeyReach MCP → Claude holds campaign data in context
- Call Neon MCP → Claude holds user data in context
- Claude tries to analyze with hardcoded data in prompts
- Context gets bloated, hallucinations creep in
This is where I see many give up and go back to traditional analytical tools.

Sure, you can build pipelines ahead of time and bring all data into one warehouse. But if you are an early team like us still experimenting with tooling, building data pipelines for every data source feels like massive overhead. In the end, we just want answers.

This is where we started dogfooding ourselves.

## The compute layer between LLM and MCPs

Instead of the LLM copying data between MCPs, Datagen is a compute layer between your LLM and MCPs. And instead of asking LLM to directly call  MCP, Datagen ask LLM to create code to "orchestrate MCPs"

Now when I ask "which campaign brought the most signups," Datagen:
1. Writes code to a) fetch data, b) join, dedupe, and calculate conversion rates
2. Returns clean results: "Campaign X: 124 messages, 4 signups, 3.2% conversion"

And because it's code, it's fast, reliable, and most importantly, auditable. 

What makes Datagen even more powfeful is it can automatically deploy our analysis as:
- An API endpoint (for dashboards or Clay like  integrations)
- New MCP tools (so I don't wait 10 minutes in Claude for the same question with just different campaigns in the future)
- Cron jobs (if I want this data synced nightly)

From adding MCPs to deployed workflow. all just by talking to Claude.
(Claude artifact link in comment)

## Building What We Use

We dogfood this almost daily. Every "I wonder if..." becomes a workflow in minutes. (we recently build a discord tool so AI can quickly turn our long discussions into a list of todos and can be sent to Linear with our Linear workflow)

It's nice building for others. But even nicer building something you depend on every day.
