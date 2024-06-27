import pyttsx3

voice_var = pyttsx3.init()
message = "Hello I am samuel Kwabena"
voice_var.say(message)
voice_var.runAndWait()