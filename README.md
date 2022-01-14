# AutoZoom

Python script for automatically joining recurring meetings. Uses libraries 'pyautogui' and 'schedule'. Never be late to another class again!

---

### Description

---

AutoZoom is written using **Python 3.10**, using libraries *'pyautogui'* and *'schedule'* for automation. It is designed to run either in a command prompt or in the background, and uses Zoom **Meeting ID's and Passwords** instead of direct links. Version 1.0 schedules a job to run at the time your meeting beings, takes in the **Meeting ID** and **Password** from the *'handler'* file, then opens **Zoom** and joins your meeting for you right on time.

---

### Dependencies

---

To use this program, you'll need to download *pyautogui* and *schedule*. Install these using:

> pip install pyautogui

> pip install schedule

---

### Usage

---

You can have AutoZoom either run in the command prompt, or in the background. To run in the command prompt, open the terminal, navigate to the directory where you stored the files, then run:

> python app.py

To have AutoZoom run in the background, open a terminal and navigate to the directory where the program files are stored, then run:

> pythonw app.py

You can confirm that the file is running in the background by checking **Task Manager**

---

### About The Project and Author

---

Hey guys, thanks for checking out AutoZoom! My name is Brendyn Mullikin and I started coding in late October 2021. I have followed tutorials and written small, useless Python scripts, but this is my first project that I've created on my own. The idea for this project came from having seen other people create this type of project, and I myself was getting tired of constantly entering the Zoom meeting ID and password twice a day. I've been trying to learn more about automation using Python, so I gave it a go. The few projects that I had looked at for ideas, all used meeting links, which kept things really simple. I looked everywhere for the links to my meetings but not a one was found, so I had get a little creative. This led to me writing this little program that solved this issue, but still took the annoyance of redundancy out of the picture.

Please feel free to shoot me any suggestions or ideas you may have, I am still new to this and could use all the help I can get. You can send a pull request if you'd like or send me an email. I hope you can find some use for this script, and I appreciate you checking it out! 

