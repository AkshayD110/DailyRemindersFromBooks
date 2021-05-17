####################################
# File name: eventCreator.py       #
# Author: Akshay Deshpande         #
# Date created : 16th May 2021     #
# Last modified : 17th May 2021   #
####################################
import smtplib
import ssl
from email.message import EmailMessage

import config


class SendingMail:
    """Sends an email with your selected kindle highlights."""

    def __init__(self, highlights_selected_for_mail):
        self.highlights_selected_for_mail = highlights_selected_for_mail

    def __repr__(self):
        return f'{self.__class__.__name__}({self.highlights_selected_for_mail})'

    @property
    def highlights_selected_for_mail(self):
        return self._highlights_selected_for_mail

    @highlights_selected_for_mail.setter
    def highlights_selected_for_mail(self, highlights_selected_for_mail):
        self._highlights_selected_for_mail = highlights_selected_for_mail

    def sendmail(self):
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = config.sender_email
        receiver_email = config.receiver_email
        password = config.password

        msg = EmailMessage()
        msg.set_content(self.highlights_selected_for_mail)
        msg['Subject'] = "Daily Kindle Highlights"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.send_message(msg)
