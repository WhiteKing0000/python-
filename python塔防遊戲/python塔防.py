# 載入遊戲套件
import pygame
import os



# 遊戲基本變數設定
FPS = 60
pygame.init()
white = (255, 255, 255)
WIDTH = 1200
HEIGHT = 700
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

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


class startbutton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(startb, (800, 700))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()



# 建立角色陣列並將角色放入陣列
all_sprites = pygame.sprite.Group()
#Player()
all_sprites.add(Player())
all_sprites.add(background())
all_sprites.add(startbutton())

button_rect = startbutton.rect
# 遊戲執行迴圈
running = True
while running:
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #print('mouse button down at:', mouse_x, mouse_y)
        if button_rect.collidepoint(mouse_x, mouse_y):
            print('mouse clicked on the object')
    #更新遊戲
    all_sprites.update()
    #畫面顯示
    screen.fill((191, 239, 245))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()