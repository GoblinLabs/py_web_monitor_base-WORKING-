import smtplib, ssl

def sendMail(subject, body, to):
        mail_HOST = 'ssl0.ovh.net'
        mail_HOST_PORT = 465
        mail_USER = 'postmaster@gblnlabs.com'
        mail_USER_PASSWD = '69x&@Z8ALOK!'
        mail_ACCOIUNT_SENDER = 'postmaster@gblnlabs.com'
        #mail_ACCOIUNT_RECIEVER = 'kevingatti99@gmail.com'
        
        
        ### EMAIL BODY ETC.
        
        #mail_SUBJECT = ('Subject') 
        #mail_BODY = ('Dear. We are happy to say....')
        
        message = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (mail_ACCOIUNT_SENDER, to, subject, body)
        ##% (mail_ACCOIUNT_SENDER, mail_ACCOIUNT_RECIEVER, mail_SUBJECT, mail_BODY) 
        
        ### EMAIL SENT
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(mail_HOST, mail_HOST_PORT, context=context)
        server.login(mail_USER, mail_USER_PASSWD)
        server.sendmail(mail_ACCOIUNT_SENDER, to, message)
        server.quit()
