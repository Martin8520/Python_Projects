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
        self.actions_taken = 0

    def create_rooms(self):
        # Room 1
        room1_description = """
        You are in a dimly lit room. There is a locked door to the north.
        You see a key on a table, a note on the wall, a bookshelf, a rug, and a chest.
        """
        room1_items = ['key', 'note', 'book', 'hidden compartment', 'lockpick']

        def room1_action1(inventory):
            if 'key' not in inventory:
                print("You take the key.")
                inventory.append('key')
                return False
            else:
                print("You already have the key.")
                return False

        def room1_action2(inventory):
            if 'note' not in inventory:
                print("You take the note. It has a clue: 'Look under the rug.'")
                inventory.append('note')
                return False
            else:
                print("You already have the note.")
                return False

        def room1_action3(inventory):
            print("You search the bookshelf and find a book titled 'Secrets of the Hidden'.")
            if 'book' not in inventory:
                inventory.append('book')
            return False

        def room1_action4(inventory):
            print("You lift the rug and find a hidden compartment.")
            if 'hidden compartment' not in inventory:
                inventory.append('hidden compartment')
            return False

        def room1_action5(inventory):
            if 'hidden compartment' in inventory and 'lockpick' not in inventory:
                print("You open the hidden compartment and find a lockpick.")
                inventory.append('lockpick')
                return False
            else:
                print("There is nothing else under the rug.")
                return False

        def room1_action6(inventory):
            if 'lockpick' in inventory:
                print("You unlock the door with the lockpick and escape the room!")
                return True
            elif 'key' in inventory:
                print("You unlock the door with the key and escape the room!")
                return True
            else:
                print("You need a key or a lockpick to unlock the door.")
                return False

        room1_actions = {
            'take key': room1_action1,
            'take note': room1_action2,
            'search bookshelf': room1_action3,
            'lift rug': room1_action4,
            'open compartment': room1_action5,
            'unlock door': room1_action6
        }
        room1 = Room(room1_description, room1_items, room1_actions)

        # Room 2
        room2_description = """
        You are in a bright room with a window. There is a locked box, a rope, a painting, a cabinet, and a drawer.
        You see a knife on the shelf and a map on the floor.
        """
        room2_items = ['knife', 'map', 'key', 'box', 'rope']

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
                print("You take the map. It has a clue: 'Look behind the painting.'")
                inventory.append('map')
                return False
            else:
                print("You already have the map.")
                return False

        def room2_action3(inventory):
            print("You look behind the painting and find a hidden key.")
            if 'key' not in inventory:
                inventory.append('key')
            return False

        def room2_action4(inventory):
            if 'key' in inventory:
                print("You unlock the box and find a rope.")
                if 'rope' not in inventory:
                    inventory.append('rope')
                return False
            else:
                print("You need a key to unlock the box.")
                return False

        def room2_action5(inventory):
            print("You open the cabinet and find nothing useful.")
            return False

        def room2_action6(inventory):
            if 'knife' in inventory and 'rope' in inventory:
                print("You cut the rope with the knife and use it to escape through the window.")
                return True
            else:
                print("You need a knife and a rope to escape.")
                return False

        room2_actions = {
            'take knife': room2_action1,
            'take map': room2_action2,
            'look behind painting': room2_action3,
            'unlock box': room2_action4,
            'open cabinet': room2_action5,
            'cut rope': room2_action6
        }
        room2 = Room(room2_description, room2_items, room2_actions)

        return [room1, room2]

    def play(self):
        print("Welcome to the Escape Room Game!")
        while self.current_room < len(self.rooms):
            self.rooms[self.current_room].describe()
            while self.actions_taken < 5 or not self.rooms[self.current_room].take_action('unlock door',
                                                                                          self.inventory):
                action = input("What would you like to do? ")
                self.rooms[self.current_room].take_action(action, self.inventory)
                self.actions_taken += 1
            self.actions_taken = 0
            self.current_room += 1
            if self.current_room < len(self.rooms):
                print("You move to the next room.")
            else:
                print("Congratulations! You have escaped!")
            print("Your inventory: ", self.inventory)


if __name__ == "__main__":
    game = Game()
    game.play()
