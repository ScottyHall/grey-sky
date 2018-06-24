import os
import time
import sys
import random


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
                 health, infectedStatus, inv):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.background = background
        self.gender = gender
        self.strength = strength
        self.health = health
        self.infectedStatus = infectedStatus

        self.intro = ""
        self.job = ""
        self.secret = ""
        self.farewell = ""

        self.inventory = inv
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

    def return_intro(self):
        return self.intro

    def return_job(self):
        return self.job

    def return_secret(self):
        return self.secret

    def return_farewell(self):
        return self.farewell

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

    def set_intro(self, intro):
        self.intro = intro

    def set_job(self, job):
        self.job = job

    def set_secret(self, secret):
        self.secret = secret

    def set_farewell(self, farewell):
        self.farewell = farewell

    # add
    def add_npcItem(self, itemToAdd):
        self.inventory.append(itemToAdd)

    # remove
    def del_npcItem(self, itemToRm):
        if itemToRm in self.inventory:
            self.inventory.remove(itemToRm)
            return True
        return False


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
                 roomConnections, roomStatus, roomItems, npcPresent,
                 roomLocked, roomKey):
        self.roomName = roomName
        self.wallColor = wallColor
        self.uniqueFeatures = uniqueFeatures
        self.floorDescription = floorDescription
        self.roomConnections = roomConnections
        self.roomStatus = roomStatus
        self.roomItems = roomItems
        self.npcPresent = npcPresent
        self.isLocked = roomLocked
        self.roomKey = roomKey

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

    def return_isLocked(self):
        return self.isLocked

    def return_key(self):
        return self.roomKey

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

    def unlock_room(self):
        self.isLocked = False
        print("{} Unlocked".format(self.roomName))

    def lock_room(self):
        self.isLocked = True
        print("{} Locked".format(self.roomName))


class Item(object):
    """general item building class to set, edit, and return attributes

    Attributes:
    itemName = string
    itemDamage = 0 - 100
    itemAbility = hack, attack, heal, cure, buff, nerf
    itemMaterial = wood, metal, electronic, breakable, meltable
    itemDescription = string
    """
    def __init__(self, name, dmg, ability, material, desc,
                 unlockKey, visible, uAbility, uNum, uText,
                 uRm, crafted, useRooms):
        self.itemName = name
        self.itemDamage = dmg
        self.itemAbility = ability
        self.itemMaterial = material
        self.itemDescription = desc
        self.itemUnlockKey = unlockKey
        self.itemVisible = visible
        self.itemUnlockAbility = uAbility
        self.itemUnlockNum = uNum
        self.itemUnlockText = uText
        self.itemUnlockRm = uRm
        self.itemCrafted = crafted
        self.itemUseRooms = useRooms

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

    def return_itemUnlockKey(self):
        return self.itemUnlockKey

    def return_itemVisible(self):
        return self.itemVisible

    def return_itemUnlockAbility(self):
        return self.itemUnlockAbility

    def return_itemUnlockNum(self):
        return self.itemUnlockNum

    def return_itemUnlockText(self):
        return self.itemUnlockText

    def return_itemUnlockRm(self):
        return self.itemUnlockRm

    def return_itemCrafted(self):
        return self.itemCrafted

    def return_itemUseRooms(self):
        return self.itemUseRooms

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

    def return_book(self):
        return self.bookWriting


