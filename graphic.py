# Kiana Kianpour - 6117142462(کد درس) - Computer Graphics Project

import pygame
import random
import sys

# مقداردهی اولیه
pygame.init()

# تنظیمات صفحه
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle System - Kiana Kianpour")

clock = pygame.time.Clock()

particles = []

# کلاس ذره
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(4, 8)
        self.color = (
            random.randint(150, 255),
            random.randint(100, 255),
            random.randint(150, 255)
        )
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-4, -1)
        self.life = 255  # طول عمر

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.life -= 4

    def draw(self, surface):
        if self.life > 0:
            temp_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(
                temp_surface,
                (*self.color, self.life),
                (int(self.x), int(self.y)),
                self.radius
            )
            surface.blit(temp_surface, (0, 0))


# حلقه اصلی
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(20):
                particles.append(Particle(*event.pos))

    screen.fill((15, 15, 30))

    for particle in particles[:]:
        particle.move()
        particle.draw(screen)
        if particle.life <= 0:
            particles.remove(particle)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
