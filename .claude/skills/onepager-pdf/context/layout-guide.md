# One-Pager PDF Layout Guide

## Page Structure

The one-pager uses a single letter-sized page (612x792pt) with these sections. The agent should adapt which sections to include and how to weight them based on the research findings.

## Available Sections

### 1. Top Banner (always include)
- Dark background using the prospect's dominant brand color
- ColdIQ branding top-left (name + tagline)
- "Prepared for [Company]" top-right
- Main headline: personalized to their specific growth challenge
- Sub-headline: one line connecting cold outreach to their specific need

### 2. The Opportunity (always include)
- 2-3 sentences showing we understand their business, their ICP, and the gap
- Must reference specific details from research (product names, certifications, integrations)
- Bold the key insight (e.g., "don't know you exist yet")

### 3. Stat Boxes (always include)
- 3 boxes with ColdIQ proof points: "300+", "2 weeks", "3-5x"
- These are static ColdIQ stats, styled in the prospect's brand colors

### 4. What We'd Build (always include, content adapts)
- 3-5 numbered steps personalized to the prospect
- Step 1 is always about list building -- describe their specific ICP segments
- Remaining steps adapt based on what matters most for their business:
  - If they have a complex product: include a "Messaging & Positioning" step
  - If they sell to fragmented markets: emphasize segmentation in sequences
  - If they have compliance needs: include deliverability/compliance step
  - If they're in competitive space: include a differentiation angle step
  - Always end with an optimization/scaling step

### 5. Why ColdIQ (include if space allows)
- 3-4 bullet points from ColdIQ proof points
- Pick the bullets most relevant to the prospect's industry

### 6. Bottom CTA Bar (always include)
- "Ready to [specific outcome] for [Company]?"
- coldiq.com | hello@coldiq.com
- "Book a Call" button

## Color Mapping

Given a prospect's brand color palette (from ColorThief), map colors to roles:

| Role | How to pick |
|------|------------|
| **Primary dark** | The darkest color in the palette -- used for banner, stat boxes, section headers, CTA bar |
| **Accent** | The brightest/most saturated color -- used for headline accents, underlines, numbered circles, bullet dots, CTA button |
| **Muted accent** | A lighter/desaturated version of the accent -- used for sub-text on dark backgrounds |
| **Background** | Off-white tinted toward the dominant color family |

### Color Selection Logic

```python
# Sort palette by luminance to find darkest and brightest
def luminance(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    return 0.299 * r + 0.587 * g + 0.114 * b

# Darkest = primary dark (banner, boxes)
# Most saturated bright = accent
# Generate muted accent by blending accent toward primary dark at 40%
# Generate background by tinting white toward dominant at 5%
```

## Typography

Use Helvetica (built into reportlab):
- Headlines: Helvetica-Bold, 20-22pt
- Section headers: Helvetica-Bold, 12pt
- Step titles: Helvetica-Bold, 9.5pt
- Body text: Helvetica, 8.5-9pt
- Stats: Helvetica-Bold, 20pt

## Spacing Rules

- Page margins: 40pt left/right
- Section gap: 18-22pt
- Step gap: 16-18pt
- Banner height: dynamic -- calculated from headline + subheadline content height
- CTA bar height: 50-55pt
- Stat boxes: equal width, 8pt rounded corners, 12pt gap between

## Lessons Learned

### Never use drawString for variable-length text

`canvas.drawString()` renders text at a fixed position with no wrapping -- if the text exceeds the page width, it gets clipped silently. This is especially dangerous for headlines where personalized content varies in length.

**Bad:**
```python
c.setFont("Helvetica-Bold", 22)
c.drawString(40, y, spec["headline"])  # clips if headline > ~30 chars
```

**Good:**
```python
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

style = ParagraphStyle("hl", fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=WHITE)
p = Paragraph(spec["headline"], style)
w, h = p.wrap(max_width, 200)  # auto-wraps to fit
p.drawOn(c, 40, y - h)
```

**Rule:** Use `Paragraph` for any text that comes from variable input (headlines, descriptions, opportunity text). Only use `drawString` for short, fixed labels ("ColdIQ", "Prepared for", "Book a Call").

### Make banner height dynamic

Since headlines wrap to different heights depending on content, the banner must resize to fit. Calculate the banner height from the actual rendered heights of headline + accent line + subheadline, then draw the banner rectangle to match.
