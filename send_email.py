from email.mime.text import MIMEText
import smtplib

def send_email(email,height,weight):
    source='devneedsmail@gmail.com'
    password='******'
    dest=email
    subject="Body Mass Index"
    h=int(height)/100
    bmi=int(weight)/(h**2)
    message='Your height and weight respectively is <strong>%s %s</strong> and your BMI is <strong>%s</strong>'%(height,weight,bmi)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=dest
    msg['From']=source

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(source,password)
    gmail.send_message(msg)

