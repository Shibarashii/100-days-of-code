import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    car_manager.spawn_car()

    if player.ycor() > 280:
        player.reset()
        scoreboard.level += 1
        scoreboard.show_level()
        car_manager.increase_move_speed()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()
