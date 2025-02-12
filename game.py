from speech import eng
import time
import random
import speech_recognition as sr

seviyeler = {

    "kolay": ["dairy", "mouse", "computer"],

    "orta": ["programming", "algorithm", "developer"],

    "zor": ["neural network", "machine learning", "artificial intelligence"]

}

def dinle():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Lütfen kelimeyi söyleyin...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio, language="en-US")
    except:
        return "Anlaşılamadı"


print("Zorluk seviyesini seçin: kolay, orta, zor")
seviye = input("Seviye: ").strip().lower()

if seviye in seviyeler:
    hedef_kelime = random.choice(seviyeler[seviye])
    print(f"Lütfen şu kelimeyi söyleyin: {hedef_kelime}")

    kullanici_kelime = dinle()

    if kullanici_kelime.lower() == hedef_kelime.lower():
        print("Tebrikler! Doğru söylediniz.")
    else:
        print(f"Yanlış! Siz '{kullanici_kelime}' dediniz, doğrusu '{hedef_kelime}' olmalıydı.")
else:
    print("Geçersiz seviye seçimi!")
