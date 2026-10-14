"""
app.py
Pocket AI Assistant - mobile-friendly Streamlit chat interface.
Run with: streamlit run app.py
No API keys needed. Works offline (after pip install).
"""

import streamlit as st
from agent import PocketAgent

# --- Page setup (mobile-friendly: centered, collapsed sidebar) ---
st.set_page_config(
    page_title="Pocket AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Small CSS tweaks for phones: bigger tap targets, comfy chat ---
st.markdown(
    """
    <style>
    .stButton > button { width: 100%; padding: 0.7rem; font-size: 1rem; }
    .stChatInput { position: sticky; bottom: 0; }
    h1 { font-size: 1.6rem !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Initialise agent + chat history (kept in session state) ---
if "agent" not in st.session_state:
    st.session_state.agent = PocketAgent()
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Hi! I'm **Pocket AI**, your YouTube helper.\n\n"
                "Tap a button below or type `help` to see what I can do."
            ),
        }
    ]

st.title("🤖 Pocket AI Assistant")
st.caption("Your offline YouTube helper — scripts, titles, descriptions & more.")

# --- Quick-action buttons (big and thumb-friendly) ---
col1, col2 = st.columns(2)
with col1:
    if st.button("📝 Video script"):
        st.session_state.messages.append(
            {"role": "user", "content": "script about my next video"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond(
                 "script about my next video")})
        st.rerun()
    if st.button("🏷️ Titles"):
        st.session_state.messages.append(
            {"role": "user", "content": "titles for my next video"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond(
                 "titles for my next video")})
        st.rerun()
    if st.button("🗂️ Organise files"):
        st.session_state.messages.append(
            {"role": "user", "content": "organise my files"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond("organise my files")})
        st.rerun()
with col2:
    if st.button("📄 Description"):
        st.session_state.messages.append(
            {"role": "user", "content": "description for my next video"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond(
                 "description for my next video")})
        st.rerun()
    if st.button("💡 Video ideas"):
        st.session_state.messages.append(
            {"role": "user", "content": "ideas for my niche"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond("ideas for my niche")})
        st.rerun()
    if st.button("✅ Upload checklist"):
        st.session_state.messages.append(
            {"role": "user", "content": "upload checklist"})
        st.session_state.messages.append(
            {"role": "assistant",
             "content": st.session_state.agent.respond("upload checklist")})
        st.rerun()

st.divider()

# --- YouTube Studio: guided forms (easier than typing commands) ---
with st.expander("🎬 YouTube Studio — guided tools", expanded=False):
    from youtube_helpers import (
        generate_script, generate_titles,
        generate_description, generate_ideas,
    )

    tool = st.selectbox(
        "Choose a tool",
        ["Video script", "Titles", "Description", "Video ideas"],
    )
    if tool == "Video script":
        topic = st.text_input("Topic", placeholder="e.g. how to edit videos on phone")
        minutes = st.slider("Length (minutes)", 1, 15, 5)
        tone = st.selectbox("Tone", ["friendly", "funny", "professional", "casual"])
        if st.button("Generate script"):
            if topic.strip():
                st.markdown(generate_script(topic, minutes, tone))
            else:
                st.warning("Please enter a topic first.")
    elif tool == "Titles":
        topic = st.text_input("Topic", placeholder="e.g. morning routine", key="t2")
        if st.button("Generate titles"):
            st.markdown(generate_titles(topic) if topic.strip()
                        else "Please enter a topic first.")
    elif tool == "Description":
        topic = st.text_input("Topic", placeholder="e.g. pocket ai demo", key="t3")
        keywords = st.text_input("Keywords (optional)", key="k3")
        if st.button("Generate description"):
            st.markdown(generate_description(topic, keywords)
                        if topic.strip() else "Please enter a topic first.")
    else:
        niche = st.text_input("Your niche", placeholder="e.g. tech reviews", key="t4")
        if st.button("Generate ideas"):
            st.markdown(generate_ideas(niche) if niche.strip()
                        else "Please enter your niche first.")

st.divider()

# --- Chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
if prompt := st.chat_input("Ask me about your next video… (try 'help')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    reply = st.session_state.agent.respond(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

# --- Footer ---
st.divider()
st.caption(
    "v1 • 100% offline, no API keys • "
    "WhatsApp + auto-upload come later, always with your approval ✅"
)
