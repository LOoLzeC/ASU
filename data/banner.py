#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

from data.color import *
import random,os,sys
from data import cache
import requests
cache.cleanCache()
import requests
r=requests.get("https://raw.githubusercontent.com/LOoLzeC/ASU/master/raw/version.txt").text.replace("\n","")
menu ="""
  %s{%s01%s} Phising Attacks Vectors
  %s{%s02%s} Multi BruteForce Attacks Vectors
  %s{%s03%s} Chat Spammers Attack Vectors
  %s{%s04%s} Group Chat Spammers Attacks Vectors
  %s{%s05%s} Multi Reports Attacks Vectors
  %s{%s06%s} Auto Add Group Members
  %s{%s07%s} Auto Riset Passwords Attacks Vectors
  %s{%s08%s} Redirect To Cookie HighJacking Attacks Vectors
  %s{%s09%s} Redirect To GPS Attacks Vectors
  %s{%s10%s} ASU Server Listener
  %s{%s11%s} Update.
  %s{%s12%s} Byee"""%(
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N)
	
banner1 = """
%s%sAvailable Version: %s
   _____    _____________ ___ 
  /  _  \  /   _____/    |   \
|
 /  /_\  \ \_____  \|    |   /%sToolkit v.2%s
/    |    \/        \    |  /%sCoded By Deray%s
\____|__  /_______  /______/%sFacebook Hacking Tools%s
        \/        \/ 
%s
"""%(W,C,r,R,C,R,C,R,C,menu)

banner2 = """%s%s

        .d8b.  .d8888. db    db 
       d8' `8b 88'  YP 88    88 %sAvailable Version: %s%s
       88ooo88 `8bo.   88    88 %sFacebook%s
       88~~~88   `Y8b. 88    88 %sHacking%s
       88   88 db   8D 88b  d88 %sToolkit%s
       YP   YP `8888Y' ~Y8888P' %s
       
            [ Asu Toolkit ]
         [ Created By Deray ]
%s
"""%(W,C,R,r,C,R,C,R,C,R,C,N,menu)

banner3 = """
                           __
               _______    /*_>-< Available Version: %s
           ___/ _____ \__/ /
          <____/     \____/
        Asu Toolkit By Deray
%s
"""%(r,menu)

banner4 = """
       __
      {0O}
      \__/
      /^/
     ( (              -ASU TOOLKIT-
     \_\_____   - Facebook Hacking Toolkit -
     (_______) - Available Version: %s
    (_________()Oo
%s
"""%(r,menu)
banners=[banner1,banner2,banner3,banner4]

def _asu_banner():
	global banners
	return random.choice(banners)

def cekPlatform():
	if (sys.version_info.major !=2):
		sys.exit("%s[!]%s Oh Bro,ASU toolkit is only supported in Python2.7.XX."%(R,N))
	else:
		if ("linux" in sys.platform.lower()):
			os.system("clear")
		if ("win" in sys.platform.lower()):
			os.system("cls")
		else:
			os.system("clear")
