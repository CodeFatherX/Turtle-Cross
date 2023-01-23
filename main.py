import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.right, key="Right")
screen.onkeypress(fun=player.down, key="Down")
screen.onkeypress(fun=player.left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == 290:
        player.level_complete()
        scoreboard.next_level()
        car_manager.move_speed *= 0.9

screen.exitonclick()
