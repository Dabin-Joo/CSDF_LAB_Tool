#findind bluetooth connecting devices
import os
import plistlib
import time

def makecopy():
    now = os.getcwd()
    path = "/Library/Preferences/"
    os.chdir(path)
    #print(now)
    com = "cp com.apple.bluetooth.plist "+now+"/"+"bluetooth_log.plist"
    os.popen(com)
    time.sleep(3)
    os.chdir(now)

def CheckPlist():
    plist_name = "bluetooth_log.plist"
    try:
        with open(plist_name, 'rb') as f:
            plist_data = plistlib.load(f)
            #print(plist_data)
            value_list = plist_data["PersistentPorts"]
        with open("bluetooth_log.txt", "w") as f:
            f.write("Mac address: ")
            for device_mac in value_list.keys(): 
                f.write(device_mac+"\n") #mac 주소
                device_info = value_list[device_mac]
                for i in device_info.keys():  
                    string = str(i)+" : "+str(device_info[i])
                    f.write(string+"\n")
                f.write("\n")
        print("Check The file, 'bluetooth_log.txt'")
    except:
        print("There is no devices in Mac")

def find_BTdevices():
    makecopy()
    CheckPlist()
