from gtts import gTTS
import os

text =open("demo.txt","r",encoding="utf-8").read()
language="hi"
output =gTTS(text,lang=language,slow=False)
output.save('fileoutput.mp3')
os.system('start fileoutput.mp3')