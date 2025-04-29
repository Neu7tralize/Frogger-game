from turtle import Turtle

START_Y = -280
MOVE_UNIT = 10
HEADING = 90

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(HEADING)
        self.sety(START_Y)
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_UNIT)

    def reset_player(self):
        self.sety(START_Y)
