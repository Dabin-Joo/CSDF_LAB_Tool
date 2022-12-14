import winreg as reg  
import os     
import sqlite3
from sqlite3 import Error

#데이터베이스 테이블 로드
con = sqlite3.connect('registry_anti.db')
cursor = con.cursor()

def UserAssist():
    cursor.execute("SELECT MD5_hash_value, artifact_trace FROM UserAssist")
    talist = cursor.fetchall()
    key = reg.HKEY_CURRENT_USER
    hashlist = []
    for i in range(len(talist)):
        try:
            key_value = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist\\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\\Count"
            open = reg.OpenKey(key,key_value,0,reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            ##j번째 레지스트리 읽기
            for j in range(reglen):
                open2 = reg.EnumValue(open, j)
                regdata = open2[0]
                ##데이터베이스 i번째 데이터와 값 비교
                if talist[i][1] in regdata:
                    ap = ["UserAssist:{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass
        try:
            key_value = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist\\{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}\\Count"
            open = reg.OpenKey(key,key_value,0,reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            ##j번째 레지스트리 읽기
            for j in range(reglen):
                open2 = reg.EnumValue(open, j)
                regdata = open2[0]
                ##데이터베이스 i번째 데이터와 문자열 비교, 레지스트리에 문자열이 있으면 아티팩트, 폴더명과 해당 프로그램 해시값을 hashlist에 저장
                if talist[i][1] in regdata:
                    ap = ["UserAssist:{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass

    reg.CloseKey(open)
    
    return hashlist



def Shimcache():
    cursor.execute("SELECT MD5_hash_value,stored_path, artifact_trace FROM Shimcache")
    talist = cursor.fetchall()
    hashlist = []
    for i in range(len(talist)):
        try:
            key = reg.HKEY_LOCAL_MACHINE
            key_value = "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\AppCompatCache"
            open = reg.OpenKey(key,key_value, reg.REG_BINARY, reg.KEY_READ)
            bvalue = reg.EnumValue(open, 0)
            value = bvalue[1]
            value = value.replace(b'\\', b'')
            value = value.replace(b'\x00', b'')
            chtali = talist[i][2].replace('\\', '')
            chtali = chtali.encode('utf-8')
            if chtali in value:
                ap = ["Shimcache:AppCompatCache", talist[i][0]]
                hashlist.append(ap)
        except FileNotFoundError:
            pass
        try:
            key = reg.HKEY_CURRENT_USER
            key_value = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Compatibility Assistant\\Store"
            open = reg.OpenKey(key,key_value,0,reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            ##j번째 레지스트리 읽기
            for j in range(reglen):
                open2 = reg.EnumValue(open, j)
                regdata = open2[0]
                ##데이터베이스 i번째 데이터와 값 비교
                if talist[i][2] in regdata:
                    ap = ["Shimcache:AppCompatFlags", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass
    reg.CloseKey(open)

    return(hashlist)


def CIDSizeMRU():
    cursor.execute("SELECT MD5_hash_value, artifact_trace FROM CIDSizeMRU")
    talist = cursor.fetchall()
    hashlist = []
    for i in range(len(talist)):
        try:
            key = reg.HKEY_CURRENT_USER
            key_value = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\CIDSizeMRU"
            open = reg.OpenKey(key,key_value, reg.REG_BINARY, reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            for j in range(reglen):
                bvalue = reg.EnumValue(open, j)
                value = bvalue[1]
                value = value.replace(b'\\', b'')
                value = value.replace(b'\x00', b'')
                chtali = talist[i][1].replace('\\', '')
                chtali = chtali.encode('utf-8')
                if chtali in value:
                    ap = ["CIDSizeMRU", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass

    reg.CloseKey(open)

    return(hashlist)


def LastVisitedMRU():
    cursor.execute("SELECT MD5_hash_value, artifact_trace FROM LastVisitedMRU")
    talist = cursor.fetchall()
    hashlist = []
    for i in range(len(talist)):
        try:
            key = reg.HKEY_CURRENT_USER
            key_value = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\LastVisitedPidlMRU"
            open = reg.OpenKey(key,key_value, reg.REG_BINARY, reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            for j in range(reglen):
                bvalue = reg.EnumValue(open, j)
                value = bvalue[1]
                value = value.replace(b'\\', b'')
                value = value.replace(b'\x00', b'')
                chtali = talist[i][1].replace('\\', '')
                chtali = chtali.encode('utf-8')
                if chtali in value:
                    ap = ["LastVisitedMRU", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass

    reg.CloseKey(open)

    return(hashlist)


def OpenSaveMRU():
    cursor.execute("SELECT MD5_hash_value, artifact_trace FROM OpenSaveMRU")
    talist = cursor.fetchall()
    hashlist = []
    for i in range(len(talist)):
        try:
            key = reg.HKEY_CURRENT_USER
            key_value = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSavePidlMRU\\exe"
            open = reg.OpenKey(key,key_value, reg.REG_BINARY, reg.KEY_READ)
            ##레지스트리 개수
            open3 = reg.QueryInfoKey(open)
            reglen = open3[1]
            for j in range(reglen):
                bvalue = reg.EnumValue(open, j)
                value = bvalue[1]
                value = value.replace(b'\\', b'')
                value = value.replace(b'\x00', b'')
                chtali = talist[i][1].replace('\\', '')
                chtali = chtali.encode('utf-8')
                if chtali in value:
                    ap = ["OpenSaveMRU", talist[i][0]]
                    hashlist.append(ap)
        except FileNotFoundError:
            pass

    reg.CloseKey(open)

    return(hashlist)
