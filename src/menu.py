import pygame

import pygame

def draw_menu(screen):
    font = pygame.font.Font(None, 74)
    text = font.render('Lets Watch Ants Evolve', True, (0, 0, 50))
    screen.blit(text, (150, 150))

    font = pygame.font.Font(None, 36)
    start_text = font.render('Press Enter to Go Baby', True, (50, 0, 0))
    screen.blit(start_text, (200, 300))
