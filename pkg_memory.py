import psutil
import time
import smtplib, ssl
#from mail_sender import *


def checkMemory():
    MEM_WARN_PERCENT = 80
    MEM_CRIT_PERCENT = 90
    SERVICE_NAME= 'Check_Memory'
    HOST= 'localhost'
    mail_HOST = 'ssl0.ovh.net'
    mail_HOST_PORT = 465
    mail_USER = 'postmaster@gblnlabs.com'
    mail_USER_PASSWD = '#Bd36aO%$wAX'
    mail_ACCOIUNT_SENDER = 'postmaster@gblnlabs.com'
    mail_TO_ALERT= 'kevingatti99@gmail.com'
    
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(mail_HOST, mail_HOST_PORT, context=context)
    server.login(mail_USER, mail_USER_PASSWD)
    
    mem_warn = (MEM_WARN_PERCENT / 100) * psutil.virtual_memory()[0]
    mem_crit = (MEM_CRIT_PERCENT / 100) * psutil.virtual_memory()[0]
    ##print(round(psutil.virtual_memory()[3], 1))
    ##print('USED: ', psutil.virtual_memory()[3], ' WARN: ', mem_warn, ' Crit: ', mem_crit)
    
    if (psutil.virtual_memory()[3] >= mem_crit):
        print('MEM CRIT: ', psutil.virtual_memory()[3])
        txt = 'Memory usege @: ', psutil.virtual_memory()[3]
        subj= SERVICE_NAME, 'Status Critical. Triggered on host: ', HOST
        
        message = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (mail_ACCOIUNT_SENDER, mail_TO_ALERT, subj, txt)
        
        server.sendmail(mail_ACCOIUNT_SENDER, mail_TO_ALERT, message)
        server.quit()
        
        print('Mail CRIT sento TO: ', mail_TO_ALERT)
        time.sleep(1)
    elif (psutil.virtual_memory()[3] >= mem_warn):
        print('MEM WARN: ', psutil.virtual_memory()[3])
        txt = 'Memory usege @: ', psutil.virtual_memory()[3]
        subj= SERVICE_NAME, 'Status Warning. Triggered on host: ', HOST 
        
        message = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (mail_ACCOIUNT_SENDER, mail_TO_ALERT, subj, txt)
        
        server.sendmail(mail_ACCOIUNT_SENDER, mail_TO_ALERT, message)
        server.quit()
        
        print('Mail WARN sento TO: ', mail_TO_ALERT)
        time.sleep(1)
    else:
        print('MEM OK: ', psutil.virtual_memory()[3])