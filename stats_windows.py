import os
import psutil
import platform
import sys
import subprocess
import glob
import datetime

os.system('clear')

host = os.uname()[1]
time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
time2 = datetime.datetime.now().strftime("%Y%m%d")
time3 = datetime.datetime.now().strftime("%H:%M:%S")
net_test1 = "0"
net_test2 = "0"
net_test3 = "0"

filename = host + '_stats' + '.csv'
filename3 = host + '_' + time + '_stats' + '.csv'
filename2 = host + '_' + time2 + '_jrnl' + '.csv'
filename4 = host + '_' + time2 + '_jrnl' + '.csv'

cpuUsage = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()
memUsage = mem[2]
print'CPU % Usage = ',cpuUsage,'%'
print'Memory % used = ',memUsage,'%'
print cpuUsage,memUsage
print host,time

sys.stdout = open("c:/dev/scripts/"+filename,"w")
print time3,";",cpuUsage,";",memUsage, ";",net_test1, ";",net_test3, ";",net_test3, ";",mysql_active, ";",apache_active
sys.stdout.close()

sys.stdout = open("c:/dev/scripts/"+filename2,"a")
print time3,';',cpuUsage,";",memUsage
sys.stdout.close()
