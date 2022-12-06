import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'brazil')

def talk(text):
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()


def listen():
    listener = sr.Recognizer()    
    with sr.Microphone() as source:
        talk("estou ouvindo")
        listener.pause_treshold = 0.1              
        listener.adjust_for_ambient_noise(source)              
        pc = listener.listen(source)
        
    try:
        rec = listener.recognize_google(pc, language="pt-br")
        rec = rec.lower()
        print(rec)  # retorno do que foi falado pelo usuario
    except sr.UnknownValueError:     
        print('não entendi, tente novamente')

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return rec