import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.say("Olá Mundo, tudo bem?")
engine.runAndWait()