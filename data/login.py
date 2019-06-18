import requests

def log(session,account):
	return session.post("https://mbasic.facebook.com/login",
		data=
			{
				"email":account.split("|")[-0],
				"pass":account.split("|")[-1]
			}
	).url