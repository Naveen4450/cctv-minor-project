
import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion

window = tk.Tk()#Construct a toplevel Tk widget
window.title(" ")#name provided to the window
window.iconphoto(False, tk.PhotoImage(file='/Users/naveenkumar/Desktop/cctv  /mn.png'))#If default is True, this is applied to all future created toplevels as well.
window.geometry('1080x700')#set the dimensions
frame1 = tk.Frame(window)#container which can be used to hold the other widgets

label_title = tk.Label(frame1, text="Perfect Peep")
label_font = font.Font(size=35, weight='bold',family='Helvetica')#font
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)#Grid in Python Tkinter is a function that allows managing the layout of the widget. It takes rows and columns as an argument and places the widget in 2D format.

#pady add pixels horizontally outside the widget’s border


icon = Image.open('icons/kite.jpg')
icon = icon.resize((150 ,300), Image.ANTIALIAS)#technique used in digital imaging to reduce the visual defects that occur when high-resolution images are presented in a lower resolution
icon = ImageTk.PhotoImage(icon)#Use the Tkinter PhotoImage widget to display an image for a Label or Button .
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)#organises widgets in a table-like structure in the parent widget

btn1_image = Image.open('icons/monitor.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle.png')
btn2_image = btn2_image.resize((75,75), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/inout.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/recording.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)


# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green',command = find_motion, image=btn1_image, compound='left')# compound->position of the image relative to the text.

btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn2_image)#command is for callback function
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Capture', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=2)

btn5 = tk.Button(frame1, text="exit",height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)


frame1.pack()#Pack geometry manager packs widgets relative to the earlier widget.
window.mainloop()#tells to run  tkinter event loop
#Tkinter application runs most of its time inside an event loop, which is entered via the mainloop method. It waiting for events to happen.
# Events can be key presses or mouse operations by the user.

 