import pygame
from constants import WIDTH, HEIGHT, DARK_BLUE
from menu import Menu
from game import Board


def main():
    # Iniciar o pygame
    pygame.init()

    # Definir a resolução da janela
    res = (WIDTH, HEIGHT)

    # Criar uma janela
    display = pygame.display.set_mode(res)

    # Iniciar o jogo no ecrã do menu
    current_screen = Menu(display)
    
    # Mudar o nome da janela para "Alien vs Predator"
    pygame.display.set_caption('Alien vs Predator')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen.click()
        
        # Limpar o ecrã com um azul escuro
        display.fill(DARK_BLUE)

        # Verificar se o utlizador mudou de ecrã
        if current_screen.change_screen == True and isinstance(current_screen, Menu):
            current_screen = Board(display)
        elif current_screen.change_screen == True and isinstance(current_screen, Board):
            current_screen = Menu(display)
        
        # Desenhar o ecrã
        else:
            current_screen.update()

        # Trocar os buffers
        pygame.display.flip()


main()