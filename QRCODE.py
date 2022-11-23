'''
QR Code Generator 

'''


from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

window = Tk()
window.title("QR Code Generator")
window.geometry("750x600")


def code_entry():
    # file Dialog
    input_path = filedialog.asksaveasfilename(
        title="Save Image", filetypes=(("PNG File", ".png"), ("All Files", "*.*"))
    )
    if input_path:
        if input_path.endswith(".png"):
            get_code = pyqrcode.create(display.get())
            # save as PNG File
            get_code.png(input_path, scale=6)
        else:
            input_path = f"{input_path}.png"
            get_code = pyqrcode.create(display.get())
            get_code.png(input_path, scale=6)

        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        my_label.config(image=get_image)

        display.delete(0, END)
        display.insert(0, ">>>>>Done!<<<<<")


def clear_all():
    display.delete(0, END)
    display.config(image="")


display = Entry(window, font=("Arial", 18))
display.pack(pady=20)

btn = Button(window, text="Create QR code", command=code_entry)
btn.pack(pady=20)

btn2 = Button(window, text="Clear", command=clear_all)
btn2.pack(pady=20)

my_label = Label(window, text="Display")
my_label.pack(pady=20)

window.mainloop()
