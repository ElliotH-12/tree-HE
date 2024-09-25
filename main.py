import pygame
import math
import random
import datetime


pygame.init()


screen_width = 800
screen_height = 800



screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Recursive Tree")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))


colour = (110, 61, 35)

class Boxes:
    def __init__(self, x, y, width, height, text, value = False, change=None):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.value = value
        self.change = change
        self.font = pygame.font.SysFont(None, 24)
        self.text_surf = self.font.render(self.text, True, 'black')

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect)
        pygame.draw.rect(screen, 'black', self.rect, 2)

        if self.value:
            pygame.draw.line(screen, 'black', (self.rect.x, self.rect.y),
                             (self.rect.x + self.rect.width, (self.rect.y + self.rect.height)-1), 2)
#(self.rect.x + self.rect.width, self.rect.y + self.rect.height), 2)
        screen.blit(self.text_surf, (self.rect.x + self.rect.width + 10, self.rect.y))

    def mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            if self.x < self.rect.x + self.rect.width and self.x + self.rect.width > self.x and self.y < self.rect.y + self.rect.height and self.y + self.height > self.rect.y:
                self.value = not self.value
                if self.change is not None:
                    self.change(self.value)

class Menu:
    def __init__(self, x, y, width, height, change=None):
        self.change = change
        self.rect = pygame.Rect(x, y, width, height)

        self.random_box = Boxes(20, 170, 20, 20, 'Random', False, self.random_box_different)
        self.bendy_box = Boxes(20, 210, 20, 20, 'Bendy', False, self.bendy_box_different)
        self.thinness_box = Boxes(20, 250, 20, 20, 'Thinness', False, self.thinness_box_different)
        self.leaves_box = Boxes(20, 290, 20, 20, 'Leaves', False, self.leaves_box_different)
        self.brown_box = Boxes(20, 330, 20, 20, 'Brown', False, self.brown_box_different)

    def draw(self, screen):
        pygame.draw.rect(screen, 'lightblue', self.rect)
        self.random_box.draw(screen)
        self.bendy_box.draw(screen)
        self.thinness_box.draw(screen)
        self.leaves_box.draw(screen)
        self.brown_box.draw(screen)

    def mouse_event(self, event):
        self.random_box.mouse_event(screen)
        self.bendy_box.mouse_event(screen)
        self.thinness_box.mouse_event(screen)
        self.leaves_box.mouse_event(screen)
        self.brown_box.mouse_event(screen)

    def random_box_different(self, event):
        random_angle = value
        if self.change is not None:
            self.change()

    def bendy_box_different(self, value):
        global bendy_branches
        bendy_branches = value
        if self.change is not None:
            self.change()

    def thinness_box_different(self, value):
        global thinness_tree
        thinnes_tree = value
        if self.change is not None:
            self.change()

    def leaves_box_different(self, value):
        global leaves_tree
        leaves_tree = value
        if self.changed is not None:
            self.changed()

    def brown_box_different(self, value):
        global brown_branches
        brown_branches = value
        if self.change is not None:
            self.change()

class Branch:
    def __init__(self, x, y, angle, length, thickness, depth):
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.thickness = thickness
        self.depth = depth

    def draw(self):

        angle = math.radians(self.angle)

        x2 = self.x + self.length * math.cos(angle)
        y2 = self.y + self.length * math.sin(angle)

        colour = (
            max(0, min(255, 110 - self.depth * 3)),
            max(0, min(255, 61 + self.depth * 5)),
            35
        )

        pygame.draw.line(screen, colour, (self.x, self.y), (x2, y2), self.thickness)

    def grow(self, levels):
        if levels > 0:
            #levels -=1

            left_angle = self.angle - random.randint(15, 30)
            left_length = self.length * random.uniform(0.6, 0.8)


            left_branch = Branch(self.x + self.length * math.cos(math.radians(self.angle)),
                                 self.y + self.length * math.sin(math.radians(self.angle)),
                                 left_angle + (math.pi/6), left_length, max(1, self.thickness-2), self.depth +1)
            left_branch.draw()
            left_branch.grow(levels - 1)

            # Grow right branch
            right_angle = self.angle + random.randint(15, 30)
            right_length = self.length * random.uniform(0.6, 0.8)


            right_branch = Branch(self.x + self.length * math.cos(math.radians(self.angle)),
                                 self.y + self.length * math.sin(math.radians(self.angle)),
                                 right_angle - (math.pi/6), right_length, max(1, self.thickness-2), self.depth + 1)


            right_branch.draw()
            right_branch.grow(levels - 1)


def regrow():
    screen.fill((255, 255, 255))
    trunk = Branch(screen_width // 2, screen_height, -90, 175, 8, 0)
    trunk.draw()
    trunk.grow(10)


# Main Game Loop
running = True
drewtree = False
levels = 10

menu = Menu(10, 0, 180, 400, 1)
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                regrow()

    if not drewtree:
        trunk = Branch(screen_width//2, screen_height, -90, 110, 8, 0)  # Initial trunk
        trunk.draw()
        trunk.grow(10)
        drewtree = True

    #screen.fill((255, 255, 255))
    menu.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()