import time


def countdown(n):
    while n: 
        mins, secs = divmod(n, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        n -= 1
    print('Time is up!')

n = input('Enter the time in seconds: ') 

countdown(int(n))