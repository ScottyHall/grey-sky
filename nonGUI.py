import os


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

    # returns for person
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

    # setters for person
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


class Room(object):
    """general room building class to set, edit, and return attributes

    Attributes:
    roomName: string
    wallColor: string
    uniqueFeatures: list
    floorDescription: string
    roomConnections: dictionary (key= roomName, keyValue= 0/1 unlocked status)
    roomStatus: list (smoke, fire, cold, flooded, loud, bright, dark, quiet)
    roomItems: dictionary
    npcPresent: list (lists NPCs in room)
    """

    def __init__(self, roomName, wallColor, uniqueFeatures, floorDescription,
                 roomConnections, roomStatus, roomItems, npcPresent):
        self.roomName = roomName
        self.wallColor = wallColor
        self.uniqueFeatures = uniqueFeatures
        self.floorDescription = floorDescription
        self.roomConnections = roomConnections
        self.roomStatus = roomStatus
        self.roomItems = roomItems
        self.npcPresent = npcPresent

    # returns for room
    def return_room(self):
        return self.roomName

    def return_wallColor(self):
        return self.wallColor

    def return_uniqueFeatures(self):
        return self.uniqueFeatures

    def return_floorDescription(self):
        return self.floorDescription

    def return_roomConnections(self):
        return self.roomConnections

    def return_roomStatus(self):
        return self.roomStatus

    def return_roomItems(self):
        return self.roomItems

    def return_npcPresent(self):
        return self.npcPresent

    # setters for room
    def del_roomItem(self, itemToRm):
        if itemToRm in self.roomItems:
            self.roomItems.remove(itemToRm)
            return True
        return False

    def remove_npc(self, npcToRm):
        if npcToRm in self.npcPresent:
            self.npcPresent.remove(npcToRm)
            return True
        return False

    def add_npc(self, npcToAdd):
        self.npcPresent.append(npcToAdd)


class Item(object):
    """general item building class to set, edit, and return attributes

    Attributes:
    itemName = string
    itemDamage = 0 - 100
    itemAbility = hack, attack, heal, cure, buff, nerf
    itemMaterial = wood, metal, electronic, breakable, meltable
    itemDescription = string
    """
    def __init__(self, name, dmg, ability, material, desc):
        self.itemName = name
        self.itemDamage = dmg
        self.itemAbility = ability
        self.itemMaterial = material
        self.itemDescription = desc

    # returns for item
    def return_itemName(self):
        return self.itemName

    def return_itemDamage(self):
        return self.itemDamage

    def return_itemAbility(self):
        return self.itemAbility

    def return_itemMaterial(self):
        return self.itemMaterial

    def return_itemDescription(self):
        return self.itemDescription

    # setters for item
    def set_itemName(self, name):
        self.itemName = name

    def set_itemDamage(self, newDmg):
        self.itemDamage = newDmg

    def set_itemAbility(self, newAbil):
        self.itemAbility = newAbil

    def set_itemMaterial(self, newMaterial):
        self.itemMaterial = newMaterial

    def set_itemDescription(self, newDesc):
        self.itemDescription = newDesc


class Book(Item):
    """general book building class to set and return attributes

    Attributes:
    bookWriting = list (page number: text)
    """

    def __init__(self, writing):
        self.bookWriting = writing

    def add_bookPage(self, text):
        self.bookWriting.append(text)

    def return_writing(self, pageNO):
        return self.bookWriting[pageNO]


char1 = Person("Tubby", "Tubbs", 25,
               "this is the bg of Mr. Tubbs", 'm',
               75, 100, 0)

room1 = Room("Lab", "purple", ["smelly", "damp", "dirty"],
             "messy", "none", ["cold", "flooded"],
             ["key", "book", "table"], ["Tubby"])
room2 = Room("Kitchen", "purple", ["smelly", "damp", "dirty"],
             "messy", "none", ["cold", "flooded"],
             ["key", "book", "table"], ["Henry"])


