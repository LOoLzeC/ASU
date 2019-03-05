import threading
import mechanize
import bs4,re,sys,time
import os
import requests
from data.color import *
from data import cache
from data import multiBruteforce
import subprocess as kontolatos

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
			print "[%s*%s] Output: out/aidi.txt"%(G,N)
		self.memex=[]
		open("out/aidi.txt","w").close()
		while True:
			k=bs4.BeautifulSoup(
				self.br.response().read(),
			features="html.parser")
			for x in k.find_all("a",href=True):
				if "fref" in x["href"]:
					try:
						name=re.findall("/(.*?)\?fref",
							"%s"%(
								x["href"]))[0]
						if name in open("out/aidi.txt").read():
							pass
						else:
							self.memex.append(name)
						if name in open("out/aidi.txt").read():
							pass
						else:
							open("out/aidi.txt","a").write(name+"\n")
						print("\r[%s*%s] GET: %s ID press ctrl+z if the number not running"%(
							G,N,len(self.memex))
								),;sys.stdout.flush()
						if (len(self.memex) == self.xox):
							kontolatos.Popen(
								["killall", "python2"],
							stderr=kontolatos.PIPE,
							stdin=kontolatos.PIPE,
							stdout=kontolatos.PIPE)
					except:pass
					try:
						profile=re.findall("php\?id=(.*?)&",
							"%s"%(x["href"]))[0]
						if profile in open("out/aidi.txt").read():
							pass
						else:
							self.memex.append(profile)
						if profile in open("out/aidi.txt").read():
							pass
						else:
							open("out/aidi.txt","a").write(profile+"\n")
						if (len(self.memex) == self.xox):
							kontolatos.Popen(
								["killall", "python2"],
							stderr=kontolatos.PIPE,
							stdin=kontolatos.PIPE,
							stdout=kontolatos.PIPE)
					except:pass
				if "/friends?unit_cursor" in x["href"]:
					self.kontl=x["href"]
					self.br.open(self.url.format(x["href"]))
					
class me:
	def __init__(self):
		self.q=[]
		self.login()
	def login(self):
		email=raw_input("\n[%s*%s] Login Your Facebook ^^ \n[%s*%s] Email: "%(C,N,G,N))
		pw=raw_input("[%s*%s] Passs: "%(G,N))
		self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(email,pw)).json()
		try:
			self.r["access_token"]
			print("[%s*%s] Login Success.."%(G,N))
			print("[%s*%s] Dumping  id ..."%(G,N))
			self.dumps()
		except:sys.exit("%s[!]%s Login Failed."%(R,N))
		
	def dumps(self):
		j=requests.get("https://graph.facebook.com/me/friends?access_token=%s"%(self.r["access_token"])).json()
		for x in j["data"]:
			ids=x["id"]
			self.q.append(ids)
			print("\r[%s*%s] Writing %s id ..."%(G,N,len(self.q))),;sys.stdout.flush();time.sleep(000.001)
		o=open("out/myfriends.txt","w")
		for x in self.q:
			o.write(x+"\n")
		o.close()
		print("\n[%s*%s] %s id writted."%(G,N,len(self.q)))
		print("[%s*%s] Output: out/myfriends.txt"%(G,N))



