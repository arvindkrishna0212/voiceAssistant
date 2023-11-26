import speech_recognition as sr
import pyttsx3
import webbrowser as web
import pywhatkit as pwt
import time
import geocoder
from geopy.geocoders import Nominatim
import wikipedia
import AppOpener
import pyautogui
import pywhatkit as pwt
import pyjokes
from AppOpener import open
import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap

UI=QtWidgets.QApplication(sys.argv)
window=QtWidgets.QWidget()
window.resize(650,170)
window.move(600,400)
window.setWindowTitle('abc')
window.label_1 = QLabel("listening... ", window)
window.label_1.setStyleSheet("border :3px solid black;background: Yellow")
window.label_1.setFont(QFont('Arial', 60))
content = window.label_1.text()
print(content)
window.show()

#instantiating the Recognizer and Microphone classes
recognizer = sr.Recognizer()
mic = sr.Microphone()

geolocator = Nominatim(user_agent='arvind')

def openApp(name):
    AppOpener.open(name, match_closest=True)

def closeApp(name):
    AppOpener.close(name, match_closest=True)

def isNumber(num):
    if num=='1' or num=='2' or num=='3' or num=='4' or num=='5' or num=='6' or num=='7' or num=='8' or num=='9' or num=='0':
        return True
    return False

