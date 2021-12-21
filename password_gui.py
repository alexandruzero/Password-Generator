#!/usr/bin/env python3

from tkinter import *
from playsound import playsound
import string
import secrets


def standard_32():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 32
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def standard_64():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 64
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def standard_128():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 128
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def standard_256():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 256
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def standard_512():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 512
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def standard_1024():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = 1024
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	print("Password generated." + " [" + str(length) + "]")
	display_entry.configure(state=DISABLED)


def custom_size():
	display_entry.configure(state=NORMAL)
	display_entry.delete(0, END)
	length = int(question.get())
	total = string.ascii_letters + string.digits + string.punctuation
	my_password = "".join(secrets.choice(total) for character in range(int(length)))
	display_entry.insert(0, my_password)
	if length >= 3000:
		print("That's a long ass password!" + " [" + str(length) + "]")
	else:
		print("Password generated." + " [" + str(length) + "]" + " [custom]")
	display_entry.configure(state=DISABLED)
	if length == 69:
		playsound("nice.mp3")
		print("Password generated." + " [" + str(length) + "]" + " [custom]")


def clipper():
	root.clipboard_clear()
	root.clipboard_append(display_entry.get())
	print("Copied to clipboard.")


def clear():
	display_entry.configure(state=NORMAL)
	root.clipboard_clear()
	display_entry.delete(0, END)
	question.delete(0, END)
	print("Entries cleared.")
	display_entry.configure(state=DISABLED)


# Main window
root = Tk()
root.title('Ghost Generator')
root.minsize(500, 170)
root.maxsize(500, 170)
root.iconbitmap("@~/pycharm/execute/password/ghost.xbm")

# Password output entry
display_frame = LabelFrame(root)
display_frame.place(x=8, y=10, height=40, width=490)
display_entry = Entry(display_frame, font=("Helvetica", 14), bd=2, bg="white", width=5, state=DISABLED)
display_entry.pack(expand=True, fill=BOTH)

# Custom length entry
question_frame = LabelFrame(root)
question_frame.place(x=250, y=120, height=40, width=245)
question = Entry(question_frame, font=("Helvetica", 14), bd=2, bg="white", width=5)
question.pack(expand=True, fill=BOTH)

# Standard length frame
standard_buttons = LabelFrame(root, text="Standard length")
standard_buttons.place(x=8, y=60, height=100)

# Actions frame
actions_frame = LabelFrame(root, text="Actions")
actions_frame.place(x=250, y=60, height=50, width=245)

# Actions buttons
generate_custom = Button(actions_frame, text="Generate ", bd=1, command=custom_size)
generate_custom.grid(row=0, column=0, padx=8)

clip_button = Button(actions_frame, text="Copy", bd=1, command=clipper)
clip_button.grid(row=0, column=1, padx=8)

clear_button = Button(actions_frame, text="Clear", bd=1, command=clear)
clear_button.grid(row=0, column=2, padx=8)

# Standard length buttons
generate_32 = Button(standard_buttons, text="32 ", bd=1, command=standard_32)
generate_32.grid(row=0, column=0, padx=8, pady=8)

generate_64 = Button(standard_buttons, text="64 ", bd=1, command=standard_64)
generate_64.grid(row=0, column=1, padx=8)

generate_128 = Button(standard_buttons, text="128", bd=1, command=standard_128)
generate_128.grid(row=0, column=2, padx=8)

generate_256 = Button(standard_buttons, text="256", bd=1, command=standard_256)
generate_256.grid(row=1, column=0, padx=8)

generate_512 = Button(standard_buttons, text="512", bd=1, command=standard_512)
generate_512.grid(row=1, column=1, padx=8)

generate_1024 = Button(standard_buttons, text="1024", bd=1, command=standard_1024)
generate_1024.grid(row=1, column=2, padx=8)


root.mainloop()