# scans for .txt files in given folder to auto-add items, npcs, and books
def file_scan(folderName):  # "books", "npcs", "items"
    bookObjects = []  # used for object reference of all books created
    bookTitles = []  # used for string reference of all books created
    npcObjects = []
    npcTitles = []
    npcItemList = []  # stores npc inventory list
    userItemList = []
    itemObjects = []
    itemTitles = []
    itemRooms = []
    roomObjects = []
    roomTitles = []
    roomItemList = []
    roomConnections = []
    roomNpcList = []
    userTitle = []
    userObject = []
    for file in os.listdir(folderName):  # checks for folder names
        if file.endswith(".txt"):
            fileName = file.split(".")[0]  # ditches the '.txt'
            # print(os.path.join(folderName, file))
            joinedFileName = folderName + "/" + file
            f = open(joinedFileName, "r")
            # print("This is printing {}".format(joinedFileName))
            # checks for new lines in .txt files located in books/
            if folderName is "books":
                bookTitles.append(fileName.title())  # save file name as string list item
                bookText = ["< Press enter/return to turn the page >"]
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
                    if "Item Use Unlock" in line:
                        unlock = line.split(":")[1]
                        unlock = unlock.rstrip("\n")
                        useUnlock = unlock
                    if "Item Visible at Start" in line:
                        visible = line.split(":")[1]
                        visible = visible.rstrip("\n")
                        visStart = visible
                    if "Item Unlock Ability" in line:
                        ability = line.split(":")[1]
                        ability = ability.rstrip("\n")
                        uAbility = ability
                    if "Item Unlock Num Ability" in line:
                        ability = line.split(":")[1]
                        ability = ability.rstrip("\n")
                        ability = int(ability)
                        uNum = ability
                    if "Item Unlock Text" in line:
                        text = line.split(":")[1]
                        text = text.rstrip("\n")
                        uText = text
                    if "Item Unlock Remove" in line:
                        remove = line.split(":")[1]
                        remove = remove.rstrip("\n")
                        uRemove = remove
                    if "Item Visible Item Crafted" in line:
                        crafted = line.split(":")[1]
                        crafted = crafted.rstrip("\n")
                        uCrafted = crafted
                    if "Item Use Rooms" in line:
                        for i in range(13, len(document)):
                            room = document[i].rstrip("\n")
                            itemRooms.append(room)
                itemName = Item(itemBuildFirstName, itemBuildDamage,
                                itemBuildAbility, itemBuildMaterial, itemBuildDesc,
                                useUnlock, visStart, uAbility, uNum, uText, uRemove,
                                uCrafted, itemRooms)
                itemObjects.append(itemName)  # append object to list for zipping
                itemRooms = []
                document = ""
                f.close()
            elif folderName is "rooms":
                roomTitles.append(fileName.title())  # save file name as string list item
                document = ""
                document = f.readlines()
                itemListLen = len(document)
                for i in range(len(document)):
                    if "Connecting Rooms" in document[i]:
                        connectingStart = i + 1
                    if "Items in Room" in document[i]:
                        itemStart = i + 1
                    if "NPCs in room" in document[i]:
                        npcStart = i + 1
                    if "Room Status" in document[i]:
                        statusStart = i
                for i in range(connectingStart, (statusStart)):
                    connectRoomRange = document[i]
                    connectRoomRange = connectRoomRange.rstrip("\n")
                    connectRoomRange = connectRoomRange.title()
                    roomConnections.append(connectRoomRange)
                for i in range(itemStart, (npcStart-1)):
                    itemRoomRange = document[i]
                    itemRoomRange = itemRoomRange.rstrip("\n")
                    itemRoomRange = itemRoomRange.title()
                    roomItemList.append(itemRoomRange)
                for i in range(npcStart, (len(document))):
                    npcRoomRange = document[i]
                    npcRoomRange = npcRoomRange.rstrip("\n")
                    npcRoomRange = npcRoomRange.title()
                    roomNpcList.append(npcRoomRange)
                for line in document:
                    if "Room Name" in line:
                        name = line.split(":")[1]
                        name = name.rstrip("\n")
                        roomBuildName = name
                    if "Wall color" in line:
                        color = line.split(":")[1]
                        color = color.rstrip("\n")
                        roomBuildColor = color
                    if "Unique Features" in line:
                        feature = line.split(":")[1]
                        feature = feature.rstrip("\n")
                        roomBuildFeatures = feature
                    if "Floor Description" in line:
                        floor = line.split(":")[1]
                        floor = floor.rstrip("\n")
                        roomBuildFloor = floor
                    if "Room Status" in line:
                        rStatus = line.split(":")[1]
                        rStatus = rStatus.rstrip("\n")
                        roomBuildStatus = rStatus
                    if "Door Locked" in line:
                        lStatus = line.split(":")[1]
                        lStatus = lStatus.rstrip("\n")
                        yes = ['Yes', 'yes']
                        if lStatus in yes:
                            roomBuildLocked = True
                        else:
                            roomBuildLocked = False
                    if "Needed for unlock" in line:
                        needed = line.split(":")[1]
                        needed = needed.rstrip("\n")
                        roomBuildKey = needed
                roomName = Room(roomBuildName, roomBuildColor, roomBuildFeatures,
                                roomBuildFloor, roomConnections, roomBuildStatus,
                                roomItemList, roomNpcList,
                                roomBuildLocked, roomBuildKey)
                roomObjects.append(roomName)  # append object to list for zipping
                roomItemList = []
                roomNpcList = []
                roomConnections = []
                document = ""
                f.close()
            elif folderName is "npcs" or "user":
                if folderName is "npcs":
                    npcTitles.append(fileName.title())  # save file name as string list item
                    # npcObjects.append(file)  # save file as object list
                elif folderName is "user":
                    userTitle.append(fileName.title())
                document = ""
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
                    if "Intro" in line:
                        intro = line.split(":")[1]
                        intro = intro.rstrip("\n")
                        npcBuildIntro = intro
                    if "Job Description" in line:
                        job = line.split(":")[1]
                        job = job.rstrip("\n")
                        npcBuildJob = job
                    if "Secret known" in line:
                        secret = line.split(":")[1]
                        secret = secret.rstrip("\n")
                        npcBuildSecret = secret
                    if "Farewell" in line:
                        farewell = line.split(":")[1]
                        farewell = farewell.rstrip("\n")
                        npcBuildFarewell = farewell
                    if "Inventory" in line and folderName is "npcs":
                        itemListLen = len(document)
                        for i in range(14, itemListLen):
                            itemToAdd = document[i]
                            itemToAdd = itemToAdd.rstrip("\n")
                            itemToAdd = itemToAdd.title()
                            npcItemList.append(itemToAdd)
                    if "Inventory" in line and folderName is "user":
                        itemListLen = len(document)
                        for i in range(10, itemListLen):
                            itemToAdd = document[i]
                            itemToAdd = itemToAdd.rstrip("\n")
                            itemToAdd = itemToAdd.title()
                            userItemList.append(itemToAdd)
                    if folderName is "user":
                        if "Current Room" in line:
                            currentRoom = line.split(":")[1]
                            currentRoom = currentRoom.rstrip("\n")
                            userBuildRoom = currentRoom
                if folderName is "npcs":
                    npcName = Person(npcBuildFirstName, npcBuildLastName,
                                     npcBuildAge, npcBuildBG, npcBuildGender,
                                     npcBuildStrength, npcBuildHealth,
                                     npcBuildInfected, npcItemList)
                    npcObjects.append(npcName)  # append object to list for zipping
                    npcName.set_intro(npcBuildIntro)
                    npcName.set_job(npcBuildJob)
                    npcName.set_secret(npcBuildSecret)
                    npcName.set_farewell(npcBuildFarewell)
                    npcItemList = []
                elif folderName is "user":
                    npcName = Person(npcBuildFirstName, npcBuildLastName,
                                     npcBuildAge, npcBuildBG, npcBuildGender,
                                     npcBuildStrength, npcBuildHealth,
                                     npcBuildInfected, userItemList)
                    npcName.set_currentRoom(userBuildRoom)
                    userObject.append(npcName)
                document = ""
                f.close()
    if folderName is "books":
        # zips the two lists as a dictionary (keys are strings: values are objects)
        bookObjectLookup = dict(zip(bookTitles, bookObjects))
        # remember to build the book association to a room
        print("Loaded files from 'books/'\n\n\n\n")
        return(bookObjectLookup)
    elif folderName is "npcs":
        npcObjectLookup = dict(zip(npcTitles, npcObjects))
        print("Loaded files from 'npcs/'")
        return(npcObjectLookup)
    elif folderName is "user":
        userObjectLookup = dict(zip(userTitle, userObject))
        print("Loaded files from 'user/'")
        return(userObjectLookup)
    elif folderName is "items":
        itemObjectLookup = dict(zip(itemTitles, itemObjects))
        print("Loaded files from 'items/'")
        return(itemObjectLookup)
    elif folderName is "rooms":
        roomObjectLookup = dict(zip(roomTitles, roomObjects))
        print("Loaded files from 'rooms/'")
        return(roomObjectLookup)


