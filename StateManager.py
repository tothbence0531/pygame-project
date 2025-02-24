import pygame
from config import *
from player import *
from terrain import *
from enemy import *

class StateManager:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state


class Start:
    def __init__(self, screen, stateManager):
        self.screen = screen
        self.stateManager = stateManager

    def run(self):
        self.screen.fill(RED)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.stateManager.set_state("level")


class Level:
    def __init__(self, level, stateManager):
        self.player = None
        self.level = level
        self.stateManager = stateManager

    def run(self):
        for i, row in enumerate(self.level):
            for j, column in enumerate(row):
                if column == "T":
                    Terrain(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
