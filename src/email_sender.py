import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
load_dotenv()

email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")

def send_email_reply(to, subject, body):
    subject = subject.replace('\n', ' ').replace('\r', ' ').strip()

    msg = EmailMessage()
    msg['Subject'] = f"Re: {subject}"
    msg['From'] = email_user
    msg['To'] = to
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_user, email_pass)
            smtp.send_message(msg)
        print("✅ Reply sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

