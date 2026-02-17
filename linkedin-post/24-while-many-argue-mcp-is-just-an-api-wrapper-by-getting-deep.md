# LinkedIn Post

- **Date**: 2025-08-03T09:23:24.416Z
- **Reactions**: 10
- **Comments**: 5
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7357702621274521600

---

While many argue MCP is just an API wrapper, by getting deeper into agent/MCP development, I found two specific benefits that I can hardly find in most API designs. And no, it's not about those primitives like resource, prompts or sampling. it's b/c of their client/server design.

[OAuth Authentication]
Most APIs require static API keys or Bearer tokens. If I build something and share to you, you can't just run it. you need your own account, API key, and secure storage setup. 
In contrast, many remote MCP servers support OAuth to allow users authenticate through URLs instead of managing keys. For example, users can add Linear MCP to Datagen by simply asking Claude: "Help me add Linear MCP to Datagen." We return an auth URL, they log in, done. No API key hunting required. This smooth process is made possible by MCP servers acting as a middleman to handle auth complexity between the client and upstream API providers without relying on client supports.

[Server/client chaining]
Unlike most single-server APIs, MCP servers can also act as clients to other MCP servers, to effectively create this composable middleware. 
For example, Toolhouse can operates as an MCP client to fetch data from other MCP servers, processes it using AI agents, then passes the results back through Claude as an MCP server. Similarly, Datagen MCP lets you turn your MCP servers into Python-callable functions, executing them on our infrastructure and returning calculated results to Claude via the Datagen Server. This chaining behavior is again made possible by the client/server design at the heart of MCP. 

And I think these features are particularly relevant in AI era. with more "software" are shared through prompt, a smooth auth experience is much needed for integrations. The controllable server chaining also is super relevant to optimize the context(only expose relevant context to main agent w/o losing the source integrations).  Maybe b/c I am very limited or ignorant, I actually haven't seen much APIs can provide this level of service. 

While it's still early, simply by getting into the weeds more, I guess I start to see more of the vision from the protocol creators(?).  But TBH, quite thankful for this protocol and what it has enabled. 

ps. recommend latent space and ai + a16z 's podcast with MCP creators. can get more understanding of the origins of many less-known primitives in MCP.
