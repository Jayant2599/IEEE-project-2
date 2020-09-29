import pyttsx3   
import os
import webbrowser
import speech_rerocognition as sr 
pyttsx3.speak("I WELCOME YOU TO MY SERVICE")
print ("I WELCOME U TO MY SERVICE".end='"')   
pyttsx3.speak ("KINDLY ENTER YOUR REQUIREMENTS")
print ("KINDLY ENTER YOUR REQUIREMENTS", end='') 

r=sr.Recognizer() 
with sr.Microphone() as source: 
 print('start syaing..') 
 audio =r.listen(source)
 print('we got it' 
ch=r.recognize_google(audio) 
if("calander" in ch) and (("run" in ch)or("open" in ch)):
   webbrowser .open("http://192.168.29.152/cgi-bin/div.py?x=cal")   
elif("date" in ch) and (("run" in ch) or ("open" in ch)):
   wbebrowser .open("http://192.168.29.152/cgi-bin/div.py?x=date")   
elif("ip address" in ch) and (("show" in ch) or ("execute" in ch)):
   webbrowser .open("http://192.168.29.152/cgi-bin/div.py?x=ifconfig")
elif("directory" in ch) and (("open" in ch) or("show" in ch)):
   webbrowser .open("http:/192.168.29.152/cgi-bin/div.py?x=pwd") 
elif("file" in ch) and (("open" in ch) or (" how" in ch )): 
   webbrowser .open("http://192.168.29.152/cgi-bin/div.py?x=1s") 
elif("terminate" in ch) or ("close" in ch):  
   break
else: 
   pyttsx3.speak("I CANNOT UDERSTAND WHAT YOU SAID") 
   print ("I CANNOT UNDERSTAND WHAT YOU SAID" 
   pyttsx3.speal("THANX FOR VISITING")
   print ("THANX FOR VISITING")