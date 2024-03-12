# 載入遊戲套件
import pygame
import os

# 遊戲基本變數設定
pygame.init()
white = (255, 255, 255)
WIDTH = 1200
HEIGHT = 900
GREEN = (0, 255, 0)

#遊戲視窗初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')

#角色初始化和移動程式碼
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

#載入圖片
background_img = pygame.image.load(os.path.join("img", "300.jpeg")).convert()

# 建立角色陣列並將角色放入陣列
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 遊戲執行迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    #畫面顯示
    screen.fill((black))
    all_sprites.draw(screen)
    screen.blit(background_img, (0,0))
    pygame.display.update()

pygame.quit()
