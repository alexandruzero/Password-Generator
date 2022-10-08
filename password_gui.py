#!/usr/bin/python
from tkinter import *
import sys, os
import string
import secrets

# Different alphabets for a stronger password
cyrillic = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя' # noqa
hebrew = 'אבגדהוזחטיכךלמםנןסעפףצץקרשת' # noqa
greek = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω' # noqa
chinese = '的一是不了人我在有他這中大來上國個到說們為子和你地出道也時年' # noqa

alphabet = string.digits + string.ascii_letters + string.punctuation \
           + cyrillic + hebrew + greek + chinese
total = string.digits + string.ascii_letters + string.punctuation


def standard(pick):
    display_entry.configure(state=NORMAL)
    display_entry.delete(0, END)
    if buttons[pick]['highlightcolor'] == 'red':
        length = 32
    elif buttons[pick]['highlightcolor'] == 'blue':
        length = 64
    elif buttons[pick]['highlightcolor'] == 'green':
        length = 128
    elif buttons[pick]['highlightcolor'] == 'cyan':
        length = 256
    elif buttons[pick]['highlightcolor'] == 'black':
        length = 512
    else:
        length = 1024
    password = "".join(secrets.choice(total) for _ in range(int(length)))
    display_entry.insert(0, password)
    print("Password generated." + " [" + str(length) + "]")
    display_entry.configure(state=DISABLED)
    clipper()


def custom():
    display_entry.configure(state=NORMAL)
    display_entry.delete(0, END)
    length = int(question.get())
    if length < 3000:
        password = "".join(secrets.choice(total) for _ in range(int(length)))
        display_entry.insert(0, password)
        if length == 69 or length == 420:
            display_entry.delete(0, END)
            display_entry.insert(0, "A true man of culture.")
        else:
            print("Password generated." + " [" + str(length) + "_custom]")
    else:
        print("That's a long ass password!" + " [" + str(length) + "]")
        display_entry.insert(0, "Paranoia?")
    display_entry.configure(state=DISABLED)
    clipper()


def bulk():
    file = open('/home/alex/Desktop/bulk.txt', 'w')
    file.write('')
    n = 0
    while n < 100:
        password = ''.join(secrets.choice(total) for _ in range(64))
        file = open('/home/alex/Desktop/bulk.txt', 'a')
        file.write(password + "\n")
        file.close()
        n = n + 1


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


# Main window.
root = Tk()
root.title('Ghost Generator')
root.minsize(480, 170)
root.maxsize(480, 170)
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "ghost.png")))
# root.iconbitmap('/home/alex/projects/password/ghost.ico')

# Password output.
display_frame = Frame(root)
display_frame.place(x=8, y=10, height=40, width=463)
display_entry = Entry(display_frame, font=("Helvetica", 12), bd=2, bg="white", width=5, state=DISABLED)
display_entry.pack(expand=True, fill=BOTH)

# Entry for custom length
question_frame = Frame(root)
question_frame.place(x=220, y=120, height=40, width=250)
question = Entry(question_frame, font=("Helvetica", 14), bd=2, bg="white", width=5)
question.pack(expand=True, fill=BOTH)

# Buttons for actions frame
actions_frame = LabelFrame(root, text="Actions")
actions_frame.place(x=220, y=60, height=50, width=250)

generate_custom = Button(actions_frame, text="Generate ", bd=1, command=custom)
generate_custom.grid(row=0, column=0, padx=8)

bulk_button = Button(actions_frame, text="Bulk", bd=1, command=bulk)
bulk_button.grid(row=0, column=1, padx=8)

clear_button = Button(actions_frame, text="Clear", bd=1, command=clear)
clear_button.grid(row=0, column=2, padx=8)

# Buttons for standard length
standard_buttons = LabelFrame(root, text="Standard length")
standard_buttons.place(x=8, y=60, height=100)

generate_32 = Button(standard_buttons, text="32 ", bd=1, highlightcolor="red", command=lambda: standard(0))
generate_32.grid(row=0, column=0, padx=8, pady=8)

generate_64 = Button(standard_buttons, text="64 ", bd=1, highlightcolor="blue", command=lambda: standard(1))
generate_64.grid(row=0, column=1, padx=8)

generate_128 = Button(standard_buttons, text="128", bd=1, highlightcolor="green", command=lambda: standard(2))
generate_128.grid(row=0, column=2, padx=8)

generate_256 = Button(standard_buttons, text="256", bd=1, highlightcolor='cyan', command=lambda: standard(3))
generate_256.grid(row=1, column=0, padx=8)

generate_512 = Button(standard_buttons, text="512", bd=1, highlightcolor='black', command=lambda: standard(4))
generate_512.grid(row=1, column=1, padx=8)

generate_1024 = Button(standard_buttons, text="1024", bd=1, highlightcolor='yellow', command=lambda: standard(5))
generate_1024.grid(row=1, column=2, padx=8)

buttons = [generate_32, generate_64, generate_128, generate_256, generate_512, generate_1024]

root.mainloop()
