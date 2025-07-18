import time
import os
from dotenv import load_dotenv
load_dotenv()
from src.email_reader import FetchLatestEmail
from src.email_parser import generate_reply
from src.email_sender import send_email_reply

email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")

def should_continue():
    with open("controller.txt","r") as f:
        return f.read().strip().lower() != "stop"
    
print("📬 Email Agent Running... Type 'stop' in controller.txt to stop.")

def main():
    client = FetchLatestEmail(email_user, email_pass)
    subject = client.get_subject()
    sender = client.get_sender()
    body = client.get_body()

    if not subject or not sender or not body:
        print("📭 No new unseen email found.")
        return

    reply = generate_reply(subject, sender, body)

    if reply:
        print("\nGenerated Reply:\n")
        print(reply)
        send_email_reply(sender, subject, reply)
    else:
        print("❌ Failed to generate reply.")


while should_continue():
    try:
        main()
    except Exception as e:
        print("Error:", e)
    time.sleep(60)  



