import pygame

class Character:
    def __init__(self, name, image_path, price):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.price = price
        self.is_unlocked = False
