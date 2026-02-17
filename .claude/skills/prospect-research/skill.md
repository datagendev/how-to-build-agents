# Prospect Research

Research a B2B company and extract structured intelligence for outreach personalization.

## Trigger

When the user says `/prospect-research <company_name> <domain>` or asks to research a prospect company.

## Inputs

- **company_name** (required): The company's name (e.g., "OK Capsule")
- **domain** (required): The company's website domain (e.g., "okcapsule.com")

## Workflow

### Step 1: Company Research

Use `WebSearch` to gather intelligence on the company. Run these searches in parallel:

1. `"<domain> what does <company_name> do"` -- core business
2. `"<company_name> customers target market"` -- who they sell to
3. `"<company_name> competitors alternatives"` -- competitive landscape

From the search results, extract:
- **what_they_do**: One-line description of their core business
- **business_model**: How they make money (SaaS, marketplace, agency, manufacturing, etc.)
- **target_customers**: Who they sell to (roles, industries, company sizes)
- **key_differentiators**: What makes them different (list 3-5 bullet points)
- **likely_pain_points**: Based on their ICP and business model, what outbound/growth challenges they probably face (list 2-3)
- **company_details**: Location, founding year, team size, notable facts

### Step 2: Brand Color Extraction

Run the brand color extraction script to get the company's color palette from their logo/favicon.

```bash
source tmp/.venv/bin/activate && python3 scripts/extract_brand_colors.py <domain>
```

If the venv or dependencies don't exist yet:
```bash
cd tmp && python3 -m venv .venv && source .venv/bin/activate && pip install colorthief requests && cd ..
python3 scripts/extract_brand_colors.py <domain>
```

The script outputs a JSON object with:
- **source**: Which image the colors were extracted from
- **dominant**: The dominant hex color
- **palette**: Array of 5-6 hex colors

### Step 3: Write Output

Save the structured research to `tmp/prospect-research-<domain>.json` with this schema:

```json
{
  "company_name": "OK Capsule",
  "domain": "okcapsule.com",
  "research": {
    "what_they_do": "...",
    "business_model": "...",
    "target_customers": "...",
    "key_differentiators": ["...", "..."],
    "likely_pain_points": ["...", "..."],
    "company_details": "..."
  },
  "brand_colors": {
    "source": "...",
    "dominant": "#431463",
    "palette": ["#431463", "#64E3BC", "..."]
  }
}
```

Also print a human-readable summary to the console so the user can review before proceeding to PDF generation.

## Output

- File: `tmp/prospect-research-<domain>.json`
- Console: Human-readable summary of findings + color palette
