import pygame

pygame.init()
pygame.mixer.init()
tracks = ['1.mp3', '2.mp3', '3.mp3']
track_pos = 0
is_paused = False
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("mp3")
BLUE = (0, 128, 255)
WHITE = (255, 255, 255)
def draw_buttons():
    screen.fill(BLUE)
    font = pygame.font.SysFont(None, 36)
    play_buttton = font.render('Play', True, WHITE)
    stop_buttton = font.render('Stop', True, WHITE)
    next_buttton = font.render('Next', True, WHITE)
    prev_buttton = font.render('Prev', True, WHITE)
    screen.blit(play_buttton, (20, 20))
    screen.blit(stop_buttton, (20, 70))
    screen.blit(next_buttton, (20, 120))
    screen.blit(prev_buttton, (20, 170))
pygame.mixer.music.load(tracks[track_pos])
pygame.mixer.music.play(-1)
running = True
while running:
    draw_buttons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 20 <= mouse[0] <= 120 and 20 <= mouse[1] <= 50:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.play()
            elif 20 <= mouse[0] <= 120 and 70 <= mouse[1] <= 100:
                pygame.mixer.music.stop()
                is_paused = False
            elif 20 <= mouse[0] <= 120 and 120 <= mouse[1] <= 150:
                track_pos = (track_pos + 1) % len(tracks)
                pygame.mixer.music.load(tracks[track_pos])
                pygame.mixer.music.play(-1)
            elif 20 <= mouse[0] <= 120 and 170 <= mouse[1] <= 200:
                track_pos = (track_pos - 1) % len(tracks)
                pygame.mixer.music.load(tracks[track_pos])
                pygame.mixer.music.play(-1)
    pygame.display.flip()
    pygame.time.delay(100)
pygame.quit()