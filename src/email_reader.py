import imaplib
import email

class FetchLatestEmail:
    def __init__(self, email_user, email_pass):
        self.user = email_user
        self.password = email_pass
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.mail.login(self.user, self.password)
        self.mail.select("inbox")

        _, data = self.mail.search(None, '(UNSEEN)')
        self.mail_ids = data[0].split()
        self.latest_email_id = self.mail_ids[-1] if self.mail_ids else None

    def _fetch_email_message(self):
        if not self.latest_email_id:
            return None

        _, msg_data = self.mail.fetch(self.latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        return email.message_from_bytes(raw_email)

    def get_subject(self):
        msg = self._fetch_email_message()
        return msg["subject"] if msg else None

    def get_sender(self):
        msg = self._fetch_email_message()
        return msg["from"] if msg else None

    def get_body(self):
        msg = self._fetch_email_message()
        if msg is None:
            return None
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
        return None
