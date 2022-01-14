import pyautogui
import pymsgbox
import time

'''
This file is mostly for holding the information for the zoom meeting IDs and passwords.
Make sure to edit them so they work for your meetings!

I also added some handler functions at the bottom to check for the state of app on launch.
Happy Zooming...
'''
# **** CHANGE THESE ****
def test_meeting():
    id, pw = '123456789', '123456'
    return id, pw

def test_meeting1():
    id, pw = '987654321', '987654'
    return id, pw

# Function that will wait until the user has logged in successfully before continuing with joining a meeting
def wait_for_login():
    while True:
        wait = pyautogui.locateOnScreen('assets/join2.png')
        if not wait:
            # Change this if you want it to check at a shorter interval
            time.sleep(5)
            print("Waiting for successfull login...\n")
            continue
        else:
            break
    return

# Function that determines the state of the app on startup based on the presence of a button
# Change this if your app format is different or you want to check for a different element of the page
def check_login():
    login = pyautogui.locateOnScreen('assets/sign-in.png')
    if login:
        # Popup that asks if the user would like to login. I set the timeout to 50 seconds, considering that some will be using this to join class without actualy having to be there...
        # Edit the timeout or remove the check if you need it to join the meeting quicker
        confirm = pymsgbox.confirm(text='Would you like to login before this meeting?', title='Login option', buttons=['Yes', 'No'], timeout=50000)
        if confirm == 'Yes':
            wait_for_login()
            return True
        else:
            return False
    else:
        return True

# Check for 'invalid ID' error message and exit if True
def confirm_valid_id():
    invalid = pyautogui.locateOnScreen('assets/invalid_id.png')
    if invalid:
        pymsgbox.alert(text="The given ID for the scheduled meeting is invalid. Please fix before next run time.", title="ID Invalid", button=pymsgbox.OK_TEXT, timeout=10000)
        return False
    else:
        return True

# Check for 'invalid password' error message and exit if True
def confirm_valid_passwd():
    invalid = pyautogui.locateOnScreen('assets/incorrect_passwd.png')
    if invalid:
        pymsgbox.alert(text="Password given for this meeting is incorrect. Please fix before next run time.", title="Password Invalid", button=pymsgbox.OK_TEXT, timeout=10000)
        return False
    else:
        return True

