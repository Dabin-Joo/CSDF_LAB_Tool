# Mac_Forensic_tool

## Introduction
This is the tool that can collect data that is helpful for MacOS forensics.

## Requirement
OS : MacOS\
Langauage : Python 3.7 or above version\

## install
Download all python files in Mac_Forensic_tool and place them in one directory

## Run
```c
python main.py <parameters>
```
You can use the parameters like '-h','-b','-c', etc.\
The details are in the 'How to use'
- [How to use](#how-to-use)

## How to use
* -h : explain tool and it's parameters
```c
This is the MacOS forensic tool.
We can collect some artifacts of Mac without password.
if you want to see the explanation of the parameters, you can use "-h".

< Parameters >
 -b : Bluetooth connecting devices
 -c : command history
 -f : file metadata trace(creation, modification, last use)
 -h : help
 -l : log
 -p : installed programs' name
 -ws : web browser[Safari]
 -wc : web browser[Chrome]
```
* -b : Bluetooth connecting devices(com.apple.bluetooth.plist)
  * No other input needed
  * output : bluetooth_log.plist, bluetooth_log.txt
  * This function is to extract the original file(/Library/Preferences/com.apple.bluetooth.plist) and store the neccessary content in .txt file.

* -c : terminal instructions history 
  * input : username
  * output: command_history.txt
  * According to the version of Mac OS, choose shell type
    * 10.14 or lower : bash
    * 10.15 or higher : zsh
* -f : metadata search(creation, modification, last use time)\
  <img src = "https://user-images.githubusercontent.com/119034536/206067802-58e102cc-8905-4809-ac81-36cb67b81b54.png"/>
  * input : day(format: yyyy-mm-dd)
  * output : searching result on shell

* -p : show installed programs’ name
  * input : username
  * output : result on shell

* -ws : Safari histroy - download, visit
  * input : username
  * output : History.db, Downloads.plist, Safari_url.txt, Safari_download.txt

* -wc : Chrome history - download, visit
  * input : username
  * output : History, chrome_url.txt, chrome_download.txt

## Output
The output files will be stored in the path of working directory
