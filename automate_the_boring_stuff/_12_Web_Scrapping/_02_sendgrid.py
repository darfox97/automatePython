import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


apiemail = os.environ.get("SENDGRID_EMAIL")

mensaje = Mail(
    from_email=apiemail,
    to_emails=apiemail,
    subject="Correo de prueba",
    html_content="<b>Primer email</b> enviado con sendgrid."
)

try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(respuesta.status_code, respuesta.body, respuesta.headers)
except Exception as e:
    print(e)
