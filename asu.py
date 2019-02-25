#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import os,sys
from data import banner
banner.cekPlatform()
from data import listen
from data import cache
from data.color import *
from data import reports
from data import create_server
from data import chatSpammer
from data import grupSpammer
from data import multiBruteforce
from data import reportContent
print(banner._asu_banner())
cache.cleanCache()

class ASU:
	def __init__(self):
		try:
			self.aso()
		except Exception as f:
			print("%s[!]%s %s"%(R,N,f))
			os.sys.exit("%s[-%s User Exit."%(R,N))
	
	def aso(self):
		try:
			asw=raw_input("%s[%s+%s]%s @deray_> "%(G,R,G,N))
		except:
			sys.exit("%s[!]%s User Interrupt."%(R,N))
		if (asw == ""):
			return self.aso()
		elif (asw =="1" or asw == "01"):
			create_server.phising()
		elif (asw == ""):
			pass
		elif (asw == "2" or asw == "02"):
			multiBruteforce._prepares()
		elif (asw == "3" or asw == "03"):
			try:
				print("\n\t[ Select Actions ]\n")
				print("  {%s01%s} Single Chat Spammer"%(G,N))
				print("  {%s02%s} Mass Chat Spammer With List Of ID Targets"%(G,N))
				try:
					r=raw_input("\n%s[%s+%s]%s Actions>> "%(
					G,R,G,N))
				except:
						sys.exit("%s[!]%s User Interrupt."%(R,N))
				if (r == "1" or r == "01"):
					try:
						chatSpammer.SPAMMER()
					except Exception as __errors__:
						print("[!] %s"%(__errors__))
				elif (r == "2" or r == "02"):
					chatSpammer.massal()
				else:sys.exit("[!] Invalid Options!")
			except Exception as f:
				print("%s[!]%s %s"%(R,N,f))
				sys.exit("\n[- User Interrupt.")
		elif (asw == "4" or asw == "04"):
			try:
				print("\n\t[ Select Actions ]\n")
				print("  {%s01%s} Single Group Spam"%(G,N))
				print("  {%s02%s} Mass Spam"%(G,N))
				try:
					r=raw_input("\n%s[%s+%s]%s Actions>> "%(
					G,R,G,N))
				except:
						sys.exit("%s[!]%s User Interrupt."%(R,N))
				if (r == "1" or r == "01"):
					try:
						grupSpammer._grupSpammer()
					except Exception as __errors__:
						print("[!] %s"%(__errors__))
				elif (r == "2" or r == "02"):
					grupSpammer._spamMassal()
				else:sys.exit("[!] Invalid Options!")
			except Exception as f:
				print("%s[!]%s %s"%(R,N,f))
				sys.exit("\n[- User Interrupt.")
		elif (asw == "5" or asw == "05"):
			reports.report()
		elif (asw == "6" or asw == "06"):
			create_server.locator()
		elif (asw == "7" or asw == "07"):
			create_server.gps()
		elif (asw == "8" or asw == "08"):
			listen.listen()
		elif (asw == "9" or asw == "09"):
			reportContent.reportContent()
		elif (asw == "10"):
			exit()
		elif (asw.lower() == "banner"):
			banner.cekPlatform()
			print(banner._asu_banner())
			self.aso()
		else:
			print("[- invalid options: "+asw)
			return self.aso()
			
if __name__ == "__main__":
	ASU()
