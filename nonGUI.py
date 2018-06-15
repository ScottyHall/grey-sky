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


char1 = Person("Tubby", "Tubbs", 25,
               "this is the bg of Mr. Tubbs", 'm',
               75, 100, 0)

room1 = Room("Lab", "purple", ["smelly", "damp", "dirty"],
             "messy", "none", ["cold", "flooded"],
             {"key": "unlocks doors", "book": "a book", "table": "it's a table..."}, "Tubby")

print(char1.return_first())
print(char1.return_last())
print(char1.return_age())
print(char1.return_background())
print(char1.return_gender())
print(char1.return_strength())
print(char1.return_health())
print(char1.return_infected())
print(char1.return_currentroom())


def room_status(room):
    for i in range(len(room.return_roomStatus())):
        print("{} {}: {}".format(room.roomName, i + 1, room.roomStatus[i]))


print(room1.return_roomStatus())
room_status(room1)
