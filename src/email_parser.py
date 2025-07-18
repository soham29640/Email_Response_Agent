import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_reply(subject, sender, body):
    if subject is None or sender is None or body is None:
        return None

    prompt = f"""
You are an intelligent email assistant. Read the following email and write a polite, professional reply.
End the reply with: "Sincerely, Soham Samanta"

Email Subject: {subject}
Email From: {sender}
Email Body:
{body}

Reply:
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating reply: {e}"
