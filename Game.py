import pygame

pygame.init()
screen = pygame.display.set_mode((1200,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)

while running:
        #poll for events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
    # fill screen with color to whipe away previous frames
    screen.fill("tan")

    # RENDER GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) /1000

pygame.quit()   