""" ROOM example of creating the rooms
scanning all files and pulling information"""
# rooms = file_scan("rooms")
# roomList = list(rooms.keys())
# print("List of rooms: {}".format(roomList))
# print(rooms["Lab"].return_npcPresent())

""" ITEM example of creating the items
scanning all files and pulling dict key and damage"""
# items = file_scan("items")
# itemDisplay = list(items.keys())
# print(itemDisplay)
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

# scan through files in directory to build
rooms = file_scan("rooms")
items = file_scan("items")
npcs = file_scan("npcs")
user = file_scan("user")
books = file_scan("books")


# typing speed for 'print_slow'
standardSpeed = 0.05  # time between each character typed
fastSpeed = 0.001


# print(user["User"].return_first())

# return room status
# print(rooms[roomList[1]].return_roomStatus())
# print(rooms["Lab"].return_roomStatus())


# checks the system and clears the terminal accordingly
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():
    # open the map file and set to gameMap
    # init welcome message
    clear_terminal()
    welcome = open("game/welcome.txt", "r")
    welcomeMsg = welcome.read()
    welcome.close()

    print_slow(welcomeMsg, fastSpeed, "noWrap")
    print_slow("Press enter to continue", standardSpeed, "")
    input("")
    print("\n\n\n\n\n\n\n")


