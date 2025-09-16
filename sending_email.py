import smtplib, ssl
from mail_pass import mail, passwords, rec

def send_mail(massage):
    host = "smtp.gmail.com"
    port = 465

    username = mail
    password = passwords

    context = ssl.create_default_context()

    receiver = rec

    message = """\
    Subject : Test
    This message is send via python script by Shamim from Shamim"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
