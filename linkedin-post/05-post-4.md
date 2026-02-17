# LinkedIn Post

- **Date**: 2026-01-27T23:46:00.614Z
- **Reactions**: 14
- **Comments**: 2
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7422062354714116096

---

𝗠𝘆 𝘂𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱𝗶𝗻𝗴 𝗼𝗳 /𝗰𝗼𝗺𝗺𝗮𝗻𝗱, /𝗮𝗴𝗲𝗻𝘁, /𝘀𝗸𝗶𝗹𝗹, 𝗮𝗻𝗱 /𝗺𝗰𝗽 𝗶𝗻 𝗖𝗹𝗮𝘂𝗱𝗲 𝗖𝗼𝗱𝗲 𝘁𝗵𝗮𝘁 𝗵𝗲𝗹𝗽𝗲𝗱 𝗺𝗲 𝗯𝘂𝗶𝗹𝗱 𝗮𝗴𝗲𝗻𝘁𝘀 𝗹𝗶𝗸𝗲 𝗿𝗲𝗮𝗹 𝘀𝗼𝗳𝘁𝘄𝗮𝗿𝗲

I get asked quite a bit about the differences between /command, /skill, /mcp, and /agent, and when to use each one.

First to me the hierarchy is 
🔹 /command calls → /agent
🔹 /agent calls → /skill
🔹 /skill contains → prompts, MCPs, scripts
🔹 /mcp communicates → external services

you use command for its deterministic property instead of relying on model to trigger. you call agent to complete a task, and the task may require several skills. and the skill may or may not need to communicate to external services through MCPs. 

Here is an example: I have a /daily-activity-report agent. this agent has two skills , /product-analysis skill and  /report-generator skill. The first one focuses on framework of how we want to do analysis for user behavior with access to our Posthog and Neon through MCP. the other one is just simple report formatter and some guideline of how to make report we like. and finally the agent would use gmail mcp to send reports to stakeholders. 

This type of modulation makes my CC function more like a software with clear dependency instead of bunch of prompt files. whenever I optimize one skill, all agents using it get updated. 

I think it's also getting clear now MCP should focus on communication/auth for external services (so your agent don't have access to your raw credentials), and anything you don't want model to modify. In contrast, things like create pdf should just be skills. 

For local usage, I wrap this agent into a command so it's easy to trigger. 
But overtime I also found annoying that I have to remember to call it. so we start to deploy Claude Code agents on our own service so it can be triggered daily at 8am before I ask. By giving each of them a webhook also allows them to be easily triggered from external event(like a meeting transcript or a new sign-up). It streamlines our context update and gives a central place to manage all of the deployed agents. 

By (carefully) adding agents one by one, I can focus on the highest leverage while still keeping a good grip on everything that’s happening. it's quite liberating.
