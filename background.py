import pygame

pygame.init()

window_width = 840
window_height = 650
window = pygame.display.set_mode((window_width, window_height))

background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()

clock = pygame.time.Clock()

# Начальное положение фонового изображения
background_y = 0

# Скорость прокрутки заднего фона игры
scroll_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Обновляем координату начального положения фонового изображения
    background_y += scroll_speed

    # Показываем часть фонового изображения на экране
    window.blit(background_image, (0, background_y - window_height))
    window.blit(background_image, (0, background_y))

    # Сбросить положение фонового изображение, если оно исчезнет с экрана
    if background_y >= window_height:
        background_y = 0

    # update the display
    pygame.display.update()

    # control the frame rate
    clock.tick(60)