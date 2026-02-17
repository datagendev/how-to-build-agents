# LinkedIn Post

- **Date**: 2025-07-16T23:33:27.940Z
- **Reactions**: 8
- **Comments**: 1
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7351393563978424321

---

Use MCP + Claude to build automation 

Conclusion first: the video below shows how i use just prompt to create a daily signal table in Supabase for WingWork. 

[Background]: After watching Jordan Crawford's last Cannonball for WingWork, I decided to test if we could fully automate the account scoring table using only Claude + MCP without any code.
**disclaimer: I am by no mean a qualified GTM folks, so its just me exploring with tools and test cases

[Data Sources]:
FAA Registry
Service Difficulty Reports
Compliance Violations

[Development Process]:
1) Data Collection: Used our tool to create scrapers for SDR and compliance data, but ended up writing custom scripts for FAA registry due to data size

2) Table creation: Pure Claude + Supabase MCP for processing and our tool for enrichment. From calculating SDR per flight, fleet diversity, aircraft 
depreciation, license expiration, and compliance/maintenance stress metrics all the way to company and leadership enrichment.

3) Deployment:  Asked Claude to summarize everything into workflow.md with steps, tools, and fallback mechanisms. A 7-step workflow.md now serves as my automation code and my MCPs are the dependencies.

[What Worked]:
- Speed: As someone who's done data analysis for years, it still feels magical to just describe what you want and have it handled. This automation pipeline would normally take hours or even days to develop and deploy.

- Instructions as Code: By restricting to MCP-only interactions, brainstorming instantly becomes deployable. 

- Built-in Resilience: When my enrichment tool failed, Claude automatically fell back to web research. This adaptability beats traditional code that would just crash, but it brings unpredictability too.

- Framework Portability: The workflow.md + MCP combination works across any agent framework that supports MCP with minimal adaption.

[What Didn't Work]:
- No Task Scheduling: Biggest complaint. Claude lacks built-in scheduling while ChatGPT and Grok already have this.

- Async Limitations: Our tools use async (submit + check status) to prevent blocking, but Claude has no real polling mechanism. Hard to control when it checks back on long-running jobs.(May work with Progress with recent spec updates)

- Scale Constraints: High-volume, long-running operations remain challenging. Even our AI-generated bridge tools struggle with large datasets. something we are solving. 
 
[Lessons Learned]:
- Design atomic tools that "serves" the LLM
- Create new tables along the way as version control with full audit trails
- Need MCP-to-code converter for scalability - LLMs should summarize tool usage processes into code blocks just like they summarize context into .md
