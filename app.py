import pyautogui
import time
import schedule
import calendar
import sys, os
import pyfiglet
from telnetlib import DO
from handler import *
from datetime import date, datetime

"""
Code written by Brendyn Mullikin in Python 3.10

Hey folks, thanks for checking out my script! This is one of my first projects I've done on my own with python and coding in general.
Feel free to remove the banner and all the print statements. 
I used them to help me debug along the way, but the program should probably be ran in the background, so the print statements won't matter anyways. 
Please let me know how well it works for you! Feel free to send a pull request, or email me if you have any suggestions or ideas for elements that can be improved! 

Make sure to look at the README for usage and dependencies. 

NOTE: This can be heavily, heavily simplified to use zoom meeting links. I just used this way because I wanted a little more challenge (Honestly, I just couldn't find the links for the meetings I'm in). Feel free to use elements from here if you're going that route.
"""

# Defining global variable for screen size
SIZE = pyautogui.size()

# Initially used JOIN and CONNECT to find location of needed buttons, but I wanted to leave my math in here to make people think I'm smart
# Note that locating the buttons will be more accurate, but this is an alternative way of doing it that does seem to work

#JOIN = ((SIZE[0] // 2) - 150, (SIZE[1] // 2) - 180 + 90)
#CONNECT = ((((SIZE[0] // 3) // 2) + SIZE[0] // 3), (((SIZE[1] // 3) // 2) + (SIZE[1] // 3 + 110)))

# ASCII banner art using pyfiglet
def title_banner():
    os.system('cls')
    banner = pyfiglet.figlet_format('AutoZoom!')
    print(banner)

    print('=' * 52)
    print('|' + ' ' * 50 + '|')
    print('|  ' + '* Written by Brendyn Mullikin in Python 3.10 *' + '  |')
    print('|' + ' ' * 50 + '|')
    print('| ' + ' * AutoZoom automates the joining of your zoom' + '   |')
    print('|     ' + 'classes/meetings. Never be late again! *' + '     |')
    print('|' + ' ' * 50 + '|')
    print('=' * 52)

# Function to get the current day of the week and the time formatted to hour, minute
def check_date_time():
    day = (calendar.day_name[date.today().weekday()])
    time = datetime.now()
    curr_time = time.strftime("%H:%M")

    print(f"Opening meeting for {day} at {curr_time}...\n")
    ids = get_ID(day, time)
    return ids

# Getting the meeting ID and password based on the current day and time to be entered when we join the meeting
def get_ID(DOW, time):
    # **** CHANGE THESE ****
    if DOW == 'Monday' and time == '4:30':
        ids = test_meeting()
        return ids
    
    if DOW == 'Tuesday' and time == '6:00':
        ids = test_meeting1()
        return ids
    
    if DOW == 'Wednesday' and time == '4:30':
        ids = test_meeting()
        return ids
    
    if DOW == 'Thursday' and time == '4:30':
        ids = test_meeting1()
        return ids

    # Just set the else statement to run through the script anyways for testing purposes, could throw some sort of exit function here if you'd like. Schedule also has a job cancel function that could work here
    else:
        print("Unable to locate meeting for current date and time. Defaulting to test meeting ID and Password...\n")
        ids = test_meeting()
        return ids

# Tries to open zoom based on argv[1] (path to zoom.exe)
def open_zoom():
    path = str(sys.argv[1])

    run = os.system("start " + path)
    if run == 0:
        print("Successfull")
        pass
    else:
        print("FAILED")
        sys.exit()

    time.sleep(3)
    join_meeting()


def join_meeting():
    # Checking whether the initial screen that pops up on launch is for a logged in user or an un-logged in user
    login = check_login()
    if login:
        # Using locateOnScreen function to find position of buttons
        print("Joining meeting from authenticated session...\n")
        join_plus = pyautogui.locateOnScreen('assets/join2.png')
        join_plus_center = pyautogui.center(join_plus)
        pyautogui.click(join_plus_center)
        time.sleep(1)
    # Make sure to change these sleep calls if necessary, based on connection speed, hardware, etc. It will skip numbers if next prompt isn't fully loaded
    else:
        print("Joining meeting from unauthenticated session...\n")
        join_plus = pyautogui.locateOnScreen('assets/join1.png')
        join_plus_center = pyautogui.center(join_plus)
        pyautogui.click(join_plus_center)
        time.sleep(1)

    # Calling to function that gets our meeting id and passwords based on date and time
    ids = check_date_time()

    # Entering first value of 'ids' tuple which is our meeting ID
    pyautogui.typewrite(ids[0], interval=0.1)
    time.sleep(1)
    enter_id = pyautogui.locateOnScreen('assets/join3.png')
    enter_id_center = pyautogui.center(enter_id)
    pyautogui.click(enter_id_center)
    time.sleep(2)

    # Confirming that the ID is correct by checking for the 'invalid id' messagebox
    confirm_id = confirm_valid_id()
    if confirm_id:
        print("Meeting ID confirmed...")
        pass
    else:
        print("Meeting ID invalid or incorrect... Exiting program")
        ok = pyautogui.locateOnScreen('assets/ok_btn.png')
        pyautogui.click(ok)
        time.sleep(1)
        close = pyautogui.locateOnScreen('assets/close_zoom.png')
        pyautogui.click(close)
        time.sleep(1)
        sys.exit()

    # Entering second value of tuple which is our meeting password
    pyautogui.typewrite(ids[1], interval=0.1)
    time.sleep(1)
    enter_pw = pyautogui.locateOnScreen('assets/join4.png')
    enter_pw_center = pyautogui.center(enter_pw)
    pyautogui.click(enter_pw_center)
    time.sleep(1)

    # Checking validity of password
    confirm_passwd = confirm_valid_passwd()
    if confirm_passwd:
        print("Password is valid...")
        pass
    else:
        print("Meeting password incorrect... Exiting program")
        cancel = pyautogui.locateOnScreen('assets/cancel.png')
        pyautogui.click(cancel)
        time.sleep(1)
        exit = pyautogui.locateOnScreen('assets/close_zoom.png')
        pyautogui.click(exit)
        time.sleep(1)
        sys.exit()

    print("Joined Meeting Successfully!\n")


# Main function that calls to each element of the script
def main():
    while True:
        if len(sys.argv) != 2:
            print("Usage: python app.py <PATH_TO_ZOOM.EXE>")
            sys.exit()
        else:
            break

    # Making sure we have the failsafe on so we can exit the program if we need to by dragging cursor to top-left corner of the screen
    pyautogui.FAILSAFE = True

    # Printing our terminal banner and title art
    title_banner()

    # **** CHANGE THESE ****
    # Using schedule to define on what days and times to join meetings
    schedule.every().monday.at("16:30").do(open_zoom)
    schedule.every().tuesday.at("18:00").do(open_zoom)
    schedule.every().wednesday.at("16:30").do(open_zoom)
    schedule.every().thursday.at("16:30").do(open_zoom)
    schedule.every().thursday.at("18:00").do(open_zoom)

    # For testing, remove when fully using program
    schedule.every().friday.at("12:56").do(open_zoom)
    
    # This calls to execute the scheduled task when scheduled date and time values are TRUE
    print('''
        ==================================
       | Waiting for scheduled meeting... |
        ==================================
    ''')
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()