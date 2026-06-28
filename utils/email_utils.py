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
    """Envia um e-mail com imagem e/ou anexo de texto."""

    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    # Anexa imagem
    if imagem_bytes is not None:
        try:
            img = MIMEImage(imagem_bytes)
            img.add_header(
                "Content-Disposition",
                "attachment",
                filename=imagem_nome,
            )
            msg.attach(img)
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {e}")
            return False

    # Anexa arquivo texto
    if anexo_texto is not None:
        try:
            anexo = MIMEApplication(
                anexo_texto.encode("utf-8"),
                Name=anexo_texto_nome,
            )
            anexo.add_header(
                "Content-Disposition",
                "attachment",
                filename=anexo_texto_nome,
            )
            msg.attach(anexo)
        except Exception as e:
            st.error(f"Erro ao criar o anexo: {e}")
            return False

    # Envio do e-mail
    try:
        contexto = ssl.create_default_context()

        with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
            server.starttls(context=contexto)
            server.login(remetente, senha)
            server.send_message(msg)

        return True

    except Exception as e:
        st.error(f"Erro ao enviar o e-mail: {e}")
        return False