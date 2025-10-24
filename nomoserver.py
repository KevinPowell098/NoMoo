from flask import Flask, request
import utils.nomovolume as nomovolume
import utils.nomospeak as nomospeak
import time

app = Flask(__name__)

time_since = {}
TIMEBETWEEN = 30


def elapsed(data):
    if data in time_since:
        last = time_since[data]
        current = time.monotonic()
        if((current - last) < TIMEBETWEEN):
            print("Not been long enough")
        else:
            time_since[data] = current
        return (current - last) > TIMEBETWEEN
    else:
        time_since[data] = time.monotonic()
        return True


def processdata(data):
    with open('testing.txt', 'a') as file:
        file.write(f"{data}\n")
    if elapsed(data):
        if data == "tomoo":
            print(f"Lowering Volume")
            nomospeak.speak("Officer On Deck", 250)
            volume = nomovolume.change_volume(.2)
        elif data == "kevin":
            print("Acknowledging Kevin")
            nomospeak.speak("Hello there Kevin", 250)
        elif data == "jackson":
            print("Acknowledging Jackson")
            nomospeak.speak("Hey Jackson", 150)
        elif data == "enoch":
            print("Acknowledging Enoch")
            volume = nomovolume.change_volume(.2)
        elif data == "tate":
            print("Acknowledging Tate")
            nomospeak.speak("Hey there Tate", 150)
        elif data == "anna":
            print("Acknowledging Anna")
            nomospeak.speak("Hey Anna! You are cute", 150)
        elif data == "button":
            print("fixing volume")
            volume = nomovolume.change_volume(1)
    

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.data.decode('utf-8')
    if not data:
        return "Invalid or missing data", 400
    print("Received data:", data)
    processdata(data)
    return 'Data received', 200

if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible on your local network
    app.run(host='0.0.0.0', port=5000)