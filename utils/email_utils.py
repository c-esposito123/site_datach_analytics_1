import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit as st


def enviar_email(
    remetente: str,
    senha: str,
    destinatario: str,
    assunto: str,
    corpo: str,
    imagem_bytes: bytes | None = None,
    imagem_nome: str = "grafico.png",
    anexo_texto: str | None = None,
    anexo_texto_nome: str = "relatorio.txt",
):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    if imagem_bytes is not None:
        img = MIMEImage(imagem_bytes, name=imagem_nome)
        img.add_header("Content-Disposition", "attachment", filename=imagem_nome)
        msg.attach(img)

    if anexo_texto is not None:
        anexo = MIMEApplication(anexo_texto.encode("utf-8"), Name=anexo_texto_nome)
        anexo.add_header("Content-Disposition", "attachment", filename=anexo_texto_nome)
        msg.attach(anexo)

    contexto = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as servidor:
        servidor.starttls(context=contexto)
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
