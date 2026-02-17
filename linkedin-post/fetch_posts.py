import json
import os
import re
from datagen_sdk import DatagenClient

assert os.getenv("DATAGEN_API_KEY"), "Set DATAGEN_API_KEY first"

client = DatagenClient()

result = client.execute_tool(
    "get_linkedin_person_posts",
    {"linkedin_url": "https://www.linkedin.com/in/yu-sheng-kuo-87658743/"},
)

posts = result if isinstance(result, list) else result.get("posts", [result])

# Save full JSON dump
with open("linkedin-post/all_posts.json", "w") as f:
    json.dump(posts, f, indent=2, ensure_ascii=False)

# Save each post as individual markdown file
for i, post in enumerate(posts):
    text = post.get("text", "")
    date = post.get("activityDate", "unknown")
    reactions = post.get("reactionsCount", 0)
    comments = post.get("commentsCount", 0)
    url = post.get("activityUrl", "")

    # Create a slug from the first line of text
    first_line = text.split("\n")[0][:60].strip()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", first_line).strip("-").lower() or f"post-{i}"

    filename = f"linkedin-post/{i+1:02d}-{slug}.md"
    with open(filename, "w") as f:
        f.write(f"# LinkedIn Post\n\n")
        f.write(f"- **Date**: {date}\n")
        f.write(f"- **Reactions**: {reactions}\n")
        f.write(f"- **Comments**: {comments}\n")
        f.write(f"- **URL**: {url}\n\n")
        f.write(f"---\n\n")
        f.write(text)
        f.write("\n")

print(f"Saved {len(posts)} posts to linkedin-post/")
