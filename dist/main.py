true=True; false=False; null=None
import os 
import time 
import subprocess 
import math 

import config 
import digits 

os .system ("tput reset");
time .sleep (1)

base_characters =[[],[],[],[],[],[],[]]

base_characters [0]="█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█  "
base_characters [1]="█                         █  "
base_characters [2]="█                         ███"
base_characters [3]="█                         ███"
base_characters [4]="█                         █▀▀"
base_characters [5]="█                         █  "
base_characters [6]="▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  "


print ("\n"*int (os .get_terminal_size ().lines /2));
while (1):
    characters =[
    base_characters [0],
    base_characters [1],
    base_characters [2],
    base_characters [3],
    base_characters [4],
    base_characters [5],
    base_characters [6]
    ]
    
    charge_cur =int (subprocess .check_output (f"cat {config.battery_dir}charge_now",shell =True ))
    charge_max =int (subprocess .check_output (f"cat {config.battery_dir}charge_full",shell =True ))
    percentage =math .floor (charge_cur /charge_max *100)
    
    print ("\033[A"*8)
    for i in range (25):
        if (i <=math .ceil (percentage /4)):
            characters [1]=characters [1][:i +1]+"█"+characters [1][i +2:]
            characters [2]=characters [2][:i +1]+"█"+characters [2][i +2:]
            characters [3]=characters [3][:i +1]+"█"+characters [3][i +2:]
            characters [4]=characters [4][:i +1]+"█"+characters [4][i +2:]
            characters [5]=characters [5][:i +1]+"▀"+characters [5][i +2:]
            
        
        
    
    
    
    for i in characters :
        print (f"{i}".center (os .get_terminal_size ().columns ))
        
    
    
    status =subprocess .check_output (f"cat {config.battery_dir}status",shell =True ).decode ("utf-8")
    
    if (status =="Charging\n"):
        status ="󱐋"
        
    elif (status =="Discharging\n"):
        status =" ";
        
    elif (status =="Not charging\n"):
        status =""
        
    
    
    print (f"{percentage}% {status}".center (os .get_terminal_size ().columns ),end ='')
    
    time .sleep (1)
    



