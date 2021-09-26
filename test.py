import audioop
from typing import _SpecialForm, Mapping
from wave import Error
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import mysql.connector,Error

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
    )
myc = mydb.cursor()


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

user_info = ["first name","last name","email","gender","account_number","account_type","on hold","balance deposit"]
info = []

def create_note():
    global recognizer
    speaker.say("Enter the user info")

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.4)
                for item in user_info:
                    speaker.say(item)
                    
                    recognizer.adjust_for_ambient_noise(mic, duration=0.4)
                    audio = recognizer.listen(mic)
                    
                    details = recognizer.recognize_google(audio)
                    details = details.lower()
                    
                    info.append(details)
                    speaker.runAndWait()


           
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you ! please try again")
            speaker.runAndWait()
        try:
            sql = "INSERT INTO BANK (first_name,last_name,email,gender,account_number,account_type,on_hold,balance) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
            val = (info)
            myc.execute(sql, val)
            done = True
            speaker.say(f"I successfully create the Account with details {info}")
            speaker.runAndWait()
        except Error as error:
            speaker.say("Error")


# def add_todo():
    
#     global recognizer
#     speaker.say("what todo do ypu want to add")
#     speaker.runAndWait()

#     done = False
#     while not done:
#         try:
#             with speech_recognition.Microphone() as mic:
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.4)
#                 audio = recognizer.listen(mic)

#                 item = recognizer.recognize_google(audio)
#                 item = item.lower()

#                 todo_list.append(item)
#                 done = True
#                 speaker.say(f"I added {item} to the list!")
#                 speaker.runAndWait()
                
#         except speech_recognition.UnknownValueError:
#             recognizer = speech_recognition.Recognizer()
#             speaker.say("I did not understand you ! please try again")
#             speaker.runAndWait()


# def show_todos():

#     speaker.say("the items on your to do list are the following")
#     for item in todo_list:
#         speaker.say(item)
#     speaker.runAndWait()


def hello():
    speaker.say("hellow . what can i do for you")
    speaker.runAndWait()


def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_user": create_user,
#     "add_todo": add_todo,
#     "show_todos": show_todos,
    "exit": quit,
}
assistant = GenericAssistant(
    'intents.json', intent_methods=mappings) #, model_name="test_model")

assistant.train_model()
# assistant.save_model()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.4)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
