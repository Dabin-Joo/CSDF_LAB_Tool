#lists the installed applications' name
import sqlite3
import os
import time

def check_program():
    username = input("Input user's name: ")
    now_path = os.getcwd()
    k_path = "/Users/"+username+"/Library/Application Support/Knowledge"
    os.chdir(k_path)
    com = "cp knowledgeC.db "+now_path
    os.popen(com)
    time.sleep(3)

    os.chdir(now_path)
    con = sqlite3.connect('knowledgeC.db')
    cursor = con.cursor()
    cursor.execute("SELECT ZVALUESTRING FROM ZOBJECT")
    data = cursor.fetchall()
    con.close()
    program = []
    for i in data:
        for j in i:
            if j not in program:
                program.append(j)
    print(program)
