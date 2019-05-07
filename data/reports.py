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

class report(object):
	def __init__(self):
		self.fail=0
		self.found=0
		self.errors=0
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.req=requests.Session()
		self.akun()
		
	def akun(self):
		s=self.req.post(self.i.format("login"),data=
			{
				"email":self.config["email"],
				"pass":self.config["pass"]
			}
		).url
		if "save-device" in s or "m_sess" in s:
			self.ak()
		else:exit("%s[!]%s login failed."%(R,N))
	
	def ak(self):	
		try:
			self.a=open(raw_input("%s[?]%s Account list: "%(
				G,N))).read().splitlines()
		except Exception as e:
			print("%s[!]%s %s"%(R,N,e))
			self.akun()
		self.target()
		
	def target(self):
		self.tar=raw_input("%s[?]%s Target ID: "%(G,N))
		if self.tar =="":
			self.target()
		r=self.req.get(self.i.format(self.tar))
		if r.status_code ==200:
			bs=bs4.BeautifulSoup(r.text,features="html.parser")
			print("%s[*]%s Target Name: %s"%(
				G,N,bs.find("title").text))
			print("%s[*]%s Total Account: %s"%(G,N,len(self.a)))
			print("%s[*]%s Report Started."%(G,N))
			map(self.login,self.a)
			exit()
		else:
			print("%s[!]%s Unknown target id: %s"%(R,N,self.tar))
			self.target()
		
	def login(self,a):
		m=mechanize.Browser()
		m.set_handle_equiv(True)
		m.set_handle_redirect(True)
		m.set_handle_robots(False)
		m.addheaders=[("User-Agent",random.choice(
			open("raw/header/ua.txt").read().splitlines()))]
		m.open(self.i.format("login"))
		m._factory.is_html=True
		m.select_form(nr=0)
		m["email"]="%s"%(a.split("|")[-0])
		m["pass"]="%s"%(a.split("|")[-1])
		response=m.submit().geturl()
		if "save-device" in response or "m_sess" in response:
			try:
				self.openprof(m)
			except:
				self.errors+=1
		else:
			self.fail+=1
	
	def openprof(self,m):
		tag=json.loads(json.dumps(
			{
				"name":"profile_fake_account",
				"c":"FRX_PROFILE_REPORT_CONFIRMATION",
				"c2":"yes"}))
		m.open(self.i.format(self.tar))
		m._factory.is_html=True
		m.open(m.find_link(url_regex="mbasic/more").url)
		m._factory.is_html=True
		m.open(m.find_link(url_regex="nfx/").url)
		m._factory.is_html=True
		m.select_form(nr=0)
		m["tag"]=[tag["name"]]
		m.submit(name="action")
		m._factory.is_html=True
		m.select_form(nr=0)
		m["action_key"]=[tag["c"]]
		m.submit(name="action")
		m._factory.is_html=True
		m.select_form(nr=0)
		m["checked"]=[tag["c2"]]
		m.submit(name="action")
		m._factory.is_html=True
		self.found+=1
		print("\r[+] Reporting %s/%s login fail:-%s Error-:%s"%(
			self.found,len(self.a),self.fail,
		self.errors)),;sys.stdout.flush()
