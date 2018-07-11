from peg import Peg
from player import Player

BOARD_DIMENSIONS = {'x': 7, 'y': 6}
EMPTY_SPACE = '_'
JUNCTION = '+'
SEPARATION = '---'


class GameBoard:

    def __init__(self, players = None):
        self.players = players
        self.board = [[Peg(EMPTY_SPACE) for _ in range(BOARD_DIMENSIONS['x'])] for _ in range(BOARD_DIMENSIONS['y'])]

        self.colors = [x.color for x in players]

        self.current_color = None
        self.current_player = None

    def play(self, player):
        """
        Play the current players move
        :param player: Player Object
        :return: Bool
        """
        self.current_player = player
        self.current_color = player.color
        if self.add(player.move, player.color):
            return True

    def add(self, x, color):
        """
        Add a peg to the board
        :param x: column number
        :return: None
        """
        for i, row in enumerate(reversed(self.board)):
            if i <= BOARD_DIMENSIONS['y']:
                if row[x].color == EMPTY_SPACE:
                    row[x].color = color
                    return True
        return False


    def __str__(self):
        """
        Print the current board
        :return:
        """
        s = ""
        s += "  +"
        s += ("{}{}".format(SEPARATION, JUNCTION)) * BOARD_DIMENSIONS['x']
        s += "\n"
        # l = [x for x in reversed(range(BOARD_DIMENSIONS['y']))]
        for i, row in enumerate(self.board):
            s += "  |"
            for cell in row:
                s += " {} |".format(cell.color)
            s += "\n"
            s += "  +"
            s += ("{}{}".format(SEPARATION, JUNCTION)) * BOARD_DIMENSIONS['x']
            s += "\n"

        s += "  "

        for i in range(BOARD_DIMENSIONS['x']):
            s += "  {} ".format(str(i))

        return s


if __name__ == '__main__':

    p1 = Player('R')
    p2 = Player('B')

    gb = GameBoard(players=[p1, p2])

    p1.move = 0
    gb.play(p1)

    p2.move = 0
    gb.play(p2)

    p1.move = 1
    gb.play(p1)

    p2.move = 0
    gb.play(p2)


    print(gb)
