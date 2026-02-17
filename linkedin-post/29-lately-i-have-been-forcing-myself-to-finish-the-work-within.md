# LinkedIn Post

- **Date**: 2025-07-14T08:36:04.885Z
- **Reactions**: 7
- **Comments**: 2
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7350442954106228736

---

Lately, I have been forcing myself to finish the work within Claude + MCPs. 
Not to save a few clicks, but because completing work end-to-end in Claude + MCPs allows the whole process to be replicated and scaled without external dependencies simply by packaging the conversation into a markdown file. This mirrors the pattern I have seen in Claude Code's /command and similar approaches. 

But I kept hitting a major limitation: large context exchanges between MCP tools. 
Even just pushing a few dozen rows from Apify to Supabase causes Claude to puke [me as a proud broke Pro user] . 
Here's the typical context flow running into this issue: 
1) User asks to save Apify data to Supabase 
2) Claude calls Apify tool with massive data payload in response 
3) Claude ingests all data (heavy input tokens) 
4) Claude generates full SQL insert statements (heavy output tokens) 
5) Supabase returns simple confirmation 
Step 3 and 4 waste millions of tokens , produces unreliable results, runs extremely slow, and often crashes the workflow like a segmentation fault.

Our [tentative] solution: Build "bridge tools" between MCP tools. 
Instead of Claude memorizing and rewriting data, it calls a dedicated tool to handle the data transfer between Apify and Supabase(step 2 to 4). 
The updated flow: 
1) User makes request 
2) Claude calls Apify-to-Supabase tool (minimal tokens) 
3) Tool returns success message and data location 
This is token efficient, deterministic, fast, and transforms Claude from data messenger to orchestrator with extended working horizons. 

The challenge now is how to build these tools efficiently.
There are many possible approaches. We're working on one too.
