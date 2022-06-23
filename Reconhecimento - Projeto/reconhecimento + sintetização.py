import pyttsx3
import speech_recognition as sr
import os

en = pyttsx3.init()
en.say('Olá, gostaria de ouvir sua música?')
en.setProperty('voice', b'brasil')
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()

recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')

    if resposta=="sim":
        en.say('Ok, executando a música')
        en.setProperty('voice', b'brasil')
        en.setProperty('rate', 140)
        en.setProperty('volume', 1)
        en.runAndWait()

        os.system('musica.mp3')

    elif resposta=="não":
        en.say('ok, solicitação negada')
        en.setProperty('voice', b'brasil')
        en.setProperty('rate', 140)
        en.setProperty('volume', 1)
        en.runAndWait()

    else:
        en.say('Desculpe, não consegui entender a sua solicitação')
        en.setProperty('voice', b'brasil')
        en.setProperty('rate', 140)
        en.setProperty('volume', 1)
        en.runAndWait()
