class Room:
    def __init__(self, description, items, actions):
        self.description = description
        self.items = items
        self.actions = actions

    def describe(self):
        print(self.description)

    def take_action(self, action, inventory):
        if action in self.actions:
            return self.actions[action](inventory)
        else:
            print("Action not available.")
            return False


class Game:
    def __init__(self):
        self.inventory = []
        self.rooms = self.create_rooms()
        self.current_room = 0

    def create_rooms(self):
        # Room 1
        room1_description = """
        You are in a dimly lit room. There is a locked door to the north.
        You see a key on a table and a note on the wall.
        """
        room1_items = ['key', 'note']

        def room1_action1(inventory):
            if 'key' in inventory:
                print("You unlock the door with the key.")
                return True
            else:
                print("You need a key to unlock the door.")
                return False

        def room1_action2(inventory):
            if 'note' not in inventory:
                print("You take the note.")
                inventory.append('note')
                return False
            else:
                print("You already have the note.")
                return False

        def room1_action3(inventory):
            if 'key' not in inventory:
                print("You take the key.")
                inventory.append('key')
                return False
            else:
                print("You already have the key.")
                return False

        room1_actions = {
            'unlock door': room1_action1,
            'take note': room1_action2,
            'take key': room1_action3
        }
        room1 = Room(room1_description, room1_items, room1_actions)

        # Room 2
        room2_description = """
        You are in a bright room with a window. There is a locked box and a rope.
        You see a knife on the shelf and a map on the floor.
        """
        room2_items = ['knife', 'map']

        def room2_action1(inventory):
            if 'knife' not in inventory:
                print("You take the knife.")
                inventory.append('knife')
                return False
            else:
                print("You already have the knife.")
                return False

        def room2_action2(inventory):
            if 'map' not in inventory:
                print("You take the map.")
                inventory.append('map')
                return False
            else:
                print("You already have the map.")
                return False

        def room2_action3(inventory):
            if 'knife' in inventory:
                print("You cut the rope with the knife and use it to escape through the window.")
                return True
            else:
                print("You need a knife to cut the rope.")
                return False

        room2_actions = {
            'take knife': room2_action1,
            'take map': room2_action2,
            'cut rope': room2_action3
        }
        room2 = Room(room2_description, room2_items, room2_actions)

        return [room1, room2]

    def play(self):
        print("Welcome to the Escape Room Game!")
        while self.current_room < len(self.rooms):
            self.rooms[self.current_room].describe()
            action = input("What would you like to do? ")
            if self.rooms[self.current_room].take_action(action, self.inventory):
                self.current_room += 1
                if self.current_room < len(self.rooms):
                    print("You move to the next room.")
                else:
                    print("Congratulations! You have escaped!")
            print("Your inventory: ", self.inventory)


if __name__ == "__main__":
    game = Game()
    game.play()
