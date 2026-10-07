import smtplib
from email.mime.text import MIMEText
from processEmails import process_emails

def send_email(recipients, subject, body, sender, password):
    """
    send the email to intended recipients 
    """
    recipients = process_emails(recipients)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients) #join multiple emails

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string)
        print(f"emal sent to: {recipients}")

