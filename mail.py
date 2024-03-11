import pandas as pd
import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import argparse
# hello

parser = argparse.ArgumentParser(description='read the file')

parser.add_argument('--email_path', type=str , dest="email_path")
parser.add_argument("--password_path" , type=str , dest="password_path")
args = parser.parse_args()


from_addr='bhaarathabineshr2000@gmail.com'

data=pd.read_csv(args.email_path)            # Enter path of CSV files containing emails
to_addr=data['email'].tolist()      # Change'email' to column name containg emailids
name = data['name'].tolist()
subject = data['subject'].tolist()
content = data['content'].tolist()

l=len(name)
email="bhaarathabineshr2000@gmail.com"   #Enter Your email id here
data= pd.read_csv(args.password_path)

password=data['password'].tolist()
password=password[0]
      

for i in range (l):
    msg=MIMEMultipart()
    msg['From']=from_addr
    msg['To']=to_addr[i]
    msg['Subject']=subject[i]

    body=name[i] + content[i] 

    msg.attach(MIMEText(body,'plain'))

    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    text=msg.as_string()
    mail.sendmail(from_addr,to_addr[i],text)
    mail.quit()