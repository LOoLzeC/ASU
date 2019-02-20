# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
import re
import random
import getpass
import threading
try:
	import bs4
	import mechanize
except:
	print("[!] please install mechanize&bs4 first bro")
	print("[*] are u noob? command: pip2 install mechanize;pip2 install bs4")

_KONTOOL = ""
_TARGETS = ""
_NGENTDS = 0

print("""
spammer
   _____    _____________ ___ 
  /  _  \  /   _____/    |   \
|
 /  /_\  \ \_____  \|    |   /
/    |    \/        \    |  /
\____|__  /_______  /______/ coded by deray
        \/        \/ facebook bot chat spammer
""")
class SPAMMER:
	def __init__(self):
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.addheaders = [
			(
				"User-Agent",
				"Mozilla/5.1 (Linux Android)"
			)]
		self._url="https://mbasic.facebook.com/"
		print("[*] Login Your Facebook ^^")
		self._email = raw_input("[*] Email: ")
		self._pasw = getpass.getpass("[*] Passs: ")
		print("[+] Trying to login ...")
		self.login()
		
	def login(self):
			self.br.open("https://mbasic.facebook.com")
			self.br.select_form(nr=0)
			self.br.form["email"] = "{}".format(self._email)
			self.br.form["pass"]  ="{}".format(self._pasw)
			self.br.submit()
			if "save-device" in self.br.geturl():
				print("[*] Login success ...")
				self._generateTarget()
			else:
				print("[!] Failed to login? whut the hell?? :'v")
				exit()
				
	def _generateTarget(self):
		global _TARGETS,_KONTOOL
		_targ=raw_input("[*] Input target ID: ")
		_TARGETS=self._url+_targ
		self.br.open(_TARGETS)
		self.r=re.findall('<head><title>(.*?)</title>',
		self.br.response().read())
		if len(self.r) !=0:
			print "[*] Target name: \033[1;37m\033[31m%s\033[0m"%(self.r[0])
		else:
			print "[!] Unknown target"
			return self._generateTarget()
		self._counts=input("[+] Loop: ")
		self.br.open(_TARGETS)
		_bs = self.br.response().read()
		_b=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
		for x in _b.find_all("a",href=True):
			if "/messages/thread/" in x["href"]:
				_KONTOOL=x["href"]
		return self.inputMessages()
	
	def inputMessages(self):
		global _KONTOL
		global _NGENTDS
		print("[*] Use Sparate , (coma) to random msg: ts,spm")
		_msg=raw_input("[+] Message: ").split(",")
		print("[+] Starting!")
		print("[+] Sending %s message to \033[1;37m\033[31m%s\033[0m"%(
		self._counts,self.r[0]))
		for x in range(self._counts):
			ms=random.choice(_msg)
			self.br.open(_KONTOOL)
			self.br._factory.is_html=True
			try:
				self.br.select_form(nr=1)
				self.br.form["body"] = "{}".format(ms)
				self.br.submit()
			except:
				print "[:'(] oh bro, can't send messages"
				exit()
			_res=self.br.response().read()
			_NGENTDS+=1
			if len(re.findall(r"{}".format(ms),_res)) !=0:
				print " | \033[1;32m{} -> OK [{}]\033[0m".format(
				ms,_NGENTDS)
			else:
				print " | \033[1;37m\033[31m{} -> FALSE [{}]\033[0m".format(
				ms,_NGENTDS)
		print("[+] Finished.")
		
if __name__ == "__main__":
	SPAMMER()