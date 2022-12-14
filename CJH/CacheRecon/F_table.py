import cache_info
import extension
import os
import pandas as pd
import shutil
import data1 as d
F = cache_info.URL_info().reset_index()

#F = F.drop(['URL_Info_short'],axis = 1)
F["Extenstion"] = extension.E()

x = d.checked_fpath()
y = input("Enter route to store cache files:")
def cache():
    return y
while True:
    if os.path.isdir(y) == False:
        y = input("***Invalid Route*** Enter route to store cache files againg:")
        continue
    else:
        break

os.chdir(y)
for i in range (0,len(F)):
    if os.path.isdir(F["URL_Info_short"][i]):
        continue
    else:
        os.mkdir(F["URL_Info_short"][i])

data_type = []        
for i in range (0,len(F)):
    dt = F["Content_type"][i].split(' ')
    data_type.append(dt)
#같은값 인덱스 만들어주기 위해 일부러 숫자 지정
for i in range (0,len(data_type)):
    data_type[i].append(i)
#행 번호    
dt_loc_image =[]
dt_loc_mpeg =[]
for i in data_type:
    for j in i:
        if j == "image":
            dt_loc_image.append(data_type.index(i))
        if j == "MPEG":
            dt_loc_mpeg.append(data_type.index(i))

#비디오 모으기 및 확장자 바꾸기

for i in range(0,len(dt_loc_mpeg)):
    for j in dt_loc_mpeg:
        shutil.copy2(x+"/"+F["Data_F"][j],y)
for i in range(0,len(dt_loc_mpeg)):
    for j in dt_loc_mpeg:
        if os.path.isfile(F["Data_F"][j]+"."+data_type[j][0]):
            continue
        else:
            os.rename(F["Data_F"][j],F["Data_F"][j]+"."+data_type[j][0])
            break
for j in dt_loc_mpeg:
    shutil.move(F["Data_F"][j]+"."+data_type[j][0],y+"/"+F["URL_Info_short"][j])

    
#이미지 모으기 및 확장자 바꾸기
for i in range(0,len(dt_loc_image)):
    for j in dt_loc_image:
        shutil.copy2(x+"/"+F["Data_F"][j],y)
for i in range(0,len(dt_loc_image)):
    for j in dt_loc_image:
        if os.path.isfile(F["Data_F"][j]+"."+data_type[j][0]):
            continue
        else:
            os.rename(F["Data_F"][j],F["Data_F"][j]+"."+data_type[j][0])
            break
for j in dt_loc_image:
    shutil.move(F["Data_F"][j]+"."+data_type[j][0],y+"/"+F["URL_Info_short"][j] )


pd.set_option('display.max_columns', None) # 전체 열 보기
pd.set_option('display.max_rows', None) # 전체 행 보기
def x():
    return data_type


vid = []
for i in dt_loc_mpeg:
    a= F["URL_Info_short"][i].rstrip(".")
    b=F["URL_Info_short"][i].strip(".")
    vid.append(a)           
video_list = list(set(vid))
def video():
    return video_list

img = []
for i in dt_loc_image:
    a= F["URL_Info_short"][i].rstrip(".")
    b=F["URL_Info_short"][i].strip(".")
    img.append(a)           
image_list = list(set(img))
def image():
    return image_list
