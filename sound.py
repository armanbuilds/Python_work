import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)    #this checks the speed the ideal is 200 and volume is 0.0 to 1.0
engine.setProperty('volume', 1.0)
engine.say("Hey, Armaan, you are the boss.")
engine.runAndWait()