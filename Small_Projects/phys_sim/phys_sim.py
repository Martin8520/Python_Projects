import pygame
import sys
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


class Planet:
    def __init__(self, name, color, radius, orbit_radius, orbital_speed):
        self.name = name
        self.color = color
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbital_speed = orbital_speed
        self.angle = 0

    def update(self):
        self.angle += self.orbital_speed

    def draw(self, screen):
        x = width // 2 + self.orbit_radius * math.sin(self.angle)
        y = height // 2 + self.orbit_radius * math.cos(self.angle)
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)


sun = Planet("Sun", YELLOW, 30, 0, 0)

planets = []


def add_planet(name, color, radius, orbit_radius, orbital_speed):
    planet = Planet(name, color, radius, orbit_radius, orbital_speed)
    planets.append(planet)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                add_planet("New Planet", BLUE, 10, 200, 0.02)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                add_planet("New Planet", BLUE, 10, 200, 0.02)
            elif event.key == pygame.K_UP:
                if planets:
                    planets[-1].radius += 5
            elif event.key == pygame.K_DOWN:
                if planets:
                    planets[-1].radius = max(5, planets[-1].radius - 5)
            elif event.key == pygame.K_LEFT:
                if planets:
                    planets[-1].orbit_radius = max(0, planets[-1].orbit_radius - 10)
            elif event.key == pygame.K_RIGHT:
                if planets:
                    planets[-1].orbit_radius += 10

    screen.fill(WHITE)

    sun.draw(screen)
    for planet in planets:
        planet.update()
        planet.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
