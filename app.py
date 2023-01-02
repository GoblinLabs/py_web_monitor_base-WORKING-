from flask import Flask, render_template

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


#TO GET ONCE
hostname = (socket.gethostname())
get_local_ip = (socket.gethostbyname(socket.gethostname()))
get_os_version = platform.platform()
#get_uptime = os.popen('uptime -p').read()[:-1]


#TO UPDATE EVERY TOT SECONDS
#RAM

get_ram_gb = round(psutil.virtual_memory()[3]/1000000000, 1)

#CPU

#STORAGE
get_storage_tot = round(psutil.disk_usage('/')[0]/1000000000, 0)
get_storage_used = round(psutil.disk_usage('/')[1]/1000000000, 0)
get_storage_free = round(psutil.disk_usage('/')[2]/1000000000, 0)



app = Flask('testapp') 

@app.route('/')
def index():
    return render_template('index.html', variable='12345', hostname=hostname, get_local_ip=get_local_ip, get_os_version=get_os_version, get_ram_gb=get_ram_gb, get_storage_used=get_storage_used, get_storage_tot=get_storage_tot)


if __name__ == '__main__':
    app.run()