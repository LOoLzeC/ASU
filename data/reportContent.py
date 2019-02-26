import os
import zlib
import sys
import bs4
import random
import base64
import requests
import threading
from data import cache
from data.color import *
cache.cleanCache()

kontl=0

class report(threading.Thread):
	def __init__(self,req,url,length):
		threading.Thread.__init__(self)
		self.req=req
		self.url=url
		self.length=length
		self.heder=open(
		"raw/header/ua.txt"
		).read().splitlines()
		
	def run(self):
		global kontl
		ua={"User-Agent":random.choice(self.heder)}
		bs=bs4.BeautifulSoup(
			self.req.get(self.url,
			headers=ua).text,
		features="html.parser")
		for x in bs("form"):
			self.act= x["action"]
		for x in bs("input"):
			if "fb_dtsg" in x["name"]:
				self.dtsg= x["value"]
			if "jazoest" in x["name"]:
				self.jzst= x["value"]
			if "action" in x["name"]:
				self.sb= x["value"]
		b=bs4.BeautifulSoup(
		self.req.post(
		"https://mbasic.facebook.com/%s"%(self.act),
		data={
			"fb_dtsg":self.dtsg,
			"jazoest":self.jzst,
			"tag":"nudity",
			"action":self.sb},headers=ua).text,
		features="html.parser")
		for y in b("form"):
			self.a= y["action"]
		for k in b("input"):
			if "fb_dtsg" in k["name"]:
				self.b= k["value"]
			if "jazoest" in k["name"]:
				self.c=k["value"]
			if "action" in k["name"]:
				self.d=k["value"]
		self.req.post(
		"https://mbasic.facebook.com%s"%(self.a),
		data={
		"fb_dtsg":self.b,
		"jazoest":self.c,
		"tag":"nudity_involves_a_child",
		"action":self.d},headers=ua)
		kontl+=1
		print("\r[%s*%s] Reporting %s/%s             "%(
		G,N,kontl,self.length)),;sys.stdout.flush()
		
class reportContent:
	def __init__(self):
		self._req=requests.Session()
		self._url="https://mbasic.facebook.com{}"
		self.login()
		
	def login(self):
		self._email=raw_input("[%s*%s] Login Your Facebook ^^\n[%s*%s] Email: "%(C,N,G,N))
		self._pasw=raw_input("[%s*%s] Pass: "%(G,N))
		print("[%s*%s] Trying To Login ..."%(G,N))
		_bs=bs4.BeautifulSoup(
			self._req.get(self._url.format("/login")).text,
		features="html.parser")
		for x in _bs("input"):
			if "login" in x["name"]:
				self.submit=x["value"]
		s=self._req.post(self._url.format("/login"),
			data={
				"email":self._email,
				"pass":self._pasw,
				"login":self.submit
			}
		).url
		if "save-device" in s or "m_sess" in s:
			print("[%s*%s] Login Success."%(G,N))
			self.genTar()
		else:sys.exit("%s[!]%s Login Failed."%(R,N))
		
	def genTar(self):
		self._tg=raw_input("[%s#%s] Target ID: "%(G,N))
		if (self._tg == ""):
			return self.genTar()
		bz=bs4.BeautifulSoup(
			self._req.get(
				self._url.format("/%s"%(self._tg)
			)).text,
		features="html.parser")
		print("[%s*%s] Target Name:%s %s %s"%(
		G,N,R,bz.find("title").renderContents(),N))
		self.lop()
	
	def lop(self):
		self.lup=raw_input("[%s*%s] How many timeline page u want to get? "%(G,N))
		if (self.lup == ""):
			return self.lop()
		self.getStats()
		sys.exit("%s[%s*%s%s] %sok"%(C,R,N,C,N))
	def getStats(self):
		self.n=0
		tt=[]
		self.bs=""
		self.mom=[]
		self.bs=bs4.BeautifulSoup(
			self._req.get(
				self._url.format("/%s"%(self._tg))).text,
		features="html.parser")
		for i in range(int(self.lup)):
			self.getoken("%s"%(i),)
		for x in self.mom:
			t=report(self._req,x,len(self.mom))
			tt.append(t)
		for t in tt:
			t.start()
		for t in tt:
			t.join()
	def getoken(self,num):
		self.n+=1
		for x in self.bs.find_all("a",href=True):
			if "/nfx/basic/handle_action/" in x["href"]:
				self.mom.append(
					self._url.format(x["href"]))
				print("\r[%s+%s] GET: %s Reports Token In Page: %s  "%(
				G,N,len(self.mom),self.n
				)),;sys.stdout.flush()
			if "/profile/timeline/stream/" in x["href"]:
				self.bs=bs4.BeautifulSoup(
					self._req.get(self._url.format(
						"%s"%(x["href"])
					)).text,
				features="html.parser")
				break
		
