import winreg as reg  
import os     
import sqlite3
from sqlite3 import Error

con = sqlite3.connect('registry_anti.db')
cursor = con.cursor()

def organize(finlist):
    cursor.execute("SELECT MD5_hash_value, download_file_name FROM Wiping_tool")
    talist = cursor.fetchall()
    fintlist = []
    for i in range(len(finlist)):
        for j in range(len(talist)):
            if finlist[i][1] == talist[j][0]:
                fintlist.append(talist[j][1])
    fintlist = set(fintlist)
    
    return fintlist