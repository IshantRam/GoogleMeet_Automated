import pyautogui
import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
c = simpledialog.askstring(title="GoogleMeet Automation",
                           prompt="Enter Meetingcode(Last 10 word of meeting link):")
print(" Your Meeting Code is",c)
if c == '':
    print(" Your Meeting Code is blank")

    def alert_popup(title, message, path):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)

        w = 400     # popup window width
        h = 200     # popup window height

        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        m = message
        m += '\n'
        m += path
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()
    alert_popup("GoogleMeet Automation",
                "Please Entere Something", "Or Program Will Not execute")

ROOT = tk.Tk()

ROOT.withdraw()
d = simpledialog.askstring(title="GoogleMeet Automation",
                           prompt="Enter your attendence/Message u wana put in chatbox after just getting in the meeting:")
print("Get Ready to attende your Class/Meeting")

if d == '':
    print("You are not able to attende the class if u don't enter any Thing")

    def alert_popup(title, message, path):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)

        w = 400     # popup window width
        h = 200     # popup window height

        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        m = message
        m += '\n'
        m += path
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()

    alert_popup("GoogleMeet Automation",
                "Please Entere Something", "Or Program Will Not execute")


def sign_in(meetingcode, Attendence):
    # Opening Google Meet
    webbrowser.open("https://meet.google.com/")
    time.sleep(15)

    # Clicking on the meeting-code buton
    pyautogui.click(312, 524, button='left')

    time.sleep(2)

    # Entering meeting code
    pyautogui.write(meetingcode)
    time.sleep(2)

    # Clicking On Join Button
    pyautogui.press("enter")
    time.sleep(30)

    # Turning off Mic and Camera
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(30)

    # Joining The Meeting
    pyautogui.click(983, 440, button='left')
    pyautogui.click(1055, 420, button='left')
    time.sleep(10)

    # Giving Attendence
    pyautogui.click(1153, 94, button='left')
    time.sleep(2)
    pyautogui.write(Attendence)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(1331, 101, button='left')


sign_in(c, d)

ROOT = tk.Tk()

ROOT.withdraw()
wm = simpledialog.askstring(title="GoogleMeet Automation",
                            prompt="This Program Is Made By Ishant Ram")