class getmember:
	def __init__(self):
		self.req=requests.Session()
		self.i="https://mbasic.facebook.com/{}"
		self.gen()
	def gen(self):
		bs=bs4.BeautifulSoup(
			self.req.get(self.i.format("login")).text,
		features="html.parser")
		for x in bs("input"):
			if "login" in x["name"]:
				self.submit=x["value"]
		self.imel=raw_input("[%s*%s] Email: "%(G,N))
		self.pas=raw_input("[%s*%s] Passs: "%(G,N))
		bz=self.req.post(self.i.format("login"),data=
				{
					"email":self.imel,
					"pass":self.pas,
					"login":self.submit
				}
		).url
		if "save-device" in bz or "m_sess" in bz:
			print "[%s*%s] Login Success.."%(G,N)
			self.search()
		else:sys.exit("%s[!]%s login failed."%(R,N))
	
	def search(self):
		self.xx=0
		self.xo=[]
		self.q=raw_input("[%s*%s] Search Group Query: "%(G,N))
		print "[%s*%s] Searching qery ..."%(R,N)
		bz=bs4.BeautifulSoup(
			self.req.get(self.i.format(
				"groups/?seemore")).text,
		features="html.parser")
		for x in bz.find_all("a",href=True):
			if len(re.findall("/groups/",x["href"])) !=0:
				s=x.renderContents()
				if self.q in s:
					p=re.findall("/groups/(.*?)\?",x["href"])
					if len(p) !=0:
						self.xx+=1
						print "%s[%s]%s %s.."%(
							G,self.xx,N,s[0:40])
						self.xo.append(p[0])
		if len(self.xo) !=0:
			self.tusuk()
		else:
			print "%s[!]%s no result query: %s"%(R,N,self.q)
		
	def tusuk(self):
		try:
			s=input("\n%s[%s+%s]%s Select>> "%(G,R,G,N))
			s=s-1
			self.searc(self.xo[s])
		except Exception as f:
			print "%s[!]%s %s"%(R,N,f)
			return self.tusuk()
			
	def searc(self,q):
		self.ngewe(q)
		
	def ngewe(self,id):
		s=bs4.BeautifulSoup(
		self.req.get(self.i.format(
			"browse/group/members/?id=%s"%(id))).text,
		features="html.parser")
		for x in s.find_all("h3"):
			if "(" in x.renderContents():
				print "[%s*%s] %s %s"%(
					G,N,s.find("title").renderContents(),
						x.renderContents())
		self.ser(id)
		
	def ser(self,id):
		m=mechanize.Browser()
		m.set_handle_equiv(True)
		m.set_handle_redirect(True)
		m.set_handle_robots(False)
		m.open(self.i.format("login"))
		m._factory.is_html=True
		m.select_form(nr=0)
		m.form["email"]="%s"%(self.imel)
		m.form["pass"]="%s"%(self.pas)
		m.submit()
		s=m.open(self.i.format("browse/group/members/?id=%s"%(id)))
		print "[%s*%s] Press ctrl+c to stop."%(G,N)
		try:
			self.k(m)
		except Exception as f:
			print f
			exit("stopped.")
		
	def k(self,m):
		open("out/grup.txt","w").close()
		while True:
			self.s=m.response().read()
			for x in re.findall('member_(.*?)"',self.s):
				if "list" in x:pass
				else:
					open("out/grup.txt","a").write(x+"\n")
					s=open("out/grup.txt").readlines()
					print("\r[%s*%s] writing %s id "%(G,N,len(s))),;sys.stdout.flush()
			o=bs4.BeautifulSoup(self.s,
			features="html.parser")
			self.omg=""
			for x in o.find_all("a",href=True):
				if "browse/group/members/" in x["href"]:
					self.omg=x["href"]
			if self.omg !="":
				m.open(self.omg)
			else:exit("\n[%s*%s] %s Limit reached:("%(R,N,len(s)))
			

class searchname:
	def __init__(self):
		self.login()
		
	def login(self):
		self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(raw_input("\n[%s*%s] Login Your Facebook ^^\n[%s*%s] Email: "%(C,N,G,N)),raw_input("[%s*%s] Passs: "%(G,N)))).json()
		try:
			self.token=self.r["access_token"]
			print("[%s*%s] Login Success."%(G,N))
			print("[%s*%s] Getting Friends ..."%(G,N))
			self.q()
		except:exit("%s[!]%s login failed."%(R,N))
		
	def q(self):
		self.query=raw_input("[%s*%s] Query: "%(G,N))
		if self.query == "":
			return self.q()
		self.lot()
	def lot(self):
		found=[]
		k=requests.get("https://graph.facebook.com/me/friends?access_token=%s"%(self.token)).json()
		for x in k["data"]:
			if self.query in x["name"].lower():
				found.append(x["id"])
				print("%s[%s] %s %s"%(G,len(found),N,x["name"]))
		
		if len(found) !=0:
			print("\n[%sFound%s]: %s"%(G,N,len(found)))
			r=raw_input("[%s?%s] Write? y/n: "%(R,N))
			if r.lower() !="y":
				return self.query()
			else:
				n=raw_input("[%s?%s] File name: "%(R,N))
				for x in found:
					open("out/"+n,"a+").write(x+"\n")
				print("[%s*%s] Output: out/%s"%(G,N,n))
				
