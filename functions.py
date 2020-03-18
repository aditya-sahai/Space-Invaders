import pygame
import random
import sys

def check_event():
    """Function to check the events of pygame."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return 0
            elif event.key == pygame.K_RIGHT:
                return 1
            elif event.key == pygame.K_SPACE:
                return 2

def draw_game_window(screen_dict, ShipClass, AlienClass):
    screen_dict['surface'].fill(screen_dict['bg_color'])
    ShipClass.draw_ship(screen_dict['surface'])
    ShipClass.bullet.draw_bullets(screen_dict['surface'])
    AlienClass.draw_aliens(screen_dict['surface'])
    pygame.display.update()
