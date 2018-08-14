import pygame
import game_class

pygame.init()

res = (1080, 720)
screen = pygame.display.set_mode(res)
game = game_class.Game(screen)

done = False
while not done:
    done = game.events()
    game.draw_screen()
    pygame.display.flip()

pygame.quit()