def game_loop():
    """ game_loop loops through the main menu of the game """
    talk = ['talk', 't', '1']
    use = ['use', 'u', '2']
    inspect = ['inspect', 'i', '3']
    inventory = ['inventory', 'inv', '4']
    openDoor = ['door', 'doors', 'd', '5']
    roomDescription = ['room', 'room description', 'r', '6']
    getMap = ['map', 'm', '7']
    displayHelp = ['help', 'h', '8']

    choicesMessage = """Current Options:
    Talk(t, 1) - interact with another character
    Use(u, 2) - use an item located in your inventory
    Inspect(i, 3) - interact with an item in the current room
    Inventory(inv, 4) - display items located in your inventory
    Door(d, 5) - open a door in the room
    Room Description(r, 6) - get a description of the room
    Map(m, 7) - display the map
    Help(h, 8) - show options"""

    clear_terminal()
    print(choicesMessage)

    while True:
        # main input loop for user choice
        if valid(user["User"].return_currentroom(), "room") is True:
                userCurrent = user["User"].return_currentroom()
                print("\n\nCurrent Room: {}".format(userCurrent))
        print("Health: {}+".format(user["User"].return_health()))
        choice = input("\n'h' to display options\nEnter your action: ").lower()
        if choice in talk:
            clear_terminal()
            if valid(user["User"].return_currentroom(), "room") is True:
                userCurrent = user["User"].return_currentroom()
                print_slow("Current individuals in the {}:".format(userCurrent), standardSpeed, "noWrap")
                print(rooms[userCurrent].return_npcPresent())
                userInput = input("Enter the individual you wish to speak with: ")
                userInput = userInput.title()
                if valid(userInput, "npc") is True:
                    clear_terminal()
                    print("{}:".format(userInput))
                    print_slow(npcs[userInput].return_intro(), standardSpeed, "wrap")
                    npc_loop(userInput)
            else:
                print("ERROR: User is in a room that doesn't exist")
        elif choice in use:
            clear_terminal()
            print_slow("Current Inventory Items:", standardSpeed, "noWrap")
            print(user["User"].return_inventory())
            userChoice = input("Which item do you wish to use?: ")
            userChoice = userChoice.title()
            if userChoice in user["User"].return_inventory():
                if valid(userChoice, "book") is True:
                    read_book(userChoice)
                elif valid(userChoice, "item") is True:
                    print("It's AN ITEM!")
                else:
                    print("Error: Input not recognized as a valid item.")
            else:
                print("Input not recognized as a valid item. Please try again.")
        elif choice in inspect:
            clear_terminal()
            print_slow("Items in {}:\n{}".format(userCurrent, rooms[userCurrent].return_roomItems()), standardSpeed, "wrap")
            userChoice = input("Which item do you wish to inspect?: ")
            userChoice = userChoice.title()
            if userChoice in rooms[userCurrent].return_roomItems():
                if valid(userChoice, "book") is True:
                    read_book(userChoice)
                elif valid(userChoice, "item") is True:
                    print("It's AN ITEM!")
                else:
                    print("Error: Input not recognized as a valid item.")
            else:
                print("Input not recognized as a valid item. Please try again.")
        elif choice in inventory:
            clear_terminal()
            print_slow("Current Inventory Items:", standardSpeed, "noWrap")
            print(user["User"].return_inventory())
            print("\n\n")
        elif choice in openDoor:
            clear_terminal()
            print_slow("Current Doors in {}: {}".format(userCurrent, rooms[userCurrent].return_roomConnections()), standardSpeed, "wrap")
            doorChoice = input("Which door do you wish to open?: ")
            doorChoice = doorChoice.title()
            if valid(doorChoice.title(), "room") is True:
                if rooms[doorChoice].return_isLocked() is False:
                    change_room(doorChoice)
                else:
                    requiredItem = rooms[doorChoice].return_key()
                    if requiredItem in user["User"].return_inventory():
                        if yes_no("\nThe door to the {} is locked. Use {} to unlock it?: ".format(doorChoice, requiredItem)) is True:
                            rooms[doorChoice].unlock_room()
                            change_room(doorChoice)
                        else:
                            print_slow("Umm, alright. What are you saving that for? That's kind of why you should be carrying around that thing for...", standardSpeed, "wrap")
                    else:
                        print("It's locked, you need a key.")
            else:
                print("Door not recognized. Please try again.")
        elif choice in roomDescription:
            if valid(user["User"].return_currentroom(), "room") is True:
                print("{}: ".format(userCurrent))
                display_roomInfo(userCurrent)
        elif choice in getMap:
            clear_terminal()
            # save game map
            gameMapFile = open("game/map.txt", "r")
            gameMap = gameMapFile.read()
            gameMapFile.close()
            print(gameMap)
            print("\nYour Status:")
            print_slow("Strength: {}".format(user["User"].return_strength()), standardSpeed, "noWrap")
            print_slow("Infected Status: {}".format(user["User"].return_infected()), standardSpeed, "noWrap")
        elif choice in displayHelp:
            clear_terminal()
            print(choicesMessage)
        else:
            print("Error: command not recognized. Enter 'help' for more details.\n")


