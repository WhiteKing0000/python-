import pygame


FPS = 60
WIDGHT = 500
HEIGHT = 600
#遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDGHT, HEIGHT))
clock = pygame.time.Clock()
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