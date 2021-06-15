import pygame as p
import numpy as np
import random as r
import time as t

grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ])

for row in range(0, 9):
    for col in range(0, 9):
        number = r.randrange(0, 100)
        if number <= 45:
            grid[row][col] = 1

p.init()
width = 500
height = 500
screen = p.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
run = True

def board():
    print(grid)
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                p.draw.rect(screen, black, [row * 50, col * 50, 50, 50])
                p.display.update()

            else:
                p.draw.rect(screen, white, [row * 50, col * 50, 50, 50])
                p.display.update()


    run = False


while run:
    for event in p.event.get():

        if event.type == p.QUIT:
            run =False

        if event.type == p.KEYDOWN:
            board()





