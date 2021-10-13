from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def envia_email(email_cliente, login, senha, mensagem, assunto):
    msg = MIMEMultipart()
    msg["from"] = login
    msg["to"] = email_cliente
    msg["subject"] = assunto
    corpo = MIMEText(mensagem, 'html')
    msg.attach(corpo)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(login, senha)
        smtp.send_message(msg)