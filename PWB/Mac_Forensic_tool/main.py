import sys
from logging import getLog
from command_history import print_exCommand
from install_list import check_program
from safari_check import extract_Safari
from chrome_check import extract_Chrome
from file_trace import metadata_trace
from find_BTdevices import find_BTdevices

list_agrv = sys.argv

explain = """
This is the MacOS forensic tool.
We can collect some artifacts of Mac without password.
if you want to see the explanation of the arguments, you can use "-h" argument.

< Arguments >
 -b : Bluetooth connecting devices
 -c : command history
 -f : file metadata trace(creation, modification, last use)
 -h : help
 -l : log
 -p : installed programs' name
 -ws : web browser[Safari]
 -wc : web browser[Chrome]
"""
if len(list_agrv) ==2:
    if list_agrv[1] == "-h":
        print(explain)
    elif list_agrv[1] == "-l": #log
        print("extracting log....hold on please...")
        getLog()
    elif list_agrv[1] == "-c": #command history
        print_exCommand()
    elif list_agrv[1] == "-f" : #file_trace
        metadata_trace()
    elif list_agrv[1] == "-p": #installed program name
        check_program()
    elif list_agrv[1] == "-ws": #webbrwoser
        extract_Safari()
    elif list_agrv[1] == "-wc": #webbrwoser
        extract_Chrome()
    elif list_agrv[1] == "-b": #Bluetooth
        find_BTdevices()
    else:
        print("Wrong Command!!")
        print(explain)
else:
    print("Wrong Command!!")
    print(explain)
