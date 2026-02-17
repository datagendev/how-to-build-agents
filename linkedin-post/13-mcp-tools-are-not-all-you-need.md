# LinkedIn Post

- **Date**: 2025-10-15T20:25:17.079Z
- **Reactions**: 7
- **Comments**: 0
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7384323502444568576

---

[MCP tools are not all you need]

We’re increasingly seeing the rise of custom tools in our workflow. Unlike most MCPs’ generic tools, the ability to quickly build and deploy purpose‑built tools on top of native MCP tools gives our agents a huge performance boost. 

We recently started documenting ~40 use cases about Datagen in Notion. We wanted a Claude Code sub‑agent that, given a person’s background, can surface the best use cases to showcase. The key is staying grounded in real use cases, so identifying and referencing the most relevant ones is critical. 

But here’s the challenge: how do we identify the most relevant use case? 

We began with Notion MCP’s search and fetch tools. But quickly hit a context wall. Notion’s search only returns a title, URL and short AI summary. The only way for the agent to know whether a use case is relevant is to fetch the full page. After just a few fetches, context bloated and the agent started to hallucinate due to too much irrelevant information. 

The solution: 
We build and deploy a summarizer tool on top of Notion’s fetch tool. It takes a user’s background description and a Notion URL as input, and returns two sentences explaining if that use case is relevant. 

Now, instead of fetching the full page for every result, the agent calls the summarizer after search and only fetches full content when it deems it relevant.  

The result: 
We saw a ~40% drop in context usage and more grounded results. 
And because it’s just a tool in Datagen’s MCP, not a hard‑coded workflow or “another sub‑agent”, we can easily bring our toolset to other agents like Codex and Gemini(especially when your weekly limit hit).

With tools being easy to build and deploy in Datagen, we quickly grew a custom tool library, for example, “Search ICP docs in Notion” with a predefined data_source_url filter to prevent access to other sensitive data, or “enrich user email with LinkedIn link” with built‑in link validation. 

These dedicated tools also let us assign fewer tools (ideally < 5) to each agent with a specific scope. That significantly improves tool calling and the final outcome. 

With agent getting more powerful, we believe many complicated workflows should be abstracted into tool to keep agent architect simple, future-proof while still have ability to execute with proper guardrail.
