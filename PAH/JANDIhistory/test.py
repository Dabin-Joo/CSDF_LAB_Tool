import os
import requests
from urllib.parse import urlparse
import zipfile
import win32api
import shutil
import glob
import jsontocsv
import re
import csv
#https://tolovefeels.tistory.com/134
url = 'https://www.nirsoft.net/utils/chromecacheview.zip'
parsed_file=urlparse(url)
file_name=os.path.basename(parsed_file.path)
file = requests.get(url, allow_redirects=True)
open(file_name,'wb').write(file.content)
current=os.getcwd()
#압축 풀기
cache_zip = zipfile.ZipFile(file_name)
#별도 압축파일이 없는 폴더에서 구동할 것
cache_zip.extractall(current)
cache_zip.close()
p='https://i1.jandi.com/message-api/v1'

#chromecacheview cmd
username=input("Please enter username of target PC: ")
extractedCache = input("Path for extracted cache file: ")
if os.path.isdir(extractedCache) == False:
    os.mkdir(extractedCache)
    extract_all='ChromeCacheView.exe -folder "C:/Users/%s/AppData/Roaming/JANDI/Cache" /copycache "%s" "" /CopyFilesFolder "%s'%(username,p,extractedCache)
    cmd=os.system(extract_all)
elif os.path.isdir(extractedCache) == True:
    extract_all='ChromeCacheView.exe -folder "C:/Users/%s/AppData/Roaming/JANDI/Cache" /copycache "%s" "" /CopyFilesFolder "%s'%(username,p,extractedCache)
    cmd=os.system(extract_all)

files = glob.iglob(os.path.join(extractedCache, "*.json"))
Jsonpath=extractedCache+'/Json'
os.mkdir(Jsonpath)
dest_dir='%s/Json'%extractedCache

header=['teamId','writerId','time','content']
with open('output.csv','w',newline='') as f:
        write=csv.writer(f)
        write.writerow(header)
            
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dest_dir)

jsonfiles=os.listdir(Jsonpath)
for file in jsonfiles:
    
    jsontocsv.json_analyze(dest_dir+'/'+file)
    # except KeyError or TypeError:
    #     continue

