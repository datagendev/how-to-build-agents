# LinkedIn Post

- **Date**: 2025-08-02T07:26:21.735Z
- **Reactions**: 4
- **Comments**: 4
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7357310778149924864

---

How to Build an FAA Service Difficulty Report Database with Claude

[Background]:
Inspired by Jordan Crawford’s "Build a database from public data in an hour", we tried to follow suit and share our learnings on how to do it with Claude + MCP, so no coding or development environment is needed other than installing MCPs. I will try to share results with very specific data each time, but hopefully we can gradually generate patterns with more examples
All prompts will be shared in the comments, along with sample data. so you can feed it as doc to create your own scraper. 

[Data]
The example for this post is the FAA Service Difficulty Report, a public data source that reports all the difficulty reports for aircraft. 
This data source has been discussed in Jordan's Cannonball GTM to gain insights on aircrafts maintenance and safety.

[MCPs]
1. Supabase MCP: a database MCP to create databases and review SQL (alternative: Neon MCP)
2. Datagen MCP (from us): a Python interpreter tool with MCP access to let Claude write code to integrate with MCP as functions. (Alternative: e2b MCP, which requires providing API documentation and an API key for Supabase)

[Prompt Flow]:
1. Start by asking Claude Opus (or OpenAI o3) “How can I get data from FAA SDR?” 
2. Take the output from step 1 and ask Claude to build and execute code in Datagen MCP. If it fails, ask what it sees and why it fails to build more context. 
→ Get the working scraper and a few sample data points.
3. Take sample data from step 2 as context to let Claude use Supabase MCP to create a table, then use Datagen MCP to build the data pipeline. 
→ Full data posted in Supabase.
4. Verify the result by asking Claude, using Supabase MCP, to get a data summary. 
5. Summarize code and step flow for future use (it's important to include working code from step 3).


[Some learnings]
1. Treat Claude as a development platform instead of an answer engine. Stay away from one huge prompt; start small and iterate.
2. If possible, be specific with the tool you want.
3. Constantly summarize the conversation as a checkpoint (like Claude code's /compact).
