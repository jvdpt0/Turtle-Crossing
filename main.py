import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

count = 0
car_name = 0

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= player.target:
        player.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()