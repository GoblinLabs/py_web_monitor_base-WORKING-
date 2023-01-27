import psutil
import time
from mail_sender import *

def checkMemory():
    MEM_WARN_PERCENT = 80
    MEM_CRIT_PERCENT = 90
    SERVICE_NAME= 'Check_Memory'
    HOST= 'localhost'
    MAIL_TO_ALERT= 'chevin@duck.com'
    
    mem_warn = (MEM_WARN_PERCENT / 100) * psutil.virtual_memory()[0];
    mem_crit = (MEM_CRIT_PERCENT / 100) * psutil.virtual_memory()[0];
    ##print(round(psutil.virtual_memory()[3], 1))
    ##print('USED: ', psutil.virtual_memory()[3], ' WARN: ', mem_warn, ' Crit: ', mem_crit)
    
    if (psutil.virtual_memory()[3] >= mem_crit):
        print('MEM CRIT: ', psutil.virtual_memory()[3])
        txt = 'Memory usege @: ', psutil.virtual_memory()[3]
        subj= SERVICE_NAME, 'Status Critical. Triggered on host: ', HOST
        sendMail(subj, txt, MAIL_TO_ALERT)
        print('Mail CRIT sento TO: ', MAIL_TO_ALERT)
        time.sleep(1)
    elif (psutil.virtual_memory()[3] >= mem_warn):
        print('MEM WARN: ', psutil.virtual_memory()[3])
        txt = 'Memory usege @: ', psutil.virtual_memory()[3]
        subj= SERVICE_NAME, 'Status Warning. Triggered on host: ', HOST 
        sendMail(subj, txt, MAIL_TO_ALERT)
        print('Mail WARN sento TO: ', MAIL_TO_ALERT)
        time.sleep(1)
    else:
        print('MEM OK: ', psutil.virtual_memory()[3])