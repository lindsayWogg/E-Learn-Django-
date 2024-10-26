import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Vos informations d'identification Gmail
email_address = 'nextfoodafricamg@gmail.com'
email_password = 'ivyz bbjd rvfa rkym '

# Paramètres SMTP pour Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Destinataire
to_email = 'nextfoodafricamg@gmail.com'

# Créer un objet MIMEMultipart
message = MIMEMultipart()
message['From'] = email_address
message['To'] = to_email
message['Subject'] = 'test de mail'

# Corps du message
message_text = 'Bonjour, ceci est un e-mail envoyé depuis Python.'
message.attach(MIMEText(message_text, 'plain'))

# Établir une connexion SMTP sécurisée
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)

    # Envoyer l'e-mail
    server.sendmail(email_address, to_email, message.as_string())
    print('E-mail envoyé avec succès !')

except Exception as e:
    print('Erreur lors de l\'envoi de l\'e-mail :', str(e))

finally:
    # Fermer la connexion SMTP
    server.quit()
