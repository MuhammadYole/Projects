# MUHAMMAD HARUNA YOLE
# LANGUAGE TRANSLATOR ADVANCED



# Importing installed python libraries and API (tkinter, pyttsx3, speech recognition and google trans)
import pyttsx3
import speech_recognition as sr
from googletrans import (Translator, LANGUAGES)
import tkinter as tk
from tkinter import ttk


class SpeechTranslatorAdvancedApp:
    # Initializes the application by setting up the main tkinter window (`root`)
    # Initializes speech recognition (`recognizer`), text-to-speech engine (`engine`), and translation engine (`translator`).
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator App Advanced")

        # To initialize the speech recognition
        self.recognizer = sr.Recognizer()

        # To initialize text-to-speech
        self.engine = pyttsx3.init()

        # To initialize translator
        self.translator = Translator()

        #  Calls `self.create_gui()` to create the graphical user interface.
        self.create_gui()


# Creating the app dimensions
    def create_gui(self):
        #Creating input and output Frames
        # Creating and customising the Input frame
        input_frame = ttk.Frame(self.root, padding="100")
        input_frame.grid(row=0, column=0, sticky="nsew")

        # Creating and customising the Input widgets
        input_label = ttk.Label(input_frame, text="Enter Word To Translate")
        input_label.grid(row=0, column=0, sticky="s")

        # Creating and customising the Input String var
        self.input_text = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=self.input_text, width=150)
        input_entry.grid(row=1, column=0, padx=15, pady=20)

        # Creating and customising the Speak button
        speech_button = ttk.Button(input_frame, text="Tap to Speak", command=self.recognize_speech)
        speech_button.grid(row=1, column=1, padx=5, pady=5, sticky = "e")

        # Creating and customising the translate button
        translate_button = ttk.Button(input_frame, text="Tap to Translate", command=self.translate_text)
        translate_button.grid(row=2, column=0, padx=50, pady=5, sticky = "w")

        # Label to display status messages (Listening, Error messages)
        self.status_label = ttk.Label(input_frame, text="")
        self.status_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Creating and customising the Output frame
        output_frame = ttk.Frame(self.root, padding="100")
        output_frame.grid(row=1, column=0, sticky="n", padx=5, pady=0)

        # Creating and customising the Output widgets
        output_label = ttk.Label(output_frame, text="Translated Output:")
        output_label.grid(row=0, column=0, sticky="n")

        # Creating and customising the Output Display
        self.translated_text = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.translated_text, width=150, state="readonly")
        output_entry.grid(row=1, column=0, padx=5, pady=5, sticky = "nsew")

        # Creating and customising the Output language label
        output_language_label = ttk.Label(output_frame, text="Output Languages Menu:")
        output_language_label.grid(row=0, column=1, sticky="n")

        # Get list of language codes and names and editing the combo box
        self.languages = {code: name.capitalize() for code, name in LANGUAGES.items()}
        self.output_language = ttk.Combobox(output_frame, values=list(self.languages.values()), state="readonly")
        self.output_language.set('English')  # Default output language
        self.output_language.grid(row=1, column=1, padx=40, pady=5, sticky = "e")

    def recognize_speech(self):
        # To Display "Listening..." message in the GUI
        self.status_label.config(text="Listening...")
        self.root.update_idletasks()
        # speech recognition
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)


        # Error handling
        try:
            text = self.recognizer.recognize_google(audio)
            self.input_text.set(text)
            self.status_label.config(text="Speech recognized successfully.")
        except sr.UnknownValueError:
            print("Couldn't not understand audio \nPlease be audible")
            self.status_label.config(text="Could not understand the audio. Please try again..")
        except sr.RequestError as e:
            print(f"Please, Ensure you're connected to a network server: {e}")
            self.status_label.config(text=f"Error: {e}. Please, Ensure you're connected to a network server.")
        finally:
            self.root.update_idletasks()

    # Translation function block
    def translate_text(self):
        text = self.input_text.get()
        dest_lang = self.output_language.get()
        translation = self.translator.translate(text, src='auto', dest=dest_lang)
        self.translated_text.set(translation.text)
        self.speak(translation.text)

    # speech output function block
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


# calling functions and classes
root = tk.Tk()
app = SpeechTranslatorAdvancedApp(root)
root.mainloop()









