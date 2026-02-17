# LinkedIn Post

- **Date**: 2025-10-27T18:44:06.157Z
- **Reactions**: 8
- **Comments**: 0
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7388646693539336194

---

How to build AI workloads that can scale with LLMs

In Lance's "Learning the Bitter Lesson," he pointed out that during his open deep research project, he needed to constantly rip apart and rebuild his AI structure. And one thing he concluded: "Make it easy to remove structure." 

But how? 

Claude's recent video, "Building More Effective Agents" (an echo to their well-known "Building Effective Agents"), suggested a point that really resonated with me: migrate from an AI workflow to a workflow of agents (with a narrow scope). 
I believe it's a path forward. Instead of a rigid, predefined graph, each agent has the same structure, just with different prompts and tools. 

We all know AI agents go rogue and are slow even for simple steps. People opt into AI workflows often not because of their capability, but because of the guardrails and efficiency.  

I think "Tools" will start to fill in this gap, and proper tool design can make or break your AI agent. 

I want to share an example: a simple "Linear ticket creation" agent. For this agent, we only ask it to do one thing: take task description, create a ticket with proper title, description, assignee, team, project, label, and status. 

What we did before: 
we used official Linear MCP tools and prompted it to call 1) get_projects, 2) get_teams, 3) get_users, 4) get_issue_labels, 5) get_status_by_teams (yes, 5 different tool calls) to get the right context. But still, because Linear's create_ticket tool only requires "title" and "team_id," we often saw our tickets missing things here and there. 

This simple example manifests two problems with my AI agent: 1) poor efficiency with 5 different tool calls, and 2) no validation. 
Result: loss of trust. 

What we do now: 
we createds two custom tools that 
1) pulls all title, description, assignee, team, project, label, and status in one call, no back and forth → fast and reliable
and 
2) wraps the original Linear create_ticket to require not just title and team_id, but all of those fields above, reports a validation error if missing → guardrail. 
Unlike an AI workflow that just reports errors, AI agent can react based on failed attempts and know what needs to be done.  

Results: full delegation. No stupid errors, no missing pieces. 

Further wrapping these two tools into MCP, I can bring them anywhere: Codex, Gemini, Claude code, or even my Discord bot. There's no embedded structured code in my AI agent. Just simple prompt, tool, and  LLM calls. If I want to modify behavior, I simply change my prompts and tools. 

Just like we tailor prompts to different agents, we need to tailor tools for useful AI agents. if we need prompt library. we need tool library too. 

Don't just craft prompts, craft tools, too.

=================
And if you want to accelerate your custom MCP tool creation process, give us a try. 
We aim to make build and deploy custom tools super easy. (Yes, of course, I am writing to promote.)
