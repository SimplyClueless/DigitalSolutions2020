import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def Move(self, dirnx, dirny):
        pass

    def Draw(self, surface, eyes=False):
        pass

class Snake(object):
    def __init__(self, color, pos):
        pass

    def Move(self):
        pass

    def Reset(self, pos):
        pass

    def AddCube(self):
        pass

    def Draw(self, surface):
        pass

def DrawGrid(w, rows, surface):
    pass

def RedrawWindow(surface):
    pass

def RandomSnack(row, items):
    pass

def Message_Box(subject, content):
    pass

def Main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))
    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
    pass

Main()

