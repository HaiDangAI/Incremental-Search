from logging import RootLogger
from tkinter import ttk
from tkinter import *
from ReadSentences import sentences
ProjectCsd301 = __import__('Project Csd 301')

window = Tk()
window.title('Incremental Search')
window.geometry('500x250')


name = Label(window, text='Incremental Search', fg='red', font=('Times New Roman', 15))
name.place(x=30, y=10)


inputBox = Entry(window, width=40, font=('Times New Roman', 15))
inputBox.place(x=35, y=50)
inputBox.focus()

def updateSuggestBox(data):
    suggestBox.delete(0, END)
    for item in data:
        suggestBox.insert(END, item)

def fillInputBox(e):
    inputBox.delete(0, END)
    inputBox.insert(0, suggestBox.get(ACTIVE))
    
def check(e):
    typed = inputBox.get()
    if typed == '':
        data = sentences
    else:
        data = ProjectCsd301.getSimilarSens(typed)
    updateSuggestBox(data)

suggestBox = Listbox(window, width=40, height=5,font=('Times New Roman', 15))
suggestBox.place(x=35, y=100)


quitButton = Button(window, text='QUIT', command=window.destroy, font=('Times New Roman',10), fg='red')
quitButton.place(x=450, y=200)

updateSuggestBox(sentences)

suggestBox.bind("<<ListboxSelect>>", fillInputBox)
inputBox.bind("<KeyRelease>", check)


window.mainloop()