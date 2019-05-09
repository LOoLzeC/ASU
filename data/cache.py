#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import os

def cleanCache():
	for x in os.listdir("data"):
		if "banner.pyc" in x:
			continue
		else:
			os.system("rm -rf data/%s"%(x.replace("py","pyc")))
