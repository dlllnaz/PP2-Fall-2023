import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_color = (255, 0, 0)  # Red
ball_pos = [width // 2, height // 2]  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] = max(ball_pos[1] - 20, ball_radius)  # Ensure the ball stays inside the screen
            elif event.key == pygame.K_DOWN:
                ball_pos[1] = min(ball_pos[1] + 20, height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_pos[0] = max(ball_pos[0] - 20, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] = min(ball_pos[0] + 20, width - ball_radius)

    screen.fill((255, 255, 255)) 

    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()
