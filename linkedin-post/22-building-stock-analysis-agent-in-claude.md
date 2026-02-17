# LinkedIn Post

- **Date**: 2025-08-08T23:19:30.265Z
- **Reactions**: 10
- **Comments**: 6
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7359724971423617024

---

Building Stock Analysis agent in Claude

[Background] 
This is about my learning on how to use Claude/ChatGPT +MCP beyond "google alternative" and be "assistant" . (my def of agent is a process that given goal it would continue to use tools and take multi-steps to reach it)

[Results]
A daily stock analysis agent that: 
 -- pulls latest reddit discussion in r/wallstreetbets , r/stocks about the stock
--  calculates technical indicators  including RSI, volume analysis, etc.
--  retrieve latest news related to stocks
and finalize to a buy/put suggestions like shown in videos. 

[How]
I found it very useful to develop each “module" in separate chat. and after i get good results, i ask Claude to summarize the "process" as an artifact and save to my project. 
 * reddit: Use reddit browse MCP to pull post/comments for a given stock while ignoring all useless nonsense
 * technical indicators : I use Datagen MCP to connect to financialdataset.ai MCP so it can directly use their tools as python function to pull daily price and calculate all realtime technical indicators
* web research news: Claude’s native web research to focus on a) major potential macro economic news and b) news specific to the stock 

Finally, Attached all these artifacts to a Claude project and add an instruction with "step-by-step" prompt. with this Claude can work more like a "workflow" to follow the instructions without going wild. (you can find details in comments)

[Learning]
-- Spec is new code: coined by OpenAI. I think the way we think what makes a software is changing. To build the agent I made today an year ago would either requires me to use n8n, or code with Langchain. but now it can just be done in Claude with me talking to it. what used to be writing custom API integrations now requires just an MCP. 

-- Adaptive: if I build this agent in n8n or code. it would be painful to change number of look up days if I did not parameterize it ahead of time. while developing in Claude just need me to ask and re-summarize. It feels way more organic and can rapidly adapt my needs on the fly compared to regular codes. 

-- Portability: this is what i emphasized before with MCPs. With just few markdown file, MCP list( i intentionally only look for remote MCPs so its super easy to connect), you can start to run w/o installing any dev environments or apps. and you can run on any LLM client(OS) that supports MCPs 

While its still far fetch to consider this “software” to run mission critical workflows, but I think its perfect for individual or even small teams to delegate their small tasks for their very needs given how easy it can be built nowadays.
