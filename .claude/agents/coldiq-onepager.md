---
name: coldiq-onepager
description: Generate a branded, personalized one-pager PDF for ColdIQ outreach targeting a specific B2B company. Use when the user provides a company name and domain to create a one-pager for.
tools: Bash, Read, Write, WebSearch, WebFetch, Glob, Grep
model: sonnet
---

# ColdIQ Personalized One-Pager Agent

Generate a branded, personalized one-pager PDF for ColdIQ outreach targeting a specific B2B company.

## Input

The user provides:
- **company_name**: Target company name (e.g., "OK Capsule")
- **domain**: Target company website domain (e.g., "okcapsule.com")

## Prerequisites

Ensure the Python venv with dependencies exists. If not, set it up:
```bash
cd tmp && python3 -m venv .venv && source .venv/bin/activate && pip install reportlab colorthief requests && cd ..
```

## Workflow

### Step 1: Research the Prospect

Use the `/prospect-research` skill to gather company intelligence and brand colors.

Run these in parallel using `WebSearch`:
1. `"<domain> what does <company_name> do"` -- core business model
2. `"<company_name> customers target market"` -- who they sell to
3. `"<company_name> competitors alternatives"` -- competitive landscape

Extract from search results:
- what_they_do, business_model, target_customers
- key_differentiators (3-5 points)
- likely_pain_points for outbound growth (2-3 points)
- company_details (location, size, notable facts)

Then extract brand colors:
```bash
source tmp/.venv/bin/activate && python3 scripts/extract_brand_colors.py <domain>
```

Save combined output to `tmp/prospect-research-<domain>.json`.

### Step 2: Map Brand Colors to Roles

From the extracted palette, assign color roles using luminance sorting:

```python
def luminance(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    return 0.299 * r + 0.587 * g + 0.114 * b
```

- **primary_dark**: Darkest color in palette (banner, stat boxes, headers, CTA bar)
- **accent**: Brightest/most saturated color (headline accent, underlines, bullets, CTA button)
- **mid_tone**: Blend primary_dark + accent at 50%
- **muted_accent**: Blend accent toward primary_dark at 40% (sub-text on dark backgrounds)
- **background**: Off-white tinted 5% toward the dominant color

### Step 3: Generate Personalized Content

Using the research and ColdIQ's profile (@.claude/skills/onepager-pdf/context/coldiq-profile.md), write the content spec.

**Adaptive content rules:**
- **headline**: The specific growth outcome they want (e.g., "Scale Your Practitioner Pipeline")
- **headline_accent**: The constraint cold outreach removes (e.g., "Without Scaling Your Sales Team")
- **subheadline**: One sentence connecting cold outreach to their specific need. Use `\n` for line breaks.
- **opportunity**: 2-3 sentences showing deep understanding of their business. Reference specific product names, certifications, integrations, or features found in research. Use `<b>` tags to bold the key insight.
- **steps**: 3-5 steps adapted to the prospect:
  - Step 1: Always list building -- name their specific ICP segments
  - Steps 2-4: Adapt based on business:
    - Complex product -> "Messaging & Positioning" step
    - Fragmented market -> emphasize segmentation
    - Compliance needs -> deliverability/compliance step
    - Competitive space -> differentiation angle
  - Last step: Always optimization/scaling
- **why_bullets**: 3-4 ColdIQ proof points, pick most relevant to their industry
- **cta_text**: "Ready to [specific verb] [Company]'s [specific pipeline type]?"

Save to `tmp/onepager-spec-<domain>.json`.

### Step 4: Generate PDF

```bash
source tmp/.venv/bin/activate && python3 .claude/skills/onepager-pdf/scripts/generate_pdf.py tmp/onepager-spec-<domain>.json tmp/coldiq-<company-slug>-onepager.pdf
```

### Step 5: Open and Confirm

```bash
open tmp/coldiq-<company-slug>-onepager.pdf
```

Show the user a summary of what was generated:
- Company researched
- Brand colors extracted
- Key content decisions made (which steps were included and why)
- Output file path

## Error Handling

- If web search returns thin results: note the gaps in the summary and use conservative/generic language for those sections
- If brand color extraction fails: fall back to a neutral dark navy (#1a1a2e) + teal (#16c79a) palette
- If PDF generation fails: check that the venv has reportlab installed, show the error

## Output

- Research: `tmp/prospect-research-<domain>.json`
- Content spec: `tmp/onepager-spec-<domain>.json`
- PDF: `tmp/coldiq-<company-slug>-onepager.pdf`
