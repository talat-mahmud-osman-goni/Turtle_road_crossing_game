import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")

    car.create_car()
    car.move_car()

    # detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.result()
        car.level_up()
        player.begin_position()

screen.exitonclick()
