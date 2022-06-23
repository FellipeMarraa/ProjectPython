import pyttsx3
import speech_recognition as sr
import webbrowser

en = pyttsx3.init()
en.say('Olá, o que deseja neste momento?')
en.setProperty('voice', b'brasil')
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()

recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')

if resposta=="quero acessar o Google":
    en.say('Ok, abrindo o google')
    en.setProperty('voice', b'brasil')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()
    webbrowser.open('https://www.google.com')

elif resposta=="Qual a temperatura de hoje":
    en.say('Esta é a temperatura')
    en.setProperty('voice', b'brasil')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()
    webbrowser.open('https://www.google.com/search?client=opera-gx&q=temperatura+hoje&sourceid=opera&ie=UTF-8&oe=UTF-8')

elif resposta=="quero Abrir o YouTube":
    en.say('Ok, abrindo o youtube')
    en.setProperty('voice', b'brasil')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()
    webbrowser.open('https://www.youtube.com')

else:
    en.say('Desculpe, não consegui entender a sua solicitação')
    en.setProperty('voice', b'brasil')
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()