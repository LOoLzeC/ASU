import requests,json
import bs4,re,sys,getpass
from data.color import *
from data import cache
cache.cleanCache()

#2309895739255921

class grup:
	def __init__(self):
		self.i="https://mbasic.facebook.com/{}"
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.req=requests.Session()
		self.login()
		
	def login(self):
		a=bs4.BeautifulSoup(
			self.req.get(self.i.format("login")).text,
		features="html.parser")
		for x in a("input"):
			if "login" in x["name"]:
				self.subp=x["value"]
		s=self.req.post(self.i.format("login"),data=
			{
				"email":self.config["email"],
				"pass":self.config["pass"],
				"login":self.subp
			}).url
		if "save-device" in s or "m_sess" in s:
			print("[%s*%s] Login sukses."%(G,N))
			self.getfr()
		else:exit("%s[!]%s login failed."%(R,N))
	
	def getfr(self):
		print "[%s+%s] Mengambil teman ..."%(G,N)
		bs=bs4.BeautifulSoup(
			self.req.get(self.i.format("profile.php")).text,
		features="html.parser")
		for x in bs.find_all("a",href=True):
			if "/friends?lst=" in x["href"]:
				self.todo=x["href"]
				bz=bs4.BeautifulSoup(
					self.req.get(self.i.format(x["href"])).text,
				features="html.parser")
				for i in bz.find_all("h3"):
					self.many=i.renderContents()
					print "[%s*%s] %s"%(
					R,N,self.many)
					self.inputs()
					
	def inputs(self):
		print "%s[!]%s MAX: %s"%(R,N,
		re.findall("\((.*?)\)",
			self.many)[0].replace(".",""))
		self.man=input(
			"[%s?%s] how many friends u wanna add?: "%(
				G,N))
		if self.man == "":
			return self.inputs()
		self.getname(self.i.format(self.todo))
		
	def getname(self,url):
		self.cariteman=bs4.BeautifulSoup(
				self.req.get(url).text,
			features="html.parser")
		self.memec=[]
		while True:
			for i in self.cariteman.find_all("a",href=True):
				if "fref" in i["href"]:
					for z in re.findall('fref=fr_tab">(.*?)</a>',"%s"%(i)):
						self.memec.append(z)
						if len(self.memec) == self.man:
							self.grupid()
							exit()
						else:
							print "\r[%s+%s] GET %s/%s name"%(
							G,N,len(self.memec),
								self.man),;sys.stdout.flush()
			for x in self.cariteman.find_all("a",href=True):
				if "/friends?unit_cursor" in x["href"]:
					self.cariteman=bs4.BeautifulSoup(
						self.req.get(self.i.format(x["href"])).text,
					features="html.parser")
					
	def grupid(self):
		self.gid=raw_input("\n[%s#%s] Your group id: "%(
			G,N))
		if self.gid == "":
			return self.grupid()
		self.getid()
		
	def getid(self):
		namagrup=bs4.BeautifulSoup(
			self.req.get(self.i.format(
				"groups/members/search/?group_id=%s"%(
					self.gid))).text,
		features="html.parser")
		pq=[]
		for x in namagrup("input"):
			try:
				if "group_name" in x["name"]:
					pq.append(x["value"])
					break
			except:pass
		if len(pq) == 0:
			exit("%s[!]%s You must be an admin to add members"%(R,N))
		if len(pq) !=1:
			exit("%s[!]%s lu bukan admin ya?"%(R,N))
		else:
			print "-"*40
			print "[%s+%s] adding %s friends to group %s\n"%(
			G,N,self.man,pq[0])
		for self.x in self.memec:
			b=bs4.BeautifulSoup(
				self.req.get(self.i.format(
				"groups/members/search/?group_id=%s"%(
				self.gid))).text,
			features="html.parser")
			for fo in b("form"):
				if "members/search" in fo["action"]:
					self.actions=fo["action"]
			for k in b("input"):
				try:
					if "fb_dtsg" in k["name"]:
						self.dtsg=k["value"]
					if "jazoest" in k["name"]:
						self.jzst=k["value"]
					if "group_name" in k["name"]:
						self.gname=k["value"]
					if "group_id" in k["name"]:
						self.val=k["value"]
					if "submit" in k["type"]:
						self.sub=k["value"]

				except:pass
			bsz=bs4.BeautifulSoup(
			self.req.post(
				self.i.format(self.actions),data=
					{
						"fb_dtsg":self.dtsg,
						"jazoest":self.jzst,
						"group_name":self.gname,
						"group_id":self.val,
						"query_term":self.x,
						"submit":self.sub
					}
				).text,
			features="html.parser")
			for x in bsz("input"):
				try:
					if "fb_dtsg" in x["name"]:
						self.a=x["value"]
					if "jazoest" in x["name"]:
						self.b=x["value"]
					if "group_name" in x["name"]:
						self.c=x["value"]
					if "group_id" in x["name"]:
						self.d=x["value"]
					if "add" in x["name"]:
						self.ok=x["value"]
				except:pass
			for d in bsz("input"):
				try:
					if "addees" in d["name"]:
						self.ades=d["name"]
						self.valuades=d["value"]
						break
				except:pass
			for xx in bsz("form"):
				if "members/search" in xx["action"]:
					self.act=xx["action"]
			reqs= self.req.post(
				self.i.format(self.act),data=
					{
						"fb_dtsg":self.a,
						"jazoest":self.b,
						"group_name":self.c,
						"group_id":self.d,
						self.ades:self.valuades,
						"add":self.ok
					}).url
			try:
				cek=re.findall("added_status=(.*?)&",
					reqs)[0]
				if len(cek) ==1:
					print "[%s*%s] %s added."%(G,N,self.x)
				else:
					print "[%s*%s] %s %sAlready Added.%s"%(G,N,self.x,R,N)
			except:pass
			
