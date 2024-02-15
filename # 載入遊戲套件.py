# 載入遊戲套件
import pygame
import os

# 遊戲基本變數設定
pygame.init()

white = (255, 255, 255)
WIDTH = 860
HEIGHT = 573
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

font_name = os.path.join('JasonHandwriting4.ttf')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#初始畫面
def draw_init():
    draw_text(screen, '地球暖化塔防！', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, '點擊防禦塔標示並拖曳來擺放防禦塔～', 22, WIDTH/2, HEIGHT/2)
    draw_text(screen, '按下空白鍵開始', 22, WIDTH/2, HEIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False

#遊戲視窗初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('地球暖化塔防遊戲')

#載入圖片
#background_img = pygame.image.load(os.path.join("img", "冰層圖2.png")).convert()

#圖片放大
#scale_factor = 2

#original_size = background_img.get_size()

#scaled_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))

#scaled_image = pygame.transform.scale(background_img, scaled_size)


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


# 建立角色陣列並將角色放入陣列
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 遊戲執行迴圈
show_init = True
running = True
while running:
    if show_init:
        draw_init()
        show_init = False

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()

    #畫面顯示
    screen.fill((BLACK))
    all_sprites.draw(screen)
    #screen.blit(background_img, (0,0))
    pygame.display.update()
    pygame.display.flip()


pygame.quit()