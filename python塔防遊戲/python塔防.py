#在mac不是用pip是pip3
# 載入遊戲套件
import pygame
import os
import pyautogui
import sys


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
#字體
font = pygame.font.SysFont(None, 40)

#遊戲視窗初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')

#確保路徑正確
os.chdir('/Users/Felix-SharleenHome/Desktop/python塔防遊戲')

# 匯入圖片
road_img = pygame.image.load(os.path.join('遊戲素材', 'road.png')).convert()
backimage = pygame.image.load(os.path.join('遊戲素材', '冰川邊景有雪板.png')).convert()
startb = pygame.image.load(os.path.join('遊戲素材', '開始按鈕.png')).convert()

#角色初始化和移動程式碼

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
#Player()
all_sprites.add(Player())
all_sprites.add(background())




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
                text = font.render('game start!!!', True, BLACK)
                text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
                screen.blit(text, text_rect)
                pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            Button.color = GRAY

    #偵測滑鼠是否碰到並按下按鈕
    
    #更新遊戲
    all_sprites.update()
    #畫面顯示
    screen.fill((191, 239, 245))
    all_sprites.draw(screen)
    Button.draw(screen)
    pygame.display.update()

pygame.quit()