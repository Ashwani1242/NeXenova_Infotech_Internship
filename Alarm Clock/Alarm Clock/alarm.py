import datetime
from playsound import playsound

alarmHour = int (input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))

if alarmHour > 24 or alarmHour < 0 :
    raise ValueError ("Invalid hour value!")
if alarmMin > 60 or alarmMin < 0 :
    raise ValueError ("Invalid minute value!")

while True:
        
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..")
        playsound("alarm.wav")
        break