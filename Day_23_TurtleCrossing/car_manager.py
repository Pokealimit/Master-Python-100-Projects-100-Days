from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        # self.round = 0
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = r.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(r.choice(COLORS))
            new_car.penup()
            random_y = r.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            # new_x = car.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * self.round
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())
            # car.backward(STARTING_MOVE_DISTANCE)

    # def detect_collision(self, user) -> bool:
    #     for car in self.car_list:
    #         if abs(user.ycor() - car.ycor()) < 15 and car.distance(user) < 20:
    #             return True
            
    def clear_all_cars(self):
        for car in self.car_list:
            car.hideturtle()
        self.car_list.clear()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT