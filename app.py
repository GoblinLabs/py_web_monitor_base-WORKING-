from flask import Flask, render_template
from requests import get
import socket
import time
import datetime
import psutil
import platform
import math
import os
import json

def setOsicon(x):
    #OS icons
    os_data_name = platform.system()
    icon_win = 'https://cdn-icons-png.flaticon.com/512/888/888882.png'
    icon_linux ='https://cdn-icons-png.flaticon.com/512/226/226772.png'
    icon_osx = 'https://cdn-icons-png.flaticon.com/512/888/888841.png'
    icon_os_general = 'https://cdn-icons-png.flaticon.com/512/3274/3274633.png'
    
    if os_data_name == "Windows":
        icon_link = icon_win
    elif os_data_name == "Linux":
        icon_link = icon_linux
    elif os_data_name == "OSX":
        icon_link = icon_osx
    else:
        icon_link = icon_os_general
    
    return icon_link


app = Flask('SystemStats')

HOST= '0.0.0.0'
PORT = 3007


@app.route('/')
def index():

    #get_wanip = get('https://api.ipify.org').content.decode('utf8')
    data = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os_icon": setOsicon(platform.system()),
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
    
    
    return render_template('index.html', 
        refreshrate=5, 
        hostname=data['hostname'], 
        get_local_ip=data['ip'], 
        get_os_version=data['os_version'], 
        os_icon=data['os_icon'],
        os_platform=data['os_platform'],
        os_distro=data['os_distro'],
        get_ram_gb=data['ram_used'], 
        get_storage_used=data['storage_used'], 
        get_storage_tot=data['sorage_tot'], 
        cpu=data['cpu'], 
        ram_used_percent=data['ram_used_percent'], 
        storage_percent=data['storage_percent'], 
        ram_tot=data['ram_tot'], 
        storage_path=data['storage_path'], 
        time=data['time'], 
        wan_ip=data['wan_ip'])

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)