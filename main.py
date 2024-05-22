def main():
    name = input("What's your name, kind sir?\n")
    age = input("Tell me, how old are you? I need a number, lad.\n")
    origin = input("Tell me, what land do you hail from?\n")
    role = input("And be you fighter, mage, or rogue?\n")
    player1 = Player(name, age, origin, role)

class Player:
    def __init__(self, name, age, origin, role):
        self.name = name
        self.age = age
        self.origin = origin
        self.role = role
        print(f"New player {self.name} created!")

main()
