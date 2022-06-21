from tkinter import *
import random


def generate():
    errorLabel.config(text=' ')
    errorLabel.update()
    try:
        lngth = int(pswd_length.get())
    except:
        errorLabel.config(text='Please enter a number', fg='Red')
        errorLabel.update()

    chars = []
    with open('chars.txt', 'r') as file:
        for lines in file:
            chars.append(lines.replace('\n', ''))

    psswd = ''
    count = lngth
    while(count>=1):
        psswd += chars[random.randint(0, 46)]
        count -= 1
    print(psswd)
    output.config(text=psswd, fg='Black')
    output.update()

    root.clipboard_clear()
    root.clipboard_append(psswd)

root = Tk()
root.title('Password Generator')
root.resizable(0, 0)

number_of_chars_frame = LabelFrame(root)
psswd_length_label = Label(number_of_chars_frame, text='Number of characters: ')
psswd_length_label.pack()
pswd_length = Entry(number_of_chars_frame)
pswd_length.pack()
errorLabel = Label(number_of_chars_frame)
errorLabel.pack()
number_of_chars_frame.pack(pady=20)

generatebtn = Button(root, text='Generate', command=generate)
generatebtn.pack()

outputFrame = LabelFrame(root)
outputLabel = Label(outputFrame, text='Password')
outputLabel.pack()
output = Label(outputFrame)
output.pack(padx=30)
outputFrame.pack(pady=30)

root.geometry('500x500')
root.mainloop()

