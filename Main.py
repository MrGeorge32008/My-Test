import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up game objects
paddle_width = 10
paddle_height = 60
ball_radius = 10

player_paddle_x = 10
player_paddle_y = window_height // 2 - paddle_height // 2
computer_paddle_x = window_width - paddle_width - 10
computer_paddle_y = window_height // 2 - paddle_height // 2

ball_x = window_width // 2
ball_y = window_height // 2
ball_dx = random.choice([-2, 2])
ball_dy = random.choice([-2, 2])

player_paddle_rect = pygame.Rect(player_paddle_x, player_paddle_y, paddle_width, paddle_height)
computer_paddle_rect = pygame.Rect(computer_paddle_x, computer_paddle_y, paddle_width, paddle_height)
ball_rect = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle_rect.top > 0:
        player_paddle_rect.y -= 3
    if keys[pygame.K_s] and player_paddle_rect.bottom < window_height:
        player_paddle_rect.y += 3
    if keys[pygame.K_UP] and computer_paddle_rect.top > 0:
        computer_paddle_rect.y -= 3
    if keys[pygame.K_DOWN] and computer_paddle_rect.bottom < window_height:
        computer_paddle_rect.y += 3

    # Update ball position
    ball_rect.x += ball_dx
    ball_rect.y += ball_dy

    # Handle ball collision with walls
    if ball_rect.top < 0 or ball_rect.bottom > window_height:
        ball_dy *= -1

    # Handle ball collision with paddles
    if ball_rect.colliderect(player_paddle_rect) or ball_rect.colliderect(computer_paddle_rect):
        ball_dx *= -1

    # Draw game objects
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player_paddle_rect)
    pygame.draw.rect(window, WHITE, computer_paddle_rect)
    pygame.draw.ellipse(window, WHITE, ball_rect)
    pygame.draw.aaline(window, WHITE, (window_width // 2, 0), (window_width // 2, window_height))
    
    # Update the game display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
