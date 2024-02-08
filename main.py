# Example file showing a circle moving on screen
import pygame
import random

screen = pygame.display.set_mode((1280, 720))

width, height = screen.get_width(), screen.get_height()

height_offset = 100
ball_size = 10

ground_height = screen.get_height() / 2 + height_offset - ball_size


class MovingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        this_obj = random.randint(0, 1)
        x, y = 60, 60
        if this_obj:
            x, y = 30, 90
        self.image = pygame.Surface((x, y))

        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.x = width
        duck = 0
        if random.randint(0, 1):
            duck = -40
        self.rect.y = ground_height - y + 10 + duck
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed


# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2 - 300, screen.get_height() / 2)

start_line = pygame.Vector2(-screen.get_width(), screen.get_height() / 2 + height_offset)
end_line = pygame.Vector2(screen.get_width(), screen.get_height() / 2 + height_offset)

gravity = 0
gravity_acceleration = 50  # Change gravity to positive value

# Create a sprite group for the objects
all_objects = pygame.sprite.Group()

# Set up a timer for object spawning
spawn_timer = pygame.time.get_ticks()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Check if 10 seconds have passed since the last spawn
    current_time = pygame.time.get_ticks()
    if current_time - spawn_timer >= 3000:  # 10 seconds in milliseconds
        # Spawn a new object
        new_object = MovingObject()
        all_objects.add(new_object)

        # Reset the timer
        spawn_timer = current_time

    # Update all objects
    all_objects.update()

    all_objects = pygame.sprite.Group([obj for obj in all_objects if obj.rect.x + obj.rect.width > 0])

    all_objects.draw(screen)

    pygame.draw.line(screen, 'black', start_line, end_line)

    if player_pos.y < start_line.y:
        gravity += gravity_acceleration
        new_pos = min(player_pos.y + gravity * dt, ground_height)
        player_pos.y = new_pos

    pygame.draw.circle(screen, "black", player_pos, ball_size)

    for this_object in all_objects:
        if this_object.rect.collidepoint(player_pos):
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y == ground_height:
        gravity = -650
    elif keys[pygame.K_w] and gravity < -300:
        gravity -= 35
    if keys[pygame.K_s]:
        pass

    # Generate an object moving the left every 10 seconds
    object_rect = pygame.Rect(screen.get_width() // 2, screen.get_height() // 2, 50, 50)
    object_speed = 5

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
