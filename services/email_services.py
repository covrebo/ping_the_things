import smtplib, ssl
from typing import List


def email_report(report: List, batch: int):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "@gmail.com"
    receiver_email = "@gmail.com"
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