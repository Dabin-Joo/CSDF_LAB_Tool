#웹브라우저 기록 확인
import sqlite3
import os
import time
import plistlib

def makecopy(history, now, web):
    #print(history)
    os.chdir(history)
    #print(now)
    com = "cp History.db "+now+"/"+web+"_history.db"
    os.popen(com)
    time.sleep(3)
    com = "cp Downloads.plist "+now+"/"+web+"_download.plist"
    os.popen(com)
    time.sleep(3)

def checkDownload(): #다운로드 기록 확인
    plist_name = "Safari_download.plist"
    checklist = ['DownloadEntryProgressTotalToLoad', 'DownloadEntryDateAddedKey', 'DownloadEntryDateFinishedKey', 'DownloadEntryURL', 'DownloadEntryPath']
    #DownloadEntryProgressTotalToLoad = 다운로드 바이트 크기
    #DownloadEntryDateAddedKey = 다운로드 시작 시간(datetime)/DownloadEntryDateFinishedKey = 다운로드 끝난 시간
    #DownloadEntryURL = 다운로드 url
    #DownloadEntryPath = 다운로드 받은 파일 위치
    
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
    
def checkUrl():  #방문한 url 확인
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

def checkWeb(name): # 웹사이트 있는지 확인 -> 사파리나 파이어폭스는 바로 확인 But 구글은 임포트 함수로 이동
    lib_path = "/Users/"+name+"/Library"
    now_path = os.getcwd()
    os.chdir(lib_path)
    stream = os.popen("ls")
    webbrowser = ["Safari", "Firefox"]
    folder_name = stream.readlines() # safari 등 확인
    for i in folder_name: #폴더이름에서 웹브라우저 목록과 비교
        if "Safari\n" in i:
            print("Safari matched!") #매칭됨
            history = lib_path+"/Safari"
            makecopy(history, now_path, "Safari")
            os.chdir(now_path)
            checkUrl()
            checkDownload()
        else:
            print("There is no Safari folder")


def extract_Safari():
    #어떤 웹 브라우저 있는지 확인 -> 폴더명에서 찾기
    username = input("Input user's name: ")
    checkWeb(username)
