import time
show=(time.strftime("%y"))
hour=(time.strftime("%H:%M:%S"))
print(show)
print(hour)
hour=int(input("eneter the hours\n"))
if hour>=0 and hour<=12:
    print("good morning")
elif hour>=12 and hour<=17:
    print("good evening")
elif hour>=17 and hour<=24:
    print("good evening")