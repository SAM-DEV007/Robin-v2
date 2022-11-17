import tkinter
import tkinter.font as font
import datetime
import speech_recognition as speech
import pyttsx3
import wikipedia
from googlesearch import search
import webbrowser
import os
import random
import requests, json

#Variables

listening = False
api_key_city = "41c3a1696ef8af2f9835409e70a60645"
api_key = "d3318ab7e1e1aa8f9524a810185d2ac1"
url_weather = "http://api.openweathermap.org/data/2.5/weather?"
listener = speech.Recognizer()
replier = pyttsx3.init()
rate = replier.getProperty('rate')

replier.setProperty('rate', rate - 50)

#Arrays (or maybe dictionaries added later too .. idk)
name_interaction = [

    "Hey",
    "Yo",
    "Hello, I am at your service",
    "Hi",
    "Greetings"

]

asking_name_interaction = [

    "You just called me with my name",
    "Hi, this is Robin",
    "You know my name",
    "I am an AI Assistant named Robin",
    "Hey, this is Robin"

]

creator_interaction = [

    "I am created by Samyak",
    "My creator is Samyak",
    "Samyak is my owner and creator"

]

how_are_you_interaction = [

    "I am fine!",
    "My systems are online and working perfectly fine!",
    "Me? Yeah, I'm fine!"

]

thank_you_interaction = [

    "Welcome!",
    "It's my duty",
    "My pleasure"

]

name_not_called_interaction = [

    "Try to call me with my name!",
    "Please call me with my name",
    "I like helping you when you call me with my name"

]

