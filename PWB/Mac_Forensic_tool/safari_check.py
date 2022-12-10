#Check Safari history
import sqlite3
import os
import time
import plistlib

def makecopy(history, now, web):
    os.chdir(history)
    com = "cp History.db "+now+"/"+web+"_history.db"
    os.popen(com)
    time.sleep(3)
    com = "cp Downloads.plist "+now+"/"+web+"_download.plist"
    os.popen(com)
    time.sleep(3)

def checkDownload(): #Check the Safari Download history
    plist_name = "Safari_download.plist"
    checklist = ['DownloadEntryProgressTotalToLoad', 'DownloadEntryDateAddedKey', 'DownloadEntryDateFinishedKey', 'DownloadEntryURL', 'DownloadEntryPath']
    #DownloadEntryProgressTotalToLoad = File's byte size 
    #DownloadEntryDateAddedKey = Download start time (datetime)/DownloadEntryDateFinishedKey = Download finish time
    #DownloadEntryURL = Download url
    #DownloadEntryPath = Path to downloaded file
    
    with open(plist_name, 'rb') as f:
        plist_data = plistlib.load(f)
        value_list = plist_data["DownloadHistory"]
    with open("Safari_download.txt", "w") as f:
        f.write("ByteSize, start_time,finish_time, DownloadURL, DownloadPath\n")
        for value_dict in value_list:
            j = []
            for i in checklist:
                j.append(str(value_dict[i]))
                string = " ,".join(map(str, j))
            f.write(string+"\n")
    print("Check the file, 'Safari_download.txt'")
    
def checkUrl():  #check the visited url
    db_name = "Safari_history.db"
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute("SELECT visit_time, title FROM history_visits")
    data = cursor.fetchall()
    con.close()
    with open("Safari_url.txt", "w") as f:
        f.write("visit_time, title\n")
        for i in data:
            string = " ,".join(map(str, i))
            f.write(string+"\n")
    print("Check the file, 'Safari_url.txt'")

def checkWeb(name): #check the safari
    lib_path = "/Users/"+name+"/Library"
    now_path = os.getcwd()
    os.chdir(lib_path)
    stream = os.popen("ls")
    webbrowser = ["Safari", "Firefox"]
    folder_name = stream.readlines()
    safari = False
    for i in folder_name: 
        if "Safari\n" in i:
            print("Safari matched!") 
            history = lib_path+"/Safari"
            makecopy(history, now_path, "Safari")
            os.chdir(now_path)
            checkUrl()
            checkDownload()
            safari = True
    if not safari:
        print("There is no Safari folder")


def extract_Safari():
    username = input("Input user's name: ")
    checkWeb(username)
