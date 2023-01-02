import time
import json
import time
import datetime
import socket
import psutil
import time
import platform
import math
import os

HOST = "127.0.0.1"
PORT = 8080

#TO GET ONCE
get_hostname = (socket.gethostname())
get_local_ip = (socket.gethostbyname(socket.gethostname()))
get_os_name = platform.system()
get_os_version = platform.platform()
#get_uptime = os.popen('uptime -p').read()[:-1]


#TO UPDATE EVERY TOT SECONDS
#RAM
get_ram_percent = psutil.virtual_memory()[2]
get_ram = round(psutil.virtual_memory()[0]/1000000000, 1)
get_ram_gb = round(psutil.virtual_memory()[3]/1000000000, 1)

#CPU

#STORAGE

get_storage_tot = round(psutil.disk_usage('/')[0]/1000000000, 0)
get_storage_used = round(psutil.disk_usage('/')[1]/1000000000, 0)
get_storage_free = round(psutil.disk_usage('/')[2]/1000000000, 0)

#NETWORK

data = {"data":[
      {
         "id": "1",
         "maintenance": "false",
         "ip": get_local_ip,
         "hostname": get_hostname,
         "os_name": get_os_name,
         "os_version": get_os_version,
         "uptime": "",
         "ram_used": get_ram_gb,
         "ram_tot": get_ram,
         "storage_free": get_storage_free,
         "storage_used": get_storage_used,
         "sorage_tot": get_storage_tot,
         "cpu": ""
      },
   ],}
json_string = json.dumps(data)
