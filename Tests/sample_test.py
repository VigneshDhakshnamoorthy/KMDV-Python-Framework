import configparser
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def test_sample():
    s = smtplib.SMTP(host='outlook.office365.com', port=587)
    s.starttls()
    s.login("email", "psd")
    msg = MIMEMultipart()
    try:
        with open("../Report/report.html", 'r') as f:
            attach = f.read()
    except FileNotFoundError:
        with open(f"{os.getcwd()}/Report/report.html", 'r') as f:
            attach = f.read()
    message = "Hi Test Message"
    print(message)
    msg['From'] = "frommail"
    msg['To'] = "tomail"
    msg['Subject'] = "This is TEST"
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(attach, 'html'))

    s.send_message(msg)
    del msg
    s.quit()
