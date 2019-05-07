import threading
import mechanize
import bs4,re,sys,time,random
import os,json
import requests
from data.color import *
from data import cache
from data import language
from data import multiBruteforce
import subprocess as kontolatos
from multiprocessing.pool import ThreadPool
cache.cleanCache()

# Single
class SPAMMER(object):
	def __init__(self):
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.req = requests.Session()
		self.i="https://mbasic.facebook.com/{}"
		self.suck=0
		self.login()
		
	def login(self):
		s=self.req.post(self.i.format("login"),
			data={
				"email":self.config["email"],
				"pass":self.config["pass"]
			}
		).url
		if "save-device" in s or "m_sess" in s:
			self.target()
		else:
			exit("%s[!]%s Login Failed/checkpoint"%(R,N))
			
	def target(self):
		self.id=raw_input("%s[?]%s Target ID: "%(G,N))
		if self.id =="":
			self.target()
		k=self.req.get(self.i.format(self.id))
		if k.status_code ==200:
			bs=bs4.BeautifulSoup(k.text,features="html.parser")
			print("%s[*]%s Target: %s"%(G,N,bs.find("title").text))
			self.lup()
		else:
			print("%s[!]%s Unknown target id!"%(R,N))
			self.target()
			
	def lup(self):
		data=""
		self.datas=[]
		try:
			self.lop=input("%s[?]%s Loop: "%(G,N))
		except Exception as f:
			print("%s[!]%s %s"%(R,N,f))
			self.lup()
		a=bs4.BeautifulSoup(self.req.get(self.i.format(self.id)).text,
			features="html.parser")
		for x in a.find_all("a",href=True):
			if "messages/thread" in x["href"]:
				data=self.i.format(x["href"])
		if data !="":
			for x in range(self.lop):
				self.datas.append(data)
			self.msg()
		else:
			print("%s[!]%s cant send message."%(R,N))
				
				
	def msg(self):
		self.mes=raw_input(
			"%s[?]%s Message: "%(G,N)).split(",")
		p=ThreadPool(5)
		p.map(self.send,self.datas)
		exit("\n[*] finished.")
		
	def send(self,k):
		data=[]
		url=bs4.BeautifulSoup(self.req.get(k).text,
			features="html.parser")
		for x in url("form"):
			if "/messages/send/" in x["action"]:
				data.append(self.i.format(x["action"]))
				break
				
		for x in url("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "ids" in x["name"]:
					data.append(x["name"])
					data.append(x["value"])
					if len(data) ==7:
						break
			except:pass
		
		if len(data) ==7:
			f=self.req.post(
			data[0],
				data={
					"fb_dtsg":data[1],
					"jazoest":data[2],
					data[3]:data[4],
					data[5]:data[6],
					"body":random.choice(self.mes),
					"Send":"Kirim"}
			).url
			if "send_success" in f:
				self.suck+=1
				print("%s[%s]%s %s -> SENT!"%(
					G,self.suck,N,url.find("title").text))
			else:
				print("%s[!]%s %s -> NOT SENT."%(
					R,N,url.find("title").text))
		
		
		
# SEND Mass
class massal(object):
	def __init__(self):
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.req = requests.Session()
		self.i="https://mbasic.facebook.com/{}"
		self.suck=0
		self.login()
		
	def login(self):
		s=self.req.post(self.i.format("login"),
			data={
				"email":self.config["email"],
				"pass":self.config["pass"]}
		).url
		if "save-device" in s or "m_sess" in s:
			language.lang(self.req,self.i.format("language.php"))
			self.list()
		else:
			exit("%s[!]%s login failed/checkpoint."%(R,N))
			
	def list(self):
		try:
			self.lis=open(
				raw_input("%s[?]%s List ID: "%(
			G,N))).read().splitlines()
		except Exception as __errors__:
			print("%s[!]%s %s"%(__errors__))
			self.list()
		print("%s[!]%s Total ID: %s"%(R,N,len(self.lis)))
		print("%s[*]%s use coma (,) for random msg"%(R,N))
		self.msg()
	
	def msg(self):
		self.ms=raw_input("%s[?]%s Message: "%(
			G,N)).split(",")
		p=ThreadPool(5)
		p.map(self.cek,self.lis)
	
	def cek(self,list):
		s=self.req.get(self.i.format(list))
		if s.status_code ==200:
			self.check(bs4.BeautifulSoup(s.text,
				features="html.parser"))
				
	def check(self,bs):
		for x in bs.find_all("a",href=True):
			if "messages/thread/" in x["href"]:
				self.open(bs4.BeautifulSoup(
					self.req.get(self.i.format(x["href"])).text,
				features="html.parser"))
				break
	
	def open(self,url):
		data=[]
		for x in url("form"):
			if "/messages/send/" in x["action"]:
				data.append(self.i.format(x["action"]))
				break
				
		for x in url("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "ids" in x["name"]:
					data.append(x["name"])
					data.append(x["value"])
					if len(data) ==7:
						break
			except:pass
		if len(data) ==7:
			f=self.req.post(
			data[0],
				data={
					"fb_dtsg":data[1],
					"jazoest":data[2],
					data[3]:data[4],
					data[5]:data[6],
					"body":random.choice(self.ms),
					"Send":"Kirim"}
			).url
			if "send_success" in f:
				self.suck+=1
				print("%s[%s]%s %s -> SENT!"%(
					G,self.suck,N,url.find("title").text))
			else:
				print("%s[!]%s %s -> NOT SENT."%(
					R,N,url.find("title").text))