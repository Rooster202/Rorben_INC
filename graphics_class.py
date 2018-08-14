import pygame

class Graphic():
    def __init__(self, screen):
        self.screen = screen

        self.game_font = pygame.font.SysFont('calibri', 15)

        self.stoke_fire_stamp = self.game_font.render('stoke fire', True, (0, 0, 0))


    def draw(self):
        self.screen.blit(self.stoke_fire_stamp, (100, 50))


        pygame.draw.rect(self.screen, (0, 0, 0), (90, 40, 75, 25), 2)

    


