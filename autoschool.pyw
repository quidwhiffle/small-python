import webbrowser
import schedule
import time
import clipboard
import datetime
import math
import PySimpleGUI as sg 

def mathclass():
    webbrowser.open_new_tab("https://zoom.us/j/98705093283?pwd=THZVUzNFNjlTMTFSQm1VVmF5ZWZmZz09&uname=Jada Dixon#success")
def econclass():
    webbrowser.open_new_tab("https://zoom.us/j/99951037521?pwd=R2F0QVJwdlVXbFpweXVOYytSalMrQT09&uname=Jada Dixon")
def clclass():
    webbrowser.open_new_tab("https://zoom.us/j/99496069617?pwd=UXRIZzh4RlUrOFduZnk5Wm5XTFJWdz09&uname=Jada Dixon")
def spanclass():
    webbrowser.open_new_tab("https://zoom.us/j/93233323862?pwd=R3BlK042K0tMK1NGaWxTazdFL1lCUT09&uname=Jada Dixon")
def physclass():
    webbrowser.open_new_tab("https://zoom.us/j/95822672190?pwd=NjJGM2lWZGI3aTNDS0pBelpFRUx4UT09&uname=Jada Dixon")
def chemclass():
    webbrowser.open_new_tab("https://zoom.us/j/99306326136?pwd=VW1vZXVJZ0crT0ViSGR4ZUtvUGVrdz09&uname=Jada Dixon#success")
def itclass():
    webbrowser.open_new_tab("https://zoom.us/j/96930767687?uname=Jada Dixon#success")
def pdclass():
    webbrowser.open_new_tab("https://zoom.us/j/91427298272?pwd=Lzl6ZDliR2trYW5ZU0lTM2E0a1ZVdz09&uname=Jada Dixon#success")
def engclass():
    webbrowser.open_new_tab("https://zoom.us/j/99837612071?pwd=VFZNSTZXdXBkMXRxMmxWT1B0aHM1Zz09&uname=Jada Dixon")
def addmathclass():
    webbrowser.open_new_tab("https://zoom.us/j/94458157122?pwd=RDNONkNZazVxcS84dy9IVlk3aUtqQT09&uname=Jada Dixon#success")

def demClub():
    webbrowser.open_new_tab("https://zoom.us/j/5826894117#success")
def cfya():
    webbrowser.open_new_tab("https://zoom.us/j/99584273671?pwd=WisyTmp5M2pPcnEySUtvNHJ4RGxGUT09")

def spanPrac():
    webbrowser.open_new_tab("https://zoom.us/j/91346741102?pwd=RkpTeWpGRlcvSzRDTGlCalpvZmlBQT09")

def send_meeting():
    clipboard.copy("https://zoom.us/j/91346741102?pwd=RkpTeWpGRlcvSzRDTGlCalpvZmlBQT09 \n Here's the link guys.")


def update_status():
    today = datetime.datetime.now()
    csec = datetime.datetime(2021,6,14)
    freedom = datetime.datetime(2021, 7, 14)

    p = csec-today
    pain =math.ceil(p.total_seconds()/86400) 
    f = freedom-today
    free =math.ceil(f.total_seconds()/86400) 

    clipboard.copy(f"{pain} days till pain; {free} days till freedom.")
    print(f"{pain} days till pain; {free} days till freedom.")

def consolidate_songs():
    sg.popup('consolidate songs!')







# update_status()
    


schedule.every().monday.at("08:00").do(spanclass)
schedule.every().tuesday.at("08:00").do(spanclass)
#schedule.every().wednesday.at("08:00").do(spanclass)
schedule.every().thursday.at("08:00").do(mathclass)
schedule.every().friday.at("08:00").do(engclass)

schedule.every().monday.at('08:35').do(engclass)



schedule.every().monday.at("09:45").do(physclass)
schedule.every().tuesday.at("09:45").do(itclass)
schedule.every().wednesday.at("09:45").do(econclass)
schedule.every().thursday.at("09:45").do(econclass)
schedule.every().friday.at("09:45").do(chemclass)



schedule.every().wednesday.at("10:20").do(physclass)




schedule.every().monday.at("10:55").do(clclass)
schedule.every().tuesday.at("10:55").do(engclass)
schedule.every().wednesday.at("10:55").do(mathclass)
schedule.every().thursday.at("10:55").do(engclass)
schedule.every().friday.at("10:55").do(spanclass)



schedule.every().monday.at("12:05").do(chemclass)
schedule.every().tuesday.at("12:05").do(econclass)
schedule.every().wednesday.at("12:05").do(chemclass)
schedule.every().thursday.at("12:05").do(physclass)





schedule.every().monday.at("12:40").do(itclass)
schedule.every().tuesday.at("12:40").do(physclass)
#schedule.every().wednesday.at("12:40").do(class)
schedule.every().thursday.at("12:40").do(itclass)
schedule.every().friday.at("12:40").do(econclass)




schedule.every().monday.at("13:15").do(mathclass)


schedule.every().wednesday.at("13:15").do(engclass)
schedule.every().thursday.at("13:15").do(spanclass)
schedule.every().friday.at("13:15").do(mathclass)

schedule.every().monday.at("13:50").do(addmathclass)
schedule.every().wednesday.at("13:50").do(addmathclass)

schedule.every().friday.at("14:25").do(addmathclass)
schedule.every().thursday.at("14:25").do(send_meeting)
schedule.every().thursday.at("14:30").do(spanPrac)


schedule.every().tuesday.at("15:15").do(demClub)
schedule.every().wednesday.at("15:25").do(cfya)

# schedule.every().day.at("08:35").do(update_status)
schedule.every().friday.at("23:45").do(consolidate_songs)

send_meeting()

while True:
    schedule.run_pending()
    time.sleep(1)