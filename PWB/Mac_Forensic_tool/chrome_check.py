#웹브라우저 기록 확인
import sqlite3
import os
import time

def checkUrl():  #방문한 url 확인
    #DB 파일을 인풋으로 받아서 내용을 확인하는 함수
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

def checkDownload(): #다운로드 기록 확인
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
    #어떤 웹 브라우저 있는지 확인 -> 폴더명에서 찾기
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
    #구글 매칭되면 복사본 생성 - 'cp' 명령어 사용
    makecopy(history_path, now_path) #복사본 생성
    os.chdir(now_path)

    #url과 download 확인
    checkUrl() 
    checkDownload()

