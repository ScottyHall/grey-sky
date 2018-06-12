# grey sky labs game
import tkinter
from PIL import ImageTk, Image


def doNothing():
    print("do nothing triggered")


root = tkinter.Tk()
root.title('Grey Sky')  # window title

# file menu

menu = tkinter.Menu(root)
root.config(menu=menu)

subMenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = tkinter.Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# toolbar

toolbar = tkinter.Frame(root, bd=1, height=20, relief=tkinter.RAISED)
insertButton = tkinter.Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=tkinter.LEFT, padx=2, pady=2)
printButton = tkinter.Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=tkinter.LEFT, padx=2, pady=2)
toolbar.pack(side=tkinter.TOP, fill=tkinter.X)
userInput = tkinter.Entry(toolbar)
userInput.pack(side=tkinter.LEFT, padx=2, pady=2)
optionCanvas = tkinter.Canvas(toolbar, width=100, height=20)


optionCanvas.pack(side=tkinter.LEFT)
optionCanvas.create_text(50, 12, width=200,
                         justify=tkinter.RIGHT, text="Living Room")

# main frame and canvas

mainFrame = tkinter.Frame(root, bg="green", cursor='heart')
mainFrame.pack(anchor='w', fill=tkinter.BOTH, expand=1)

displayCanvas = tkinter.Canvas(mainFrame, width=400, height=250, cursor='man')
displayCanvas.pack(anchor='w', fill=tkinter.BOTH, expand=1, padx=10, pady=10)

# status bar

status = tkinter.Label(root, text="Preparing to do nothing...", bd=1,
                       relief=tkinter.SUNKEN, anchor=tkinter.W)
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# shape drawing

blackline = displayCanvas.create_line(3, 4, 250, 50)
redline = displayCanvas.create_line(200, 2, 20, 120, fill='red')
greenBox = displayCanvas.create_rectangle(40, 40, 120, 100, fill='green')

# displayCanvas.delete(redline)	#delete line
# displayCanvas.delete(ALL)	#delete all from canvas

saveImg = ImageTk.PhotoImage(Image.open("save.png"))
displayCanvas.create_image(10, 10, anchor=tkinter.NW,
                           image=saveImg, tags='image1')
displayCanvas.create_image(80, 80, anchor=tkinter.NW,
                           image=saveImg, tags='image2')
displayCanvas.delete('image1')

# create text
displayText = "Testing. I hope this works and is able to wrap correctly"
displayCanvas.create_text(100, 200, anchor=tkinter.NW, text=displayText,
                          width=200, tags='text')


root.mainloop()
