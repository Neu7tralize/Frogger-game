from turtle import Turtle
import random as r

MOVE_UNIT = 10

class CarManager:

    def __init__(self):
        self.dealer = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(r.random(), r.random(), r.random())
        new_car.penup()
        random_y = r.randrange(-240, 241, 20)
        new_car.goto(320, random_y)
        self.dealer.append(new_car)

    def car_move(self):
        for car in self.dealer:
            car.backward(MOVE_UNIT)
            if car.xcor() < -320:
                del self.dealer[0]

    def clear(self):
        for car in self.dealer:
            car.ht()
        self.dealer.clear()
