import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from gtts import gTTS

print("Gatot AI")
MASTER = "Faris dan Gareth"

# Deklarasi variabel recognizer untuk sr.Recognizer()
recognizer = sr.Recognizer()

# Setup untuk Text to Speech
engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)  # Untuk mengatur kecepatan AI berbicara
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Untuk mengatur suara AI menjadi cowok/cewek

# Fungsi untuk melakukan AI berbicara
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Fungsi untuk menyapa user/pengguna sesuai dengan jamnya, Good Morning ketika jam 12 malam hingga jam 12 siang, Good Afternoon ketika Sore, dan Good Evening ketika malam
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk(f"Hello, Good Morning {MASTER}")
    elif hour >= 12 and hour < 18:
        talk(f"Hello, Good Afternoon {MASTER}")
    else:
        talk(f"Hello, Good Evening {MASTER}")

#Fungsi untuk melakukan proses penerimaan input dari Microphone pada device user, lalu inputan tersebut ke command
def take_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("Waiting for command...")
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            command = command.lower()
            if "gatot" in command:
                print(command)  
                command = command.replace("gatot", "")
                talk(command) 
    except:
        pass

    return command

wishMe()
talk("I am Gatot, your Artificial Intelligence assistant.")
     
# Melakukan perulangan terus menerus hingga user mengatakan "enough" untuk memberhentikan eksekusi program
while True:

    talk("Is there anything I can help?")
    command = take_command()
    
    # Nested If atau percabangan If untuk menyaring perintah yang sesuai
    if 'play' in command:
        song = command.replace("play", "")
        print(command) 
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(f"The time now is {time}")

    elif 'wikipedia' in command:
        search_term = command.replace("wikipedia", "")
        info = wikipedia.summary(search_term, sentences=5)
        print(command) 
        talk(f"Searching Wikipedia for {search_term}")
        print(info)
        talk(info)

    elif 'enough' in command:
        talk(f"Okay, see you later {MASTER}")
        break
        
    else:
        talk("I'm not sure I understand. Please try another command.")
