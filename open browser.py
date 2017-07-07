import webbrowser
import time

times = 1

print("This program started on "+ time.ctime())
while times <= 1: #everything is below this line is inside the loop
    time.sleep(10) #delay is always in seconds
    webbrowser.open("https://www.google.com")
    times = times + 1
