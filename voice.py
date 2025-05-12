import pyttsx3 as pyt
eng = pyt.init()

voices = eng.getProperty('voices')
rate = eng.getProperty('rate')
eng.setProperty('rate',140)
eng.setProperty('voice', voices[1].id)
a=input("Enter your name: ")
msg=f"Teri gand marlunga  {a}"
eng.say(msg)
eng.runAndWait()
