import pygame
from constants import PLAY, EXIT, TILE_SIZE, LOGO, PLAY_HIGHLIGHT, EXIT_HIGHLIGHT


class Menu:
    def __init__(self, display):
        self.change_screen = False
        self.display = display
        self.buttons = [pygame.Rect(565, 345, 150, 75), pygame.Rect(565, 450, 150, 75)]


    # Função para quando o utilizador clica no ecrã
    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.collidepoint(mouse_pos):
                if button == self.buttons[0]:
                    self.change_screen = True
                elif button == self.buttons[1]:
                    exit()

    # Função para fazer update ao ecrã
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.display.blit(PLAY, self.buttons[0])
        self.display.blit(EXIT, self.buttons[1])

        self.display.blit(LOGO, (256, 50, 768, 250))

        for button in self.buttons:
            if button.collidepoint(mouse_pos):
                if button == self.buttons[0]:
                    self.display.blit(PLAY_HIGHLIGHT, self.buttons[0])
                elif button == self.buttons[1]:
                    self.display.blit(EXIT_HIGHLIGHT, self.buttons[1])

