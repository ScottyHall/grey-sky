# grey sky labs game
import tkinter
from PIL import ImageTk, Image


class Person(object):
    """general person building class to set, edit, return attributes

    Attributes:
    firstName: string
    lastName: string
    age: int 1 - 100
    background: long string
    gender: m/f
    strength: 0 - 100
    health: 1 - 100
    infected status: 0/1
    inventory: list
    current room: room object
    """

    def __init__(self, firstName, lastName, age,
                 background, gender, strength,
                 health, infectedStatus):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.background = background
        self.gender = gender
        self.strength = strength
        self.health = health
        self.infectedStatus = infectedStatus
        self.inventory = []
        self.currentRoom = ""

    # returns

    def return_first(self):
        return self.firstName

    def return_last(self):
        return self.lastName

    def return_age(self):
        return self.age

    def return_background(self):
        return self.background

    def return_gender(self):
        return self.gender

    def return_strength(self):
        return self.strength

    def return_health(self):
        return self.health

    def return_infected(self):
        return self.infectedStatus

    def return_inventory(self):
        return self.inventory

    def return_currentroom(self):
        return self.currentRoom

    # setters

    def set_first(self, first):
        self.firstName = first

    def set_last(self, last):
        self.lastName = last

    def set_age(self, age):
        self.age = age

    def set_background(self, bg):
        self.background = bg

    def set_gender(self, gender):
        self.gender = gender

    def set_strength(self, strength):
        self.strength = strength

    def set_health(self, health):
        self.health = health

    def set_infectedStatus(self, infected):
        self.infectedStatus = infected

    def set_currentRoom(self, room):
        self.currentRoom = room


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

# displayCanvas.delete(redline) #delete line
# displayCanvas.delete(ALL) #delete all from canvas

saveIcon = "images/save.png"  # file location for icons
saveImg = ImageTk.PhotoImage(Image.open(saveIcon))
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
