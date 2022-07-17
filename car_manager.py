from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list_of_car = []
        # self.move()


    def move(self):
        for cars in self.list_of_car:
            cars.setheading(180)
            cars.forward(STARTING_MOVE_DISTANCE)


    def creat_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            ncar = Turtle()
            ncar.penup()
            ncar.shape("square")
            ncar.shapesize(stretch_wid=1, stretch_len=2)
            ncar.color(random.choice(COLORS))
            ncar.setposition(x=310, y=random.randint(-250, 280))
            self.list_of_car.append(ncar)


