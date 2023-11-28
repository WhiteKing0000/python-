import pygame

FPS = 60
white = (255, 255, 255)
width = 500 
height = 600
GREEN = (0, 255, 0)
#遊戲初始化
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('第一個射擊遊戲')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def _init_ (self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)



running = True
#遊戲迴圈
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     #更新遊戲
     

     
    #畫面顯示
    screen.fill(white)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()

