# LinkedIn Post

- **Date**: 2025-11-03T21:11:13.304Z
- **Reactions**: 9
- **Comments**: 1
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7391220432336543744

---

How to Know if My LinkedIn Post Works

Yesterday, I was thinking about whether I could better understand if my posts actually bring in any visits and what content attracts people. (In the end, my posts are solely for that purpose. I have no interest in sharing my thoughts with others. I mean, who cares?)

We have PostHog, but to be honest, I have no idea how to use PostHog properly, let alone knowing how to build queries, join it with LinkedIn, and get insights.

But luckily, PostHog has MCP, and I have a LinkedIn MCP installed . So here's what I did:
1) Install PostHog MCP to Datagen.
2) Ask Claude how to use the PostHog MCP tool to get my page views data and analytics.
3) Ask it to check my LinkedIn tool and come up with a way to analyze my post-to-page relationships.

And man, I just got a table that clearly shows me how each post brings in page views. 5 minutes. For a complete newbie like me who has struggled to figure out how to do queries through the PostHog UI. I get good. analysis in attached pic(embarrassing traffic I know). 

With Datagen, I can:
1) Continue to add MCPs without worrying about bloating context and easily get the tools I need through Datagen's tool search.

2) Use not just "tool mode" but "code mode" in Datagen to let it build the code to join potshog mcp tool output and linkedin tool output data before returning back to LLM.  Fast and scalable even you have hundreds of posts.
 
3) Deploy this post-to-view analysis as a custom tool, so next time I can just call it and get results. or my AI agent can either use this tool to suggest content improvements or do intent analysis.

I am kind of surprising how good AI is now, and by providing the right tools, how quickly you can turn any random ideas into real actions in minutes. Wild.