class Robin(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        master.geometry("500x500")

        self.pack()

        Main_Frame = master

        label = tkinter.Label(Main_Frame, text = "VIRTUAL ASSISTANT!", foreground = "blue", bg = "white", width = "500")
        label['font'] = font.Font(family = "Cooper", size = "30")
        label.pack(side = "top")

        credits = tkinter.Label(Main_Frame, text = "Robin is currently Under Development! Made by Samyak!", width = "500", bg = "black", fg = "white")
        credits['font'] = font.Font(family = "Cooper", size = "9")
        credits.pack(side = "bottom")

        robin = tkinter.Label(Main_Frame, text = "Robin", bg = "white", width = "50")
        robin['font'] = font.Font(family = "Arial", size = "10")
        robin.pack(pady = "20")

        self.RobinUse = tkinter.StringVar()
        lbl = tkinter.Label(Main_Frame, textvariable = self.RobinUse, bg = "yellow",  width = "50", height = "4", wraplength = "400", justify = "left")
        lbl['font'] = font.Font(family = "Cooper", size = "10")
        lbl.pack(pady = "20")

        client = tkinter.Label(Main_Frame, text = "User", bg = "white", width = "50")
        client['font'] = font.Font(family = "Cooper", size = "10")
        client.pack(pady = "20")

        self.CLientUse = tkinter.StringVar()
        label = tkinter.Label(Main_Frame, textvariable = self.CLientUse, bg = "yellow",  width = "50", height = "4", wraplength = "400", justify = "left")
        label['font'] = font.Font(family = "Cooper", size = "10")
        label.pack(pady = "20")

        def Button():
            self.Button = tkinter.StringVar()
            self.Button.set("LISTEN")
            button = tkinter.Button(Main_Frame, textvariable = self.Button, bg = "cyan", width = "10", command = self.run_robin)
            button.pack(pady = "10")

        Button()

        self.ButtonText = tkinter.StringVar()
        self.ButtonText.set("QUIT")
        button = tkinter.Button(Main_Frame, textvariable = self.ButtonText, bg = "cyan", width = "10", command = Main_Frame.destroy)
        button.pack(pady = "10")

        self.after(2000, self.MainFuntion)

    #Functions
    def MainFuntion(self):
        global listening

        self.Intro()

    def Time(self, i):
        _hour = datetime.datetime.now().hour

        if i == "Intro":
            if _hour > 5 and _hour < 12:
                greetings = "Good Morning!"
            elif _hour >= 12 and _hour < 18:
                greetings = "Good Afternoon!"
            else:
                greetings = "Good Evening!"

            return greetings

        elif i == "Outro":
            if _hour >= 18 or _hour < 5:
                greetings = "Good Night!"
            else:
                greetings = "Have a good day!"

            return greetings

    def Intro(self):
        global replier

        _greet = self.Time("Intro")

        self.RobinUse.set(_greet + " Robin is online!")
        replier.say(_greet + " Robin is online!")
        replier.runAndWait()

    def weather_city_finder(self, city):
        global url_weather
        global api_key

        complete_url_weather_city = url_weather + "appid=" + api_key + "&q=" + city
        response = requests.get(complete_url_weather_city)

        x = response.json()

        if x["cod"] != "404":
            y = x["main"]

            current_temp = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]

            weather_desc = z[0]["description"]

            temp_celsius = (current_temp - 273.15)
            temp_celsius = "{:.2f}".format(temp_celsius)

            #Converting them to strings
            temperature = str(temp_celsius)
            humidity = str(current_humidity)
            weather = str(weather_desc)

            return True, temperature, humidity, weather

        else:
            return False, None, None, None

    def weather_finder(self):
        global api_key
        global url_weather

        my_ip_url = "https://ip.42.pl/raw"
        response_ip = requests.get(my_ip_url)

        my_ip = response_ip.text

        city_finder_url = "http://api.ipstack.com/" + my_ip +"?access_key=" + api_key_city
        res = requests.get(city_finder_url)

        a = res.json()

        city_name = a["city"]

        complete_url_weather = url_weather + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url_weather)

        x = response.json()

        if x["cod"] != "404":
            y = x["main"]

            current_temp = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]

            weather_desc = z[0]["description"]

            temp_celsius = (current_temp - 273.15)
            temp_celsius = "{:.2f}".format(temp_celsius)

            #Converting them to strings
            temperature = str(temp_celsius)
            humidity = str(current_humidity)
            weather = str(weather_desc)

            return True, temperature, humidity, weather

        else:
            return False, None, None, None

    def random_chooser(self, i):
        if i == 1 or i == 2:
            random_num = random.randrange(0, 5, 1)

        elif i == 3:
            random_num = random.randrange(0, 3, 1)

        elif i == 4:
            random_num = random.randrange(0, 2, 1)

        return random_num

    def Speak(self, text):
        global replier

        replier.say(text)
        replier.runAndWait()

    def Search(self, text):
        query = text.strip()

        for url in search(query, tld = "co.in", num = 1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % query)

    def Search_Google(self):
        webbrowser.open("https://webmail.licindia.in/owa/")

    def Search_App(self, app):
        os.system(app)

    def Open_Website(self, text):
        web = text.strip()

        webbrowser.open("https://" + web + ".com")

    def Search_YT(self, text):
        query = text.strip()

        for url in search(query, tld = "co.in", num = 1, stop = 1, pause = 2):
            webbrowser.open("https://youtube.com/search?q=%s" % query)

    def take_cmd(self):
        cmd = ""
        global listening
        global listener

        if listening:
            try:
                with speech.Microphone() as source:
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source)
                    cmd = listener.recognize_google(voice)
                    cmd = cmd.lower()

                    self.Button.set("LISTEN")
                    listening = False
            except:
                pass

        #time.sleep(1)

        if cmd != None:
            return cmd

    def robin_commands(self, cmd):
        global listening
        global Main_Frame
        global time

        if "play" in cmd:
            YT = cmd.replace("play", "", 1)
            YT = YT.strip()

            self.CLientUse.set(cmd)

            self.RobinUse.set("Opening youtube and searching " + YT)
            self.Speak("opening youtube and searching " + YT)
            self.Search_YT(YT)

        elif "weather of city" in cmd:
            self.CLientUse.set(cmd)
            city_commanded = cmd.partition("city")[1]

            status, temp_city, hum_city, weather_city = self.weather_city_finder(city_commanded)

            if status:
                self.RobinUse.set(

                "Temperature is " + temp_city + " °C" +
                ", Humidity is " + hum_city + " %" +
                ", Weather is " + weather_city

                )

                self.Speak("temperature is " + temp_city + " degree celsius. Humidity is " + hum_city + " percent. Weather is " + weather_city)
            else:
                self.RobinUse.set("City not found or Services Offline!")
                self.Speak("city not found or services offline")

        elif "weather" in cmd:
            self.CLientUse.set(cmd)

            status, temp_here, hum_here, weather_here = weather_finder()

            if status:
                self.RobinUse.set(

                "Temperature is " + temp_here + " °C" +
                "\n Humidity is " + hum_here + " %" +
                "\n Weather is " + weather_here

                )

                self.Speak("temperature is " + temp_here + " degree celsius. Humidity is " + hum_here + " percent. Weather is " + weather_here)
            else:
                self.RobinUse.set("City not found or Services Offline!")
                self.Speak("city not found or services offline")

        elif "time" in cmd:
            self.CLientUse.set(cmd)

            time = datetime.datetime.now().strftime("%I:%M %p")

            self.RobinUse.set("It's " + time + " now")
            self.Speak("It's " + time + " now")

        elif "search wiki" in cmd:
            search_info = cmd.replace("search wiki", "", 1)
            info = wikipedia.summary(search_info, 3)

            self.CLientUse.set(cmd)

            self.RobinUse.set(info)
            self.Speak(info)

        elif "google search" in cmd:
            search_google = cmd.replace("google search", "", 1)
            search_google = search_google.strip()

            self.CLientUse.set(cmd)

            self.RobinUse.set("Opening chrome and searching " + search_google)
            self.Speak("opening chrome and searching " + search_google)
            self.Search(search_google)

        elif "open website" in cmd:
            website = cmd.replace("open website", "", 1)
            website = website.strip()

            self.CLientUse.set(cmd)

            self.RobinUse.set("Opening " + website)
            self.Speak("opening " + website)
            self.Open_Website(website)

        elif "name" in cmd:
            global asking_name_interaction
            self.CLientUse.set(cmd)

            random_number = self.random_chooser(2)
            self.RobinUse.set(asking_name_interaction[random_number])
            self.Speak(asking_name_interaction[random_number])

        elif "creator" in cmd or "created" in cmd or "owner" in cmd:
            global creator_interaction
            self.CLientUse.set(cmd)

            random_number_Chosen = self.random_chooser(3)
            self.RobinUse.set(creator_interaction[random_number_Chosen])
            self.Speak(creator_interaction[random_number_Chosen])

        elif "how are you" in cmd:
            global how_are_you_interaction
            self.CLientUse.set(cmd)

            num_chosen = self.random_chooser(3)
            phrase_selected = how_are_you_interaction[num_chosen]

            self.RobinUse.set(phrase_selected)
            self.Speak(phrase_selected)

        elif "thank you" in cmd:
            global thank_you_interaction
            self.CLientUse.set(cmd)

            _num = self.random_chooser(3)
            _phrase = thank_you_interaction[_num]

            self.RobinUse.set(_phrase)
            self.Speak(_phrase)

        elif "hi" in cmd or "hello" in cmd or "hey" in cmd:
                global name_interaction

                random_num_chosen = self.random_chooser(1)
                self.RobinUse.set(name_interaction[random_num_chosen])
                self.Speak(name_interaction[random_num_chosen])

        elif "see you later" in cmd or "good night" in cmd or "bye" in cmd or "goodbye" in cmd or "good bye" in cmd or "later" in cmd:
            self.CLientUse.set(cmd)

            _greetings = self.Time("Outro")

            self.RobinUse.set("Robin going offline! " + _greetings)
            self.Speak("Robin going offline! " + _greetings)

            exit()

        else:
            self.CLientUse.set(cmd)

            self.RobinUse.set("Unable to understand your command!")
            self.Speak("Unable to understand your command")

    def run_robin(self):
        global listening
        listening = True

        if listening:
            cmd = self.take_cmd()

            if cmd != None:
                if cmd != "":
                    if "robin" in cmd:
                        self.CLientUse.set(cmd)
                        cmd = cmd.replace("robin", "", 1)

                        if "hi" in cmd or "hello" in cmd or "hey" in cmd or "see you later" in cmd or "good night" in cmd or "open webite" in cmd or "google search" in cmd or "search wiki" in cmd or "time" in cmd or "play" in cmd or "name" in cmd or "creator" in cmd or "created" in cmd or "owner" in cmd or "weather" in cmd or "weather of city" in cmd or "how are you" in cmd or "thank you" in cmd:
                            self.robin_commands(cmd)

                        else:
                            self.CLientUse.set(cmd)

                            self.RobinUse.set("Unable to understand your command!")
                            self.Speak("unable to understand your command")

                    else:
                        global name_not_called_interaction
                        self.CLientUse.set(cmd)

                        _Random = self.random_chooser(4)
                        _Phrase_Selected = name_not_called_interaction[_Random]

                        self.RobinUse.set(_Phrase_Selected)
                        self.Speak(_Phrase_Selected)
                else:
                    self.CLientUse.set("*NO INPUT*")
                    self.RobinUse.set("")
            else:
                self.CLientUse.set("*NO INPUT*")
                self.RobinUse.set("")

    listening = False                    


def Main():
    root = tkinter.Tk()
    root.title("Robin v2")
    window = Robin(root)
    window.mainloop()

Main()

