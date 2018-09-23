from tkinter import *
from tkinter.scrolledtext import *
import os

#variables
textbox_width = 50
textbox_height = 20
paper_colour = "white"
current_chapter = 1
book_title = "Alice in Wonderland" #v2, turn this into a variable for user to select
image_path = "Library/" + book_title + "/bookCover.gif" #tkinter only recognises .gifs
button1 = 'Prev'
button2 = 'Next'
button3 = 'X'

#functions

def nextChap():
    global current_chapter
    if(current_chapter < count_chapters()):
        current_chapter = current_chapter+1
        update_chapter_contents()
        update_chapter_label()

def prev():
    global current_chapter
    if (current_chapter > 1):
        current_chapter = current_chapter-1
        update_chapter_contents()
        update_chapter_label()

def update_chapter_contents():
    chapter_path = "Library/" + book_title + "/chapter" + str(current_chapter) + ".txt"
    filein = open(chapter_path, encoding="utf-8")
    book_content = filein.read()
    filein.close()
    chapter_text.delete(1.0, END) # Clear previous chapter text
    chapter_text.insert(END, book_content) #add chapter contents

def count_chapters():
    number_of_chapters = 0
    path = "Library/" + book_title
    files = os.listdir(path)
    for file in files:
        if file[:5] == "Chapter":
            number_of_chapters = number_of_chapters+1
    return number_of_chapters

def update_chapter_label():
    chapter_label_text = "Chapter " + str(current_chapter)
    chapter_label.config(text=chapter_label_text)

def quit_book():
    window.withdraw()
    window.quit()

#main loop
window = Tk()
window.title("pyReader eBook Reader")

#Title textbox
title = Text(window, width=textbox_width, height=1, background=paper_colour)
title.grid(row=0, column=1, sticky=W)

#Book title
title.insert(END, book_title)

#Scrolling textbox
chapter_text = ScrolledText(window, width=textbox_width, height=textbox_height,
                            background=paper_colour, wrap=WORD)
chapter_text.grid(row=1, column=1, sticky=W)

#Add text from chapter
update_chapter_contents()

#add cover image
book_image = PhotoImage(file=image_path)
picture_label = Label(image=book_image)
picture_label.grid(row=1, column=2, sticky=N)


#add buttons
buttons = Frame(window)
buttons.grid(row=3, column=2, sticky=S)
Button(buttons, text=button1, width=10, command=prev).grid(row=3, column=1)
Button(buttons, text=button2, width=10, command=nextChap).grid(row=3, column=2)
Button(buttons, text=button3, width=10, command=quit_book).grid(row=3, column=3)

#run loop
window.mainloop()
