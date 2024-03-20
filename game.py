# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
square_width = 800
pixel_width = 25
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True


def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [
        random.randrange(*position_range),
        random.randrange(*position_range),
    ]


def reset():
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return [snake_pixel.copy()]


def isOutOfBounds():
    return (
        snake_pixel.bottom > square_width
        or snake_pixel.top < 0
        or snake_pixel.left < 0
        or snake_pixel.right > square_width
    )


# snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

# target
target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if isOutOfBounds():
        snake = reset()

    if snake_pixel.center == target.center:
        target.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = (0, -pixel_width)
    if keys[pygame.K_s]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = (-pixel_width, 0)
    if keys[pygame.K_d]:
        snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_pixel)

    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-1:]

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()
