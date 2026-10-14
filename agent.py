"""
agent.py
The "brain" of the Pocket AI Assistant.
Simple rule-based logic - no API keys, no internet needed.
Beginner-friendly: read the respond() method to see how it picks answers.
"""

from youtube_helpers import (
    generate_script,
    generate_titles,
    generate_description,
    generate_ideas,
    file_organiser_guide,
    upload_checklist,
)


class PocketAgent:
    """A tiny offline assistant that helps with YouTube workflow."""

    def __init__(self, name="Pocket AI"):
        self.name = name

    def respond(self, message):
        """
        Take a user message (str) and return a reply (str).
        Intent detection is keyword-based so it always works offline.
        """
        text = message.lower().strip()

        if not text:
            return "Say something to get started — try 'help'."

        # Greetings
        if any(w in text for w in ["hello", "hi", "hey", "salam", "assalam"]):
            return (
                "Hello! 👋 I'm your Pocket AI assistant.\n\n"
                "I can help you:\n"
                "- 📝 Write a video **script**\n"
                "- 🏷️ Generate **titles**\n"
                "- 📄 Write a **description**\n"
                "- 💡 Brainstorm **video ideas**\n"
                "- 🗂️ **Organise** your files\n"
                "- ✅ Make an **upload checklist**\n\n"
                "Try: `script about cooking biryani` or tap a button above."
            )

        # Help
        if "help" in text or "what can you do" in text:
            return (
                "**Here's what I understand:**\n"
                "- `script about <topic>` → full script outline\n"
                "- `titles for <topic>` → 5 title ideas\n"
                "- `description for <topic>` → description + hashtags\n"
                "- `ideas for <niche>` → video ideas\n"
                "- `organise` → file organisation guide\n"
                "- `checklist` → pre-upload checklist\n"
                "- `whatsapp` → what's planned for WhatsApp control\n\n"
                "Example: `script about morning routines, 5 minutes, funny`"
            )

        # WhatsApp roadmap
        if "whatsapp" in text:
            return (
                "📱 **WhatsApp control (coming later):**\n\n"
                "The plan is: you message the assistant on WhatsApp, it drafts "
                "scripts/titles, and only uploads to YouTube **after you approve**.\n\n"
                "v1 here is the chat brain. Later versions can connect via the "
                "WhatsApp Business API + YouTube Data API (both need setup and "
                "your explicit approval for uploads)."
            )

        # Script generation: "script about X" or "script: X"
        if "script" in text:
            topic = self._extract_after(text, ["about", "for", "script:", "script"])
            tone = "funny" if "funny" in text else (
                "professional" if "professional" in text else "friendly"
            )
            minutes = 5
            for n in ["3", "5", "7", "10"]:
                if f"{n} min" in text or f"{n} minutes" in text:
                    minutes = int(n)
            return generate_script(topic or "your video topic",
                                   duration_minutes=minutes, tone=tone)

        # Titles
        if "title" in text:
            topic = self._extract_after(text, ["for", "about", "titles:", "title:"])
            return generate_titles(topic or "your video topic")

        # Description
        if "description" in text:
            topic = self._extract_after(text, ["for", "about", "description:"])
            return generate_description(topic or "your video topic")

        # Ideas
        if "idea" in text:
            niche = self._extract_after(text, ["for", "about", "ideas:"])
            return generate_ideas(niche or "your niche")

        # Organise files
        if "organis" in text or "organize" in text or "files" in text:
            return file_organiser_guide()

        # Upload checklist
        if "checklist" in text or "upload" in text:
            return upload_checklist()

        # Fallback
        return (
            "Hmm, I'm not sure I got that. 🤔\n\n"
            "Try one of these:\n"
                "- `script about <your topic>`\n"
                "- `titles for <your topic>`\n"
                "- `description for <your topic>`\n"
                "- `ideas for <your niche>`\n"
                "- `organise my files`\n\n"
            "Or type `help`."
        )

    @staticmethod
    def _extract_after(text, markers):
        """Return the text after the first matching marker, cleaned up."""
        for m in markers:
            if m in text:
                after = text.split(m, 1)[1].strip(" :,-")
                # Remove trailing modifiers like ", 5 minutes, funny"
                for sep in [", 5 minutes", ", 3 minutes", ", funny",
                            ", professional", ", friendly"]:
                    after = after.replace(sep, "")
                return after.strip()
        return ""
