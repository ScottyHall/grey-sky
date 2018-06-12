# grey sky labs game
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image



def doNothing():
	print("do nothing triggered")

root = Tk()
root.title('Grey Sky')	# window title

# file menu

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# toolbar

toolbar = Frame(root, bd=1, height=20, relief=RAISED)
insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
userInput = Entry(toolbar)
userInput.pack(side=LEFT, padx=2, pady=2)
optionCanvas = Canvas(toolbar, width=100, height=20)
optionCanvas.pack(side=RIGHT)
optionCanvas.create_text(40, 12, width=50, justify=RIGHT, text="Living")

# main frame and canvas

mainFrame = Frame(root, bg="green", cursor='heart')
mainFrame.pack(anchor='w', fill=BOTH, expand=1)

displayCanvas = Canvas(mainFrame, width=400, height=250, cursor='man')
displayCanvas.pack(anchor='w', fill=BOTH, expand=1, padx=10, pady=10)

# status bar

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# shape drawing

blackline = displayCanvas.create_line(3, 4, 250, 50)
redline = displayCanvas.create_line(200, 2, 20, 120, fill='red')
greenBox = displayCanvas.create_rectangle(40, 40, 120, 100, fill='green')

#displayCanvas.delete(redline)	#delete line
#displayCanvas.delete(ALL)	#delete all from canvas

saveImg = ImageTk.PhotoImage(Image.open("save.png"))
displayCanvas.create_image(10, 10, anchor=NW, image=saveImg, tags='image1')
displayCanvas.create_image(80, 80, anchor=NW, image=saveImg, tags='image2')
displayCanvas.delete('image1')

# create text
displayText = "Testing. I hope this works and is able to wrap correctly"
displayCanvas.create_text(100, 200, anchor=NW, text=displayText, width=200, tags='text')


root.mainloop()



