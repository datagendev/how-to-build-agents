# LinkedIn Post

- **Date**: 2025-10-09T04:06:34.038Z
- **Reactions**: 6
- **Comments**: 1
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7381902872965419008

---

[Datagen Demo] Use Datagen to automatically send LinkedIn experts' latest posts to our Slack channel

This one’s a really simple automation, but nice to have.
We have a small(but growing) list of MCP voices we want to track. Every day, we pull their latest LinkedIn posts and send the summaries to a Slack channel so the team can stay in the loop without checking manually.

Unlike most automation platforms, Datagen doesn’t have built-in app integrations(we are working on it).

Instead, anyone can add any MCP they want. Once added, the integration is available to you without you need to worry about authentication and documentation to know how to use it. It's all written in MCP. 

We simply ask Claude to add google Sheet MCP and Slack MCP to Datagen(I use Klavis AI (YC X25)'s MCP here) with the respective server url 

Then ask Claude to: 
1️⃣ Find our my Google Sheet (ID: <google_sheet_id>)
2️⃣ Check if there’s a new post
3️⃣ Push the summary to Slack (<slack_channel_id>)
4️⃣ Update the sheet so it won’t send duplicates
5️⃣ Deploy and Schedule it to run daily at noon

Behind the scenes, DG + Claude take care of:
* MCP authentication
* Integrating MCPs into code
* Code to chain up these services and find out latest posts
* Deployment + scheduling

Unlike n8n or Zapier (which are limited to curated integrations), Datagen connects directly with any MCP. This unlocks access to a rapidly growing ecosystem that most automation platforms don't support — like DeepWiki for GitHub repo understanding or Browserbase for scalable browser automation.

One thing worth emphasizing:
Datagen uses LLMs to write code that incorporates MCPs — not to run them.
So automations are deterministic, fast, and cheap (similar to Cloudflare’s recent “code mode”).

A small learning from this automation:
Handling user-defined data (like Google Sheets) can be tricky the first time because of unknown schemas. Agentic loops usually solve it, but we’re making that process more reliable.

ps. you can learn more from this automation by asking Claude to explain workflow : 1f74e803-93f1-46a8-8414-804ac3940a6c.( a public one) 
B/c it would provide complete context to Claude about this workflow, you can easily ask Claude to explain or modify it to whatever you want, like "instead of sending post, please research some interesting perspective for this post and send to my slack". ( after you add Datagen MCP)
