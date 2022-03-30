from cgitb import text
from ctypes import alignment
from lib2to3.pgen2.token import COLONEQUAL
from operator import index
from platform import platform
from sqlite3 import Row
import tkinter as tk
from tkinter import*
from turtle import bgcolor, position, right, width
import psutil
from tkinter import font
from psutil import disk_usage
import time
from datetime import datetime
from psutil import cpu_count
import GPUtil
from tabulate import tabulate
import platform
import speedtest



p = psutil.Process()





def reload():
    
    root = tk.Tk()
    root.title('System Performance')
    root.resizable(width=False, height=False)

    
    
    
    #Division of Canvas
    canvas1 = Canvas(root, width=500, height=170, bg="green")
    canvas1.grid(row=1,column=0)
    
    canvas2 = Canvas(root, width=500, height=170, bg="green")
    canvas2.grid(row=1,column=1)
    
    canvas3 = Canvas(root, width=500, height=100, bg="green")
    canvas3.grid(row=2,column=0)
    
    canvas4 = Canvas(root, width=500, height=100, bg="green")
    canvas4.grid(row=2,column=1)
    
    canvas5 = Canvas(root, width=500, height=70, bg="green")
    canvas5.grid(row=3,column=0)
    
    canvas6 = Canvas(root, width=500, height=70, bg="green")
    canvas6.grid(row=3,column=1)
    
    canvas7 = Canvas(root, width=500, height=150, bg="green")
    canvas7.grid(row=4,column=0)
    
    canvas8 = Canvas(root, width=500, height=150, bg="green")
    canvas8.grid(row=4,column=1)

    canvas9 = Canvas(root,width=1000,height=100, bg="green")
    canvas9.grid(row=5,column=0,columnspan=2)

    
    
    #monitoring
    monitor_username = p.username()
    monitor_boot = psutil.boot_time()
    monitor_boot_date = datetime.fromtimestamp(monitor_boot)
    monitor_cpu_cores = psutil.cpu_count()
    monitor_cpu_usage = psutil.cpu_percent()
    monitor_cpu_freq = psutil.cpu_freq()
    monnitor_ram_usage = psutil.virtual_memory().percent
    monitor_ram_total = psutil.virtual_memory().total
    monnitor_ram_available = psutil.virtual_memory().available
    monitor_disk_usage = psutil.disk_usage('/').percent
    monitor_network_sent = psutil.net_io_counters().bytes_sent
    monitor_network_recv = psutil.net_io_counters().bytes_recv
    monitor_system_info = platform.uname()
    monitor_gpu = GPUtil.getGPUs()




    #realtime code
    
    
    
    
    #Canvas/ Display Area
    canvas1.create_text(50, 15,font=("Ariel",12,font.BOLD), text="System Info")
    canvas1.create_text(170,40,font=("Ariel",12), text="Username: {}".format(monitor_username))
    canvas1.create_text(69,60,font=("Ariel",12), text="System: {}".format(monitor_system_info.system))
    canvas1.create_text(48,80,font=("Ariel",12), text="Release: {}".format(monitor_system_info.release))
    canvas1.create_text(77,100,font=("Ariel",12), text="Version: {}".format(monitor_system_info.version))
    canvas1.create_text(67,120,font=("Ariel",12), text="Machine: {}".format(monitor_system_info.machine))
    canvas1.create_text(230,140,font=("Ariel",12), text="Processor: {}".format(monitor_system_info.processor))
    
    canvas2.create_text(73, 15,font=("Ariel",12,font.BOLD), text="Boot date & Time:")
    canvas2.create_text(115,50,font=("Ariel",12), text=(f"Date: {monitor_boot_date.year}/{monitor_boot_date.month}/{monitor_boot_date.day} Time:{monitor_boot_date.hour}:{monitor_boot_date.minute}:{monitor_boot_date.second}"))
    
    canvas3.create_text(40, 15,font=("Ariel",12,font.BOLD), text="CPU Util ")
    canvas3.create_text(55, 40,font=("Ariel",12), text="CPU Cores: {}".format(monitor_cpu_cores))
    canvas3.create_text(73, 60,font=("Ariel",12), text="CPU Usage: {}".format(monitor_cpu_usage)+ "%")
    canvas3.create_text(126, 80,font=("Ariel",12), text="CPU Max Frequency: {:.2f}Mhz".format(monitor_cpu_freq.max))
    #canvas3.create_text(110, 100,font=("Ariel",12), text="CPU Min Frequency: {:.2f}Mhz".format(monitor_cpu_freq.min))
    
    canvas4.create_text(50, 15,font=("Ariel",12,font.BOLD), text="RAM Usage ")
    canvas4.create_text(93, 35,font=("Ariel",12), text="Percentage Used: {}%".format(monnitor_ram_usage))
    canvas4.create_text(85, 60,font=("Ariel",12), text="Total Memory: {:0.2f} GB".format(monitor_ram_total / 1073741824))
    canvas4.create_text(100,80,font=("Ariel",12), text="Available Memory: {:0.2f} GB".format(monnitor_ram_available / 1073741824))
    
    canvas5.create_text(53,15,font=("Ariel",12,font.BOLD), text="Disk Usage ")
    canvas5.create_text(28,50,font=("Ariel",12), text="{}%".format(monitor_disk_usage))
    
    canvas6.create_text(68,15,font=("Ariel",12,font.BOLD), text="Ethernet Usage")
    canvas6.create_text(127,40,font=("Ariel",12), text="Total Bytes sent: {:0.2f} Kbps".format(monitor_network_sent/1024))
    canvas6.create_text(150,60,font=("Ariel",12), text="Total Bytes Received: {:0.2f} Kbps".format(monitor_network_recv/1024))
    
    canvas7.create_text(30,15, font=("Ariel",12, font.BOLD), text="GPU")
    canvas7.create_text(30,30, font=("Ariel",12, font.BOLD), text=GPUtil.showUtilization())

    canvas8.create_text(80,15, font=("Ariel",12, font.BOLD), text="Internet Speed Test")

    mylabel1 = tk.Label(font=("Ariel,",12,font.BOLD),text = "Click the speed test to run!",bg="green")
    mylabel1.place(x=510,y=380)

    mylabel2 = tk.Label(text = "",bg="green")
    mylabel2.place(x=510,y=400)

    mylabel3 = tk.Label(text = "",bg="green")
    mylabel3.place(x=510,y=420)

    mylabel4 = tk.Label(text = "",bg="green")
    mylabel4.place(x=510,y=440)

   

        
    def destroy():
        root.destroy()
        reload()

    def speed_test():


        test = speedtest.Speedtest()
        test.get_servers()
        best = test.get_best_server()
        download_result = test.download()
        upload_result = test.upload()
        ping_result = test.results.ping

        
        
        mylabel1.config(font=("Ariel",12),text = f"Found: {best['host']} Located in {best['country']}")
        mylabel2.config(font=("Ariel",12),text =f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
        mylabel3.config(font=("Ariel",12),text =f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
        mylabel4.config(font=("Ariel",12),text =f"Ping: {ping_result:.2f} ms")


        '''
        canvas8.create_text(150,40,font=("Ariel",12), text=f"Found: {best['host']} Located in {best['country']}")
        canvas8.create_text(119,60,font=("Ariel",12),text =f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
        canvas8.create_text(105,75, font=("Ariel",12), text=f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s") 
        canvas8.create_text(58,95, font=("Ariel",12), text=f"Ping: {ping_result:.2f} ms")'''

  


    btn_refresh = tk.Button(root, text="Speed Test", bg="Blue", fg="white",command=speed_test)
    btn_refresh.place(height=50, width=150,x=550, y=530)

    btn_refresh = tk.Button(root, text="Refresh", command=destroy, bg="Blue", fg="white")
    btn_refresh.place(height=50, width=150,x=300, y=530)


    #end
    
    root.mainloop()
  
    


    
reload()

