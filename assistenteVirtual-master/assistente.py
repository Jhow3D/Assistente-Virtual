from PyQt5 import uic,QtWidgets
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'brazil')


interface = uic.loadUi("TELA_PRINCIPAL.ui")

def talk(text):
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()


def listen():
    listener = sr.Recognizer()    
    with sr.Microphone() as source:
        ouvindo = "estou ouvindo" 
        talk(ouvindo)
        interface.label_2.setText(ouvindo)
        interface.label_2.adjustSize()
        listener.pause_treshold = 0.1              
        listener.adjust_for_ambient_noise(source)              
        pc = listener.listen(source)
        
    try:
        rec = listener.recognize_google(pc, language="pt-br")
        rec = rec.lower()
        interface.label_3.setText(rec)  # retorno do que foi falado pelo usuario
        interface.label_3.adjustSize()
    except sr.UnknownValueError:
        erro = 'não entendi, tente novamente' 
        interface.label_3.setText(erro)
        interface.label_3.adjustSize()

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return rec