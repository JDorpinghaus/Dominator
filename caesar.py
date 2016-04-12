from secret import *
import requests
from splinter import Browser

caesar_url='https://hdfw-tehgame.herokuapp.com/challenge/caesar'
caesar_cracker='http://www.mygeocachingprofile.com/codebreaker.caesarcipher.aspx'
get_headers = {'authorization': authorization}
post_headers = {'authorization': authorization,'content-type':'application/json'}

def getCaesar():
		r=requests.get(caesar_url, headers=get_headers)
		if(r.json()["status"]=="success"):
				return r.json()["challenge"]["start"]
		else:
				print(r.json()["error"])
				exit()

def getCaesarArray(caesar):
		answers=[]
		answers.append(caesar);
		with Browser('chrome') as b:
				b.visit(caesar_cracker)
				b.find_by_css('#EncryptedText').fill(caesar)
				b.find_by_css('#Key').fill('hackdfw')
				b.find_by_css('#ButtonCodebreak').first.click()
				result=b.find_by_css('#Message').text
				splitted=result.split()
		for x in range(0,26):
				answers.append(splitted[(8*x)-1])
		return answers
		
def postCaesar(array):
		for x in array:
				res=requests.post(caesar_url+"/verify",headers=post_headers,data='{"answer":"'+x+'"}')
				if("Correct" in res.json()["message"]):
						print("Success! "+x)
						exit()
caesar = getCaesar()
solutions=getCaesarArray(caesar)
postCaesar(solutions)