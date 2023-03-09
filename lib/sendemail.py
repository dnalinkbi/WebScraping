import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.header import Header
from email import encoders

from datetime import datetime
import os, sys
import yaml

with open('config.yaml') as f:
		yaml = yaml.load(f, Loader=yaml.FullLoader)

sender = yaml['sender']
receiver = yaml['receiver']
carbon_copy = yaml['carbon_copy']
blind_carbon_copy = yaml['blind_carbon_copy']
password = yaml['password']


searchEngine=sys.argv[1]
keyword=sys.argv[2]

smtp = smtplib.SMTP('smtp.gmail.com', 587)

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Cc'] = carbon_copy
msg['Bcc'] = ''
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = Header(s=datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " " + searchEngine + " " + keyword + " monitoring TOP 20", charset='utf-8')
body = MIMEText('check your attachment', _charset='utf-8')
msg.attach(body)

files = searchEngine + 'scraping.txt'
attachment = open(files, "rb")
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', os.path.basename(files)))
msg.attach(part)

mailServer = smtplib.SMTP_SSL('smtp.gmail.com')
mailServer.login(sender, password)

mailServer.send_message(msg)
mailServer.quit()




