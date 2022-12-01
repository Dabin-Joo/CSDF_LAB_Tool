#bash_history or zsh_history 분석 파일 -> 완
import os

def print_exCommand():
    username = input("Input user's name: ")
    
    lines = os.popen("sw_vers")
    for line in lines:
        list1 = line.split(":")
        #print(list1)
        if list1[0] == "ProductVersion":
            os_version = list1[1]
            os_version = os_version.replace("\t", "")
            os_version = os_version.replace("\n", "")
            os_list = os_version.split(".")
            for idx, i in enumerate(os_list):
                os_list[idx] = int(i)
    #mac 기본 쉘 타입 = 10.15 미만은 bash, 10.15 이상 zsh 기본 사용
    if os_list[0] < 10:
        history_path = "/Users/"+username+"/.bash_history"
    elif os_list[0] ==10 and os_list[1]<15:
        history_path = "/Users/"+username+"/.bash_history"
    else:
        history_path = "/Users/"+username+"/.zsh_history" #데이터 무결성 확인 방법

    with open(history_path, "rb") as file:
        lines = file.readlines()
        with open("command_history.txt", "w") as f:
            for i in lines:
                f.write(str(i)+"\n")
    print("Check the file, 'command_history.txt'")