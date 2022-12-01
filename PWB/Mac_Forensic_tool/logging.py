#Using 'log show' command without password
import os

def getLog():
    stream = os.popen('log show')
    output = stream.readlines()

    now_path = os.getcwd()
    file = now_path+"/log.txt"
    with open(file, "w") as f: 
        for i in range(0, len(output)):
            f.write(output[i])
    print("Check the file, 'log.txt'")
