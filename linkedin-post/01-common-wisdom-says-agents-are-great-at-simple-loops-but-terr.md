# LinkedIn Post

- **Date**: 2026-02-12T22:02:02.673Z
- **Reactions**: 8
- **Comments**: 0
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7427834396742774784

---

Common wisdom says agents are great at simple loops but terrible at complex workflows. 

Because context tend to grow linearly in workflow, agents tend to forget later steps as context builds up, can't reliably respect dependency graphs, and either block on sequential execution or blindly charge ahead without waiting for upstream results
I used to believe this too. Not anymore.

With the recent introduction of Tasks in Claude Code and all the built-in harness, last weekend I just built a 12-step company enrichment agent using /agent . It handles fan-in, fan-out, parallel execution, and dependency management and all are defined in natural language. What used to require carefully orchestrated workflow code now lives in an agent prompt file.

Here's what I've learned about making complex Claude Code agents reliable:

1. Agent.md with indexed step files:  Vercel's recent comparison of Skills vs. Agent.md showed that using an agent prompt file with indexed links to detailed step descriptions reduces context bloat at startup while achieving 100% pass rate compared to 53% with default Skills usage.

2. Explicit task list generation : Ask the model to build a task list upfront. This triggers it to pre-define the dependency graph before execution, allowing parallel work while respecting step dependencies. Critical for any workflow with branching logic.

3. Script-based intermediate outputs: Instead of asking the model to digest tool output inline, have it write simple scripts that export MCP tool results to tmp/ files. This prevents context bloat from large tool outputs, lets the model revisit data at any point, and provides persistent results for recovery when tools or the model fail. 

4. Structured output with hook validation: Pre-define expected output schemas for each step. Use hooks to validate output files — if the model misses anything, the hook raises an error and forces a revisit.

Here's the bigger implication I keep thinking about:
For a long time, workflows and agents were two distinct architectures with different strengths. But with this pattern of "workflow of agents", a more unified paradigm is emerging. And workflow typically requires a lot of code.

What used to be:  idea → English → (llm generated) code → results 
Now becomes: idea → English → LLM + harness → results

To be clear , I'm not talking about "vibe coding" where LLMs write your dashboard or workflow code. I'm talking about **LLM agents as the output generators**. The compute is coming from the model, not your CPU.

With minimum involvement of code. What used to require  Domain Expert + Technical Engineer  to build a product playbook can now be  Domain Expert + Claude Code. And these agents can be served through email, SMS, Slack, or Discord.

The real differentiator really comes down to how well you can encode your expertise, your judgment, your process into a Claude Code agent with the right Skills, MCPs, and context and build a feedback loop to continuously improve it.
