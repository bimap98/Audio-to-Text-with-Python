import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("Jae.mp3") as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Working")
        print(text)
    except:
        print("Sorry")
