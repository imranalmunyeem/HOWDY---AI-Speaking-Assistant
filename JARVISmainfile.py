import random, pywhatkit, pyttsx3, datetime, sys, time, os, pyautogui, requests, serial
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QMainWindow

from Business.crypto_assistant import crypto_analysis_assistant
from Business.stock_assistant import stock_analysis_app
from Professional.cover_letter import create_cover_letter
from Security.fuzzing import automated_fuzzer
from Security.port_scanner import perform_port_scan
from Professional.resume_maker import create_resume
from Security.securityscanner import perform_security_scan
from jarvisChitChat import jarvyChatBot
from JARVISmainfileGUI import Ui_JARVISmainUI
from Security.url_checker import url_threat_checker

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 175)
temp = False


def speak(audio):
    ui.updateMoviesDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishing():
    ui.updateMoviesDynamically("loading")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        ui.terminalPrint("Howdy says ->: Good Morning! How can I assist you today?")
        speak("Good Morning! How can I assist you today?")
    elif 12 <= hour < 17:
        ui.terminalPrint("Howdy says ->: Good Afternoon! How can I assist you today?")
        speak("Good Afternoon! How can I assist you today?")
    elif 17 <= hour < 21:
        ui.terminalPrint("Howdy says ->: Good Evening! How can I assist you today?")
        speak("Good Evening! How can I assist you today?")
    else:
        ui.terminalPrint("Howdy says ->: Good Night! How can I assist you today?")
        speak("Good Night! How can I assist you today?")


def playSong():
    from os import startfile, listdir, path
    from random import choice
    songsPath = "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/audio lib"
    songsList = listdir(songsPath)
    songName = choice(songsList)
    songName = songName.lstrip(".mp3")
    startfile(path.join(songsPath, songName))
    ui.jarvisPrint(f"Playing {songName[:20]}")
    speak(f"Playing {songName}")


def wakeUpCommands():
    ui.updateMoviesDynamically("sleeping")
    ui.terminalPrint("Howdy is Sleeping...")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source,duration=1)
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {query}\n")
        except:
            query = "none"
        if "wake up" in query:
            break


