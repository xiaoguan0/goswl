#by XiaoguanStudio
import os

print("GoWSL v1.0 by XiaogaunStudio 由Python构建")
while True:
	print("Ctrl + D 关闭目前使用的命令行，注意！关闭后可能不会保存输出历史记录")
	print("由于系统限制，Ctrl + D暂不支持CMD与PowerShell")
	print("Ctrl + D后出现抽风显示错误的情况，不必在意，正常使用即可")
	print("info：ubuntu kali node debain cmd powershell(po)")
	wsla = input("请输入要切换的系统： ")
	if wsla == 'cmd':
		print(" ")
		print("正在切换至命令提示符")
		os.system('cmd')
	if wsla == 'po':
		print(" ")
		print("已识别")
		print("正在切换至PowerShell")
		os.system('powershell')
	if wsla == 'powershell':
		print(" ")
		print("正在切换至PowerShell")
		os.system('powershell')
	if wsla == 'ubuntu':
		print(" ")
		print("正在切换至Ubuntu")
		os.system('C:\Windows\system32\wsl.exe -d Ubuntu')
	if wsla == 'kali':
		print(" ")
		print("正在切换至Kali-linux")
		os.system('C:\Windows\system32\wsl.exe -d kali-linux')
	if wsla == "kail":
		print(" ")
		print("对不起打错了，纠正：kali")
		print("正在切换至Kali-linux")
		os.system("C:\Windows\system32\wsl.exe -d kali-linux")
	if wsla == "node":
		print(" ")
		print("正在切换至node-js")	
		os.system("node.exe")
	if wsla == "debian":
		print(" ")
		print("正在切换至Debian")	
		os.system("debian.exe")
	else:
		print("错误，请重试")
