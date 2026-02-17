# LinkedIn Post

- **Date**: 2026-01-08T18:16:06.602Z
- **Reactions**: 22
- **Comments**: 5
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7415093963163873280

---

It’s getting clear that Claude Code is not just another coding assistant, but an agentic OS layer on top of my personal computer 

*Coding Agent vs Personal OS*
When treating Claude Code as a coding agent, it’s the assistant serving the software I am creating. But when I use Claude Code as my personal OS, the agent becomes the first-class citizen. My docs and my software are now serving my Claude Code agent to help it finish tasks easily.

A few tips I’ve found useful when building CC as my OS:

1. Give it a clean file structure:
I treat file structure as my context scaffolding. I typically co-iterate it along with CLAUDE.md. A good file structure improves agentic search and results in better context.

2. Give it (many) granular, modular tools:
I’ve found that small tools empower the agent to easily mix and match through prompting, instead of modifying a huge end-to-end workflow. I use our MCP gateway to integrate MCP tools and wrap them into python script as code for scale and efficient token usage. (I prefer this over giving agent my api credentials and rewrite each integrations)

3. Give it a memory hook:
I treat this as a bridge between sessions. I use bead at the moment.

4. Pair it with a database:
While .md files are handy, I’ve found them hard to scale. no indexing, no easy querying, and no built-in ACID to avoid racing when running multiple agents. Neon is my go-to.

5. Build determinism through a harness
For example, I typically use commands to trigger agents or skills instead of relying on model to guess. This brings certainty. The same applies to hooks.

A few observations:

Obs1: I Want More Tools, Not Less
I only use the Context7 MCP when using Claude Code as a coding agent, but I find myself using a lot of MCPs when I use Claude Code as a personal OS. I want almost everything I’ve used to be available to CC (Gmail, Calendar, PostHog, Neon, Firefly, etc.). These tools are like nodes, and CC is the tissue that interconnects them. not just context compounding, tool compounding too (literally n(n-1)).

Obs2: SaaS is here to stay but likely different
I have no interest in “vibe-coding” another SaaS. If anything, using CC as a personal OS makes me want to buy more software. I’d rather use Gamma for PPT than tune a crappy PPT skill that can’t even align fonts properly. That said, the product needs to be API-first (I don’t use Granola for this reason). I also feel a new type of software emerging for CC. For example, I now use bead over Linear for task tracking.

I feel a lot of resemblance between Notion and CC. Tons of flexibility and capability, but very hard to know how and when to use them. Plugins help, but most plugins today are still mainly focusing on coding. I hope more templates show up for PM, GTM, and Operations to further democratize these capabilities. like good old William Gibson quote: “The future is already here—it’s just not evenly distributed.”
