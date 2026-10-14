"""
youtube_helpers.py
Helper functions for the Pocket AI Assistant.
All functions work OFFLINE - no API keys needed.
Beginner-friendly: each function does one job and is well commented.
"""

import random


def generate_script(topic, duration_minutes=5, tone="friendly"):
    """
    Generate a simple YouTube video script outline.

    Args:
        topic (str): Video topic, e.g. "how to cook biryani"
        duration_minutes (int): Target length of the video
        tone (str): "friendly", "funny", "professional", or "casual"

    Returns:
        str: A formatted script outline in Markdown.
    """
    topic = topic.strip() or "your topic"

    tones = {
        "friendly": "warm and encouraging, like talking to a friend",
        "funny": "playful with light humour",
        "professional": "clear, confident and to the point",
        "casual": "relaxed and conversational",
    }
    tone_desc = tones.get(tone.lower(), tones["friendly"])

    # Rough pacing: ~130 words per minute of speech
    target_words = max(150, duration_minutes * 130)

    script = f"""## 🎬 Video Script: {topic.title()}

**Length:** ~{duration_minutes} minutes (~{target_words} words)
**Tone:** {tone_desc}

---

### 1. HOOK (0:00 - 0:30)
> "Stop scrolling! In the next {duration_minutes} minutes, I'll show you everything you need to know about **{topic}** — even if you're a complete beginner."

### 2. INTRO (0:30 - 1:00)
- Welcome viewers back to the channel
- One sentence on why {topic} matters right now
- Tease the outcome: "By the end, you'll be able to..."

### 3. MAIN CONTENT
**Point 1 — The basics of {topic}**
- Explain it simply, no jargon
- Give one quick example

**Point 2 — Common mistakes to avoid**
- Mistake 1 and how to fix it
- Mistake 2 and how to fix it

**Point 3 — Pro tip**
- Share one tip most beginners miss about {topic}

### 4. CALL TO ACTION
> "If this helped, hit subscribe and tell me in the comments what you want next about {topic}!"

### 5. OUTRO
- Recap the 3 points in 20 seconds
- End screen: suggest your next video

---
*Tip: read this aloud once and time yourself. Cut or expand Point 2 to hit {duration_minutes} minutes.*
"""
    return script


def generate_titles(topic, count=5):
    """
    Generate catchy YouTube title ideas from templates.
    Returns a numbered list as a string.
    """
    topic = topic.strip() or "your topic"
    t = topic.title()

    templates = [
        f"{t} for Beginners: Everything You Need to Know",
        f"I Tried {t} for 30 Days — Here's What Happened",
        f"5 {t} Mistakes You're Probably Making",
        f"{t} Explained in {random.choice(['5', '7', '10'])} Minutes",
        f"How to Master {t} (Step-by-Step Guide)",
        f"{t}: Tips Nobody Tells Beginners",
        f"Stop Doing {t} Wrong — Do This Instead",
    ]
    random.shuffle(templates)
    chosen = templates[:max(1, min(count, len(templates)))]
    lines = [f"**Title ideas for '{topic}':**", ""]
    for i, title in enumerate(chosen, 1):
        lines.append(f"{i}. {title}")
    return "\n".join(lines)


def generate_description(topic, keywords=""):
    """
    Generate a YouTube video description with hashtags.
    """
    topic = topic.strip() or "your topic"
    keywords = keywords.strip()

    hashtags = " ".join(
        "#" + "".join(ch for ch in w if ch.isalnum())
        for w in topic.split()
        if w.isalnum() or w.replace("-", "").isalnum()
    )

    desc = f"""Learn {topic} step by step in this beginner-friendly guide.

In this video:
✅ What {topic} is and why it matters
✅ Common beginner mistakes (and fixes)
✅ One pro tip to get better results faster

{"Keywords: " + keywords if keywords else ""}

👉 Subscribe for more videos like this!

{hashtags} #YouTubeBeginner #HowTo
"""
    return desc


def generate_ideas(niche, count=5):
    """Generate video idea prompts for a niche."""
    niche = niche.strip() or "your niche"
    ideas = [
        f"Beginner's guide to {niche}",
        f"5 mistakes beginners make with {niche}",
        f"{niche} on a budget: what actually works",
        f"I asked experts about {niche} — here's what they said",
        f"{niche} in 2026: what's changed",
        f"Day in the life: {niche} edition",
        f"{niche} Q&A: answering your top questions",
    ]
    random.shuffle(ideas)
    chosen = ideas[:max(1, min(count, len(ideas)))]
    lines = [f"**Video ideas for '{niche}':**", ""]
    for i, idea in enumerate(chosen, 1):
        lines.append(f"{i}. {idea}")
    return "\n".join(lines)


def file_organiser_guide():
    """Return a simple file organisation guide."""
    return """## 🗂️ Organise Your Video Files

Use this simple folder structure for every video:

```
MyChannel/
  01_Scripts/
  02_Footage/
  03_Audio/
  04_Thumbnails/
  05_Exports/
  06_UploadReady/
```

**Naming rule:** `YYYY-MM-DD_topic_version`
Example: `2026-10-14_pocket-ai-demo_v1.mp4`

**Checklist:**
- [ ] Script saved in 01_Scripts
- [ ] Raw footage moved to 02_Footage
- [ ] Final export in 05_Exports
- [ ] Thumbnail (1280x720) in 04_Thumbnails
- [ ] Copy ready for upload in 06_UploadReady
"""


def upload_checklist():
    """Return a pre-upload checklist (approval step before automation)."""
    return """## ✅ Pre-Upload Checklist

Go through this BEFORE you hit publish. (Future versions can automate
uploads only after you tick every box.)

- [ ] Title written (under 60 characters ideally)
- [ ] Description written with keywords + hashtags
- [ ] Thumbnail uploaded (1280x720, < 2MB)
- [ ] Video file checked: correct resolution + audio levels
- [ ] End screen + cards added
- [ ] Playlist chosen
- [ ] Visibility set: Private → review → Public/Scheduled
- [ ] You approved the upload ✅

*Nothing uploads automatically in v1 — you stay in control.*
"""
