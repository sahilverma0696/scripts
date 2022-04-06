#!/usr/bin/env python3

from os import system
import subprocess
from subprocess import check_output
from time import sleep

upper_limit = 77 # 77%
min = 200 # 200 minutes


def notify(title, text):
    system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def get_battey_status():
    out = check_output("pmset -g batt",shell=True)
    out = str(out)
    result = []
    if(out.find("discharging")):
        result.append(False)
    else:
        result.append(True)
    

    #dirty parsing 
    i = out.find("\\t")
    i = i+2
    percentage  =""
    while out[i]!='%':
        percentage +=out[i]
        i = i+1
    
    result.append(int(percentage))
    
    return result

def timer():
    while(1):
        result = get_battey_status()
        if(result[0]==False):
            notify("Battery Status","Not charging")
            exit(0)
        elif(result[0]==True and result[1]<upper_limit):
            sleep(min)
        else:
            notify("Battery Status","Please unplug the charger")
            exit(0)


timer()