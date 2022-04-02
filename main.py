from turtle import Screen
from player import Player
from wall import WallCreator
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
wall = WallCreator()


game_is_on = True
a = 0  # wynik gracza / przebyty dystans

while game_is_on:  # kod gry
    pass


screen.exitonclick()
