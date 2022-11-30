import time
import vrchatapi
from vrchatapi.api import system_api
from pprint import pprint
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

with vrchatapi.ApiClient() as api_client:

    api_instance = system_api.SystemApi(api_client)



window = tk.Tk()
window.title('VRChat Population')
window.configure(bg='#555555')
window_width = 400
window_height = 200
window.resizable(0,0)

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

try:
    api_response = api_instance.get_current_online_users()
    pprint(api_response)
except vrchatapi.ApiException as e:
    print("Exception when calling SystemApi->get_current_online_users: %s\n" % e)

label = tk.Label(window, text = "Players Currently Online:", font = ('Arial', 20))
label.configure(bg = '#555555')
label.pack()
label2 = tk.Label(window, text = api_response, font=('Arial', 50))
label2.configure(bg = '#555555')
label2.pack(pady=25)
def task():
    try:
        api_response = api_instance.get_current_online_users()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_current_online_users: %s\n" % e)

    label2.config(text = api_response)
    window.after(60000, task)  # reschedule event in 60 seconds

window.after(60000, task)

window.mainloop()





