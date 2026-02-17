# LinkedIn Post

- **Date**: 2025-06-09T20:26:29.109Z
- **Reactions**: 8
- **Comments**: 2
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7337938157763444736

---

Centralized vs Embedded AI
I got pulled into this discussion after seeing Pipedream's (an MCP gateway vendor) recent design decision to only expose instructions(a natural language interface to control their tool) in contrast to typical input arguments of the underlying API.

While I think the major motivation behind their move is to lock in users, it's still interesting to consider whether we should wrap our MCP tool to work like a small embedded AI agent specialized in its respective tool and take instructions from other AI.

As someone who both uses and builds MCPs, I see 4 major issues with embedded AI in MCP tools:

Prompt: Using embedded AI means asking the LLM to guess the optimal prompt for getting results. It's much simpler to provide input arguments directly and let it update based on deterministic error messages feed back loop.

Eval: It's far easier to detect incorrectly typed input parameters than to evaluate the effectiveness of prompts for tool calls.

Reliability: Since most people interact with MCPs through LLM clients, each additional layer of LLM calls introduces more potential points of failure.

Control: Most MCPs are vendor-provided. If vendors wrap their LLM on top of their tool and the LLM wrapper performs poorly, you're bottlenecked by their implementation regardless of how advanced your LLM client model is.

When I use a screwdriver, I don't want its manual to change every time. I want it to be reliable and work as expected, every single time. So if you're building an MCP for your service, don't overthink it. Focus on clear documentation and use case but keep the tool as boring as possible. Delegate tool usage to a centralized AI layer controlled by users

While automation almost feels like a despicable term compared to AI agent, I would focus more on building reliable automation to create truly useful AI applications. I would take 5% failure rate due to missed edge cases than a 10% failure rate on 68% of my common cases every-single-time.
