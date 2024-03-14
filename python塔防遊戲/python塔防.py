#在mac不是用pip是pip3
# 載入遊戲套件
import pygame
import os
import pyautogui
import sys
import time


# 遊戲基本變數設定
FPS = 60
pygame.init()
white = (255, 255, 255)
WIN_WIDTH, WIN_HEIGHT = 800, 600
WIDTH = 1200
HEIGHT = 700
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
show_start = True
#字體
font = pygame.font.SysFont(None, 40)

#遊戲視窗初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')



# 匯入圖片
road_img = pygame.image.load(os.path.join('遊戲素材', 'road.png')).convert()
backimage = pygame.image.load(os.path.join('遊戲素材', '冰川邊景有雪板.png')).convert()
startb = pygame.image.load(os.path.join('遊戲素材', '開始按鈕.png')).convert()
trash_can = pygame.image.load(os.path.join('遊戲素材', '垃圾桶怪物.png')).convert()


class attack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(trash_can, (120, 100))
        #self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 0)
        

        

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if self.rect.y != 200:
            self.rect.y += 1
        elif self.rect.x != 530:
            self.rect.x += 1
        elif self.rect.y != 650:
            self.rect.y += 1
                
          
            


#設定敵方進攻路徑素材
class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(road_img, (800, 700))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()


class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(backimage, (800, 700))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

#定義按鈕類物件
class button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.text != '':
            font_surface = font.render(self.text, True, BLACK)
            win.blit(font_surface, (self.rect.x + self.rect.width/2 - font_surface.get_width()/2, 
                                    self.rect.y + self.rect.height/2 - font_surface.get_height()/2))

    def is_over(self, pos):
        return self.rect.collidepoint(pos)



# 建立角色陣列並將角色放入陣列
all_sprites = pygame.sprite.Group()
#建立按鈕
Button = button(800, 0, 200, 100, GRAY, 'press me')
first_attack = attack(100, 50)
#Player()
all_sprites.add(Player())
all_sprites.add(background())
all_sprites.add(first_attack)

screen.fill((191, 239, 245))
all_sprites.draw(screen)
Button.draw(screen)
text = font.render('game start!!!', True, BLACK)
text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))

# 遊戲執行迴圈
running = True

while running:
    #關掉遊戲視窗
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #如果滑鼠點擊按鈕
            if Button.is_over(pygame.mouse.get_pos()):
                Button.color = BLACK
                pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            Button.color = GRAY

    
    all_sprites.update()
    all_sprites.draw(screen)
    #畫面顯示

    #刷新螢幕
    pygame.display.update()    
pygame.quit()