import calculate_offset
import byte_size
import os

data_path= input("Please enter the cache file route that has data_#(0,1,2,3):")
#data_path = data_path.replace("\"","").replace("\\","/")

while True:
    if os.path.isdir(data_path) == False:
        data_path=input("***Invalid Route*** Please enter the route again:")
        continue
    data_check = data_path.replace("\\","/")
    if os.path.isfile(data_check+"/data_0") == False:
        data_path=input("***Cant find all data_# file*** Please enter the route again:")
        continue
    if os.path.isfile(data_check+"/data_1") == False:
        data_path=input("***Cant find all data_# file*** Please enter the route again:")
        continue
    if os.path.isfile(data_check+"/data_2") == False:
        data_path=input("***Cant find all data_# file*** Please enter the route again:")
        continue
    if os.path.isfile(data_check+"/data_3") == False:
        data_path=input("***Cant find all data_# file*** Please enter the route again:")
        continue
    else:
        break

def path():
    return data_path        
    

file = open(data_path +"/data_0",'rb')
size = byte_size.size(file)
file.seek(8192,1)
loc= 0
data =[]
url = []
offset_data1 = []
offset_data2 = []
offset_data3 = []
while True:
    loc = file.tell()
    if loc >= size:
        break
    y =file.read(36)
    if y.hex() == "000000000000000000000000000000000000000000000000000000000000000000000000":
        continue
    data.append(y.hex())

for i in range(0,len(data)):
    url.append(data[i][48:56])
for i in range(0, len(url)):
    if url[i][4:6] == "01":
        idx = url[i][2:4]+url[i][0:2]    
        result = calculate_offset.data1(idx)
        offset_data1.append(result)
    elif url[i][4:6] == "02":
        idx = url[i][2:4]+url[i][0:2]
        result = calculate_offset.data2(idx)
        offset_data2.append(result)
    elif url[i][4:6] == "03":
        idx = url[i][2:4]+url[i][0:2]
        result = calculate_offset.data3(idx)
        offset_data3.append(result)
    else:
        print("Error: Wrong Data")

def offset_1():
    return offset_data1
def offset_2():
    return offset_data2
def offset_3():
    return offset_data3

