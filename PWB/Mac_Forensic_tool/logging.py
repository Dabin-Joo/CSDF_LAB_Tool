#log show 명령어 사용해서 콘솔 출력 없이 사용
import os

def getLog():
    stream = os.popen('log show')
    output = stream.readlines()
    #for i in range(0,10):
    #    print(output[i])
    now_path = os.getcwd()
    file = now_path+"/log.txt"
    with open(file, "w") as f: #현재 경로에 다른 파일(log.txt)로 저장 -> 이 과정에서의 데이터 무결성은 어떻게 확인?
        for i in range(0, len(output)):
            f.write(output[i])
    print("Check the file, 'log.txt'")
