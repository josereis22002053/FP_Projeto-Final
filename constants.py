import pygame


# COLORS
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 20)
RED = (255, 0, 0)

# SCREEN DIMENSIONS
WIDTH = 1280
HEIGHT = 720

# BOARD DIMENSIONS
ROWS = 8
COLUMNS = 8
TILE_SIZE = 64

"""
O tabuleiro ocupa uma área de 88 quadrados, ou seja, 512512 px. Para calcular a posição do tabuleiro de modo a que fique centrado no ecrã:

        Para a largura:
            WIDTH_OFFSET = (1280 - 512) // 2 = 384

        Para a altura:
            HEIGHT_OFFSET = (720 - 512) // 2 = 104
"""
WIDTH_OFFSET = 384
HEIGHT_OFFSET = 104



# PIECES
ALIEN = pygame.image.load('alien.png')
PREDATOR = pygame.image.load('predator.png')

# BUTTONS
PLAY = pygame.image.load('play.png')
PLAY_HIGHLIGHT = pygame.image.load('play_highlight.png')
EXIT = pygame.image.load('exit.png')
EXIT_HIGHLIGHT = pygame.image.load('exit_highlight.png')
MENU = pygame.image.load('menu.png')
MENU_HIGHLIGHT = pygame.image.load('menu_highlight.png')


LOGO = pygame.image.load('logo.png')