class jarvisCodingClass(QThread):
    def __init__(self):
        super(jarvisCodingClass, self).__init__()
        self.fanStatus = True
        self.lightStatus = True
        self.isIronHomeConnected = self.ConnectIronHome()


    def run(self):
        if self.isIronHomeConnected:
           ui.UpdateIronHomeLabels("ironHomeONLINE")
        else:
           ui.UpdateIronHomeLabels("ironHomeOFFLINE")
        self.executeJARVIS()


    def filterTheQueryForSpecificWord(self, queryToBeFiltered):
        queryToBeFiltered = queryToBeFiltered.replace("jarvis",'')
        query = queryToBeFiltered.replace("javed",'')
        query = query.replace("hey",'')
        query = query.replace("can",'')
        query = query.replace("please",'')
        query = query.replace("bro",'')
        query = query.replace("pro",'')
        query = query.replace("baby",'')
        query = query.replace("jarvy",'')
        query = query.replace("ok",'')
        query = query.replace("now",'')
        query = query.replace("you",'')
        query = query.replace("no",'')
        query = query.replace("the",'')
        query = query.replace("to",'')
        query = query.replace("do",'')
        query = query.replace("this",'')

        return query

    def listenWithoutFilter(self):
        ui.updateMoviesDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            ui.terminalPrint("Wait for few Moments..")
            ui.updateMoviesDynamically("loading")
            self.query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {self.query}")
            ui.terminalPrint("")
        except:
            ui.terminalPrint("Please tell me again")
            speak("Please tell me again")
            self.query = ""

        return self.query

    def listen(self):
        ui.updateMoviesDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            ui.terminalPrint("Wait for few Moments..")
            ui.updateMoviesDynamically("loading")
            self.query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {self.query}")
            ui.terminalPrint("")
            self.query = self.query.lower()
            self.query = self.query.replace("jarvis", "")
            self.query = self.query.replace("javed", '')
            self.query = self.query.replace("hey", '')
            self.query = self.query.replace("can", '')
            self.query = self.query.replace("please", '')
            self.query = self.query.replace("bro", '')
            self.query = self.query.replace("pro", '')
            self.query = self.query.replace("baby", '')
            self.query = self.query.replace("jarvy", '')

        except:
            ui.terminalPrint("Please tell me again")
            speak("Please tell me again")
            self.query = ""

        return self.query


    def minimise(self):
        pyautogui.hotkey('win', 'down')
        pyautogui.hotkey('win', 'down')
        ui.jarvisPrint("Recent window was minimised sir")
        speak("Recent window was minimised sir")
    def maximise(self):
        pyautogui.hotkey('win', 'up')
        pyautogui.hotkey('win', 'up')
        ui.jarvisPrint("Recent window was maximised sir")
        speak("Recent window was maximised sir")

    def filterAndType(self, searchQuery):
        try:
            filteredQuery = searchQuery.replace("search", "")
            filteredQuery = filteredQuery.replace("please", "")
            filteredQuery = filteredQuery.replace("google", "")
        except:
            filteredQuery = searchQuery
            print("filter error")
        time.sleep(0.5)
        pyautogui.write(filteredQuery)
        time.sleep(0.5)

    def ConnectIronHome(self):
        print("Connecting Smart Home")
        try:
            self.serialCom = serial.Serial('COM10', 9600, timeout=1)
            print("Smart Home Online")
            isIronHomeConnected = True
            temp = True
            self.serialCom.write(b'j')
        except:
            print("Bluetooth not connected")
            temp = False
            isIronHomeConnected = False

        return isIronHomeConnected

    def LightSwitch(self, lightStatus):
        try:
            if lightStatus:
                self.serialCom.write(b'b')
                self.lightStatus = True
                ui.UpdateIronHomeLabels("lightON")
            elif not lightStatus:
                self.serialCom.write(b'a')
                self.lightStatus = False
                ui.UpdateIronHomeLabels("lightOFF")
        except:
            speak("Unable to Switch Fan Sir")

    def FanSwitch(self, fanStatus):
        try:
            if fanStatus:
                self.serialCom.write(b'd')
                self.fanStatus = True
                ui.UpdateIronHomeLabels("fanON")
            elif not fanStatus:
                self.serialCom.write(b'c')
                self.fanStatus = False
                ui.UpdateIronHomeLabels("fanOFF")
        except:
            speak("Unable to Switch Fan Sir")

    def executeJARVIS(self):
        # wakeUpCommands()


        wishing()
        while True:
            self.query = self.listen()
            if self.query:
                self.commands()
            else:
                pass

    def commands(self):


        if 'time' in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            ui.jarvisPrint(f"The Time is {strTime}")
            speak(f"The Time is {strTime}")

        elif self.query == 'exit program' or self.query == 'exit the program' or self.query == 'exit':
            ui.jarvisPrint("I'm Quiting. BYEE!")
            speak("I'm Quiting. BYEE!")
            ui.jarvisPrint("Program quited")
            ui.close()

        elif self.query == "resume" or self.query == "cv" or 'cb' in self.query or 'resu' in self.query:
            create_resume()

        elif self.query == "cover" or self.query == "cober" or 'letter' in self.query or 'kover' in self.query:
            create_cover_letter()

        elif self.query == "security" or self.query == "secu":
            perform_security_scan()

        elif self.query == "url" or self.query == "threat" or self.query == "weburl":
            url_threat_checker()

        elif self.query == "fuzz" or self.query == "fuz" or self.query == "fuzzing" or self.query == "fuzzing" or self.query == "fajing" or self.query == "fuj" or self.query == "fazing" or self.query == "playload":
            automated_fuzzer()

        elif self.query == "port" or self.query == "por" or self.query == "pol" or self.query == "pot":
            perform_port_scan()

        elif self.query == "stock" or self.query == "stok" or self.query == "estok" or self.query == "stroke":
            stock_analysis_app()

        elif self.query == "crypto" or self.query == "cryptocurrency" or self.query == "bitcoin" or self.query == "etherium" or self.query == "kripto" or self.query == "kipto":
            crypto_analysis_assistant()

        elif 'wikipedia' in self.query:
            wikiQuery = self.query
            speak("Searching in Wikipedia")
            try:
                ui.updateMoviesDynamically("loading")
                from wikipedia import summary
                filteredQuery = wikiQuery.replace("wikipedia", "")
                results = summary(filteredQuery, sentences=1)
                speak("According to Wikipedia,")
                ui.jarvisPrint(results)
                speak(results)
            except Exception as e:
                ui.jarvisPrint(e)
                speak("No Results found...")
                ui.jarvisPrint("No results Found")
        elif self.query == 'play music' or self.query == 'put some music' or 'music' in self.query or 'song' in self.query:
            speak("Yea sure")
            ui.jarvisPrint("Yea sure")
            playSong()
            while True:
                query = self.listen().lower()
                if "change" in query or "next" in query or "forward" in query:
                    speak("Changing song")
                    ui.jarvisPrint("changing song")
                    playSong()
                elif "stop" in query or "exit" in query:
                    pyautogui.hotkey('alt', 'f4')
                    speak("Music turned off")
                    ui.jarvisPrint("Music turned off")
                    speak("Seems like you're out of mood now")
                    ui.jarvisPrint("Seems like you're out of mood now")
                    break
                elif "pause" in query or "play" in query or 'pass' in query:
                    pyautogui.press('space')
                elif 'mute' in query or 'sleep' in query:
                    ui.jarvisPrint("I'm going to sleep mode")
                    speak("I'm going to sleep mode")
                    wakeUpCommands()
                    break
                else:
                    pass
        elif self.query == "mute" or self.query == "sleep" or 'go to sleep' in self.query or 'mute' in self.query:
            ui.jarvisPrint("I'm going to sleep mode")
            speak("I'm going to sleep mode")
            wakeUpCommands()
        elif 'close this tab' in self.query or 'exit this tab' in self.query or 'close the tab' in self.query or 'exit the tab' in self.query:
            pyautogui.hotkey('ctrl', 'w')
            ui.jarvisPrint("Recent tab was closed")
            speak("Recent tab was closed")
        elif 'close this window' in self.query or 'exit this window' in self.query or 'close the window' in self.query or 'exit the window' in self.query or 'close all window' in self.query:
            pyautogui.hotkey('alt', 'f4')
            ui.jarvisPrint("Recent window was closed")
            speak("Recent window was closed")
        elif 'minimise this window' in self.query or 'minimise this window' in self.query or 'minimise the window' in self.query or 'minimise the window' in self.query\
                or 'minimize this window' in self.query or 'minimize this window' in self.query or 'minimize the window' in self.query or 'minimize the window' in self.query:
            self.minimise()
        elif 'minimize all windows' in self.query:
            pyautogui.hotkey('win', 'd')
            ui.jarvisPrint("All windows are minimised")
            speak("All windows are minimised")
        elif 'maximise this window' in self.query or 'maximise this window' in self.query or 'maximise the window' in self.query or 'maximise the window' in self.query \
                or 'maximize this window' in self.query or 'maximize this window' in self.query or 'maximize the window' in self.query or 'maximize the window' in self.query:
            self.maximise()
        elif self.query.startswith('open'):
            query = self.query.replace("open", "")
            query = query.replace("my","")
            query = query.replace("for me", "")
            ui.jarvisPrint(f"Opening {query}")
            speak(f"Opening {query}")
            pyautogui.hotkey('win', 's')
            time.sleep(0.2)
            pyautogui.write(query)
            pyautogui.press('enter')
            ui.jarvisPrint("It's on your screen")
            speak("It's on your screen")
        elif 'google' in self.query or 'browse' in self.query or 'browser' in self.query or 'search' in self.query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            ui.jarvisPrint("What should I search...")
            speak("What should I search...")
            browserQuery = self.listen().lower()
            if 'close this tab' in browserQuery or 'exit this tab' in browserQuery or 'close the tab' in browserQuery or 'exit the tab' in browserQuery:
                pyautogui.hotkey('ctrl', 'w')
                speak("closing browser")
            elif 'close this window' in browserQuery or 'exit this window' in browserQuery or 'close the window' in browserQuery or 'exit the window' in browserQuery or 'close all window' in browserQuery:
                pyautogui.hotkey('alt', 'f4')
            elif "minimise" in browserQuery or "minimize" in browserQuery:
                pyautogui.hotkey('win', 'down', 'down')
            elif "maximise" in browserQuery or "maximize" in browserQuery:
                pyautogui.hotkey('win', 'up', 'up')
            else:
                self.filterAndType(browserQuery)
                pyautogui.press('enter')
                ui.jarvisPrint("Here's what I found!")
                speak("Here's what I found!")
        elif 'screenshot' in self.query or 'screen shot' in self.query:
            pyautogui.hotkey('win', 'alt', 'prtsc')
            ui.jarvisPrint("Screenshot is saved")
            speak("Screenshot is saved")
        elif 'joke' in self.query:
            from pyjokes import get_joke
            from jarvisChitChat import jokeReplyQuery
            ui.jarvisPrint("Yes sure")
            speak("Yes sure")
            joke = get_joke('en')
            ui.jarvisPrint(joke)
            speak(joke)
            reply = random.choice(jokeReplyQuery)
            ui.jarvisPrint(reply)
            speak(reply)
        elif 'location' in self.query or 'find me' in self.query:
            ui.jarvisPrint("Fetching details")
            speak("Fetching details")
            ipAdd = requests.get('https://api.ipify.org').text
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            locDetails = requests.get(url)
            locDetails2 = locDetails.json()
            city = locDetails2['city']
            state = locDetails2['region']
            country = locDetails2['country']
            ui.jarvisPrint(f"You're in {city} city which is inside {state} State of {country} country")
            speak(f"You're in {city} city which is inside {state} State of {country} country")

        elif 'youtube' in self.query and 'play' in self.query:
            try:
                filQuery = self.query.replace("play", "")
                filQuery = filQuery.replace("youtube", "")
                filQuery = filQuery.replace("go to", "")
                filQuery = filQuery.replace("and", "")
            except:
                filQuery = self.query
            ui.jarvisPrint(f"Playing{filQuery}")
            speak(f"Playing{filQuery}")
            pywhatkit.playonyt(self.query)
        elif 'write a note' in self.query or 'notepad' in self.query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")
            speak("Opened Notepad application")
            speak("Please direct me what should I write for you")
            while True:
                query = self.listenWithoutFilter()
                pyautogui.write(query)
                filteredQuery = self.filterTheQueryForSpecificWord(self.query)
                if self.query.startswith('exit') or self.query.startswith('stop') or self.query.startswith('close'):
                    speak('okay')
                    pyautogui.hotkey('ctrl', 'w')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    break
                elif 'save' in filteredQuery:
                    pyautogui.hotkey('ctrl', 's')
                    currTime = datetime.datetime.now().strftime("%H:%M:%S")
                    fileName = str(currTime).replace(":","-") + ".jarvis.txt"
                    time.sleep(0.4)
                    pyautogui.write(fileName)
                    pyautogui.press('enter')
                    ui.jarvisPrint("file Saved successfully")
                    speak("file Saved successfully")
                    break
        elif 'weather' in self.query or 'climate' in self.query:
            from weatherAPI import weatherCheck
            try:
                temp, tempFeelsLike, hum, pressure, weatherReport, wind = weatherCheck()
                ui.jarvisPrint(f"The temperature is around {temp}")
                speak(f"The temperature is around {temp}")
            except:
                ui.jarvisPrint("Apologies! I'm getting error while fetching weather update")
                speak("Apologies! I'm getting error while fetching weather update")
        elif self.query.startswith('type'):
            self.query.replace('type', '')
            pyautogui.write(self.query)


        elif 'connect' in self.query:
            speak("Connecting Iron Home")
            self.ConnectIronHome()
            if self.isIronHomeConnected:
                speak("Iron Home Online")
            else:
                speak("Unable to Connect Sir")

        else:
            if self.query == "":
                pass
            else:
                chatting = jarvyChatBot(self.query)
                ui.jarvisPrint(chatting)
                speak(chatting)


