import cache_info as CI
import data1 as d
import pandas as pd

file0 = d.file_0()
file1 = d.file_1()
file2 = d.file_2()
file3 = d.file_3()
t = CI.F_info().reset_index()
pd.set_option('display.max_columns', None) # 전체 열 보기
pd.set_option('display.max_rows', None)

before =[]
after = []
for i in range (0,len(t)):
    if t['MDF_Number'][i] == "0":
        file0.seek(t['Metadata_location'][i],1)
        info = file0.read(t['Metadata_size'][i])
        info_decode= info.decode('utf-8','ignore')
        file0.seek(-(t['Metadata_location'][i]+t['Metadata_size'][i]),1)  
        before.append(info_decode)  
    elif t['MDF_Number'][i] == "1":
        file1.seek(t['Metadata_location'][i],1)
        info = file1.read(t['Metadata_size'][i])
        info_decode= info.decode('utf-8','ignore')
        file1.seek(-(t['Metadata_location'][i]+t['Metadata_size'][i]),1)
        before.append(info_decode)
    elif t['MDF_Number'][i] == "2":
        file2.seek(t['Metadata_location'][i],1)
        info = file2.read(t['Metadata_size'][i])
        info_decode= info.decode('utf-8','ignore')
        file2.seek(-(t['Metadata_location'][i]+t['Metadata_size'][i]),1)
        before.append(info_decode)
    elif t['MDF_Number'][0] == "3":
        file3.seek(t['Metadata_location'][i],1)
        info = file3.read(t['Metadata_size'][i])
        info_decode= info.decode('utf-8','backslashreplace')
        file3.seek(-(t['Metadata_location'][i]+t['Metadata_size'][i]),1)
        before.append(info_decode)
for i in range (0, len(before)):
    for j in range(0, len(before)):
        a = str(before[i]).replace("\\x%d%d"%(i,j), "")
        before[i] = a


def Meta_data():
    return before

