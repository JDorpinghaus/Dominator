from secret import *
import requests
from splinter import Browser

vigenere_url='https://hdfw-tehgame.herokuapp.com/challenge/vigenere'
vigenere_cracker='http://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx'
capped_Vigenere = ''
get_headers = {'authorization': authorization}
post_headers = {'authorization': authorization,'content-type':'application/json'}

def getVigenere():
		r=requests.get(vigenere_url, headers=get_headers)
		if(r.json()["status"]=="success"):
				return r.json()["challenge"]["start"]
		else:
				print(r.json()["error"])
				exit()
		
def solveVigenere():
		with Browser('chrome') as b:
				b.visit(vigenere_cracker)
				b.find_by_css('#EncryptedText').fill(vigenere)
				b.find_by_css('#Key').fill('hackdfw')
				b.find_by_css('#ButtonCodebreak').first.click()
				result=b.find_by_css('#Message').text
		return(result[49:59].strip())

vigenere=getVigenere()
print(vigenere)
solved_Vigenere=solveVigenere()
for x in range(0,10):
		if (vigenere[x].isupper()):
				capped_Vigenere += solved_Vigenere[x].upper()
		else:
				capped_Vigenere += solved_Vigenere[x]
print(capped_Vigenere)
res=requests.post(vigenere_url+"/verify",headers=post_headers,data='{"answer":"'+capped_Vigenere+'"}')
if("Correct" in res.json()["message"]):
		print("Success!")
else:
		print("Incorrect answer.")