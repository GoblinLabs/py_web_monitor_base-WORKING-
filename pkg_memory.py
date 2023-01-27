import psutil
import time
import socket
import time
import datetime

def checkMemory():
    warn_PERCENT = 80
    crit_PERCENT = 90
    service_NAME= 'Check_Memory'
    service_pkg=psutil.virtual_memory()[3]
    host= socket.gethostname()
    lan_ip= socket.gethostbyname(socket.gethostname())
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    mem_warn = (warn_PERCENT / 100) * psutil.virtual_memory()[0]
    mem_crit = (crit_PERCENT / 100) * psutil.virtual_memory()[0]
    
    if (psutil.virtual_memory()[3] >= mem_crit):
        print(timestamp, ' Node:', host, '|', lan_ip, '=>' ,'MEM CRIT:', service_pkg)
        time.sleep(1)
    elif (psutil.virtual_memory()[3] >= mem_warn):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Node:', host, '|', lan_ip, '=>' , 'MEM WARN:', service_pkg)
        time.sleep(1)
    else:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Node:', host, '|', lan_ip, '=>' ,'MEM OK:', service_pkg)