# scans for .txt files in given folder to auto-add items, npcs, and books
def file_scan(folderName):  # "books", "npcs", "items"
    bookObjects = []  # used for object reference of all books created
    bookTitles = []  # used for string reference of all books created
    npcObjects = []
    npcTitles = []
    npcItemList = []  # stores npc inventory list
    itemObjects = []
    itemTitles = []
    roomObjects = []
    roomTitles = []
    for file in os.listdir(folderName):
        if file.endswith(".txt"):
            fileName = file.split(".")[0]  # ditches the '.txt'
            # print(os.path.join(folderName, file))
            joinedFileName = folderName + "/" + file
            f = open(joinedFileName, "r")
            # print("This is printing {}".format(joinedFileName))
            if folderName is "books":
                bookTitles.append(fileName)  # save file name as string list item
                bookText = ["Click the next Arrow to turn the page"]
                file = Book(bookText)
                bookObjects.append(file)  # save file as object list
                for line in f:
                    if "END" in line:  # looks for 'END'
                        document = f.readlines()
                        lastLine = document[-1]
                        lastLine = lastLine.split(":")[1]
                        bookTitles.append(lastLine)
                        bookObjects.append("")
                        break
                    file.add_bookPage(line)
                f.close()
            elif folderName is "npcs":
                npcTitles.append(fileName.title())  # save file name as string list item
                # npcObjects.append(file)  # save file as object list
                document = f.readlines()
                for line in document:
                    if "First Name" in line:
                        name = line.split(":")[1]
                        name = name.rstrip("\n")
                        npcBuildFirstName = name
                    if "Last Name" in line:
                        name = line.split(":")[1]
                        name = name.rstrip("\n")
                        npcBuildLastName = name
                    if "Age" in line:
                        age = line.split(":")[1]
                        age = age.rstrip("\n")
                        age = int(age)
                        npcBuildAge = age
                    if "Background" in line:
                        bg = line.split(":")[1]
                        bg = bg.rstrip("\n")
                        npcBuildBG = bg
                    if "Gender" in line:
                        gender = line.split(":")[1]
                        gender = gender.rstrip("\n")
                        npcBuildGender = gender
                    if "Strength" in line:
                        strength = line.split(":")[1]
                        strength = strength.rstrip("\n")
                        strength = int(strength)
                        npcBuildStrength = strength
                    if "Health" in line:
                        health = line.split(":")[1]
                        health = health.rstrip("\n")
                        health = int(health)
                        npcBuildHealth = health
                    if "Infected" in line:
                        infected = line.split(":")[1]
                        infected = infected.rstrip("\n")
                        infected = int(infected)
                        npcBuildInfected = infected
                    if "Inventory" in line:
                        itemListLen = len(document)
                        for i in range(10, itemListLen):
                            itemToAdd = document[i]
                            itemToAdd = itemToAdd.rstrip("\n")
                            itemToAdd = itemToAdd.title()
                            npcItemList.append(itemToAdd)
                npcName = Person(npcBuildFirstName, npcBuildLastName,
                                 npcBuildAge, npcBuildBG, npcBuildGender,
                                 npcBuildStrength, npcBuildHealth, npcBuildInfected)
                npcObjects.append(npcName)  # append object to list for zipping

            elif folderName is "items":
                itemTitles.append(fileName.title())  # save file name as string list item
                document = f.readlines()
                for line in document:
                    if "Item Name" in line:
                        name = line.split(":")[1]
                        name = name.rstrip("\n")
                        itemBuildFirstName = name
                    if "Item Damage" in line:
                        dmg = line.split(":")[1]
                        dmg = dmg.rstrip("\n")
                        dmg = int(dmg)
                        itemBuildDamage = dmg
                    if "Item Ability" in line:
                        ability = line.split(":")[1]
                        ability = ability.rstrip("\n")
                        itemBuildAbility = ability
                    if "Item Material" in line:
                        material = line.split(":")[1]
                        material = material.rstrip("\n")
                        itemBuildMaterial = material
                    if "Item Description" in line:
                        description = line.split(":")[1]
                        description = description.rstrip("\n")
                        itemBuildDesc = description
                itemName = Item(itemBuildFirstName, itemBuildDamage,
                                itemBuildAbility, itemBuildMaterial, itemBuildDesc)
                itemObjects.append(itemName)  # append object to list for zipping
            elif folderName is "rooms":
                pass

    if folderName is "books":
        # zips the two lists as a dictionary (keys are strings: values are objects)
        bookObjectLookup = dict(zip(bookTitles, bookObjects))
        # remember to build the book association to a room
        return(bookObjectLookup)
    elif folderName is "npcs":
        npcObjectLookup = dict(zip(npcTitles, npcObjects))
        return(npcObjectLookup)
    elif folderName is "items":
        itemObjectLookup = dict(zip(itemTitles, itemObjects))
        return(itemObjectLookup)
    elif folderName is "rooms":
        roomObjectLookup = dict(zip(roomTitles, roomObjects))
        return(roomObjectLookup)


""" ITEM example of creating the items
scanning all files and pulling dic key and damage"""
# items = file_scan("items")
# itemDisplay = list(items.keys())
# print("{} does a total of {} damage!".format(itemDisplay[0], items["Thor'S Hammer"].return_itemDamage()))


""" NPC example of creating the npcs
scanning files and pulling backgrounds"""
# npcs = file_scan("npcs")
# print(npcs["Henry"].return_background())
# print(npcs["Peter"].return_background())

""" BOOK example of pulling a page from a book.
First book in object list, 3rd index (2nd line of txt)"""
# books = file_scan("books")
# print("Printing the book")
# print(books["book1"].return_writing(1))
# print(books["The King Who Ruled the World"].return_writing(3))


# iterates through room status list
def room_status(room):
    for i in range(len(room.return_roomStatus())):
        print("{} {}: {}".format(room.roomName, i + 1, room.roomStatus[i]))


# iterates through room item keys
def room_itemKeys(room):
    for i in range(len(room.return_roomItems())):
        print("{} item {}: {}".format(room.roomName, i + 1,
                                      room.return_roomItems()[i]))


# removes specified item from specified room if present
def rm_roomItem(room, itemToRm):
    if room.del_roomItem(itemToRm) is True:
        print("Successfully removed '{}', from {}".format(itemToRm, room.roomName))
    else:
        print("'{}', is not located in {}".format(itemToRm, room.roomName))


# removes NPC from room and changes to new (if needed)
def npc_changeroom(currentRoom, npc, newRoom):
    npcName = npc.firstName
    if currentRoom.remove_npc(npcName) is True:
        if newRoom is 0:  # specify 0 as new room if no new room
            print("Successfully removed '{}', from {}.\nNo new room specified".format(npcName, currentRoom.roomName))
        else:
            newRoom.add_npc(npc.firstName)
            print("Successfully removed '{}', from {}.\nChanged to {}".format(npcName, currentRoom.roomName, newRoom.roomName))


rm_roomItem(room1, "key")


print(room1.return_roomStatus())
room_itemKeys(room1)

print("\n{}".format(room1.return_npcPresent()))
npc_changeroom(room1, char1, room2)
print("\n{}".format(room1.return_npcPresent()))
print("\n{}".format(room2.return_npcPresent()))
