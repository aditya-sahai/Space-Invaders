import pygame
import sys
import random

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
        self.points = 0
        self.level = 1

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


class Alien:
    """A class for alien attributes."""
    def __init__(self):
        """Initialize alien class."""
        self.aliens = []
        self.image_1 = pygame.image.load('Images\\alien_1.png')
        self.image_2 = pygame.image.load('Images\\alien_2.png')
        self.image_3 = pygame.image.load('Images\\alien_3.png')
        self.image_4 = pygame.image.load('Images\\alien_4.png')
        self.image_5 = pygame.image.load('Images\\alien_5.png')
        self.image_6 = pygame.image.load('Images\\alien_6.png')
        self.image_7 = pygame.image.load('Images\\alien_7.png')
        self.images = [
            self.image_1, self.image_1, self.image_1,
            self.image_1, self.image_1, self.image_1,
            self.image_2, self.image_2, self.image_2,
            self.image_2, self.image_2, self.image_3,
            self.image_3, self.image_3, self.image_3,
            self.image_4, self.image_4, self.image_4,
            self.image_5, self.image_5, self.image_6,
            self.image_7,
            ]

    def get_image_imagerect(self):
        """Return a random image along with a random number."""
        image = random.choice(self.images)
        points = (self.images.index(image) + 1) * 10
        image_rect = image.get_rect()
        x_change = random.choice([10, -10])
        return [image, points, image_rect, x_change, 0]

    def move(self, screen_dict):
        """Change the aliens x and y."""
        for alien in self.aliens:
            if alien[1][0] <= 0:
                alien[4][0] = 10
                alien[4][1] = 10
            elif alien[1][0] + alien[3][2] >= screen_dict['width']:
                alien[4][0] = -10
                alien[4][1] = 10
            else:
                alien[4][1] = 0

            alien[1][0] += alien[4][0]
            alien[1][1] += alien[4][1]


    def generate_aliens(self, screen_dict):
        """Generates a list of aliens."""
        for num in range(0,5):
            x = random.randint(0, screen_dict['width'] - 200)
            y = random.randint(0, int(screen_dict['height'] / 2))
            image, points, image_rect, x_change, y_change = self.get_image_imagerect()
            self.aliens.append([image, [x, y], points, image_rect, [x_change, y_change]])

    def draw_aliens(self, screen):
        """Draw the aliens on the screen."""
        for alien in self.aliens:
            screen.blit(alien[0], alien[1])
