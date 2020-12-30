import os
import smtplib
from datetime import datetime
from plyer import notification as nt
import pandas as pd
from email.message import EmailMessage
import imghdr

my_name = os.environ['MY_NAME']
my_email = os.environ["EMAIL_ADDRESS"]
my_password = os.environ["EMAIL_PASSWORD"]

def send_mail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, my_password)
    server.send_message(msg)
    server.close()


df = pd.read_excel('event_list.xlsx')
today = int(datetime.now().strftime("%d%m"))


for i, j in df.iterrows():
    event_date = j['Date']
    if event_date == today and int(datetime.now().strftime("%Y")) == j['Year']:
        nt.notify(
            title = j['Name'] + "'s " + j['Event'] + "!",
            message = j['Event'] + " wish sent!",
            timeout = 10,
            app_icon = "D:\\PythonProjects\\Extras\\automatic_event_wisher\\event.ico"
        )
        if j['Email'] != 'BLANK':
            emails = j['Email'].split(',')
            for email in emails:
                msg = EmailMessage()
                msg['Subject'] = j['Subject']
                msg['From'] = my_name
                msg['To'] = email
                msg.set_content(f"{j['Message']}\n\n{my_name}")

                if j['Image'] != 'BLANK':
                    images = j['Image'].split(',')
                    for image in images:
                        with open(image, 'rb') as f:
                            image_data = f.read()
                            image_type = imghdr.what(f.name)
                        msg.add_attachment(image_data, maintype = "image", subtype = image_type, filename = "memory")
                send_mail(msg)
            df.loc[i, 'Year'] += 1
            df.to_excel('event_list.xlsx', index = False)
    continue