class search_people:
	def __init__(self):
		self.req=requests.Session()
		self.i="https://mbasic.facebook.com/{}"
		self.login()
		
	def login(self):
		s=bs4.BeautifulSoup(
			self.req.get(self.i.format("login")).text,
		features="html.parser")
		for x in s("input"):
			if "login" in x["name"]:
				self.sub=x["value"]
		print("[%s*%s] Login your facebook ^^"%(C,N))
		l=self.req.post(self.i.format("login"),data=
			{
				"email":raw_input("[%s*%s] Email: "%(G,N)),
				"pass":raw_input("[%s*%s] Passs: "%(G,N)),
				"login":self.sub
			}
		).url
		if "save-device" in l or "m_sess" in l:
			print("[%s*%s] Login Success..."%(G,N))
			self.search()
		else:exit("%s[!]%s Login Failed"%(R,N))
		
	def search(self):
		q=raw_input("%s[?]%s Search Query: "%(G,N))
		if q == "":
			return self.search()
		if os.path.exists("out/search.txt"):
			if os.path.getsize("out/search.txt") !=0:
				print "[%s*%s] File Exists: out/search.txt"%(R,N)
				o=raw_input("[%s?%s] Append id? y/n?): "%(R,N))
				if o.lower() !="y":
					print "%s[*]%s output: out/search.txt"%(G,N)
					open("out/search.txt","w").close()
				self.recon(q)
			print "%s[*]%s output: out/search.txt"%(G,N)
			self.recon(q)
		else:
			print "%s[*]%s output: out/search.txt"%(G,N)
			open("out/search.txt","w").close()
			self.recon(q)
		
	def recon(self,query):
		self.memek=bs4.BeautifulSoup(
			self.req.get(
				self.i.format("search/top/?q=%s"%(
					query))).text,
		features="html.parser")
		for x in self.memek.find_all("a",href=True):
			if "graphsearch" in x["href"]:
				self.gelud(self.i.format(x["href"]))
				break
	
	def gelud(self,url):
		self.m=bs4.BeautifulSoup(
			self.req.get(url).text,features="html.parser")
		while True:
			for x in self.m.find_all("div",class_="ce"):
				print "\r[%s*%s] %s"%(G,N,x.renderContents())
			for x in self.m.find_all("a",href=True):
				k=re.findall('href="/(.*?)"',"%s"%(x))
				if len(k) !=0:
					if "_" in k[0] or "&" in k[0] or "messages" in k[0]:
						pass
					else:
						ii=k[0]
						if "profile.php" in ii:
							ss=re.findall("profile.php\?id=(.*?)$",ii)
							if len(ss) !=0:
								if ss[0] in open("out/search.txt").read():
									pass
								else:
									open("out/search.txt","a").write(ss[0]+"\n")
						else:
							if ii in open("out/search.txt").read():
								pass
							else:open("out/search.txt","a").write(ii+"\n")
			
			for i in self.m.find_all("a",href=True):
				if "pivot&cursor" in i["href"]:
					self.biji=i["href"]
					if self.biji !="":
						for x in ["|","/","-","\\"]:
							print "\r[%s%s%s] Writing .. %s"%(
							R,len(open("out/search.txt").readlines()),N,x),;sys.stdout.flush();time.sleep(0.1)
						self.m=bs4.BeautifulSoup(
							self.req.get(i["href"]).text,
						features="html.parser")
					else:
						sys.exit("\n[%s*%s] finished"%(G,N))
				
class pilihan():
	def __init__(self):
		print "\n\t[ Select Actions ]\n"
		print "{%s01%s} Dump ID from your friends"%(G,N)
		print "{%s02%s} Robber ID from targets friend"%(G,N)
		print "{%s03%s} JUMPING"%(G,N)
		print "{%s04%s} Dump ID From GROUP"%(G,N)
		print "{%s05%s} Dump ID From Friends Search Name Query"%(G,N)
		print "{%s06%s} Dump ID by explore search name query"%(G,N)
		print "{%s07%s} Start Multi BruteForce"%(G,N)
		print "{%s08%s} Start MultiBruteForce v.2\n"%(G,N)
		f=raw_input("%s[%s+%s]%s Actions>> "%(G,R,G,N))
		if f == "1" or f == "01":
			self.a()
		elif f == "2" or f == "02":
			self.b()
		elif f == "3" or f == "03":
			self.c()
		elif f == "4" or f == "04":
			self.newmodule()
		elif f == "5" or f == "05":
			self.newmodule1()
		elif f == "6" or f == "06":
			self.serpipel()
		elif f == "7" or f == "07":
			self.d()
		elif f == "8" or f == "08":
			multiBruteforce.prepare()
		else:sys.exit("%s[!]%s Invalid options!"%(R,N))
		
	def serpipel(self):
		search_people()
		
	def a(self):
		me()
		
	def b(self):
		rs=raw_input("[%s+%s] Target friends ID: "%(G,N))
		if rs == "":
			return self.b()
		dumpper(rs)
	
	def c(self):
		jamping()
		
	def d(self):
		multiBruteforce._prepares()
		
	def newmodule(self):
		print("\n\t [ Select Actions ]\n")
		print("{%s01%s} Dump id from group\n"%(G,N))
		c=raw_input("%s[%s+%s]%s Actions>> "%(G,R,G,N))
		if (c == "1" or c == "01"):
			getmember()
		else:exit("%s[!]%s invalid option"%(R,N))
		
	def newmodule1(self):
		searchname()
