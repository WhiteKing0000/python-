import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置游戏窗口大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame 文字显示示例")

# 设置文本字体和大小
font = pygame.font.Font(None, 36)

# 设置文本内容和颜色
text = font.render("这是要显示的文本", True, (255, 255, 255))

# 设置文本位置
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)

# 控制文本显示的变量和时间
show_text = False
show_start_time = 0
show_duration = 2000  # 显示时间，以毫秒为单位

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 按下空格键切换文本的显示状态，并记录开始显示的时间
                show_text = True
                show_start_time = pygame.time.get_ticks()

    # 绘制背景
    screen.fill((0, 0, 0))

    # 根据条件绘制文本
    if show_text:
        current_time = pygame.time.get_ticks()
        if current_time - show_start_time < show_duration:
            screen.blit(text, text_rect)
        else:
            show_text = False

    # 刷新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
