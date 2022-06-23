import speech_recognition as sr
import webbrowser

print('OLÁ, DESEJA FINALIZAR A APRESENTAÇÃO?')

recon = sr.Recognizer()

with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')

if resposta =="sim":
    print('FINALIZANDO...')
    webbrowser.open(r'https://1drv.ms/u/s!Ap5Wbk-5j8Yj2xk4zxUuH3eIn4CZ?e=VGilMx')
elif resposta =="não":
    print('SOLICITAÇÃO NEGADA!')