from gingerit.gingerit import GingerIt
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python.
from spellchecker import SpellChecker  # for checking spelling errors
# convert the spoken words into text, make a query or give a reply
import speech_recognition as sr
import language_tool_python
import datetime
import wikipedia  # pipinstall wikipedia
import webbrowser
import os  # interaction b/w system and user
import requests
#from bs4 import BeautifulSoup


# The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # to get details of current voice
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    # command for speech or voice, This function will make the speech audible in the system
    engine.runAndWait()
def correct_grammar(paragraph):
    # Create a GingerIt instance
    parser = GingerIt()

    # Parse the paragraph and get the result
    result = parser.parse(paragraph)

    # Get the corrected text
    corrected_paragraph = result['result']

    return corrected_paragraph

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("GOOD MORNING!")

    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON!")

    else:
        speak("GOOD EVENING!")

    speak("I am Tanya sir. and I am your AI desktop assistant. Please tell how may i help you")

def check_grammar(sentence):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(sentence)
    mistakes = len(matches)
    
    if mistakes == 0:
        print("No grammar mistakes found.")
    else:
        print(f"{mistakes} grammar mistake(s) found:")
        for match in matches:
            print(f"Mistake: {match.message}")
            print(f"Suggested correction: {match.replacements}\n")


def takeCommand():
    # takes input from the user and returns the output in string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # in secs
        audio = r.listen(source)

    try:  # in case of any error
        print("Recognizing...")
        # for using google in voice regonition.
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        # if you have improper voice it will print this
        print("Say that again please...")
        return "None"   # string called none will be returned
    return query

def spell_check(text):
    spell = SpellChecker()      #creating the object of spellchecker class
    # Split the text into words
    words = text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Correct misspelled words
    corrected_text = []
    for word in words:
        if word in misspelled:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)

    # Join the corrected words back into a sentence
    corrected_text = ' '.join(corrected_text)

    return corrected_text


# to allow or prevent parts of code from being run when the modules are imported.
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

# logic for executing commands based on query

    # defining command 1 to search something from wikipedia
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            # replacing wikipedia in query
            # query = query.replace("wikipedia","")
            # for returning 2 sentences from wikipedia
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "how are you" in query:
            speak("I am very good sir!!, Hope you are good too.")

        elif "hi" in query:
            speak("hi sir!! , how may I help you?")

        elif "hello" in query:
            speak("hello sir!! , how may I help you?")
        elif "who are you" in query:
            speak("hello sir, ny names is tanya and i am your voice desktop assistant.")

    # command 2 to open youtube in web browser(internet)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    # command 3 to open google site in a web browser
        elif 'open google' in query:
            webbrowser.open("google.com")

    # command 4 to play music
        elif 'play music' in query:
            music_dir = "C:\\Users\\Tanya Tiwari\\Desktop\\musicc\\favourite"
            # used to get the list of all files and directories in the specified directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

    # command 5 to know the current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\SOFTWARES\\visual studio\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open google' in query:
            webbrowser.open("http://www.google.com")
#FOR CHECKING SPELLING MISTAKES
        elif "check spelling voice" in query:
            speak("Sure, please say the text you want to spell check.")
            text = takeCommand()
            corrected_text = spell_check(text)
            print("Corrected text:", corrected_text)
            speak("The corrected text is: " + corrected_text)

        elif "check spelling" in query:
            speak("Sure, please enter the text you want to spell check.")
            ttext = str(input("enter text"))
            ctext = spell_check(ttext)
            print("correct text: ",ctext)
        
        elif 'check grammar' in query:
            speak("Sure, please enter the text you want to grammar check.")
            senten = takeCommand()
            senten = spell_check(senten)
            corrected_text = correct_grammar(senten)
            print(corrected_text)
        elif 'exit' in query:
            speak("exiting....")
            break
