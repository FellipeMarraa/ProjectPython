import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Descreva a sua multiplicação')
        audio = recon.listen(source)

        txsoma = recon.recognize_google(audio, language='pt')
        if txsoma =="fechar": break

        print('Sua multiplicação : ' + str(txsoma))
        print('Resultado: ' + str(int(txsoma[0]) * int(txsoma[4])))