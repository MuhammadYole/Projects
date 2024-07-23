
# #MUHAMMAD HARUNA YOLE
# SPEECH INPUT LANGUAGE TRANSLATOR
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

#  To initialize the speech recognition
r = sr.Recognizer()

# Initializing the Translator from googletrans library
translator = Translator()

# Initializing the pyttsx3 library
engine = pyttsx3.init()

while True:


    # user input speech/text
    options = input("Do you want to type or speak \nPress 'S' to speak \npress 'T' to type \n")

    if options.upper() == "S":
        # Function to translate speech

        def translate_speech():
            with sr.Microphone() as source:
                print("Speak something:")
                audio = r.listen(source)

                try:
                    # Function to recognize speech using Google Speech Recognition
                    text = r.recognize_google(audio)
                    print("You said: ", text)

                    print("LANGUAGE MENU")
                    print("1-FRANCE \n2-ITALY \n3-ARABIC \n4-RUSSIAN \n5-HAUSA, \n6-Yoruba, \n7-Igbo")
                    # Function to translate speech to each target language using for loop
                    language_choice = input("Enter the number corresponding to your choice: ")
                    if language_choice == "1":
                        translated_text = translator.translate(text, src='auto', dest='fr')
                        print(f"Translated to France: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "2":
                        translated_text = translator.translate(text, src='auto', dest='it')
                        print(f"Translated to Italy: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "3":
                        translated_text = translator.translate(text, src='auto', dest='ar')
                        print(f"Translated to Arabic: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "4":
                        translated_text = translator.translate(text, src='auto', dest='ru')
                        print(f"Translated to Russian: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "5":
                        translated_text = translator.translate(text, src='auto', dest='ha')
                        print(f"Translated to Hausa: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "6":
                        translated_text = translator.translate(text, src='auto', dest='yo')
                        print(f"Translated to Yoruba: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    elif language_choice == "7":
                        translated_text = translator.translate(text, src='auto', dest='ig')
                        print(f"Translated to Igbo: {translated_text.text}")
                        engine.say(translated_text.pronunciation)
                        engine.runAndWait()

                    else:
                        print("Entered Unknown Value.. \nPlease restart the process.")

                # function if speech isn't recognised
                except sr.UnknownValueError:
                    print("Couldn't not understand audio \nPlease be audible")
                # function if there's network issue
                except sr.RequestError as e:
                    print(f"Please, Ensure you're connected to a network server: {e}")
                # Other Errors
                except Exception as e:
                    print("Error:", e)


        # Function to call translate speech
        translate_speech()

    elif options.upper() == "T":
        print("LANGUAGE MENU")
        print("1-FRANCE \n2-ITALY \n3-ARABIC \n4-RUSSIAN \n5-HAUSA, \n6-Yoruba, \n7-Igbo")
        text = input("what do you want to translate?")
        try:

            language_choice = input("Enter the number corresponding to your choice: ")
            if language_choice == "1":
                translated_text = translator.translate(text, src='auto', dest='fr')
                print(f"Translated to France: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "2":
                translated_text = translator.translate(text, src='auto', dest='it')
                print(f"Translated to Italy: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "3":
                translated_text = translator.translate(text, src='auto', dest='ar')
                print(f"Translated to Arabic: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "4":
                translated_text = translator.translate(text, src='auto', dest='ru')
                print(f"Translated to Russian: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "5":
                translated_text = translator.translate(text, src='auto', dest='ha')
                print(f"Translated to Hausa: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "6":
                translated_text = translator.translate(text, src='auto', dest='yo')
                print(f"Translated to Yoruba: {translated_text.text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            elif language_choice == "7":
                translated_text = translator.translate(text, src='auto', dest='ig')
                print(f"Translated to Igbo: {translated_text}")
                engine.say(translated_text.pronunciation)
                engine.runAndWait()

            else:
                print("Entered Unknown Value.. \nPlease restart the process.")



        except sr.UnknownValueError:
            print("Type correctly")

        except sr.RequestError as e:
            print(f"Please, Ensure you're connected to a network server: {e}")

        except Exception as e:
            print("Error:", e)

    else:
        print("ENTERED WRONG VALUE")


