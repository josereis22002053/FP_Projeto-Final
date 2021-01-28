import pygame, pygame.freetype
from constants import WIDTH_OFFSET, HEIGHT_OFFSET, TILE_SIZE, ALIEN, PREDATOR, MENU, WHITE, RED, MENU_HIGHLIGHT

class Board:
    def __init__(self, display):
        self.change_screen = False
        self.display = display
        self.button = pygame.Rect(25, 620, 150, 75)

        self.button_color = (255, 255, 255)
        self.font = pygame.freetype.Font('recharge-bd.ttf', 30)
    
        self.turn_text = ''

        self.board = []
        self.create_board()
        self.turn = 'p'
        self.selected = False
        self.sheep_coords = (7, 4)
        self.wolves_won = False

        self.valid_moves = []

    # Função para criar um tabuleiro novo
    def create_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if row == 0:
                    if ((col % 2) != 0):
                        self.board[row].append('a')
                    else:
                        self.board[row].append(0)
                elif row == 7:
                    if col == 4:
                        self.board[row].append('p')
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    
    # Função para desenhar o tabuleiro
    def draw_board(self, display):
        y = HEIGHT_OFFSET
        for row in range(8):
            x = WIDTH_OFFSET
            for col in range(8):
                pygame.draw.rect(display, (RED), (x, y, TILE_SIZE, TILE_SIZE), 2)
                x += TILE_SIZE
            y += TILE_SIZE


    # Função para desenhar as peças
    def draw_pieces(self, display):
        x = WIDTH_OFFSET
        for col in range(0, 8):
            y = HEIGHT_OFFSET
            for row in range(0, 8):
                if self.board[row][col] == 'a':
                    display.blit(ALIEN, (x, y, TILE_SIZE, TILE_SIZE))
                elif self.board[row][col] == 'p':
                    display.blit(PREDATOR, (x, y, TILE_SIZE, TILE_SIZE))
                y += TILE_SIZE
            x += TILE_SIZE
    

    # Função para fazer update ao ecrã
    def update(self):
        self.display.blit(MENU, self.button)
        self.draw_board(self.display)
        self.draw_pieces(self.display)

        mouse_pos = pygame.mouse.get_pos()
        if self.button.collidepoint(mouse_pos):
            self.display.blit(MENU_HIGHLIGHT, self.button)

        if self.turn == 'a':
            self.turn_text = 'ALIEN TURN'
        elif self.turn == 'p':
            self.turn_text = 'PREDATOR TURN'

        textRect = self.font.get_rect(self.turn_text)
        self.font.render_to(self.display, ((WIDTH_OFFSET + TILE_SIZE * 4) - textRect.width // 2, HEIGHT_OFFSET // 2), self.turn_text, (WHITE))

        if self.selected == True:
            if self.valid_moves:
                self.show_valid_moves()

    
    # Função para quando o utilizador clica no ecrã
    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button.collidepoint(mouse_pos):
            self.change_screen = True
        else:

            x = (mouse_pos[1] - HEIGHT_OFFSET) // TILE_SIZE
            y = (mouse_pos[0] - WIDTH_OFFSET) // TILE_SIZE
            
            # Verificar se o click for dentro do tabuleiro
            if ((x >= 0 and x <= 7) and (y >= 0 and y <= 7)):

                # Verificar se carregou numa peça do turno atual
                if self.board[x][y] == self.turn:
                    self.selected = True
                    self.source_tile = (x, y)

                    self.get_valid_moves(x, y)

                # Se uma peça já tiver sido selecionada, receber o campo para onde o jogador se tentou mover
                elif self.selected == True:
                    
                    self.target_tile = (x, y)
                   
                    # Verificar se foi feita uma jogada válida. Se sim, trocar o conteúdo do target tile pelo conteúdo do source tile (mover a peça)
                    if self.target_tile in self.valid_moves:
                        self.board[self.source_tile[0]][self.source_tile[1]] = 0
                        self.board[self.target_tile[0]][self.target_tile[1]] = self.turn

                        # Verificar se a ovelha ganhou
                        if self.turn == 'p' and self.target_tile[0] == 0:
                            self.turn_text = 'PREDATOR WINS!'
                            self.turn = None
                        
                        # Se o jogo não tiver acabado, guardar coordenadas da ovelha para verificar se os lobos ganharam
                        elif self.turn == 'p' and self.target_tile[0] != 0:
                            self.sheep_coords = self.target_tile
        
                        
                        self.source_tile = None
                        self.target_tile = None
                        self.selected = False

                    # Se não tiver sido feita uma jogada válida a peça deixa de estar selecionada
                    else:
                        self.selected = False
                        return
                    
                    # Se foi feita uma jogada válida, passar a jogada para o outro jogador
                    if self.turn == 'p':
                        self.turn = 'a'
                    elif self.turn == 'a':                              
                        self.turn = 'p'
                    
                    # Verificar se os lobos ganharam
                    if self.turn == 'p' and self.sheep_coords[0] != 0:
                            self.check_if_wolves_won()
                            
                            if self.wolves_won == True:
                                self.turn_text = 'ALIEN WINS!'
                                self.turn = None
    

    # Função para calcular os movimentos possíveis
    def get_valid_moves(self, x, y):
        self.valid_moves = []      
        
        # Calcular movimentos possíveis para a ovelha
        if self.turn == 'p':
                  
            if (((x - 1) >= 0) and ((y - 1) >= 0)):
                if self.board[x - 1][y - 1] == 0:
                    self.valid_moves.append((x - 1, y - 1))
                    if (((x - 1) >= 0) and ((y + 1) < 8)):
                        if self.board[x - 1][y + 1] == 0:
                            self.valid_moves.append((x - 1, y + 1))
                elif (((x - 1) >= 0) and ((y + 1) < 8)):
                    if self.board[x - 1][y + 1] == 0:
                        self.valid_moves.append((x - 1, y + 1))
            elif (((x - 1) >= 0) and ((y + 1) < 8)):
                if self.board[x - 1][y + 1] == 0:
                    self.valid_moves.append((x - 1, y + 1))
                    if (((x - 1) >= 0) and ((y - 1) >= 0)):
                        if self.board[x - 1][y - 1] == 0:
                            self.valid_moves.append((x - 1, y - 1))       

        # Calcular movimentos possíveis para o lobo. Os movimentos possíveis para o lobo são também possíveis para a ovelha, uma vez que esta pode andar para cima e para baixo 
        if self.turn == 'a' or self.turn == 'p':
        
            if (((x + 1) < 8) and ((y - 1) >= 0)):
                if self.board[x + 1][y - 1] == 0:
                    self.valid_moves.append((x + 1, y - 1))
                    if (((x + 1) < 8) and ((y + 1) < 8)):
                        if self.board[x + 1][y + 1] == 0:
                            self.valid_moves.append((x + 1, y + 1))
                    elif (((x + 1) < 8) and ((y + 1) < 8)):
                        if self.board[x + 1][y + 1] == 0:
                            self.valid_moves.append((x + 1, y + 1))
                elif (((x + 1) < 8) and ((y + 1) < 8)):
                        if self.board[x + 1][y + 1] == 0:
                            self.valid_moves.append((x + 1, y + 1))
            elif (((x + 1) < 8) and ((y + 1) < 8)):   
                if self.board[x + 1][y + 1] == 0:
                    self.valid_moves.append((x + 1, y + 1))
                    if (((x + 1) < 8) and ((y - 1) >= 0)): 
                        if self.board[x + 1][y - 1] == 0:
                            self.valid_moves.append((x + 1, y - 1))
        
              

    # Funcao para verificar se os lobos ganharam
    def check_if_wolves_won(self):
        self.get_valid_moves(self.sheep_coords[0], self.sheep_coords[1])
        if not self.valid_moves:
            self.wolves_won = True

    
    # Função para mudar a cor dos sítios para onde a peça se pode mexer
    def show_valid_moves(self):
        for move in range(len(self.valid_moves)):
            display_x = TILE_SIZE * self.valid_moves[move][1] + WIDTH_OFFSET
            display_y = TILE_SIZE * self.valid_moves[move][0] + HEIGHT_OFFSET

            pygame.draw.rect(self.display, (WHITE), (display_x + 2, display_y + 2, TILE_SIZE - 3, TILE_SIZE - 3), 0)
