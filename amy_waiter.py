import speech_recognition as sr
import pyttsx3
import requests

SERVER_IP = "http://127.0.0.1:8000"   # change later for laptop-2
TABLE_NO = 1

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

menu = {
    "coffee": 80,
    "cold coffee": 120,
    "sandwich": 150,
    "veg sandwich": 150,
    "burger": 180
}

current_order = []

def speak(text):
    print("Amy:", text)
    engine.say(text)
    engine.runAndWait()

def send(data):
    requests.post(SERVER_IP + "/send", json=data)

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

print("Amy is running...")
speak("Amy is ready.")

while True:

    text = listen()

    if "amy" not in text:
        continue

    speak("Yes, what would you like?")

    command = listen()
    print("Heard:", command)

    # SERVICE REQUEST
    if any(w in command for w in ["water", "spoon", "napkin", "tissue"]):
        send({
            "type": "service",
            "table": TABLE_NO,
            "message": command
        })
        speak("I have informed the staff.")
        continue

    # BILL REQUEST
    if any(w in command for w in ["bill", "check", "total"]):
        total = sum(item["price"] for item in current_order)

        speak(f"Your bill is rupees {total}")

        send({
            "type": "bill",
            "table": TABLE_NO,
            "amount": total
        })

        speak("How was your experience today from one to five?")

        rating = listen()

        send({
            "type": "feedback",
            "table": TABLE_NO,
            "rating": rating
        })

        speak("Thank you for your feedback.")
        continue

    # FOOD ORDER
    items = []

    for item in menu:
        if item in command:
            items.append(item)

    if items:
        for it in items:
            current_order.append({"name": it, "price": menu[it]})

        send({
            "type": "order",
            "table": TABLE_NO,
            "items": items
        })

        speak("Added to your order.")
    else:
        speak("Sorry, I did not understand that.")