# yes or no text input
def yes_no(textToDisplay):
    yes = ['yes', 'y']
    no = ['no', 'n']
    while True:
        userChoice = input(textToDisplay)
        userChoice = userChoice.lower()
        if userChoice in yes:
            return True
        elif userChoice in no:
            return False
        else:
            print("\nEnter 'y' for yes or 'n' for no")


# prints out book line by line
def read_book(selectBook):
    for i in range(len(books[selectBook].return_book())):
        clear_terminal()
        print("{}: Page {} of {}\n".format(selectBook, i + 1, len(books[selectBook].return_book())))
        input("{}\n".format(books[selectBook].return_writing(i)))


def npc_loop(npc):
    """ method loops through talking with an npc"""
    scan = ['scan', 's', '1']
    ask = ['ask', 'a', '2']
    secret = ['secret', 'se', '3']
    bye = ['bye', 'b', '4']
    displayHelp = ['help', 'h', '5']

    npcChoiceMessage = """    Scan(s, 1) - ask to scan employee badge
    Ask(a, 2) - ask about work
    Secret(se, 3) - try to get more information
    Bye(b, 4) - say goodbye
    Help(h, 5) - display choices"""

    print("\nCurrent Options with {}:".format(npc))
    print(npcChoiceMessage)
    while True:
        userInput = input("\n'h' to display options\nEnter your action: ")
        if userInput in scan:
            print_slow("......................beep......boop", standardSpeed, "noWrap")
            clear_terminal()
            print("---Scan-Complete---")
            print_slow("{} {}".format(npc, npcs[npc].return_last()), standardSpeed, "noWrap")
            print_slow("Age: {}".format(npcs[npc].return_age()), standardSpeed, "noWrap")
            print_slow("Gender: {}".format(npcs[npc].return_gender()), standardSpeed, "noWrap")
            print_slow("Background: {}".format(npcs[npc].return_background()), standardSpeed, "wrap")
        elif userInput in ask:
            clear_terminal()
            print_slow("{}: {}".format(npc, npcs[npc].return_job()), standardSpeed, "noWrap")
        elif userInput in secret:
            clear_terminal()
            if secret_roll(75) is True:
                print_slow("{}: {}".format(npc, npcs[npc].return_secret()), standardSpeed, "noWrap")
            else:
                print_slow("{}: Sorry, I'm not permitted to tell you anything confidential.".format(npc), standardSpeed, "noWrap")
                npcs[npc].set_secret("Look, I already told you I can't tell you anything else.")
        elif userInput in bye:
            clear_terminal()
            print_slow("{}: {}".format(npc, npcs[npc].return_farewell()), standardSpeed, "noWrap")
            break
        elif userInput in displayHelp:
            print("Current Options with {}:".format(npc))
            print(npcChoiceMessage)


