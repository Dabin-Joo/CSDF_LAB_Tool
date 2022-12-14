import data0 as d0
import data1 as d
import table
x = d0.offset_1()

#Cache_info 표만들기
t = table.t_maker(9,len(x),0)
ind = []
for i in range (0,len(x)):
    ind.append(i)
col = ["URL_size", "Metadata_size","Data_size","Metadata_location"\
    ,"MDF_Number","Data_location","DF_Number","Data_F","data1_offset"]
t.columns = col
t.index = ind

t["URL_size"] = d.US()
t["Metadata_size"] = d.MS()
t["Data_size"] = d.DS()
t["Metadata_location"] = d.ML()
t["Data_location"] = d.DL()
t["Data_F"] = d.F()
t["MDF_Number"] = d.MDF()
t["DF_Number"] = d.DF()
t["data1_offset"]= x


#URl_info 표만들기
p = table.t_maker(3,len(x),0)
pnd =[]
for i in range (0,len(x)):
    pnd.append(i)
pol = ["URL_Info","URL_Info_short","Content_type"]
p.columns = pol
p.index = pnd
p["URL_Info"] = d.UI()
p["URL_Info_short"] = d.UIS()
p["Content_type"]=d.CT()
p["Data_F"] = d.F()
p = p.query('Data_F != "0"')

#F_info 표만들기
df = t.query('Data_F != "0"')
a=p.drop(['URL_Info','URL_Info_short','Content_type'],axis = 1)
a["Metadata_location"] = df["Metadata_location"]
a["Metadata_size"] = df["Metadata_size"]
a["MDF_Number"] = df["MDF_Number"]


def Cache_info():
    return t
def URL_info():
    return p
def F_info():
    return a

