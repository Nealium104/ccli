class Player:
    def __init__(self, name, role = "mage", exp = 0, age = 100, origin = 'yo mama'):
        self.name = name
        self.role = role
        self.exp = exp
        self.expquizzes_completed = []
        print(f"Player {self.name} loaded!")