terminate = False
while not terminate:
    try:
        # Setting up the text-to-speech engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        with mic as source:
            engine.say('Listening')
            engine.runAndWait()
            print("Listening...")

            #Converting speech-to-text
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            recognizer.dynamic_energy_threshold = True
            audio = recognizer.listen(source, 3, 10)
            audioText = recognizer.recognize_google(audio)
            print(audioText)
            audioText = audioText.lower()

        if audioText == 'close window':
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')

        elif 'close browser tab' in audioText:
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')
            pyautogui.keyUp('ctrl')
            engine.say("Closed browser tab")

        elif audioText[0: 4] == 'type':
            search = audioText.replace('type ', '')
            letters = list(search)
            for i in letters:
                pyautogui.press(i)

        elif audioText == 'select all':
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")
            engine.say('selected')

        elif audioText == 'copy':
            pyautogui.keyDown("ctrl")
            pyautogui.press("c")
            pyautogui.keyUp("ctrl")
            engine.say("copied")

        elif audioText == 'paste':
            pyautogui.keyDown("ctrl")
            pyautogui.press("v")
            pyautogui.keyUp("ctrl")
            engine.say("pasted")

        elif audioText == 'delete':
            pyautogui.press("delete")
            engine.say("deleted")

        elif 'retry' in audioText:
            engine.say('Processes terminated')
            engine.runAndWait()
            engine.say('Try again')
            continue

        elif audioText[0: 8] == 'open app':
            search = audioText.replace('open app ', '')
            engine.say("Opening " + search)
            engine.runAndWait()
            openApp(search)

        elif 'close app' in audioText:
            search = audioText.replace('close app ', '')
            engine.say('Closing ' + search)
            engine.runAndWait()
            closeApp(search)

        elif "open" in audioText:
            search = audioText.replace('open ', '')
            engine.say("Opening " + search)
            engine.runAndWait()
            website = search.replace(' ', '')
            web.open('https://www.' + website + '.com/', new=2)

        elif 'youtube search' in audioText:
            search = audioText.replace('youtube search ', '')
            engine.say("Opening youtube")
            engine.runAndWait()
            pwt.playonyt(search)


        elif audioText[0: 24] == 'send whatsapp message to':
            query = audioText.replace('send whatsapp message to ', '')
            reciever = ''
            for i in range(0, len(query), 1):
                if(query[i] == ' ' and not isNumber(query[i+1])):
                    break
                reciever = reciever + query[i]
            reciever1 = reciever.replace(' ', '')
            print(reciever1)
            message = query.replace(reciever+' ', '')
            number = "+91" + reciever1
            if reciever1 == 'dad':
                number = '+918220204418'
            if reciever1 == 'mom':
                number = '+919952754702'
            if reciever1 == 'arvind':
                number = '+919381845300'
            engine.say('opening whatsapp web')
            engine.runAndWait()
            engine.say('sending message')
            pwt.sendwhatmsg_instantly(number, message)

        elif 'call' in audioText:
            reciever = audioText.replace('call ', '')
            letters = list(reciever)
            for i in letters:
                pyautogui.press(i)
            engine.say("calling " + reciever)
            pyautogui.moveTo(207, 223)
            pyautogui.click(button='left')
            pyautogui.moveTo(1780, 75, duration=2, tween=pyautogui.easeInOutSine)
            pyautogui.click(button='left')

        elif 'what is' in audioText:
            search = audioText.replace('what is ', '')
            content = wikipedia.summary(search, sentences=1)
            print(content)
            engine.say(content)
            engine.runAndWait()

        elif 'who is' in audioText:
            search = audioText.replace('who is ', '')
            content = wikipedia.summary(search, sentences=1)
            print(content)
            engine.say(content)
            engine.runAndWait()

        elif audioText == "screenshot":
            pyautogui.screenshot('screenshot.png')
            engine.say("screenshot captured")

        elif 'location of' in audioText:
            engine.say("Opening Google Maps")
            engine.runAndWait()
            search = audioText.replace('location of ', '')
            location = geolocator.geocode(search)
            lat = str(location.latitude)
            long = str(location.longitude)
            web.open('https://www.google.com/maps/@' + lat + ',' + long +',19z', new=2)

        elif 'tell me a joke' in audioText:
            joke = pyjokes.get_joke()
            print(joke)
            engine.say(joke)
            engine.runAndWait()

        elif 'quit' in audioText or 'stop' in audioText:
            output = 'terminating'
            print(output)
            engine.say(output)
            engine.runAndWait()
            terminate = True
            break

        elif 'latest news' in audioText:
            url = 'https://www.thehindu.com/latest-news/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            count = 1
            for x in headlines:
                count += 1
                print(x.text.strip())
                engine.say(x.text.strip())
                if count >= 4:
                    break

        else:
            search = audioText.replace(' ', '+')
            url = "https://www.google.com/search?q=" + search + "&sxsrf=ALiCzsbwx-Lg9DdRtpMBtaq2pF8Nd-0FsQ%3A1673002349856&ei=bf23Y_j2M-L04-EP35KEsAE&ved=0ahUKEwi44ZW247L8AhVi-jgGHV8JARYQ4dUDCA4&uact=5&oq=hello+bye&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCC4QgAQyBQgAEIAEMgUILhCABDIFCAAQgAQyCAguENQCEIAEMggILhDUAhCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6DAguEMgDELADEEMYAjoHCAAQsQMQQzoHCC4Q1AIQQzoECC4QQzoKCAAQgAQQhwIQFDoKCC4QgAQQhwIQFDoLCAAQgAQQsQMQgwE6CwguEIAEELEDEIMBOggIABCABBCxAzoLCC4Q1AIQsQMQgAQ6CAguEIAEELEDOgsILhCABBCxAxDUAjoICC4QgAQQ1AJKBAhBGABKBAhGGAFQyl1Yk2xgknVoAnABeACAAc8DiAHBCpIBBzItMi4xLjGYAQCgAQHIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz-serp"
            web.open(url, new=2)

    except sr.UnknownValueError:
        output = "Unable to recognize speech"
        print(output)
        engine.say(output)
        time.sleep(0.5)
        engine.say("retry")
        engine.runAndWait()
        terminate = False

    except sr.WaitTimeoutError:
        output = "You took too long"
        print(output)
        engine.say(output)
        time.sleep(0.5)
        engine.say("retry")
        engine.runAndWait()
        terminate = False

