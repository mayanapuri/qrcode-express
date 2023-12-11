import pyqrcode
from PIL import Image as PILImage
from PIL import ImageTk
from tkinter import *
import time

root = Tk()
photo = None  

def show():
    global photo  # Use the global photo variable
    qr_code = pyqrcode.create(entry.get())
    filename = filename_entry.get()
    qr_code.png(f'{filename}.png', scale=6)

    time.sleep(1)  

    image = PILImage.open(f"{filename}.png")
    photo = ImageTk.PhotoImage(image)

    label2 = Label(root, image=photo, borderwidth=3, relief=SUNKEN)
    label2.image = photo
    label2.grid(row=3, column=0)

root.geometry("500x400")

label1 = Label(root, text="Enter text to generate QR code")
label1.grid(row=0, column=0)

entry_value = StringVar()
entry = Entry(root, textvariable=entry_value)
entry.grid(row=0, column=1)

filename_label = Label(root, text="Enter filename for the QR code")
filename_label.grid(row=1, column=0)

button = Button(root, text="Generate QR Code", command=show)
button.grid(row=2, column=1)

filename_value = StringVar()
filename_entry = Entry(root, textvariable=filename_value)
filename_entry.grid(row=1, column=1)

root.mainloop()
