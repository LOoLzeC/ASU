import requests,time,os
os.system("clear")
print requests.get("https://raw.githubusercontent.com/LOoLzeC/ASU/master/raw/license.txt").text
raw_input("press enter ...")
os.system("python2 main.py")