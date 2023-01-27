from requests import get
import socket
import time
import datetime
import psutil
import platform
import math
import os
import json
import smtplib

##CONST VARS
MAIL_HOST = 'ssl0.ovh.net'
MAIL_HOST_PORT = 465
MAIL_USER = 'postmaster@gblnlabs.com'
MAIL_USER_PASSWD = '69x&@Z8ALOK!'
MAIL_ACCOIUNT_SENDER = 'postmaster@gblnlabs.com'
MAIL_ACCOIUNT_RECIEVER = 'chevin@duck.com'

smtp_server=smtplib.SMTP(MAIL_HOST,MAIL_HOST_PORT)
smtp_server.ehlo() #setting the ESMTP protocol
smtp_server.starttls() #setting up to TLS connection
smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
smtp_server.login(MAIL_ACCOIUNT_SENDER,MAIL_USER_PASSWD) #logging into out email id

msg_to_be_sent ='''
Hello, receiver!
Hope you are doing well.
Welcome to PythonGeeks!
'''
#sending the mail by specifying the from and to address and the message 
smtp_server.sendmail(MAIL_ACCOIUNT_SENDER,MAIL_ACCOIUNT_RECIEVER,msg_to_be_sent)
print('Successfully the mail is sent') #priting a message on sending the mail
smtp_server.quit()#terminating the server

data = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os_platform": platform.system(),
        "os_distro": platform.release(),
        "os_version": platform.version(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "wan_ip": get('https://api.ipify.org').content.decode('utf8'),
        "hostname": socket.gethostname(),
        "domain": ".lcl",
        "ram_tot": round(psutil.virtual_memory()[0]/1073741824, 1),
        "ram_used": round(psutil.virtual_memory()[3]/1073741824, 1),
        "ram_used_percent": psutil.virtual_memory().percent,
        "storage_path": "/",
        "storage_percent": psutil.disk_usage('/')[3],
        "storage_free": round(psutil.disk_usage('/')[2]/1073741824, 0),
        "storage_used": round(psutil.disk_usage('/')[1]/1073741824, 0),
        "sorage_tot": round(psutil.disk_usage('/')[0]/1073741824, 0),
        "cpu": psutil.cpu_percent(interval=None, percpu=False)
        }