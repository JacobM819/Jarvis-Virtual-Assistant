import speech_recognition as sr
import pyttsx3
import webbrowser
import lists
import sys
engine = pyttsx3.init()
engine.runAndWait()
# log_file = open("log.txt", "r+")

useVoice = False

standBy = False

# recognize speech using Google Speech Recognition
user_input = ""
input_list = []
command = ""
def firstPresident():
    engine.say("The first president is George Washington sir.")
    engine.runAndWait()
    return print("The first president is George Washington sir."), read_input("What is it sir?:", "list")

def repeat():
    if useVoice == True:
        phrase = read_input("What do you want me to say?: ", "text_end")
    else:
        phrase = input("What do you want me to say?: ")
    # VOICE read_input("What do you want me to say?: ", "text_end")
    # TEXT input("What do you want me to say?: ")
    engine.say(phrase)
    engine.runAndWait()
    return print(phrase), read_input("What is it sir?:", "list")

def newTab():
    webbrowser.open("https://google.com")
    engine.say("I will open a new tab in google sir.")
    engine.runAndWait()
    return print("I will open a new tab in google sir."), read_input("What is it sir?:", "list")

def stop():
    engine.say("Ok, goodbye.")
    engine.runAndWait()
    print("Ok, goodbye.")
    sys.exit()

def calculate():
    try:
        global user_input
        if "plus" in user_input or "+" in user_input:
            answer = float(input_list[3]) + float(input_list[5])
            answer = "%.4f" % answer
            opWord = " plus "
            op = " + "
        if "minus" in user_input or "-" in user_input:
            answer = float(input_list[3]) - float(input_list[5])
            opWord = " minus "
            op = " - "
        if "times" in user_input or "*" in user_input:
            answer = float(input_list[3]) * float(input_list[5])
            opWord = " times "
            op = " * "
        if "divided by" in user_input or "/" in user_input:
            answer = float(input_list[3]) / float(input_list[5])
            opWord = " divided by "
            op = " / "
        if "to the power of" in user_input or "^" in user_input:
            answer = int(input_list[3]) ^ int(input_list[5])
            opWord = " to the power of "
            op = " ^ "
        answer = str(answer)
        engine.say(input_list[3] + opWord + input_list[5] + " is equal to " + answer)
        engine.runAndWait()
        print(input_list[3] + op + input_list[5] + " = " + answer)
    except ZeroDivisionError as err:
        engine.say("You can not divide by zero stupid.")
        engine.runAndWait()
        print("You can not divide by zero stupid.")
        read_input("What is it sir?: ", "list")
    except ValueError:
        engine.say("Sorry sir, I could not understand the equation. Try again.")
        engine.runAndWait()
        print("Sorry sir, I could not understand the equation. Try again.")
        read_input("What is it sir?: ", "list")
    return read_input("What is it sir: ", "list")

def search(phrase):
    global user_input
    user_input = user_input.replace("Jarvis " + phrase + " ", "")
    search = user_input
    webbrowser.open('https://www.google.com/search?q=' + search)
    engine.say("Ok I will search for " + search)
    engine.runAndWait()
    print("Ok I will search for " + search)
    return read_input("What is it sir: ", "list")

def standby():
    global standby
    standby = True
    engine.say("Going into standby mode.")
    engine.runAndWait()
    print("Going into standby mode.")
    return read_input("Standing by: ", "list")

def exitStandby():
    global standby
    if standby == True:
        standby = False
        engine.say("Exiting standby mode.")
        engine.runAndWait()
        print("Exiting standby mode.")
    else:
        engine.say("I am not in standby mode sir.")
        engine.runAndWait()
        print("I am not in standby mode sir.")
        return read_input("What is it sir: ", "list")

command = ""

def find_command():
    global command
    for word in input_list:
        if word == "Jarvis":
            index = input_list.index("Jarvis")+1
            while index < len(input_list):
                command = command + input_list[index] + " "
                index += 1
    return command
            
class Command:
    def __init__(self, name, keyword, phrase, function):
        self.name = name
        self.keyword = keyword
        self.phrase = phrase
        self.function = function

#Every word after "Jarvis" will turn into the phrase
    def respond(self):
        global command
        global user_input
        for phrase in self.phrase:
            command = ""
            if phrase in find_command():
                if self.function == "first_president":
                    firstPresident()
                if self.function == "repeat":
                    repeat()
                if self.function == "newTab":
                    newTab()
                if self.function == "stop":
                    stop()
                if self.function == "calculate":
                    calculate()
                if self.function == "search":
                    search(phrase)
                if self.function == "standby":
                    standby()
                if self.function == "exitStandby":
                    exitStandby()
                
def dispatch():
    command1.respond()
    command2.respond()
    command3.respond()
    command4.respond()
    command5.respond()
    command6.respond()
    command7.respond()
    command8.respond()
    read_input("What is it sir: ", "list")

command1 = Command("ask president", "Jarvis", lists.firstPresident, "first_president")
command2 = Command("repeat", "Jarvis", lists.repeat, "repeat")
command3 = Command("new tab", "Jarvis", lists.newTab, "newTab")
command4 = Command("stop running", "Jarvis", lists.stop, "stop")
command5 = Command("calulate", "Jarvis", lists.calculate, "calculate")
command6 = Command("search", "Jarvis", lists.search, "search")
command7 = Command("stand by", "Jarvis", lists.standby, "standby")
command8 = Command("exit stand by", "Jarvis", lists.exitStandby, "exitStandby")

try:
    # for testing purposes this is the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    def activateVoice(ask):
        global r
        global audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(ask)
            audio = r.listen(source)
            return r.recognize_google(audio)

    def read_input(ask, output):
        global r
        global audio
        global user_input
        global input_list
        if useVoice == True:
            user_input = activateVoice(ask)
        else:
            user_input = input(ask)
        # TEXT input(ask)
        # VOICE input = r.recognize_google(audio)
        input_list = user_input.split()
        print("Jarvis thinks you said " + user_input)
        if output == "text":
            return user_input, dispatch()
        if output == "list":
            return input_list, dispatch()
        if output == "text_end":
            return user_input
    if useVoice == True:
        read_input("Say something sir: ", "list")
    else:
        read_input("What is it sir?: ", "list")

except sr.UnknownValueError:
    print("Jarvis could not understand audio")
    activateVoice("Say something sir: ")
except sr.RequestError as e:
    print("Could not request results from Jarvis's recognition service; {0}".format(e))
    activateVoice("Say something sir: ")