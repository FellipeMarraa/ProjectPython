import speech_recognition as sr
import webbrowser
import pyttsx3

en = pyttsx3.init()
en.say('DESEJA FINALIZAR A APRESENTAÇÃO?')
en.setProperty('voice', b'brasil')
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()

recon = sr.Recognizer()

with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')

if resposta =="sim":
    print('FINALIZANDO...')
    webbrowser.open(r'https://1drv.ms/u/s!Ap5Wbk-5j8Yj2xk4zxUuH3eIn4CZ?e=VGilMx')
elif resposta =="não":
    print('SOLICITAÇÃO NEGADA!')