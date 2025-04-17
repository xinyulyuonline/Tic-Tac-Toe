import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

black = pygame.image.load("images/load/black.png").convert_alpha()
white = pygame.image.load("images/load/white.png")
icon_image = pygame.image.load("icon.png").convert_alpha()

pygame.display.set_icon(icon_image)
pygame.display.set_caption("Tic Tac Toe")

alpha = 255
black.set_alpha(alpha)

size_icon = icon_image.get_size()
min_size = (size_icon[0] - 150, size_icon[1] - 150)
max_size = (size_icon[0] - 100, size_icon[1] - 100)

time_passed = 0
start_time = pygame.time.get_ticks()

loading = True
while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = False

    if pygame.time.get_ticks() - start_time >= 3000:
        loading = False

    if alpha > 0:
        alpha -= 1
        black.set_alpha(max(0, alpha))

    time_passed += 0.05
    scale_factor_icon = (math.sin(time_passed) + 1) / 2
    new_width = int(min_size[0] + (max_size[0] - min_size[0]) * scale_factor_icon)
    new_height = int(min_size[1] + (max_size[1] - min_size[1]) * scale_factor_icon)

    icon_image_scaled = pygame.transform.smoothscale(icon_image, (new_width, new_height))
    icon_scaled_rect = icon_image_scaled.get_rect(center=(400, 400))

    screen.blit(white, (0, 0))
    screen.blit(icon_image_scaled, icon_scaled_rect)
    screen.blit(black, (0, 0))

    pygame.display.flip()
    clock.tick(60)

font = pygame.font.Font("fonts/Bungee-Regular.ttf", 60)
text = font.render("Tic Tac Toe", True, (75, 0, 130))

pygame.mixer.music.load("music/menu.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

    screen.fill((200, 160, 255))
    screen.blit(text, text.get_rect(center=(400, 150)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

pygame.mixer.music.stop()
