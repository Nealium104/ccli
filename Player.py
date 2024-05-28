class Player:
    def __init__(self, name, role, exp = 0, age = 100, origin = 'yo mama'):
        self.name = name
        self.role = role
        self.exp = exp
        print(f"New player {self.name} created!")
