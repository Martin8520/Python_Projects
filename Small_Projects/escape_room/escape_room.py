class Room:
    def __init__(self, description, actions):
        self.description = description
        self.actions = actions

    def describe(self):
        print(self.description)

    def list_actions(self):
        print("Available actions:")
        for i, action in enumerate(self.actions.keys(), 1):
            print(f"{i}. {action}")

    def take_action(self, action_num, inventory):
        action = list(self.actions.keys())[action_num - 1]
        return self.actions[action](inventory)


class Game:
    def __init__(self):
        self.inventory = []
        self.rooms = self.create_rooms()
        self.current_room = 0
        self.actions_taken = 0
        self.points = 5

    def create_rooms(self):
        # Room 1
        room1_description = """
        You are in a dimly lit room. There is a locked door to the north.
        You see a key on a table, a note on the wall, and a chest.
        """

        def room1_action1(inventory):
            if 'key' not in inventory:
                print("You take the key.")
                inventory.append('key')
                return False
            else:
                print("You already have the key.")
                return False

        def room1_action2(inventory):
            print("The note says: 'The key is the way out.'")
            return False

        def room1_action3(inventory):
            if 'key' in inventory:
                print("You unlock the door with the key and escape the room!")
                return True
            else:
                print("You need a key to unlock the door.")
                return False

        room1_actions = {
            'take key': room1_action1,
            'read note': room1_action2,
            'unlock door': room1_action3
        }
        room1 = Room(room1_description, room1_actions)

        # Room 2
        room2_description = """
        You are in a bright room with a window. There is a locked box, a rope, and a painting.
        You see a knife on the shelf.
        """

        def room2_action1(inventory):
            if 'knife' not in inventory:
                print("You take the knife.")
                inventory.append('knife')
                return False
            else:
                print("You already have the knife.")
                return False

        def room2_action2(inventory):
            if 'knife' in inventory:
                print("You cut the rope with the knife and use it to escape through the window.")
                return True
            else:
                print("You need a knife to cut the rope.")
                return False

        def room2_action3(inventory):
            print("The painting hides a keyhole, but you have no key.")
            return False

        room2_actions = {
            'take knife': room2_action1,
            'cut rope': room2_action2,
            'inspect painting': room2_action3
        }
        room2 = Room(room2_description, room2_actions)

        # Room 3
        room3_description = """
        You are in a dusty attic. There is a locked chest, a window, and a trapdoor in the floor.
        You see a crowbar, a flashlight, and a map on the table.
        """

        def room3_action1(inventory):
            if 'crowbar' not in inventory:
                print("You take the crowbar.")
                inventory.append('crowbar')
                return False
            else:
                print("You already have the crowbar.")
                return False

        def room3_action2(inventory):
            if 'flashlight' not in inventory:
                print("You take the flashlight.")
                inventory.append('flashlight')
                return False
            else:
                print("You already have the flashlight.")
                return False

        def room3_action3(inventory):
            if 'crowbar' in inventory:
                print("You use the crowbar to pry open the trapdoor and escape the attic!")
                return True
            else:
                print("You need a crowbar to open the trapdoor.")
                return False

        room3_actions = {
            'take crowbar': room3_action1,
            'take flashlight': room3_action2,
            'open trapdoor': room3_action3
        }
        room3 = Room(room3_description, room3_actions)

        # Room 4
        room4_description = """
        You are in a secret lab. There is a locked door to the north. 
        You see a computer, a safe, and a desk.
        """

        def room4_action1(inventory):
            print(
                "You turn on the computer and find a clue:"
                " 'The code is the answer to life, the universe, and everything.'")
            return False

        def room4_action2(inventory):
            if 'code' not in inventory:
                print("You take the note with the code '42'.")
                inventory.append('code')
                return False
            else:
                print("You already have the code.")
                return False

        def room4_action3(inventory):
            if 'code' in inventory and inventory.count('code') == 1:
                print("You use the code '42' to unlock the door and escape the lab!")
                return True
            else:
                print("You need the correct code to unlock the door.")
                return False

        room4_actions = {
            'use computer': room4_action1,
            'take code': room4_action2,
            'unlock door': room4_action3
        }
        room4 = Room(room4_description, room4_actions)

        return [room1, room2, room3, room4]

    def play(self):
        print("Welcome to the Escape Room Game!")
        while self.current_room < len(self.rooms) and self.points > 0:
            self.rooms[self.current_room].describe()
            while self.actions_taken < 5 or not self.rooms[self.current_room].take_action(3, self.inventory):
                self.rooms[self.current_room].list_actions()
                try:
                    action_num = int(input("Choose an action (1, 2, or 3): "))
                    if action_num not in [1, 2, 3]:
                        raise ValueError
                    if self.rooms[self.current_room].take_action(action_num, self.inventory):
                        break
                    else:
                        self.actions_taken += 1
                        if self.actions_taken >= 5:
                            print("You have taken the maximum allowed actions for this room.")
                            break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 3.")
                self.points -= 1
                if self.points > 0:
                    print(f"Incorrect choice. You lose 1 point. Points remaining: {self.points}")
                    print(f"The unknown entity is getting closer... you can feel its presence.")
                else:
                    print("You have run out of points. The unknown entity reaches you. Game over!")
                    return
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
