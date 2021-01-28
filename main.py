import pygame


def main():
    # Iniciar o pygame
    pygame.init()

    # Definir a resolução da janela
    res = (WIDTH, HEIGHT)

    # Criar uma janela
    display = pygame.display.set_mode(res)
    
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


        # Trocar os buffers
        pygame.display.flip()


main()