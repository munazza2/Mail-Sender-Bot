import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


server_login_mail = '' #write your email to send email
server_login_password = ''#write your email password

server.login(server_login_mail,server_login_password)


email=EmailMessage()

email['From'] = server_login_mail
email['To'] = '' #write email here on which you have to send message
email['Subject'] = '' #write subject here
email.set_content('') #write message here
server.send_message(email)