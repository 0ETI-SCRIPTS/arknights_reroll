import imaplib
import smtplib

import datetime
import re
import os

import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from ark_config import (
    FROM_EMAIL,
    FROM_PWD
)

ORG_EMAIL   = "@gmail.com"
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def get_recent_code():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        status, data = mail.search(
            None, 
            "(FROM 'info@mail.yo-star.com') (UNSEEN)"
        )

        for index, num in enumerate(data[0].split()):
            status, message_data = mail.fetch(num, "(RFC822)")

            raw_email = message_data[0][1]

            # Construct an email message object for ease of use
            email_message = email.message_from_bytes(raw_email)
            # print(email_message["To"])
            # print(email.utils.parseaddr(email_message['From']))
            # print(email_message["Subject"])

            content_type = email_message.get_content_type()
            body = email_message.get_payload(decode=True).decode()

            code = re.search(r"\d{6}", body).group(0)

            return code if code else None

    except Exception as e:
        print(str(e))


def send_image(img_path, subject):
    img_data = open(img_path, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = str(subject)
    msg['From'] = FROM_EMAIL
    msg['To'] = FROM_EMAIL

    text = MIMEText("Shot @ {0}".format(datetime.datetime.now()))
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(img_path))
    msg.attach(image)

    s = smtplib.SMTP_SSL(SMTP_SERVER)
    s.login(FROM_EMAIL, FROM_PWD)
    s.sendmail(FROM_EMAIL, FROM_EMAIL, msg.as_string())
    s.quit()


# print(get_recent_code())
# send_image("./test.jpg", "Patchouli")
