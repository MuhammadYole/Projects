


# #MUHAMMAD HARUNA YOLE
# #SPEECH INPUT LANGUAGE TRANSLATOR
import speech_recognition as sr
from googletrans import Translator

#  To initialize the speech recognition
r = sr.Recognizer()

# Initialize translator
translator = Translator()

# Defining the target languages
languages = ['fr','it', 'ar', 'ru']

# Function to translate speech

def translate_speech():
    with sr.Microphone() as source:
        print("Speak something:")
        audio = r.listen(source)

        try:
        # Function to recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            print("You said: ", text)

        # Function to translate speech to each target language
            for lang in languages:
                translated_text = translator.translate(text, src='auto', dest=lang)
                print(f"Translated to {lang}: {translated_text.text}")
        # function if speech isn't recognised
        except sr.UnknownValueError:
            print("Couldn't not understand audio \nPlease be audible")
        # function if there's network issue
        except sr.RequestError as e:
            print(f"Please, Ensure you're connected to a network server: {e}")
        #Other Errors
        except Exception as e:
            print("Error:", e)

# Function to call translate speech
translate_speech()




