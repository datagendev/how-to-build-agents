# One-Pager PDF Generator

Generate a branded, personalized one-pager PDF for ColdIQ outreach.

## Trigger

When the user says `/onepager-pdf` or asks to generate a one-pager PDF for a prospect.

## Inputs

This skill expects a prospect research JSON file at `tmp/prospect-research-<domain>.json` (output from `/prospect-research`). Alternatively, the user can provide the research details directly.

## Workflow

### Step 1: Load Research Data

Read the prospect research from `tmp/prospect-research-<domain>.json`. If the file doesn't exist, ask the user to run `/prospect-research` first or provide the details.

### Step 2: Map Brand Colors

Using the `brand_colors.palette` from the research, assign color roles. Follow the color mapping logic in @.claude/skills/onepager-pdf/context/layout-guide.md:

```python
def luminance(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    return 0.299 * r + 0.587 * g + 0.114 * b

# Sort by luminance
# Darkest -> primary_dark
# Brightest/most saturated -> accent
# Blend for muted_accent and background
```

### Step 3: Generate Content Spec

Using the research data and ColdIQ's profile (@.claude/skills/onepager-pdf/context/coldiq-profile.md), create a JSON content spec:

```json
{
  "company_name": "...",
  "colors": {
    "primary_dark": "#...",
    "accent": "#...",
    "muted_accent": "#...",
    "mid_tone": "#...",
    "background": "#..."
  },
  "headline": "...",
  "headline_accent": "...",
  "subheadline": "...",
  "opportunity": "...",
  "steps": [...],
  "why_bullets": [...],
  "cta_text": "..."
}
```

**Content adaptation rules** (see @.claude/skills/onepager-pdf/context/layout-guide.md for full details):

- **headline + headline_accent**: Personalize to their specific growth challenge. Line 1 = the outcome they want. Line 2 = the constraint they have.
- **opportunity**: 2-3 sentences. Reference specific details from research. Bold the key insight with `<b>` tags.
- **steps**: 3-5 steps adapted to the prospect. Always start with list building for their ICP. Adapt middle steps based on their business complexity. Always end with optimization.
- **why_bullets**: Pick 3-4 ColdIQ proof points most relevant to their industry.
- **cta_text**: "Ready to [specific verb] [Company]'s [specific pipeline]?"

Save the spec to `tmp/onepager-spec-<domain>.json`.

### Step 4: Generate PDF

Run the PDF generation script:

```bash
source tmp/.venv/bin/activate && python3 .claude/skills/onepager-pdf/scripts/generate_pdf.py tmp/onepager-spec-<domain>.json tmp/coldiq-<company>-onepager.pdf
```

If the venv doesn't exist:
```bash
cd tmp && python3 -m venv .venv && source .venv/bin/activate && pip install reportlab && cd ..
```

### Step 5: Open and Review

Open the generated PDF for the user:
```bash
open tmp/coldiq-<company>-onepager.pdf
```

## Output

- Content spec: `tmp/onepager-spec-<domain>.json`
- PDF file: `tmp/coldiq-<company>-onepager.pdf`
