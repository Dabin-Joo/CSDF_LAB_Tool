import data0 as d
import Little_endian
import calculate_offset
import magic
import byte_size as b
import check_data_f_route as f
#pip install python-magic-bin
x = d.offset_1()
file0 = open(d.path() +"/data_0",'rb')
file1 = open(d.path() +"/data_1",'rb')
file2 = open(d.path() +"/data_2",'rb')
file3 = open(d.path() +"/data_3",'rb')
def file_0():
    return file0
def file_1():
    return file1
def file_2():
    return file2
def file_3():
    return file3


URL_size =[]
Metadata_size=[]
Data_size = []
Metadata_location = []
Data_location = []
MDf_Number = [] # data_0,1,2,3 체크 datafile metadata 용
"""Meta_F =[]
Meta_F_Number = []"""
Data_F = []
Data_F_NoZero =[]
Df_Number = [] # data_0,1,2,3 체크 datafile data 용

for i in range(0,len(x)):
    file1.seek(x[i] + 32,1)
    U_size = file1.read(4)
    file1.read(4)
    M_size = file1.read(4)
    D_size = file1.read(4)
    file1.read(8)
    M_loc = file1.read(2)
    check_M_loc = file1.read(1)
    check_f = file1.read(1)
    D_loc = file1.read(2)
    check_D_loc = file1.read(1)
    check_f_d = file1.read(1)
    
    """if check_f.hex() == "80":
        f_nb = "f_" + check_M_loc.hex() + M_loc.hex()[2:4]+M_loc.hex()[0:2]
        Meta_F.append(f_nb)
        Meta_F_Number.append(i)"""
    if check_M_loc.hex() == "01":
        result = calculate_offset.data1(Little_endian.LD(M_loc))
        Metadata_location.append(result)
    elif check_M_loc.hex() == "02":
        result = calculate_offset.data2(Little_endian.LD(M_loc))
        Metadata_location.append(result)
    elif check_M_loc.hex() == "03":
        result = calculate_offset.data3(Little_endian.LD(M_loc))
        Metadata_location.append(result)
    else:
        Metadata_location.append("0")
    
    
    if check_D_loc.hex() == "01":
        result = calculate_offset.data1(Little_endian.LD(D_loc))
        Data_location.append(result)
    elif check_D_loc.hex() == "02":
        result = calculate_offset.data2(Little_endian.LD(D_loc))
        Data_location.append(result)
    elif check_D_loc.hex() == "03":
        result = calculate_offset.data3(Little_endian.LD(D_loc))
        Data_location.append(result)
    else:
        Data_location.append("0")
    if check_f_d.hex() == "80":
        f_nb = "f_" + check_D_loc.hex() + D_loc.hex()[2:4]+D_loc.hex()[0:2]
        Data_F.append(f_nb)
        Data_F_NoZero.append(f_nb)
    else:
        Data_F.append("0")
   
    MDf_Number.append(check_M_loc.hex()[1])
    Df_Number.append(check_D_loc.hex()[1])
    URL_size.append(int(Little_endian.LD(U_size),16))
    Metadata_size.append(int(Little_endian.LD(M_size),16))
    Data_size.append(int(Little_endian.LD(D_size),16))
    file1.seek(-(x[i]+64),1)

def start():
    return x
def US():
    return URL_size
def MS():
    return Metadata_size
def DS():
    return Data_size
def ML():
    return Metadata_location  
def MDF():
    return MDf_Number
def DL():
    return Data_location  
def DF():
    return Df_Number
def F():
    return Data_F
URL_Info =[]

for i in range (0,len(x)):
    file1.seek(x[i]+96,1)
    URL = file1.read(URL_size[i])
    URL_decode= URL.decode('utf-8','ignore')
    if URL_size[i] == "00000000":
        URL_Info.append("X")
    else:
        URL_Info.append(URL_decode)
    file1.seek(-(x[i]+96+URL_size[i]),1)
for i in range (0, len(URL_Info)):
    a = URL_Info[i].replace("\x00","")
    URL_Info[i] = a
def UI_specific():
    return URL_Info
URL = []
c1=0
c2=0
for i in range(0,len(URL_Info)):
    for j in range (0,len(URL_Info[i])):
        if URL_Info[i][j:j+4] == ".com":
            c1 = j
        a = URL_Info[i].replace(URL_Info[i][c1+4:0],"")
        if URL_Info[i][j:j+5] == "https":
            c2 = j
        a = URL_Info[i].replace(URL_Info[i][0:c2],"")
    #a = URL_Info[i].replace(URL_Info[i][0:c2],"").replace(URL_Info[i][c1+4:],"")
    URL.append(a)        
def UI():
    return URL
URL_Info_short =[]
c3=0
c4=0
for i in range(0,len(URL)):
    for j in range (0,len(URL[i])):
        if URL[i][j:j+4] == ".com":
            c3 = j
        #a = URL_Info[i].replace(URL_Info[i][c1+4:0],"")
        if URL[i][j:j+8] == "https://":
            c4 = j
        #a = URL_Info[i].replace(URL_Info[i][0:c2],"")
    a = URL[i].replace(URL[i][0:c4+8],"").replace(URL[i][c3+4:],"")
    change = a.maketrans({"/":"."})
    a=a.translate(change)
    URL_Info_short.append(a)

def UIS():
    return URL_Info_short

fpath = input("Please enter the cache file route that has f_\#\#\#\#\#\# in it:")
fpath = f.f_path(fpath,Data_F_NoZero)
def checked_fpath():
    return fpath
Content_type = []
for i in range (0,len(x)):
    file0_size=b.size(file0)
    file1_size=b.size(file1)
    file2_size=b.size(file2)
    file3_size=b.size(file3)
    back = int(Data_location[i]) + Data_size[i]
    
    if (Df_Number[i] == "0") & (b.check(file0_size,back) == True):
        file0.seek(int(Data_location[i]),1)
        CT = file0.read(Data_size[i])
        Content_type.append(magic.from_buffer(CT))
        file0.seek(-back,1)
        
    elif (Df_Number[i] == "1")& (b.check(file1_size,back) == True):
        file1.seek(int(Data_location[i]),1)
        CT = file1.read(Data_size[i])
        Content_type.append(magic.from_buffer(CT))
        file1.seek(-back,1)
    elif (Df_Number[i] == "2")& (b.check(file2_size,back) == True):
        file2.seek(int(Data_location[i]),1)
        CT = file2.read(Data_size[i])
        Content_type.append(magic.from_buffer(CT))
        file2.seek(-back,1)
    elif (Df_Number[i] == "3")& (b.check(file3_size,back) == True):
        file3.seek(int(Data_location[i]),1)
        CT = file3.read(Data_size[i])
        Content_type.append(magic.from_buffer(CT))
        file3.seek(-back,1)
    elif (Df_Number[i] =="0") & (Data_F[i][0]=="f"):
        CT=magic.from_file(fpath+"%s"%("/"+Data_F[i]))
        Content_type.append(CT)
    else:
        Content_type.append("Data has no size")
for i in range(0,len(Content_type)):
    for j in range (0,len(Content_type[i])):
        if Content_type[i][j:j+4] == "data":
            Content_type[i]=Content_type[i].replace(Content_type[i][j+4:],"")
             
def CT():
    return Content_type        

