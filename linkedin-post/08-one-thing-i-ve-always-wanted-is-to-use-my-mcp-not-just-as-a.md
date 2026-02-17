# LinkedIn Post

- **Date**: 2025-12-11T18:40:14.421Z
- **Reactions**: 7
- **Comments**: 0
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7404953175520124928

---

One thing I've always wanted is to use my MCP not just as a tool for AI agents, but as a function that can be directly called in code.

Why? 

Yesterday, while preparing my outreach, I used my LinkedIn MCP to pull posts, but Claude Code soon complained that the tool returned too many tokens(50 posts) 

The problem:
- ❌ Token limits blocked my workflow
- ❌ Couldn't process large amounts of data through AI tools
- ❌ Had to rewrite seperate integrations

What if we could use MCP as code instead?

With MCP as code, I could:
- ✅ Save posts locally to offload context
- ✅ Write scripts to clean and process the output
- ✅ Let Claude Code read through saved files at its own pace
- ✅ No need to rewrite another seperate integrations

The solution:

So we built a thin SDK on top of Datagen, an MCP Gateway.
Here's how it works: 
1️⃣ Add as many MCPs as you want on Datagen 
2️⃣ Datagen MCP has searchTools/getToolDetails tools to guide Claude Code on what tools are available and how to use it
3️⃣ Claude Code can use any tools in code through SDK
Example:
from datagen_sdk import DatagenClient 
client = DatagenClient() 
# call MCP as function 
posts = client.execute_tool( 
"get_linkedin_person_posts", {"linkedin_url": lead.linkedin_url}, ) 
# save to local
with open("./linkedin_posts.json", "w", encoding="utf-8") as f: json.dump(posts, f, indent=2)

Benefits: 
1. ✅ Super easy integration:
One client, one credential, like your 1Password. No more copying and pasting API keys or rewriting auth flows/integrations for each project. 

2. ✅ Embedded Tool documentation:
All tool details can be accessed through the getToolDetails tool. No need to feed documentation here and there. Much faster development and less hallucination.

3. ✅ Safer to use in Claude Code: 
Unlike having your credentials in environment variables where your AI agent could potentially write any API to use them, with Datagen, Claude Code can only access the tools you give it and cannot access the raw credentials. 

4. ✅ Run anywhere:
Unlike "Code Mode", the script you have can run at any Python runtime. Can easily integrate with your local files/runtime without spinning up another remote container.

you can find more from our repo: 
https://lnkd.in/gzJy7dbX
