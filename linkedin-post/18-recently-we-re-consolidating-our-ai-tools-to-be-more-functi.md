# LinkedIn Post

- **Date**: 2025-09-26T22:29:42.007Z
- **Reactions**: 9
- **Comments**: 6
- **URL**: https://www.linkedin.com/feed/update/urn:li:activity:7377469443175792640

---

Recently, we're consolidating our AI tools to be more functional-focused instead of loading them with many irrelevant MCP tools and hoping they pick the right path every time.

Take a simple creating a CRM contact as example.
This is the typical flow for AI to complete it:
Given email, name, company, and company domain:
1) Search contact by email → hubspot-search-objects tool with email filter → get contact_id or null
2) Create contact if not found → hubspot-batch-create-objects tool with email, first_name, last_name, phone → get contact_id
3) Search company by domain → hubspot-search-objects tool with domain filter → get company_id or null
4) Create company if not found → hubspot-batch-create-objects tool with company_name, domain → get company_id
5) Associate contact + company → hubspot-batch-create-associations tool with contact_id and company_id → confirm association
Return → final contact_id, company_id, association_status

Instead of letting an AI agent directly call MCP tools to do all of the above every time, we let Claud to use Datagen to build and deploy a focused "create-contact" tool by chaining these MCP tools in code. 
It's faster, cheaper, and more reliable. Now rather than exposing a generic MCP toolset, we expose a series of highly focused functional tools in Datagen MCP that we can easily plug and play in any agent framework or ai agent app. 

And because Datagen's tool also comes with a server-less API deployment, we can use this "create-contact" API in Clay, n8n, or even Lovable.

By the way, wrapping these API calls not only makes our workflows more modular; it also means that if Clay ever decides to charge credits for API calls, compressing five API calls into one would simply reduce the cost by about 5×.

As usual, if you are interested in how we use Claude to build this create-contact API, check the comments.
