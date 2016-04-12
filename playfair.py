from secret import *
import requests
import time
from splinter import Browser

playfair_url='https://hdfw-tehgame.herokuapp.com/challenge/playfair'
playfair_cracker='http://www.dcode.fr/playfair-cipher'
get_headers = {'authorization': authorization}
post_headers = {'authorization': authorization,'content-type':'application/json'}

def getPlayfair():
		r=requests.get(playfair_url, headers=get_headers)
		if(r.json()["status"]=="success"):
				return r.json()["challenge"]["start"]
		else:
				print(r.json()["error"])
				exit()
				
def solvePlayfair(playfair):
		with Browser('chrome') as b:
				b.visit(playfair_cracker)
				b.find_by_css('#decipher_playfair_ciphertext').fill(playfair)
				b.find_by_css("input[name='grid_alphabet']").type('HACKDFWBEGILMNOPQRSTUVXYZ')
				b.find_by_css("button[post='ciphertext,grid,grid_h,grid_w,shift_same_line,shift_same_column,order_rectangle'").first.click()
				time.sleep(1)
				result=b.find_by_css('.result').text
		return(result)

def formatPlayfair(playfair):
		playfair = playfair.replace("I","J")
		if(len(playfair) > 10):
				playfair = playfair.replace("X","")
		return playfair
		
def postPlayfair(playfair):
		res=requests.post(playfair_url+"/verify",headers=post_headers,data='{"answer":"'+playfair+'"}')
		if("Correct" in res.json()["message"]):
				print("Success! "+playfair)
		else:
				print("ERROR "+playfair)
postPlayfair(formatPlayfair(solvePlayfair(getPlayfair())))