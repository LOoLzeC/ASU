import requests
def token(akun):
	try:
		s=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(akun.split("|")[-0],akun.split("|")[-1]))
		if "Account Temporarily Unavailable" in s.text:
			return "checkpoint"
		else:return s.json()["access_token"]
	except:
		return False
