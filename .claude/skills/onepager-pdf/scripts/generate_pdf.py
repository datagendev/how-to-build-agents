#!/usr/bin/env python3
"""Generate a personalized one-pager PDF from a JSON content spec.

Usage:
    python3 generate_pdf.py <content.json> [output.pdf]

The JSON spec should contain:
{
  "company_name": "OK Capsule",
  "colors": {
    "primary_dark": "#431463",
    "accent": "#64E3BC",
    "muted_accent": "#B89CC8",
    "background": "#F8F5FB"
  },
  "headline": "Scale Your Practitioner Pipeline",
  "headline_accent": "Without Scaling Your Sales Team",
  "subheadline": "How OK Capsule can turn cold outreach into...",
  "opportunity": "OK Capsule's manufacturing-as-a-service platform...",
  "steps": [
    {"title": "Step Title", "description": "Step description..."},
    ...
  ],
  "why_bullets": [
    "Bullet point 1",
    "Bullet point 2"
  ],
  "cta_text": "Ready to fill OK Capsule's practitioner pipeline?"
}
"""

import json
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle


WIDTH, HEIGHT = letter
WHITE = HexColor("#FFFFFF")

# Static ColdIQ stats
STATS = [
    ("300+", "outbound systems\nbuilt by ColdIQ"),
    ("2 weeks", "from kickoff to\nfirst campaigns live"),
    ("3-5x", "pipeline ROI vs.\ninbound alone"),
]


def draw_rounded_rect(c, x, y, w, h, r, fill_color):
    c.setFillColor(fill_color)
    c.setStrokeColor(fill_color)
    c.roundRect(x, y, w, h, r, fill=1, stroke=0)


def draw_circle_icon(c, x, y, radius, color, number):
    c.setFillColor(color)
    c.circle(x, y, radius, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x, y - 4, str(number))


def blend_color(hex1, hex2, ratio=0.4):
    """Blend two hex colors. ratio=0 gives hex1, ratio=1 gives hex2."""
    r1, g1, b1 = int(hex1[1:3], 16), int(hex1[3:5], 16), int(hex1[5:7], 16)
    r2, g2, b2 = int(hex2[1:3], 16), int(hex2[3:5], 16), int(hex2[5:7], 16)
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"


