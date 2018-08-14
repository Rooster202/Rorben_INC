import pygame

class Game():
    def __init__(self, screen):
        self.screen = screen
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.k_ESCAPE:
                return True

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        
    def point_collision(self, point, rect):
        if (point[0] > rect[0] and point[1] > rect[1] and
            point[0] < rect[0]+rect[2] and
            point[1] < rect[1]+rect[3]):
            return True
        else:
            return False

    def button(self):
        pass

    