jarvisBackend = jarvisCodingClass()


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.jarvisui = Ui_JARVISmainUI()
        self.jarvisui.setupUi(self)

        self.jarvisui.exitButton.clicked.connect(self.close)
        self.jarvisui.enterButton.clicked.connect(self.manuallyCoded)
        self.runallMovies()


    def terminalPrint(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(text)

    def terminalPrintUserInput(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(f">>> {text}")

    def jarvisPrint(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(f"Howdy says ->: {text}")

    def manuallyCoded(self):
        if self.jarvisui.terminalInputBox.text():
            var = self.jarvisui.terminalInputBox.text()
            self.jarvisui.terminalInputBox.clear()
            self.terminalPrintUserInput(var)
            if var == "Exit":
                ui.close()
            elif var == "help":
                self.terminalPrint("I can perform various tasks which is programmed inside me\n"
                                   "Examples are: Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")
            elif var == "features":
                self.terminalPrint("Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")
            elif var == 'exit':
                self.terminalPrint("Quiting")
                self.close()

            else:
                pass


    def updateMoviesDynamically(self, state):
        if state == "speaking":
            self.jarvisui.jarvisSpeakingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.show()    #
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "listening":
            self.jarvisui.listeningLabel.show()    #
            self.jarvisui.listeningLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "loading":
            self.jarvisui.jarvisLoadingLabel.show()
            self.jarvisui.jarvisLoadingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "sleeping":
            self.jarvisui.sleepingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.sleepingLabel.show()
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()


        else:
            pass

    def runallMovies(self):

        self.jarvisui.listeningMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/listening.gif")
        self.jarvisui.listeningLabel.setMovie(self.jarvisui.listeningMovie)
        self.jarvisui.listeningMovie.start()

        self.jarvisui.speakingMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/speaking.gif")
        self.jarvisui.jarvisSpeakingLabel.setMovie(self.jarvisui.speakingMovie)
        self.jarvisui.speakingMovie.start()

        self.jarvisui.arcMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/techcircle.gif")
        self.jarvisui.arcLabel.setMovie(self.jarvisui.arcMovie)
        self.jarvisui.arcMovie.start()

        self.jarvisui.backgroundMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/background-cropped.gif")
        self.jarvisui.backgroundgifLabel.setMovie(self.jarvisui.backgroundMovie)
        self.jarvisui.backgroundMovie.start()

        self.jarvisui.loadingMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/tech loading-cropped.gif")
        self.jarvisui.jarvisLoadingLabel.setMovie(self.jarvisui.loadingMovie)
        self.jarvisui.loadingMovie.start()

        self.jarvisui.sleepingMovie = QtGui.QMovie("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/sleepmode.gif")
        self.jarvisui.sleepingLabel.setMovie(self.jarvisui.sleepingMovie)
        self.jarvisui.sleepingMovie.start()

        self.jarvisui.ironHomeReactorMOVIE = QtGui.QMovie(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/smarthomereactor.gif")
        self.jarvisui.ironHomeReactorLabel.setMovie(self.jarvisui.ironHomeReactorMOVIE)
        self.jarvisui.ironHomeReactorMOVIE.start()

        jarvisBackend.start()

    def UpdateIronHomeLabels(self, status):
        if status == "lightON":
            self.jarvisui.IHLightsONLabel.show()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHLightsON.show()
            self.jarvisui.IHLightsOFF.hide()
        elif status == "lightOFF":
            self.jarvisui.IHLightsONLabel.hide()
            self.jarvisui.IHLightsOFFLabel.show()
            self.jarvisui.IHLightsON.hide()
            self.jarvisui.IHLightsOFF.show()
        elif status == "fanON":
            self.jarvisui.IHFanONLabel.show()
            self.jarvisui.IHFanOFFLabel.hide()
            self.jarvisui.IHFanON.show()
            self.jarvisui.IHFanOFF.hide()
        elif status == "fanOFF":
            self.jarvisui.IHFanONLabel.hide()
            self.jarvisui.IHFanOFFLabel.show()
            self.jarvisui.IHFanON.hide()
            self.jarvisui.IHFanOFF.show()
        elif status == "ironHomeONLINE":
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.IHOnlineLabel.show()
            self.jarvisui.IHOfflineLabel.hide()
            self.jarvisui.IHLightsON.show()
            self.jarvisui.IHLightsOFF.hide()
            self.jarvisui.IHFanON.show()
            self.jarvisui.IHFanOFF.hide()
            self.jarvisui.IHLightsONLabel.show()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHFanOFFLabel.show()
            self.jarvisui.IHFanOFFLabel.hide()
        elif status == "ironHomeOFFLINE":
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.IHOfflineLabel.show()
            self.jarvisui.IHOnlineLabel.hide()
            self.jarvisui.IHLightsON.hide()
            self.jarvisui.IHLightsOFF.show()
            self.jarvisui.IHFanON.hide()
            self.jarvisui.IHFanOFF.show()
            self.jarvisui.IHLightsONLabel.hide()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHFanONLabel.hide()
            self.jarvisui.IHFanOFFLabel.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()
    sys.exit(app.exec_())
