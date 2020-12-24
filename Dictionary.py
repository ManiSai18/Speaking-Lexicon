import json
import speech_recognition as sr
import pyttsx3
from difflib import get_close_matches

data = json.load(open("data  .json"))
g = "Hello, Welcome To MSP Dictionary"
print(g)


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def translate(w):
    print(w)
    SpeakText(w)
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":

            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


SpeakText(g)
while True:
    r = sr.Recognizer()
    a = "Spell dictionary to know the meanings or definitions of required words"
    c = "Spell exit To exit from dictionary"

    print("Spell \n"
          "'Dictionary'-Meaning Of a Word\n"
          "'exit'-Exit from Dictionary\n")
    SpeakText(a)
    SpeakText(c)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        ch = r.recognize_google(audio)
        ch = ch.lower()
    if ch == "dictionary":

        try:
            r = sr.Recognizer()
            with sr.Microphone() as source2:
                s = "Speak The Word For The Meaning"
                print("Speak The Word For The Meaning")
                SpeakText(s)
                r.adjust_for_ambient_noise(source2)
                audio2 = r.listen(source2)
                print("Processing...")
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                output = translate(MyText)
                if type(output) == list:
                    for item in output:
                        print(item)
                        SpeakText(item)
                else:
                    print(output)
                    SpeakText(output)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
    elif ch == "exit":
        def SpeakText(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()


        t = "Hope You got to know the meanings of some Words ThankYou See You NextTime"

        print("Hope You got to know the meanings of some Words\n"
              "ThankYou!\n"
              "See You NextTime!!")
        SpeakText(t)
        break
    else:
        print("Invalid Input")
