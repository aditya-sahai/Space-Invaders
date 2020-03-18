import pygame
import sys

class Bullet:
    """A class to store bullet data."""

    def __init__(self):
        """Initialize bullet attributes."""
        self.bullets = []
        self.color = (0, 255, 0)
        self.width = 4
        self.height = 9
        self.y_change = -15

    def fire(self, ship):
        """FIre the bullets and store them in a list."""
        bullet = pygame.Rect(int(ship.x + ship.width / 2 - self.width / 2), ship.y + 1, self.width, self.height)
        self.bullets.append(bullet)

    def draw_bullets(self, screen):
        """Draw the bullets on the screen."""
        for index, bullet in enumerate(self.bullets):
            if bullet[1] + bullet[3] < 0:
                del self.bullets[index]
                print(self.bullets)
            else:
                pygame.draw.rect(screen, (0, 255, 0), bullet)
                bullet[1] += self.y_change


class Ship:
    """A class representing the players spaceship."""
    def __init__(self, screen_dict):
        """Initializing the starting positions and attributes."""
        self.img = pygame.image.load("Images\\player_ship.png")
        self.width = 64
        self.height = 32
        self.x_change = 10
        self.y_change = 0
        self.x = int((screen_dict['width'] / 2) - (self.width / 2))
        self.y = screen_dict['height'] - 2 * self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bullet = Bullet()

    def draw_ship(self, screen):
        """Draw the ship on the screen."""
        screen.blit(self.img, self.rect[:2])

    def check_boundaries(self, screen_dict):
        if self.x <= 0:
            self.x_change = 10
        elif self.x + self.width >= screen_dict['width']:
            self.x_change = -10

    def move(self, key, screen_dict):
        """Changes the x value of the ship on the basis of a key."""
        if key == 0:
            self.x_change = -10
        elif key == 1:
            self.x_change = 10
        elif key == 2:
            self.bullet.fire(self)

        self.check_boundaries(screen_dict)
        self.x += self.x_change

        self.rect[0] = self.x
