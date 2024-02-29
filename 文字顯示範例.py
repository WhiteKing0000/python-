import pygame
import sys

# 初始化Pygame
pygame.init()

# 設置視窗大小
WIN_WIDTH, WIN_HEIGHT = 800, 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("顯示文字")

# 設置顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 設置字體
font = pygame.font.SysFont(None, 40)

# 定義文字類
class Text:
    def __init__(self, content, color, duration):
        self.content = content
        self.color = color
        self.duration = duration
        self.timer = 0
        self.visible = True  # 初始時文字可見

    def draw(self, surface, x, y):
        if self.visible:
            text_surface = font.render(self.content, True, self.color)
            surface.blit(text_surface, (x, y))

    def update(self, dt):
        self.timer += dt
        # 如果計時器超過指定的時間，則設置文字不可見
        if self.timer >= self.duration:
            self.visible = False

# 創建文字對象
text = Text("Hello, Pygame!", BLACK, 3000)  # 顯示時間為3秒

# 主循環
running = True
clock = pygame.time.Clock()
while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清除畫面
    win.fill(WHITE)

    # 更新和繪製文字
    text.draw(win, WIN_WIDTH/2 - 100, WIN_HEIGHT/2)
    text.update(clock.get_time())

    # 更新畫面
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()
sys.exit()