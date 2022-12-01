#Check the Chrome data
import sqlite3
import os
import time

def checkUrl():  #check the url in chrome history file
    con = sqlite3.connect('chrome_history')
    cursor = con.cursor()
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
    data = cursor.fetchall()
    con.close()
    with open("chrome_url.txt", "w") as f:
        f.write("url, title, visit_count, last_visit_time\n")
        for i in data:
            string = " ,".join(map(str, i))
            f.write(string+"\n")
    print("Check the file, 'chrome_url.txt'")

def checkDownload(): #check the download history in chrome history file
    con = sqlite3.connect('chrome_history')
    cursor = con.cursor()
    cursor.execute("SELECT target_path, start_time, tab_url FROM downloads")
    data = cursor.fetchall()
    con.close()
    with open("chrome_download.txt", "w") as f:
        f.write("target_path, start_time, tab_url\n")
        for i in data:
            string = " ,".join(map(str, i))
            f.write(string+"\n")
    print("Check the file, 'chrome_download.txt'")

def makecopy(history, now):
    os.chdir(history)
    #print(now)
    com = "cp History "+now+"/chrome_history"
    os.popen(com)
    time.sleep(3)

def extract_Chrome():
    username = input("Input user's name: ")
    now_path = os.getcwd()
    os.chdir("/Users/"+username+"/Library/Application Support/")
    stream = os.popen("ls")
    out = stream.readlines()
    #print(out)
    tp =0
    for i in out:
        if "Google" in i:
            print("Google matched!")
            history_path = "/Users/"+username+"/Library/Application Support/Google/Chrome/Default"
            tp +=1
    if tp ==0:
        print("There is no Chrome.")
        return
    
    makecopy(history_path, now_path) #make the copy file
    os.chdir(now_path)

    #check url and download history
    checkUrl() 
    checkDownload()

