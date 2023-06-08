from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_confirmation_email(user):
    message = Mail(
        from_email='fabio1010c@hotmail.com',
        to_emails=user.email,
        subject='Confirmação de registro',
        html_content='<strong>Clique no link abaixo para confirmar seu registro:</strong>'
                     f'<a href="http://seu-site.com/confirmar/{user.pk}">Confirmar Registro</a>'
    )

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
