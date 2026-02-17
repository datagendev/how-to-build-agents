# LinkedIn Post

- **Date**: 2025-12-10T18:35:54.123Z
- **Reactions**: 11
- **Comments**: 15
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7404589695885783041

---

Using Claude Code(CC) + MCP Gateway has probably been my biggest productivity gain recently.

We recently deployed a Claude agent to boost our user email → LinkedIn profile enrichment rate from ~40% to nearly 80%. 

Here's what we did:
We first asked CC to create a subagent with the following logic:
" 
1. Use mcp_linkedin_search_person tool to get LinkedIn URL from email. 
If not found:
2. use our mcp_Posthog_query tool to get user city from IP
3. Include this with email and come up with the best possible query
4. Use mcp_Linkup_search to search for LinkedIn
5. Use mcp_Exa_search if no good results are found
6. Use mcp_Linkedin_profile to validate the LinkedIn URL found
7. If found, update our user_crm table in Neon with mcp_Neon_use_sql"
We then tested and asked CC to optimize the prompt and deploy to Railway as a webhook that can be triggered whenever we have a new signup.

I used 5 different MCPs (LinkedIn, PostHog, Linkup, Exa, Neon) without needing to manage any MCPs individually to avoid context bloat, thanks to using MCP gateway.  I can also easily add or remove servers just through prompts without touching any code or MCP configurations. Way faster iterations.

I see three major benefits of using gateway for agent:

1. Allows MCPs to compound: 
The more MCPs I have, the more contexts are ready to be reached by my agent. Using MCP gateway makes it just a prompt away without context bloat.

2. Much faster agent DevOp: 
We use Claude Agent SDK, basically a deployable Claude Code. Using tools through MCP means I can directly test and optimize in Claude Code's subagent (same context, same tools) instead of running in another dedicated test environment to load my custom tools. During deployment, instead of configuring 5 different MCP auth/configs, I just need one. Life saver. 

It also further allows me to template my agent to only take prompt and model as input. Internally we start to experiment if we can further simplify the whole process to deploy my CC subagent to cloud through a single toml file + cli tool. 

3. Unified retry/rate-limit/error handling middleware: iykyk 

Besides agent development, using gateway also allows me to easily switch between coding agents without worrying about syncing their MCP configs. Having all the MCPs available at the same time also allows for much better synergy to serve my everyday needs. Highly recommend.
