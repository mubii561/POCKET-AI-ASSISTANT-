# 🤖 Pocket AI Assistant (v1)

A beginner-friendly, **100% offline** personal AI assistant for YouTubers.
Chat with it to generate video scripts, titles, descriptions, ideas,
organise your files, and prepare uploads — no API keys, no paid services.

> **Goal:** eventually control this from WhatsApp. v1 is the chat brain
> with a mobile-friendly web UI. WhatsApp + auto-upload come later,
> always **after your approval**.

---

## ✨ What it does (v1)

- 💬 Mobile-friendly chat interface (Streamlit)
- 📝 Video script generator (topic → full outline)
- 🏷️ Title ideas generator
- 📄 Description + hashtag generator
- 💡 Video idea brainstormer
- 🗂️ File organisation guide
- ✅ Pre-upload checklist (approval-first: nothing uploads automatically)

All logic is rule-based in `agent.py` + `youtube_helpers.py` — it works
without internet once installed.

---

## 📁 Project structure

```
pocket-ai-assistant/
├── app.py                # Streamlit chat UI (start here)
├── agent.py              # Assistant "brain" - understands your messages
├── youtube_helpers.py    # Script/title/description generators (offline)
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .streamlit/
    └── config.toml       # Theme + mobile-friendly settings
```

---

## 🚀 Run it on your computer

```bash
cd pocket-ai-assistant
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL it shows (usually http://localhost:8501).

---

## 📱 Run it from an Android phone

### Option A — Streamlit Cloud (easiest, recommended, free)

No Python install needed on your phone. You deploy once, then use it
like any website.

1. On your phone's Chrome, create free accounts at **github.com**
   and **share.streamlit.io**.
2. Upload this project to GitHub:
   - In the GitHub app/site, create a new repository called
     `pocket-ai-assistant`.
   - Upload all files (`app.py`, `agent.py`, `youtube_helpers.py`,
     `requirements.txt`, `README.md`, `.streamlit/config.toml`).
     Keep the folder structure the same.
3. Go to **share.streamlit.io** → **New app** → connect your GitHub
   → pick the repository → set main file to `app.py` → **Deploy**.
4. Wait 2–3 minutes. You get a free public link like
   `https://your-app.streamlit.app` — bookmark it, add to home screen.
5. To update: just upload new versions of the files to GitHub;
   Streamlit redeploys automatically.

### Option B — Termux (runs fully on your phone, offline after install)

1. Install **Termux** from F-Droid (not Play Store — the Play version
   is outdated).
2. In Termux, run:
   ```bash
   pkg update && pkg install python -y
   pip install -r requirements.txt
   ```
   (Copy the project folder to your phone first, then `cd` into it.)
3. Start the app:
   ```bash
   streamlit run app.py
   ```
4. Open the local URL Termux prints in Chrome.
   Tip: keep the phone awake while it runs.

### Option C — Ask me to test/fix

If anything breaks, paste the error message here and I'll fix it.

---

## 🧪 Try these first

In the chat, type:

- `help`
- `script about how to edit videos on a phone, 5 minutes, funny`
- `titles for morning routine`
- `description for pocket ai demo`
- `ideas for tech reviews`
- `organise my files`
- `upload checklist`
- `whatsapp` (see the roadmap)

---

## 🗺️ Roadmap (after v1 works)

- [ ] Connect to WhatsApp (via WhatsApp Business API / bot)
- [ ] YouTube Data API for uploads — **only after you tap approve**
- [ ] Save drafts to Google Drive / phone folders
- [ ] Voice notes: send a voice message, get a script back

Nothing in v1 uploads or messages anyone. Approval-first by design.

---

## 🤝 Beginner notes

- `app.py` = what you see. `agent.py` = how it understands you.
  `youtube_helpers.py` = the actual generators. Start reading in that order.
- To add a new command: add a keyword check in `agent.py`'s
  `respond()` method, then write a helper in `youtube_helpers.py`.
- No secrets in this project. If you later add API keys, never commit
  them to GitHub — use Streamlit's **Secrets** settings instead.

Made with ❤️ — v1, offline and free.