def build_pdf(spec, output_path):
    colors = spec["colors"]
    PRIMARY = HexColor(colors["primary_dark"])
    ACCENT = HexColor(colors["accent"])
    MUTED = HexColor(colors.get("muted_accent", blend_color(colors["accent"], colors["primary_dark"], 0.4)))
    BG = HexColor(colors.get("background", "#F8F5FB"))
    MID = HexColor(colors.get("mid_tone", blend_color(colors["primary_dark"], colors["accent"], 0.5)))

    c = canvas.Canvas(output_path, pagesize=letter)

    # Full page background
    c.setFillColor(BG)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)

    # --- Top banner (sized dynamically below based on headline content) ---

    # Headlines (using Paragraph for auto-wrapping)
    max_text_w = WIDTH - 80
    hl_style = ParagraphStyle("hl", fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=WHITE)
    hl_p = Paragraph(spec["headline"], hl_style)
    hl_w, hl_h = hl_p.wrap(max_text_w, 200)

    ha_style = ParagraphStyle("ha", fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=ACCENT)
    ha_p = Paragraph(spec["headline_accent"], ha_style)
    ha_w, ha_h = ha_p.wrap(max_text_w, 200)

    sub_style = ParagraphStyle("sub", fontName="Helvetica", fontSize=10, leading=14, textColor=MUTED)
    sub_text = spec["subheadline"].replace("\n", "<br/>")
    sub_p = Paragraph(sub_text, sub_style)
    sub_w, sub_h = sub_p.wrap(max_text_w, 200)

    # Recalculate banner height to fit all headline content
    banner_h = 48 + hl_h + ha_h + sub_h + 12  # 48 = top padding for ColdIQ branding + gaps

    # Redraw banner with correct height
    c.setFillColor(PRIMARY)
    c.rect(0, HEIGHT - banner_h, WIDTH, banner_h, fill=1, stroke=0)

    # Redraw ColdIQ branding and Prepared for (on top of resized banner)
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, HEIGHT - 28, "ColdIQ")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(40, HEIGHT - 40, "GTM Systems That Sell For You")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawRightString(WIDTH - 40, HEIGHT - 28, "Prepared for")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(WIDTH - 40, HEIGHT - 40, spec["company_name"])

    # Draw headlines and subheadline
    hl_y = HEIGHT - 48
    hl_p.drawOn(c, 40, hl_y - hl_h)
    ha_p.drawOn(c, 40, hl_y - hl_h - ha_h)
    sub_p.drawOn(c, 40, hl_y - hl_h - ha_h - sub_h - 4)

    y = HEIGHT - banner_h - 25

    # --- Opportunity ---
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "The Opportunity")
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(40, y - 6, 180, y - 6)
    y -= 24

    opp_style = ParagraphStyle("opp", fontName="Helvetica", fontSize=9, leading=13, textColor=HexColor("#2A2A2A"))
    p = Paragraph(spec["opportunity"], opp_style)
    pw, ph = p.wrap(WIDTH - 80, 200)
    p.drawOn(c, 40, y - ph)
    y -= ph + 18

    # --- Stat boxes ---
    box_w = (WIDTH - 80 - 24) / 3
    box_h = 68
    for i, (num, label) in enumerate(STATS):
        bx = 40 + i * (box_w + 12)
        draw_rounded_rect(c, bx, y - box_h, box_w, box_h, 8, PRIMARY)
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(bx + box_w / 2, y - 28, num)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8)
        for j, line in enumerate(label.split("\n")):
            c.drawCentredString(bx + box_w / 2, y - 44 - j * 11, line)
    y -= box_h + 22

    # --- Steps ---
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, f"What We'd Build for {spec['company_name']}")
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(40, y - 6, 40 + 240, y - 6)
    y -= 20

    for i, step in enumerate(spec["steps"]):
        draw_circle_icon(c, 55, y - 7, 10, MID, i + 1)
        c.setFillColor(PRIMARY)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(75, y - 4, step["title"])
        desc_style = ParagraphStyle(f"s{i}", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=HexColor("#4A4A4A"))
        p = Paragraph(step["description"], desc_style)
        pw, ph = p.wrap(WIDTH - 120, 100)
        p.drawOn(c, 75, y - 6 - ph)
        y -= ph + 18
    y -= 4

    # --- Why ColdIQ ---
    if spec.get("why_bullets") and y > 120:
        c.setFillColor(PRIMARY)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, "Why ColdIQ")
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.5)
        c.line(40, y - 6, 130, y - 6)
        y -= 20

        for bullet in spec["why_bullets"]:
            c.setFillColor(ACCENT)
            c.circle(49, y - 2, 3, fill=1, stroke=0)
            bs = ParagraphStyle("b", fontName="Helvetica", fontSize=8.5, leading=11, textColor=HexColor("#2A2A2A"))
            p = Paragraph(bullet, bs)
            pw, ph = p.wrap(WIDTH - 105, 50)
            p.drawOn(c, 60, y - ph + 2)
            y -= ph + 6

    # --- CTA bar ---
    cta_h = 52
    draw_rounded_rect(c, 0, 0, WIDTH, cta_h, 0, PRIMARY)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, 26, spec.get("cta_text", f"Ready to grow {spec['company_name']}'s pipeline?"))

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawString(40, 13, "coldiq.com  |  Let's talk: hello@coldiq.com")

    btn_w, btn_h = 120, 28
    btn_x = WIDTH - 40 - btn_w
    btn_y = (cta_h - btn_h) / 2
    draw_rounded_rect(c, btn_x, btn_y, btn_w, btn_h, 14, ACCENT)
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(btn_x + btn_w / 2, btn_y + 9, "Book a Call")

    c.save()
    print(f"PDF saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_pdf.py <content.json> [output.pdf]", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        spec = json.load(f)

    output = sys.argv[2] if len(sys.argv) > 2 else f"tmp/coldiq-{spec.get('company_name', 'prospect').lower().replace(' ', '-')}-onepager.pdf"
    build_pdf(spec, output)
