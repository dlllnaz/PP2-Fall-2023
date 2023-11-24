import pygame
import sys
from datetime import datetime
pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")
wallpaper = pygame.image.load("main-clock.png")  
mickey_right_hand = pygame.image.load("right-hand.png")  
mickey_left_hand = pygame.image.load("left-hand.png")  

def rotate(image, angle):
    return pygame.transform.rotate(image, angle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    current_time = datetime.now().time()
    minutes = current_time.minute
    seconds = current_time.second
    minutes_angle = -(minutes * 6) 
    seconds_angle = -(seconds * 6) 

    rotated_mickey_right_hand = rotate(mickey_right_hand, minutes_angle)
    rotated_mickey_left_hand = rotate(mickey_left_hand, seconds_angle)

    window.blit(pygame.transform.scale(wallpaper, (width, height)), (0, 0))

    window.blit(rotated_mickey_right_hand, (width // 2 - rotated_mickey_right_hand.get_width() // 2, height // 2 - rotated_mickey_right_hand.get_height() // 2))
    window.blit(rotated_mickey_left_hand, (width // 2 - rotated_mickey_left_hand.get_width() // 2, height // 2 - rotated_mickey_left_hand.get_height() // 2))
    pygame.display.flip()
    pygame.time.Clock().tick(1)
