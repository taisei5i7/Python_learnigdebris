from datetime import datetime
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

time_now = datetime.today()
right_this_minute = time_now.minute

for num in range(5):
    print(right_this_minute)

if right_this_minute in odds:
    print ("Index of minute is uneven number.")
else:
    print ("Index of minute is not uneven number.")
    
from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for num in range(6):
    print(right_this_minute)

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("Hello World")
    else:
        print("Good Night World")

    time.sleep(10)



