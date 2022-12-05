from PyQt5 import uic
from datetime import datetime, date
from google1 import get_calendar_service
from assistente import *
import time
calendar_service = get_calendar_service()
interface = uic.loadUi("TELA_PRINCIPAL.ui")


def take_event_title():
    try:
        T_evento = "Qual o titulo do evento?"
        talk(T_evento)
        interface.label_2.setText(T_evento)
        interface.label_2.adjustSize()
        listened_title = listen()
    except:
        erro = 'não entendi, tente novamente'
        talk(erro)
        interface.label_2.setText(erro)
        interface.label_2.adjustSize()
        listened_title = take_event_title()
    return listened_title

def take_event_desc():
    try:
        descricao = "Qual a descrição do evento?"
        talk(descricao)
        
        listen_desc = listen()
    except:
        erro = 'não entendi, tente novamente' 
        talk(erro)
        interface.label_2.setText(erro)
        interface.label_2.adjustSize()
        listen_desc = take_event_title()
    return listen_desc

def take_start_date():
    try:
        data = "Qual a data e horário inicial?" 
        talk(data)
        interface.label_2.setText(data)
        interface.label_2.adjustSize()
        listened_date = listen().replace(' as ', ' de ')
        if '2000' in listened_date:
            listened_date = listened_date.replace('2000 22', '2022')
        listened_date = listened_date.split(' de ')
        new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
            + ' ' + listened_date[3]
        date_isoformat = datetime.fromisoformat(new_date).isoformat()
    except:
        erro = 'não entendi, tente novamente' 
        talk(erro)
        interface.label_2.setText(erro)
        interface.label_2.adjustSize()
        date_isoformat = take_start_date()
    return date_isoformat

def take_end_date():
    try:
        data = "Qual a data e horário final?"  
        talk(data)
        interface.label_2.setText(data)
        interface.label_2.adjustSize()
        listened_date = listen().replace(' às ', ' de ')
        if '2000' in listened_date:
            listened_date = listened_date.replace('2000 22', '2022')
        listened_date = listened_date.split(' de ')
        new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
            + ' ' + listened_date[3]

        date_isoformat = datetime.fromisoformat(new_date).isoformat()
    except:
        erro = 'não entendi, tente novamente' 
        talk(erro)
        interface.label_2.setText(erro)
        interface.label_2.adjustSize()
        date_isoformat = take_end_date()
    return date_isoformat


def create_event():
    event_title = take_event_title()
    time.sleep(0.5)
    event_desc = take_event_desc()
    time.sleep(0.5)
    start_date = take_start_date()
    time.sleep(0.5)
    end_date = take_end_date()
    time.sleep(0.5)
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Sao_Paulo'},
            "end": {"dateTime": end_date, "timeZone": 'America/Sao_Paulo'},
        }
    ).execute()

    evento = "Seu evento foi criado com sucesso!" 
    talk(evento)
    interface.label_2.setText(evento)
    interface.label_2.adjustSize()
    

'''
def create_manual():
  
    event_title = textbox1.Text()
    event_desc = textbox2.Text()
    start_date =  convertDatetime(textbox3.Text())
    end_date =  convertDatetime(textbox4.Text())

    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Sao_Paulo'},
            "end": {"dateTime": end_date, "timeZone": 'America/Sao_Paulo'},
        }
    ).execute()
'''


def convertDatetime(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def menu():
    pass


"""if __name__ == '__main__':
    create_event()"""