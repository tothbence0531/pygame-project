import pygame
from config import *

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Apply the camera offset to an entity (e.g., a sprite)
        entity.rect.topleft = (entity.rect.x - self.camera.x, entity.rect.y - self.camera.y)

    def update(self, target):
        # Center the camera on the target (e.g., the player)
        self.camera.x = target.rect.centerx - SCREEN_WIDTH // 2
        self.camera.y = target.rect.centery - SCREEN_HEIGHT // 2

        # Clamp the camera to stay within the map bounds
        self.camera.x = max(0, min(self.camera.x, self.width - SCREEN_WIDTH))
        self.camera.y = max(0, min(self.camera.y, self.height - SCREEN_HEIGHT))
