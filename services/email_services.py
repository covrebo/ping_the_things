import smtplib, ssl, os
from typing import List


def email_report(report: List, batch: int):
    port = os.getenv("EMAIL_PORT")  # For starttls
    smtp_server = os.getenv("SMTP_SERVER")
    sender_email = os.getenv("SENDING_EMAIL")
    receiver_email = "@gmail.com"
    password = os.getenv("EMAIL_PW")
    if not password:
        password = input("Type your password and press enter:")
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    return None