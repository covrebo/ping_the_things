import smtplib, ssl, os
from typing import List, Dict


def email_report(report: List, changes: Dict, batch: int):
    # get the hosts that are down and convert to format the message can use
    down_hosts = ""
    for result in report:
        if result[1] == 0:
            down_hosts = down_hosts + "\t" + result[0] + "\n"

    # get the hosts that are up and convert to format the message can use
    up_hosts = ""
    for result in report:
        if result[1] == 1:
            up_hosts = up_hosts + "\t" + result[0] + "\n"

    # get the changes and convert to message format
    now_up_hosts = ""
    for item in changes["now_up"]:
        now_up_hosts = now_up_hosts + "\t" + item[0] + " which is " + item[
            1] + "\n"
    if not now_up_hosts:
        now_up_hosts = "\tNo changes"

    now_down_hosts = ""
    for item in changes["now_down"]:
        now_down_hosts = now_down_hosts + "\t" + item[0] + " which is " + item[1] + "\n"
    if not now_down_hosts:
        now_down_hosts = "\tNo changes."

    new_hosts = ""
    for item in changes["new_host"]:
        new_hosts = new_hosts + "\t" + item[0] + " which is " + item[1] + "\n"
    if not new_hosts:
        new_hosts = "\tNo changes."

    no_change_hosts = ""
    for item in changes["no_change"]:
        no_change_hosts = no_change_hosts + "\t" + item[0] + " which is " + \
                          item[1] + "\n"
    if not no_change_hosts:
        no_change_hosts = "\tNo changes."

    port = os.getenv("EMAIL_PORT")  # For starttls
    smtp_server = os.getenv("SMTP_SERVER")
    sender_email = os.getenv("SENDING_EMAIL")
    receiver_email = "@gmail.com"
    password = os.getenv("EMAIL_PW")
    if not password:
        password = input("Type your password and press enter:")
    message = """Subject: Network Report No. {batch}\n
    
    ###  THESE HOSTS ARE DOWN  ###
    {down_hosts}
    
    ###  THESE HOSTS ARE UP  ###
    {up_hosts}
    
    -----------
    CHANGES
    -----------
    
    ###  THESE HOSTS HAVE CHANGED TO UP  ###
    {now_up_hosts}
    
    ###  THESE HOSTS HAVE CHANGED TO DOWN  ###
    {now_down_hosts}
    
    ###  THESE HOSTS ARE NEW  ###
    {new_hosts}
    
    ###  THESE HOSTS ARE UNCHANGED  ###
    {no_change_hosts}
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(
            sender_email,
            receiver_email,
            message.format(
                batch=batch,
                down_hosts=down_hosts,
                up_hosts=up_hosts,
                now_up_hosts=now_up_hosts,
                now_down_hosts=now_down_hosts,
                new_hosts=new_hosts,
                no_change_hosts=no_change_hosts))

    return None
