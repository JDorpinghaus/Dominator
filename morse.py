from secret import *
import requests
import time
import base64
from pydub import AudioSegment
import wave
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
from splinter import Browser

morse_url='https://hdfw-tehgame.herokuapp.com/challenge/morse-mp3'
morse_cracker='http://mattfedder.com/cgi-bin/morse.pl'
get_headers = {'authorization': authorization}
post_headers = {'authorization': authorization,'content-type':'application/json'}
def getMorse():
		r=requests.get(morse_url, headers=get_headers)
		if(r.json()["status"]=="success"):
				return r.json()["challenge"]["start"]
		else:
				print(r.json()["error"])
				exit()
				
def generateMP3(morse):
		with open("morse.mp3", "wb") as f:
				f.write(base64.b64decode(morse))

def convert():
		song=AudioSegment.from_mp3("morse.mp3")
		song.export("morse.wav",format="wav")

def formatAudio(audio):
		single_audio=[]
		pulses=[]
		for x in audio:
				if(abs(x[0])>8000) or (abs(x[0])<50):
						single_audio.append(abs(x[0]))
		plt.plot(single_audio)
		count=0
		c=0
		count2=0
		c2=0
		bc=0
		bcc=0
		for x in single_audio:
				if(x>8000):
						c=0
						bc=0
						count+=1
				elif(count!=0):
						c+=1
						if(c>100):
								pulses.append(count)
								bcc=0
								count=0
				else:
						bc+=1
				if(bc>10000):
						if(bcc==0):
								pulses.append('x')
						bc=0
						bcc+=1
		return pulses[0:(len(pulses)-1)]
morsetext=[]
def formatCode(pulses):
		for i,x in enumerate(pulses):
				if(x!='x'):
						if(x>500):
								morsetext.append('_')
						elif(x<500):
								morsetext.append('.')
				else:
						morsetext.append(" ")
		return morsetext

def solveMorse(morsecode):
		with Browser('chrome') as b:
				b.visit(morse_cracker)
				b.find_by_css("textarea[name='message']").fill(morsecode)
				b.find_by_css("input[value='Translate']").first.click()
				time.sleep(3)
				result=b.find_by_css("textarea[name='message']").text
		return(result)
		
def postMorse(answer):
		res=requests.post(morse_url+"/verify",headers=post_headers,data='{"answer":"'+answer+'"}')
		if("Correct" in res.json()["message"]):
				print("Success! "+answer)
				exit()
		else:
				print("ERROR "+answer)

generateMP3(getMorse())
convert()
input_data = read("morse.wav")
postMorse(solveMorse(''.join(formatCode(formatAudio(input_data[1])))))
