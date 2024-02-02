# 載入遊戲套件
import pygame
import os
from PIL import Image

# 遊戲基本變數設定
FPS = 60
pygame.init()
white = (255, 255, 255)
WIDTH = 1200
HEIGHT = 900
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#遊戲視窗初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')

# 匯入圖片
background_img = pygame.image.load(os.path.join('遊戲素材', '冰川簡單版.png')).convert()

#角色初始化和移動程式碼
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(background_img, (1200, 800))
        self.image.set_colorkey(BLACK)
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)


# 建立角色陣列並將角色放入陣列
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 遊戲執行迴圈
running = True
while running:
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    all_sprites.update()
    #畫面顯示
    screen.fill((white))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()