import bs4
import requests
import mechanize

def lang(cookies,url):
	s=bs4.BeautifulSoup(
		cookies.get(url).text,features="html.parser")
	for x in s.find_all("a",href=True):
		if "id_ID&" in x["href"]:
			cookies.get(
				"https://mbasic.facebook.com/"+x["href"]
			).text			
			
def mec(cookies,url):
	cookies.open(url)
	cookies._factory.is_html=True
	c=cookies.find_link(url_regex="id_ID&").url
	cookies.open("https://mbasic.facebook.com/"+c)
	cookies._factory.is_html=True


#language.lang(self.req,
				#"https://mbasic.facebook.com/language.php")
#language.mec(s,"https://mbasic.facebook.com/language.php")