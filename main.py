# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

height_offset = 100
start_line = pygame.Vector2(-screen.get_width(), screen.get_height() / 2 + height_offset)
end_line = pygame.Vector2(screen.get_width(), screen.get_height() / 2 + height_offset)

gravity = 0
gravity_acceleration = -10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.line(screen, 'black', start_line, end_line)

    if player_pos.y > start_line.y:
        gravity -= gravity_acceleration
        player_pos.y -= gravity
    else:
        gravity = 0

    pygame.draw.circle(screen, "black", player_pos, 10)

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

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
