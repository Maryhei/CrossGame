import time
from turtle import Screen

import car_manager
import scoreboard
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("CROSS GAME")
screen.setup(width=600, height=600)
screen.tracer(0)
cars = CarManager()
Player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(fun=Player.up, key="Up")
screen.onkey(fun=Player.down, key="Down")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.creat_car()
    cars.move()
    screen.update()
    if Player.ycor() > player.FINISH_LINE_Y:
        scoreboard.LEVEL += 1
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        Player.refresh()
        score.clear()
        score.new_score()
    for carss in cars.list_of_car:
        # distance = Player.ycor() - carss.ycor
        if Player.ycor() - carss.ycor() > 20 or Player.ycor() - carss.ycor() < 20:
            if Player.distance(carss) < 33:
                game_is_on = False
                score.game_over()
screen.exitonclick()