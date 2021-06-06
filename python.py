import pyautogui
import tkinter
from tkinter import *
import tkinter as tk
import keyboard
from tkinter import filedialog
from PIL import Image, ImageTk



root = Tk()
root.title("Make Screenshoot by GlaW1n")
root.geometry("400x400")
root.resizable(False, False)
root.iconbitmap("icon.ico")
root.configure(bg="#f5f5f5")

def makeScreenshoot():
    locate_screen = filedialog.asksaveasfilename(defaultextension='.png')
    if (locate_screen != ""):
        screen = pyautogui.screenshot(locate_screen)
    

keyboard.add_hotkey('CTRL + L', makeScreenshoot)


canvas = tkinter.Canvas(root, height=95, width=95)
image = Image.open("fav.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(50, 50, image=photo)
canvas.pack(side=TOP, pady=20)

textRes = Label(root, text="Разрешение экрана:" + str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()), font=("Arial", 16), bg="#f5f5f5")
textRes.pack(side=TOP)

textHotKey = Label(root, text="Горячия клавиша: CTRL + L", font=("Arial", 16), bg="#f5f5f5")
textHotKey.pack(side=TOP)

makeScreenButton = Button(root, text="Сделать скриншот", font=("Arial", 16), bg="#ffffff", fg="#000000", border=0, command=makeScreenshoot)
makeScreenButton.place(x=0, y=350, width=400, height=50)




root.mainloop()


    