# ✉️ Email Response Agent

A simple AI-powered email assistant that:
- Fetches unread emails
- Summarizes message using LLM
- Suggests auto-replies
- Sends replies via SMTP
- Includes a Streamlit dashboard

## 📁 Structure

- `src/email_reader.py` → fetch emails
- `src/llm_responder.py` → generate reply
- `src/email_sender.py` → send reply

## 🛠️ Setup

1. Fill `.env` with Gmail + OpenAI keys
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run main.py
