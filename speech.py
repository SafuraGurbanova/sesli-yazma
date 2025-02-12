import speech_recognition

def turkce():
    microphone = speech_recognition.Microphone()
    kayit = speech_recognition.Recognizer()
    with microphone as ses:
        kayit.adjust_for_ambient_noise(ses)
        al  = kayit.listen(ses)
        try:
            return kayit.recognize_google(al,language="tr-TR")
        except:
            return "ne dedigini anlamadim"
def eng():
    microphone = speech_recognition.Microphone()
    kayit = speech_recognition.Recognizer()
    with microphone as ses:
        kayit.adjust_for_ambient_noise(ses)
        al  = kayit.listen(ses)
        return kayit.recognize_google(al,language="eng-US")

print("konusabilirsiniz dinleme baslamistir.")
saf = turkce()
print(saf)
