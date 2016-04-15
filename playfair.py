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
		playfairarray=[]
		playfairitems=list(playfair)
		playfairarray.append(playfair)
		c=playfair.count("I")
		d=playfair.count("X")
		if(c==1):
				j_playfair=playfair.replace("I","J")
				playfairarray.append(j_playfair)
		elif(c==2):
				j_playfair=playfair.replace("I","J")
				playfairarray.append(j_playfair)
				for i,x in enumerate(playfairitems):
						newplayfairitems=playfairitems
						if(x=="I"):
								newplayfairitems[i]="J"
								playfairarray.append("".join(newplayfairitems))
		for i,x in enumerate(playfairarray):
				playfairarray[i]=removeX(playfairarray[i])
		return playfairarray
		
def postPlayfair(playfair):
		for x in playfair:
				res=requests.post(playfair_url+"/verify",headers=post_headers,data='{"answer":"'+x+'"}')
				if("Correct" in res.json()["message"]):
						print("Success! "+x)
						exit()
				else:
						print("ERROR "+x)
						
def combNum(num,group):
		return(factorial(group)/(factorial(num)*factorial(group-num)))
		
def removeX(playfair):
		newplayfair=list(playfair)
		for i, x in enumerate(newplayfair):
				if (x=='X'):
						if(i!=0):
								if(i!=len(newplayfair)-1):
										if(newplayfair[i-1]==newplayfair[i+1]):
												newplayfair[i]=""
								else:
										newplayfair[i]=""
		s="".join(newplayfair)
		return s

postPlayfair(formatPlayfair(solvePlayfair(getPlayfair())))