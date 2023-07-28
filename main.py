import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, receiver_email, password):
    #Setupo the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    #The body and the attachments for the mail
    message.attach(MIMEText(body, 'plain'))

    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    #start tls for security
    session.starttls()

    #Authentication
    session.login(sender_email, password)

    #send the mail
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()

    subject = "Newsletter Subject"
    body = "This is your monthly newsletter"
    sender_email = "your_email@gmal.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_password"

    send_email(subject, body, sender_email, receiver_email, password)