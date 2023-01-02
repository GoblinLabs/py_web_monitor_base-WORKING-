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
"""
data = {
         "ip": socket.gethostbyname(socket.gethostname()),
         "hostname": socket.gethostname(),
         "domain": ".lcl",
         "os_version": platform.platform(),
         "ram_used": round(psutil.virtual_memory()[3]/1000000000, 1),
         "storage_free": round(psutil.disk_usage('/')[2]/1000000000, 0),
         "storage_used": round(psutil.disk_usage('/')[1]/1000000000, 0),
         "sorage_tot": round(psutil.disk_usage('/')[0]/1000000000, 0),
         "cpu": ""
      }
"""

app = Flask('testapp') 

@app.route('/')
def index():
    data = {
         "ip": socket.gethostbyname(socket.gethostname()),
         "hostname": socket.gethostname(),
         "domain": ".lcl",
         "os_version": platform.platform(),
         "ram_used": round(psutil.virtual_memory()[3]/1000000000, 1),
         "ram_used_percent": psutil.virtual_memory().percent,
         "storage_free": round(psutil.disk_usage('/')[2]/1000000000, 0),
         "storage_used": round(psutil.disk_usage('/')[1]/1000000000, 0),
         "sorage_tot": round(psutil.disk_usage('/')[0]/1000000000, 0),
         "cpu": psutil.cpu_percent(interval=None, percpu=False)
      }
    
    return render_template('index.html', refreshrate=5, hostname=data['hostname'], get_local_ip=data['ip'], get_os_version=data['os_version'], get_ram_gb=data['ram_used'], get_storage_used=data['storage_used'], get_storage_tot=data['sorage_tot'], cpu=data['cpu'], ram_used_percent=data['ram_used_percent'])


if __name__ == '__main__':
    app.run()