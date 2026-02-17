# LinkedIn Post

- **Date**: 2025-10-31T20:00:31.810Z
- **Reactions**: 12
- **Comments**: 1
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7390115478624460800

---

Use Claygent + MCP in Clay to detect if a website uses certain vendor

TL;DR, inspired by Shane Firek's post, I created a Claygent + Datagen MCP to just take in 1) company website URL, and 2) vendor you want to detect, then it would tell you if it found any evidence from their website using the vendor's tech in real time.  video is a quick how-to

I simply gave it two tools. One is a web research tool to gather information for front-end patterns and paths, the other is a custom web probe tool that returns whether any patterns are matched. 

With these simple two tools, Claygent can go on to check any website, with any tech without  predefined pattern library and paths to look for. And the web_probe tool gives the LLM clean and deterministic pattern-matched results instead of whole rendered htmls.

While this is a simple use case, I can already see how it can be used in my other workflows:  pull my user's most recent usage query from Supabase, find the most relevant use case I saved in Notion, and generate a personalized outreach email. all w/o me setting up 100 columns. simply describing it. And honestly, I argue many would out-perform ai workflow if you setup the tool right if and give it more compute. 

It actually leads me to my final question: how do you design your AI workload so that it can scale with compute? 

Most AI workflows plateau when you give them more compute. If you predefine your query keywords, then define how many pages it can fetch, your AI is just a summarization machine. 

But if you define the goal, let it decide the query > check results> requery > and find the best content, then the more compute you give it, the better results you get. I think that is the part we need to be trained on, not whether you use n8n or Clay or any fancy builder but really down to design the problem worth tackling, the prompt to spec AI, and the tools to act and validate its work.
