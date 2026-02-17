# LinkedIn Post

- **Date**: 2025-09-30T05:28:59.221Z
- **Reactions**: 12
- **Comments**: 3
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7378662123775655936

---

I think "tools" are going to be the moat for AI agents, not scaffolded AI workflows

Image below is from Voyager AI paper, a well-known work let AI agent explores Minecraft. 

It shows by letting AI agent build and use their own "skill library" significantly enhancing its capabilities (orange vs blue line)

This matches my experience. And surprisingly align well with what we want to do.

Most MCP tools today are like LEGO bricks. Even for the same task, the agent has to re-chain the bricks each time. These tools are generic and lack context for "my" use case. However, what I want is a tool library with context-aware modules built on top of those LEGO bricks that fit my needs.

I think to allow AI agent build and use this "tool library" takes: 
1. Memory:  to know what you need
2. Search:  to get right tool 
3. Sandbox:  to assemble existing tool into custom tools
4. Deployment:  to publish and version tools 
5. Observation:  to fix issues
6. Governance: to auth and assign right tools

This is what we’re building at Datagen: a tool-building platform for AI agents. And by offering it as an MCP, anyone can bring their tool library to any agent platform they want. 

In our view, this portability guarantees the independence of what we build from the LLM providers.

What it means for use cases: 
- Short term: people can easily build individual automations and APIs, and they can use them in tools like Clay or n8n -- Build custom tools

- Mid term: let people plug in their specialized tool sets they built into agents to complete tasks faster and more reliable. -- Use customs tools 

- Long term: AI can take a task and let the agent use Datagen to build and deploy the required tools end to end, even if those tools don’t exist yet 

We still have plenty to build and improve, but it’s been a lot of fun building this with my teammates.
