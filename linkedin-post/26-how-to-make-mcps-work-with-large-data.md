# LinkedIn Post

- **Date**: 2025-07-25T07:20:49.819Z
- **Reactions**: 15
- **Comments**: 4
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7354410283068518401

---

How to make MCPs work with large data

TL;DR: Use code.

Say you use MCP to scrape Google Maps data from Apify MCP, and now you want to save it to Supabase for analysis. Before you realize it, you get hit with "your new limit starts at 4am tomorrow" while transferring just 200 rows of data due to the number of tokens it requires to let the LLM copy and paste it.

In contrast, if you simply ask Claude to write code to pass data from Apify to Supabase, those same 20 tokens of code can now scale to handle thousands of rows without adding any additional tokens.

However, here's the problem: even if you have Apify MCP and Supabase MCP, Claude still can't access them through code. It typically requires heavy investment in context engineering like providing additional API docs, including API output examples, and handling separate authentication for your API keys/tokens (let alone all these different API designs like GraphQL vs REST).

But what if LLMs could use MCP in code just like they do in context? From this question, we started to build a code execution tool that can convert MCP into Python functions. So now your MCP can not only provide context to the LLM but can also be used by the LLM as code.

The video below shows how Claude easily transfers 300K tokens of data with just 2K tokens of code from Apify to Supabase. No more context blow up, no additional API docs, no separate auth flow, no another MCP server — just your original MCPs + our code execution tool.

What this unlocks is that now you can:
1) Scrape anything you want on the internet and save it into your database( Apify <-> Supabase MCP)
3) Enrich them in bulk (Supabase <-> Fullenrich MCP)
4) Push newly qualified lead into CRM (Supabase <-> Hubspot MCP)
5) Create email campaigns from your CRM (Hubspot <-> Smartlead MCP)
All can be done in Claude + few MCPs in minutes without writing any codes yourself.

I always believe the real power of LLM + MCP is not controlling a single server with natural language, but allowing the LLM to orchestrate across all your data that is scattered in silos and quickly turn your ideas into results. 

And I think by allowing MCP to be used both in context and code can fully unlock this potential.
