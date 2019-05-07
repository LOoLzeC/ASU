#-*-coding:utf-8-*-
import re
import os
import bs4
import sys
import json
import time
import random
import requests
from data import language
from data.color import *
from multiprocessing.pool import ThreadPool


class reportContent(object):
	def __init__(self):
		self.wal=[]
		self.failed=0
		self.suck=0
		self.ua=random.choice(
			open("raw/header/ua.txt").read().splitlines())
		self.headers={"User-Agent":self.ua}
		self.req=requests.Session()
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.mbasic()
		
	def mbasic(self):
		s=self.req.post(self.i.format("login"),
			data=
				{
					"email":self.config["email"],
					"pass":self.config["pass"]
				}
		).url
		if "save-device" in s or "m_sess" in s:
			language.lang(self.req,
				self.i.format("language.php"))
			self.Dump()
		else:
			exit("%s[!]%s login failed."%(R,N))
		
		
	def Dump(self):
		self.target=raw_input("%s[?]%s Target ID: "%(
			G,N))
		if self.target =="":
			self.Dump()
		z=requests.get(self.i.format(self.target),
			headers={"User-Agent":self.ua})
		if z.status_code ==200:
			p=bs4.BeautifulSoup(
				self.req.get(self.i.format(self.target),
			headers=self.headers).text,
			features="html.parser")
			print("%s[*]%s Target: %s"%(
				G,N,p.find("title").text))
			self.inputs()
		else:
			print("%s[!]%s Unknown target id: %s"%(
				R,N,self.target))
			self.Dump()
			
	def inputs(self):
		try:
			self.num=input(
			"%s[?]%s How many status you want to reports? "%(G,N))
		except Exception as e:
			print("%s[*]%s %s"%(R,N,e))
			self.inputs()
		self.opens(self.i.format("%s?v=timeline"%(
			self.target)))
			
	def opens(self,url):
		bs=bs4.BeautifulSoup(self.req.get(url,
		headers=self.headers).text,
			features="html.parser")
		for x in bs.find_all("a",href=True):
			if "berikan masukan" in x.text.lower():
				if len(self.wal) ==self.num:
					break
				else:
					print("\r* GET: %s Status..."%(
						len(self.wal))),;sys.stdout.flush()
					self.wal.append(self.i.format(x["href"]))
			if "lihat berita lain" in x.text.lower():
				self.opens(self.i.format(x["href"]))
		print 
		if len(self.wal) !=0:
			if len(self.wal) < self.num:
				print("%s[!]%s hanya bisa mengambil %s status"%(R,N,len(self.wal)))
			o=ThreadPool(5)
			o.map(self.cek,self.wal)
			print("\n[*] finished.")
		else:
			print("%s[!]%s no posts."%(R,N))
			
	def cek(self,url):
		data=[]
		bs=bs4.BeautifulSoup(self.req.get(url,
			headers=self.headers).text,
		features="html.parser")
		for x in bs("form"):
			data.append(self.i.format(x["action"]))
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "nudity" in x["value"]:
					data.append(x["value"])
					break
			except:continue
		if len(data) ==4:
			bsd=bs4.BeautifulSoup(
			self.req.post(data[0],
			data={
				"fb_dtsg":data[1],
				"jazoest":data[2],
				"tag":data[3],
				"action":"Kirim"},headers=self.headers).text,
			features="html.parser")
			self.nexts(bsd)
		else:
			self.failed+=1
			
	def nexts(self,parse):
		data=[]
		for x in parse("form"):
			data.append(self.i.format(x["action"]))
		for x in parse("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "nudity_involves_a_child" in x["value"]:
					data.append(x["value"])
			except:pass
		if len(data) ==4:
			bs=self.req.post(
			data[0],
			data=
				{
					"fb_dtsg":data[1],
					"jazoest":data[2],
					"tag":data[3],
					"action":"Kirim"
			},headers=self.headers).text
			if "Anda telah mengirimkan laporan." in bs:
				self.suck+=1
				print(
					"\r%s[*]%s Reporting %s/%s Error: %s"%(
					G,N,self.suck,
				len(self.wal),self.failed)),;sys.stdout.flush()
		else:
			self.failed+=1

