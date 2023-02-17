import os

wsla = input("请输入要切换的系统： ")
if wsla == 'ubuntu':
    os.system('C:\Windows\system32\wsl.exe -d Ubuntu')
if wsla == 'kali':
    os.system('C:\Windows\system32\wsl.exe -d kali-linux')
if wsla == "kail":
    print("对不起打错了，kali")
    os.system("C:\Windows\system32\wsl.exe -d kali-linux")
if wsla == "node":
    os.system("C:\Program Files\nodejs\node.exe")
if wsla == "debian":
    os.system("debian.exe")
