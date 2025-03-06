import pygame
from player import *
from terrain import *
from config import *
from camera import *
from enemy import *
from debug import*

pygame.init()
font = pygame.font.SysFont('Arial', 30)

class Game:
    def __init__(self):
        self.player = None
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = Camera()
        self.terrain = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.running = True
        self.clock = pygame.time.Clock()
        self.create_tilemap()
        self.stateManager = StateManager("start")
        self.start = Start(self.screen, self.stateManager)
        self.level = Level(self, self.stateManager)
        self.fight = Fight(self.screen, self.stateManager, self)
        self.states = {
            "start": self.start,
            "level": self.level,
            "fight": self.fight
        }
        self.debug = Debug(self.screen, font)

    def create_tilemap(self):

        for i, row in enumerate(SAFEHOUSE):
            for j, column in enumerate(row):
                if column == "T":
                    Terrain(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)

    def loop(self):

        while self.running:

            self.clock.tick(60)
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.states[StateManager.get_state(self.stateManager)].run()

            pygame.display.flip()

        pygame.quit()


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
        self.level = level
        self.stateManager = stateManager


    def run(self):
        self.level.all_sprites.custom_draw(self.level.player)
        self.level.all_sprites.update()

class Fight:
    def __init__(self, screen, stateManager, game):
        self.screen = screen
        self.stateManager = stateManager
        self.value = ""
        self.game = game
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.value = self.value[:-1]
                    else:
                        self.value += event.unicode
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False

            game.debug.draw(self.value)
            pygame.display.flip()

game = Game()
game.loop()