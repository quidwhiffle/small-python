
import time
import PySimpleGUI as sg 
import playsound 
import pyinputplus as pyin 

def seconds(hr,mins):
    sec = (hr*3600) + (mins*60)
    return sec

def countdown(t, mp3):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        try:
            print(timer, end='\r')
            time.sleep(1)
            t-= 1
        except KeyboardInterrupt:
            input('press enter to continue')            
    playsound.playsound(mp3)
    sg.popup("time's up",auto_close=True, auto_close_duration=1,keep_on_top=True )

def pomotimer():

    work = pyin.inputNum('enter the time in seconds you want to work for')
    sbreak =pyin.inputNum('enter the time in seconds you want to be on break for')
    lbreak = pyin.inputNum('enter the time in seconds you want to be on a longer break for')
    times = pyin.inputNum('enter how many times you want to pomodoro for')
    n = pyin.inputNum('enter the amount of short breaks you want to have before a long break')

    
    choice = pyin.inputYesNo('Do you want to change the sound that plays when time is up?')
    if choice== 'yes':
        mp3 = sg.popup_get_file('search for the mp3 you want')
    else:
        mp3 = 'takeabreak.mp3'

    completed = 0
    
    for i in range(1, times):
        if i != 0 and i % (n+1) == 0:
            print('long break!')
            countdown(lbreak,  mp3)
        print(f'Session number {i}')
        print('work')
        countdown(work, mp3)
        print('short break')
        countdown(sbreak, mp3)
        completed +=1

def timer():
    s= pyin.inputYesNo('Do you know the time in seconds you want to exercise for')
    if s == 'yes':
        t = pyin.inputNum('Enter the time in seconds you want the timer to go for')
    else:
      hours = pyin.inputInt('Enter the amount of hours you will be working for')
      mins = pyin.inputInt('Enter the amount of hours you will be working for')
      t = seconds(hours, mins)
        

    choice =pyin.inputYesNo('Do you want to change the default alarm sound for the timer?')
    if choice == 'yes':
        mp3 = sg.popup_get_file('Search for the sound file that you want')
    else:
        mp3 = 'takeabreak.mp3'   
    countdown(t, mp3)
   

def interval_timer():
    times = pyin.inputInt('How many sets do you want to do?')
   
    n = pyin.inputNum('after how many sets do you have to do this thing?')
    work3 = pyin.inputNum('Enter the time you will work for in seconds.') 
   
    work = pyin.inputNum('Enter the time you will work for in seconds.') 
    notwork = pyin.inputNum('Enter the time you will be on break for in seconds.')
    choice =pyin.inputYesNo('Do you want to change the default alarm sound for the timer?')

    if choice == 'yes':
        mp3 = sg.popup_get_file('Search for the sound file that you want')
    else:
        mp3 = 'takeabreak.mp3'
    for i in range(1,times):
        if i % int(n+1) == 0:
            print('break but fin')
            countdown(work3, mp3)
        else:
            print('work')
            countdown(work, mp3)
            print('break')
            countdown(notwork, mp3)




  


timer_choice = pyin.inputMenu(['timer/alarm', 'interval timer', 'pomodoro timer'], prompt='Choose which kind of timer you want \n', numbered=True)
if timer_choice == 'timer/alarm':
    timer()
elif timer_choice == 'interval timer':
    interval_timer()
else:
    pomotimer()




