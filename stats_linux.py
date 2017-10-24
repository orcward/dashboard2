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

hostname = "www.google.com" 
response1 = os.system("ping -n 1 " + hostname)

if response1 == 0:
        net_test1 = "1"
        print hostname, 'is up!'
else:
        net_test1 = "0"
        print hostname, 'is down!'

hostname = "ftp.is.co.za" 
response2 = os.system("ping -n 1 " + hostname)

if response2 == 0:
        net_test2 = "1"
        print hostname, 'is up!'
else:
        net_test2 = "0"
        print hostname, 'is down!'

hostname = "www.yahoo.com"
response3 = os.system("ping -n 1 " + hostname)

if response3 == 0:
        net_test3 = "1"
        print hostname, 'is up!'
else:
        net_test3 = "0"
        print hostname, 'is down!'

p = subprocess.Popen(["ps", "-A"], stdout=subprocess.PIPE)
out, err = p.communicate()

apache_active = "0"
mysql_active = "0"

if ('apache2' in out):
        print('apache2 running')
        apache_active = "1"
if ('mysql' in out):
        print('mysql running')
        mysql_active = "1"


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
