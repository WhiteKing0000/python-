import pygame
import os

pygame.init()
white = (255, 255, 255)
WIDTH = 1200
HEIGHT = 900
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        key_pressed = pygame.key.get_pressed()
        self.rect.x += 2
        if self.rect.right > WIDTH:
            self.rect.x = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((white))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()