# input percentage of success and return outcome
def secret_roll(percentage):
    if random.randrange(1, 101, 1) < percentage:
        return True
    else:
        return False


def print_slow(text, delay, inf):
    """ print each character from text with a delay on the same line
    text = text to display
    delay = time between char
    inf = "noWrap" is ignore text wrap
    any other value from inf = text wrapping on"""
    textWrapLength = 50
    i = 0
    for char in text:
        if inf != "noWrap":
            i = i + 1
        if i < textWrapLength:
            print(char, end="")
            sys.stdout.flush()
        elif i >= textWrapLength and char is " ":
            print(char)
            i = 0
        else:
            print(char, end="")
            sys.stdout.flush()
        time.sleep(delay)
    print("")

# VALIDITY CHECKING
# checks validity on input with the dict keys from file input
def valid(testItem, typeTest):
    # define list of valid definitions
    roomList = list(rooms.keys())
    itemList = list(items.keys())
    npcList = list(npcs.keys())
    bookList = list(books.keys())
    userList = list(user.keys())

    # checks if the item has been created
    if testItem in roomList and typeTest is "room":
        return True
    elif testItem in itemList and typeTest is "item":
        return True
    elif testItem in npcList and typeTest is "npc":
        return True
    elif testItem in bookList and typeTest is "book":
        return True
    else:
        if typeTest is "room":
            return False
        elif typeTest is "item":
            return False
        elif typeTest is "npc":
            return False
        elif typeTest is "book":
            return False


