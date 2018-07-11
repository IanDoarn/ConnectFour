class Player:

    def __init__(self, color):
        self.color = color
        self.move = None

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color