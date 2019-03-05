#-*-coding:utf-8-*-
# Coded By Deray
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3
'''
	 Rebuild Copyright Can't make u real programmer
'''

import os,sys,requests
from data import banner
banner.cekPlatform()
from data import listen
from data import cache
from data.color import *
from data import reports
from data import dumpper
from data import risetPass
from data import create_server
from data import chatSpammer
from data import grupSpammer
from data import multiBruteforce
from data import reportContent
from data import auto_addgrup

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
			dumpper.pilihan()
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
			print "\n\t[ Select Actions ]\n"
			print "{%s01%s} Report Status"%(G,N)
			print "{%s02%s} Mass Report"%(G,N)
			i=raw_input("\n%s[%s+%s] %sActions>> "%(
			G,R,G,N))
			if (i == "1" or i == "01"):
				reportContent.reportContent()
			elif (i == "2" or i == "02"):
				reports.report()
			else:sys.exit("%s[!]%s invalid options!"%(R,N))
		elif (asw == "6" or asw == "06"):
			auto_addgrup.grup()
		elif (asw == "7" or asw == "07"):
			risetPass.risetPass()
		elif (asw == "8" or asw == "08"):
			create_server.locator()
		elif (asw == "9" or asw == "09"):
			create_server.gps()
		elif (asw == "10"):
			listen.listen()
		elif (asw == "11"):
			print("[%s#%s] Updating Asu Toolkit ..."%(G,N))
			os.system("git pull")
			print "%s[%s**%s]%s Asu was updated. ¯\_(ツ)_/¯"%(G,R,G,N)
			exit()
				
		
		elif (asw == "12"):
			exit("%s[%s*%s%s]%s Bye ¯\_(ツ)_/¯"%(C,R,N,C,N))
		elif (asw.lower() == "banner"):
			banner.cekPlatform()
			print(banner._asu_banner())
			self.aso()
		else:
			print("[- invalid options: "+asw)
			return self.aso()
			
if __name__ == "__main__":
	ASU()
