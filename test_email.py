import imaplib
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# --- Test IMAP (receiving) ---
try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Change if not Gmail
    mail.login(EMAIL_USER, EMAIL_PASS)
    print("✅ IMAP Login Successful")
    mail.logout()
except Exception as e:
    print("❌ IMAP Login Failed:", e)

# --- Test SMTP (sending) ---
try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Change if not Gmail
    smtp_server.login(EMAIL_USER, EMAIL_PASS)
    print("✅ SMTP Login Successful")
    smtp_server.quit()
except Exception as e:
    print("❌ SMTP Login Failed:", e)
