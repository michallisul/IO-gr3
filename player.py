from turtle import Turtle

class Player(Turtle):
    def __init__(self): #utworzenie żółwia
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()

    def fall(self): #opadanie żółwia
        new_y = self.ycor() - 5
        self.goto(self.xcor(),new_y)

    def jump(self): #podskoczenie żółwia
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
