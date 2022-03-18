from cgitb import text
from lib2to3.pgen2.token import COLONEQUAL
from sqlite3 import Row
import tkinter as tk
from tkinter import*
from turtle import width
import psutil
import os
from tkinter import font

from psutil import disk_usage
import time

from datetime import datetime

from psutil import cpu_count
import GPUtil
from gpu import gpu 


p = psutil.Process()


def reload():
    
    root = tk.Tk()
    root.title('System Performance')
    root.resizable(width=False, height=False)
    
    #Division of Canvas
    canvas1 = Canvas(root, width=500, height=70, bg="green")
    canvas1.grid(row=1,column=0)
    
    canvas2 = Canvas(root, width=500, height=70, bg="green")
    canvas2.grid(row=2,column=0)
    
    canvas3 = Canvas(root, width=500, height=70, bg="green")
    canvas3.grid(row=3,column=0)
    
    canvas4 = Canvas(root, width=500, height=100, bg="green")
    canvas4.grid(row=4,column=0)
    
    canvas5 = Canvas(root, width=500, height=70, bg="green")
    canvas5.grid(row=5,column=0)
    
    canvas6 = Canvas(root, width=500, height=70, bg="green")
    canvas6.grid(row=6,column=0)
    
    canvas7 = Canvas(root, width=500, height=150, bg="green")
    canvas7.grid(row=7,column=0)
    
    canvas8 = Canvas(root, width=500, height=70, bg="green")
    canvas8.grid(row=8,column=0)
    
    #monitoring
    monitor_username = p.username()
    monitor_boot = psutil.boot_time()
    monitor_boot_date = datetime.fromtimestamp(monitor_boot)
    monitor_cpu_cores = psutil.cpu_count()
    monitor_cpu_usage = psutil.cpu_percent()
    monnitor_ram_usage = psutil.virtual_memory().percent
    monitor_ram_total = psutil.virtual_memory().total
    monnitor_ram_available = psutil.virtual_memory().available
    monitor_disk_usage = psutil.disk_usage('/').percent
    monitor_network_sent = psutil.net_io_counters().bytes_sent
    monitor_network_recv = psutil.net_io_counters().bytes_recv
    
    #Canvas/ Display Area
    canvas1.create_text(52, 15,font=("Ariel",12,font.BOLD), text="Username: ")
    canvas1.create_text(100, 50,font=("Ariel",12), text="{}".format(monitor_username))
    
    canvas2.create_text(73, 15,font=("Ariel",12,font.BOLD), text="Boot date & Time:")
    canvas2.create_text(60,50,font=("Ariel",12), text=(f" {monitor_boot_date.year}/{monitor_boot_date.month}/{monitor_boot_date.day}\t{monitor_boot_date.hour}:{monitor_boot_date.minute}:{monitor_boot_date.second}"))
    
    canvas3.create_text(40, 15,font=("Ariel",12,font.BOLD), text="CPU Util ")
    canvas3.create_text(55, 40,font=("Ariel",12), text="CPU Cores: {}".format(monitor_cpu_cores))
    canvas3.create_text(74, 60,font=("Ariel",12), text="CPU Usage: {}".format(monitor_cpu_usage)+ "%")
    
    canvas4.create_text(50, 15,font=("Ariel",12,font.BOLD), text="RAM Usage ")
    canvas4.create_text(93, 35,font=("Ariel",12), text="Percentage Used: {}%".format(monnitor_ram_usage))
    canvas4.create_text(122, 60,font=("Ariel",12), text="Total Memory: {} bytes".format(monitor_ram_total))
    canvas4.create_text(136,80,font=("Ariel",12), text="Available Memory: {} bytes".format(monnitor_ram_available))
    
    canvas5.create_text(53,15,font=("Ariel",12,font.BOLD), text="Disk Usage: ")
    canvas5.create_text(28,50,font=("Ariel",12), text="{}%".format(monitor_disk_usage))
    
    canvas6.create_text(68,15,font=("Ariel",12,font.BOLD), text="Ethernet Usage: ")
    canvas6.create_text(120,40,font=("Ariel",12), text="Total Bytes sent: {} bytes".format(monitor_network_sent))
    canvas6.create_text(145,60,font=("Ariel",12), text="Total Bytes Received: {} bytes".format(monitor_network_recv))
    
    canvas7.create_text(30,15, font=("Ariel",12, font.BOLD), text="GPU")
    canvas7.create_text(240,70, font=("Ariel",10), text="{}".format(GPUtil.getAvailable()))

    def destroy():
        root.destroy()
        reload()


   
    btn_refresh = tk.Button(root, text="Refresh", command=destroy, bg="Blue", fg="white")
    btn_refresh.grid(row=8,column=0)
    


   
    #end
    
    root.mainloop()
  
    


    
reload()





