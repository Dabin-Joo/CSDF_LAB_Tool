import F_Info
import re
import cache_info
#Meta data에서 확장자 가져오기
table = F_Info.Meta_data()
#byte 값 제거하기 위해 string 변환
real = []
for i in range(0,len(table)):
    a=str(table[i].encode('utf-8'))
    real.append(a)

# content type으로 정렬해서 확장자 알아내기(확인 결과 content-type, Content-Type)
ddc = []#content type 정규 표현식으로 추출
ddc_string = []#r모듈 사용하여 re.match값으로 표현되어 string변환

bbc = []#Content Type 정규 표현식으로 추출
bbc_string = []#r모듈 사용하여 re.match값으로 표현되어 string변환
for i in range(0, len(real)):
    g = re.search("content-type:(.*?);",real[i])
    y = re.search('Content-Type:(.*?);',real[i])
    ddc.append(y)
    bbc.append(g)
for i in range(0,len(real)):
    bbc_string.append(str(bbc[i]))
    ddc_string.append(str(ddc[i]))
#바이트 인식 못하는 오류 제거 위해 \값을 ^ 변환
#이후 type: ~ ^까지의 값을 추출
c1 =0
c2 =0
c3=0
c4=0
Extension=[]
CT_d=[]
for i in range(0,len(bbc_string)):
    change_bbc = bbc_string[i].maketrans({"\\":"^"})
    a=bbc_string[i].translate(change_bbc)
    for j in range(0,len(a)):

        if a[j:j+5] == "type:":
            c1 = j
        if a[j:j+5] == "^^x00":
            c2 = j
            
    a = a.replace(a[0:c1+5],"").replace(a[c2:],"")
    Extension.append(a)
for i in range(0,len(bbc_string)):
    change_ddc = ddc_string[i].maketrans({"\\":"^"})
    a=ddc_string[i].translate(change_bbc)
    for j in range(0,len(a)):

        if a[j:j+5] == "Type:":
            c3 = j
        if a[j:j+5] == "^^x00":
            c4 = j
            
    a = a.replace(a[0:c3+5],"").replace(a[c4:],"")
    CT_d.append(a)
# 두 리스트를 하나로 합침(None의 값이 있기 떄문)
for i in range(0,len(CT_d)):
    if Extension[i] == "":
        Extension[i] = CT_d[i]
def E():
    return Extension