# check if the items in list are built
def check_lists(listToCheck):
    if listToCheck is "RoomNPCs":
        roomList = list(rooms.keys())
        npcsToRemove = []
        for room in roomList:
            roomNPCs = rooms[room].return_npcPresent()
            for npc in roomNPCs:
                if valid(npc, "npc") is False:
                    npcsToRemove.append(npc)
            del_roomNPCs(room, npcsToRemove)
    elif listToCheck is "NPCitems":
        npcList = list(npcs.keys())
        itemsToRemove = []
        for npc in npcList:
            npcItems = npcs[npc].return_inventory()
            for item in npcItems:
                if valid(item, "item") is True:
                    pass
                elif valid(item, "book") is True:
                    pass
                elif valid(item, "item") is False and valid(item, "book") is False:
                    itemsToRemove.append(item)
                else:
                    print("Error: 'check_lists' Checking npcs items failed")
            del_npcItems(npc, itemsToRemove)
    elif listToCheck is "RoomItems":
        roomList = list(rooms.keys())
        itemsToRemove = []
        for room in roomList:
            roomItems = rooms[room].return_roomItems()
            for item in roomItems:
                if valid(item, "item") is True:
                    pass
                elif valid(item, "book") is True:
                    pass
                elif valid(item, "item") is False and valid(item, "book") is False:
                    itemsToRemove.append(item)
                else:
                    print("Error: 'check_lists' Checking room items failed")
            del_roomItems(room, itemsToRemove)
    else:
        print("Error 'check_list' listToCheck not recognized")


# delete room item passes from 'check_lists'
def del_roomItems(room, itemList):
    print("Warning: The following items are assigned to rooms, but don't have a .txt file in the 'items' folder:")
    print("{}\n".format(itemList))
    for item in itemList:
        rooms[room].del_roomItem(item)


# delete room npc passes from 'check_lists'
def del_roomNPCs(room, npcList):
    print("Warning: The following NPCs are assigned to rooms, but don't have a .txt file in the 'npcs' folder:")
    print("{}\n".format(npcList))
    for npc in npcList:
        rooms[room].remove_npc(npc)

# delete npc item passes from 'check_lists'
def del_npcItems(npc, itemList):
    print("Warning: The following items are assigned to NPCs, but don't have a .txt file in the 'items' folder:")
    print("{}\n".format(itemList))
    for item in itemList:
        npcs[npc].del_npcItem(item)
# END OF VALIDITY CHECKING

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


# for user
# edits user's current room (walks through door)
def change_room(newRoom):
    if valid(newRoom, "room") is True:
        user["User"].set_currentRoom(newRoom)
        print("Entered the {}".format(newRoom))
        display_roomInfo(newRoom)


# prints a description of the room
def display_roomInfo(room):
    wallColor = rooms[room].return_wallColor()
    floorDesc = rooms[room].return_floorDescription()
    roomStatus = rooms[room].return_roomStatus()
    doorNum = len(rooms[room].return_roomConnections())
    uniqueFeature = rooms[room].return_uniqueFeatures()
    if doorNum is 1:
        thereIs = "There is"
        door = "door"
    else:
        thereIs = "There are"
        door = "doors"
    print_slow("\nThe walls are {}, the floor is {}, and it's {}. {} {} {} in the room. {}".format(wallColor, floorDesc, roomStatus, thereIs, doorNum, door, uniqueFeature), standardSpeed, "wrap")


check_lists("RoomItems")  # checks lists to actual txt build files
check_lists("RoomNPCs")
check_lists("NPCitems")
welcome_message()  # displays welcome message
game_loop()  # user input loops

""" example and testing of adding people and rooms
without a file to pull it from
char1 = Person("Tubby", "Tubbs", 25,
               "this is the bg of Mr. Tubbs", 'm',
               75, 100, 0)

room1 = Room("Lab", "purple", ["smelly", "damp", "dirty"],
             "messy", "none", ["cold", "flooded"],
             ["key", "book", "table"], ["Tubby"])
room2 = Room("Kitchen", "purple", ["smelly", "damp", "dirty"],
             "messy", "none", ["cold", "flooded"],
             ["key", "book", "table"], ["Henry"])

rm_roomItem(room1, "key")


print(room1.return_roomStatus())
room_itemKeys(room1)

print("\n{}".format(room1.return_npcPresent()))
npc_changeroom(room1, char1, room2)
print("\n{}".format(room1.return_npcPresent()))
print("\n{}".format(room2.return_npcPresent()))"""
