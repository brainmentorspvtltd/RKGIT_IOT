from datetime import datetime as dt

chat = True
greetIntent = ["hi","hello","hey","hello there","hi there"]
dateIntent = ["date","tell me date","please tell me date"]
timeIntent = ["time","tell me time","please tell me time"]

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :",date.strftime("%d %B, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is :",time.strftime("%H:%M:%S, %p"))
    elif msg == "bye":
        print("Bye User...")
        chat = False
    else:
        print("I don't understand")
