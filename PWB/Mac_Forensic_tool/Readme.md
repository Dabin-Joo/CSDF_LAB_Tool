# Mac_Forensic_tool

## Introduction
This is the tool that can collect data that is helpful for MacOS forensics.

## Requirement
OS : MacOS\
Langauage : Python 3.7 or above version\
There is no need to install other libraries.(we use only Python standard library)

## install
Download all python files and place all files in one directory

## Run
```c
python main.py <parameters>
```
You can use the parameters like '-h','-b','-c', etc.\
The details are in the 'How to use'
- [How to use](https://github.com/CSDF-LAB/tool/main/PWB/Mac_Forensic_tool/Readme.md#how-to-use)

## How to use
- -h : explain tool and it's arguments\
```c
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
```
- -b : Bluetooth connecting devices\

- -c : terminal instructions history\
 
- -f : metadata search(creation, modification, last use time)\

- -p : show installed programs’ name\
 
- -ws : Safari histroy - download, visit\

- -wc : Chrome history - download, visit\


## Output
The output files will be stored in the path of working directory
