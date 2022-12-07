#Check the file metadata up to () days ago -> mdls command(Spotlight)
import os
def createTime(date):
    stream = os.popen("mdfind -onlyin $HOME 'kMDItemContentCreationDate>$time.iso("+date+")'")
    output = stream.readlines()
    for i in output:
        print(i)

def modTime(date):
    stream = os.popen("mdfind -attr kMDItemContentModificationDate -onlyin $HOME 'kMDItemContentModificationDate>$time.iso("+date+")'")
    output = stream.readlines()
    for i in output:
        print(i)

def lastuseTime(date):
    stream = os.popen("mdfind -attr kMDItemLastUsedDate -onlyin $HOME 'kMDItemLastUsedDate>$time.iso("+date+")'")
    output = stream.readlines()
    for i in output:
        print(i)

def metadata_trace():
    menu = """
    <menu>
    1. Created Time
    2. Modified Time
    3. Last Use Time
    """
    print(menu)
    num = int(input("Type the number of menu which you want to know. : "))
    if num == 1:
        date = input("Files which were created after...(ex- 2020-01-01) : ")
        createTime(date)
    elif num == 2:
        date = input("Files which were modified after...(ex- 2020-01-01) : ")
        modTime(date)
    elif num == 3:
        date = input("Files which were used after...(ex- 2020-01-01) : ")
        lastuseTime(date)
    else:
        print("Wrong Command")
