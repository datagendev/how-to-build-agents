#!/usr/bin/env python3
"""Extract brand colors from a website's logo/favicon using ColorThief.

Usage:
    python3 scripts/extract_brand_colors.py <domain>
    python3 scripts/extract_brand_colors.py okcapsule.com
    python3 scripts/extract_brand_colors.py okcapsule.com --json  # JSON output only
"""

import io
import json
import re
import sys
import requests
from colorthief import ColorThief
from urllib.parse import urljoin


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def fetch_logo_urls(domain):
    """Scrape the homepage for logo/favicon image URLs."""
    url = f"https://{domain}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    html = resp.text

    urls = []

    # 1. Look for favicon links
    favicon_patterns = [
        r'<link[^>]+rel=["\'](?:icon|shortcut icon|apple-touch-icon)["\'][^>]+href=["\']([^"\']+)["\']',
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\'](?:icon|shortcut icon|apple-touch-icon)["\']',
    ]
    for pat in favicon_patterns:
        for match in re.finditer(pat, html, re.IGNORECASE):
            urls.append(urljoin(url, match.group(1)))

    # 2. Look for og:image
    og_match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
    if og_match:
        urls.append(urljoin(url, og_match.group(1)))

    # 3. Look for img tags with "logo" in src, alt, or class
    logo_imgs = re.finditer(r'<img[^>]+(?:src|alt|class)[^>]*logo[^>]*>', html, re.IGNORECASE)
    for m in logo_imgs:
        src_match = re.search(r'src=["\']([^"\']+)["\']', m.group())
        if src_match:
            urls.append(urljoin(url, src_match.group(1)))

    # 4. Fallback: standard favicon path
    urls.append(f"{url}/favicon.ico")

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)

    return unique


def extract_colors_from_url(image_url, color_count=6):
    """Download image and extract palette using ColorThief."""
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(image_url, headers=headers, timeout=10)
    resp.raise_for_status()

    img_bytes = io.BytesIO(resp.content)
    ct = ColorThief(img_bytes)

    dominant = ct.get_color(quality=1)
    palette = ct.get_palette(color_count=color_count, quality=1)

    return dominant, palette


def extract_brand_colors(domain, color_count=6, verbose=True):
    """Extract brand colors from a domain's logo/favicon images."""
    if verbose:
        print(f"Extracting brand colors for: {domain}\n", file=sys.stderr)

    logo_urls = fetch_logo_urls(domain)
    if verbose:
        print(f"Found {len(logo_urls)} image candidates:", file=sys.stderr)
        for u in logo_urls:
            print(f"  - {u}", file=sys.stderr)
        print(file=sys.stderr)

    for img_url in logo_urls:
        try:
            if verbose:
                print(f"Trying: {img_url}", file=sys.stderr)
            dominant, palette = extract_colors_from_url(img_url, color_count)
            if verbose:
                print(f"  Dominant: {rgb_to_hex(*dominant)}", file=sys.stderr)
                for c in palette:
                    print(f"  Palette:  {rgb_to_hex(*c)}", file=sys.stderr)
                print(file=sys.stderr)
            if len(palette) >= 3:
                return {
                    "source": img_url,
                    "dominant": rgb_to_hex(*dominant),
                    "palette": [rgb_to_hex(*c) for c in palette],
                }
        except Exception as e:
            if verbose:
                print(f"  Failed: {e}\n", file=sys.stderr)

    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_brand_colors.py <domain> [--json]", file=sys.stderr)
        sys.exit(1)

    domain = sys.argv[1]
    json_only = "--json" in sys.argv

    result = extract_brand_colors(domain, verbose=not json_only)

    if result:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps({"error": f"Could not extract brand colors for {domain}"}))
        sys.exit(1)
