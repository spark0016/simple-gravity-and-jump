import pygame

SCREEN_HEIGHT = 600

x = 50
y = 0

num = 5

velocity = 0
acceleration = .1

gameRunning = True

display = pygame.display.set_mode((800, SCREEN_HEIGHT))

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    y += velocity
    velocity += acceleration

    if y >= SCREEN_HEIGHT - 50:
        velocity = -num
        num -= 2
    
    if num <= 0:
        num = 0
    
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        num = 5
    
    display.fill((255, 255, 255))

    pygame.draw.rect(display, (0, 0, 0), (x, y, 50, 50))

    pygame.display.update()

    pygame.time.delay(5)
