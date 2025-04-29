from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import asyncio

screen = Screen()
screen.setup(width= 600, height= 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "space")
run = True

async def cars():
    while run:
        await asyncio.sleep(0.5)
        car_manager.create_car()

async def behaviour():
    global run
    time = 0.1
    while run:
        await asyncio.sleep(time)
        screen.update()
        car_manager.car_move()

        #Detect level winning condition
        if player.ycor() >= 280:
            scoreboard.level_up()
            player.reset_player()
            car_manager.clear()
            time *= 0.8

        #Detect game over
        for car in car_manager.dealer:
            if player.distance(car) < 20:
                scoreboard.game_over()
                run = False

async def game():
    await asyncio.gather(asyncio.create_task(cars()), asyncio.create_task(behaviour()))

asyncio.run(game())
screen.exitonclick()
