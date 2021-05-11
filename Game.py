import pygame, os, sys
from Board import Board

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_NAME = "Tic Tac Toe"


def draw_text(screen, text, size, location):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, text.get_rect(center = location))


def turn(pos, block, xo, board, screen):
    for i in range(3):
        for j in range(3):
            if pygame.Rect(block[i][j][0] - SCREEN_WIDTH/6, block[i][j][1] - SCREEN_HEIGHT/6, SCREEN_WIDTH/3, SCREEN_HEIGHT/3).collidepoint(pos):
                if board.available_block((i, j)):
                    draw_text(screen, xo, 120, block[i][j])
                    board.set_block((i, j), xo)
                    return True
                else:
                    return False


def GameLoop():
    board = Board()

    player1 = "X"
    player2 = "O"

    player_turn = player1

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_NAME)

    if getattr(sys, 'frozen', False):
        icon = pygame.image.load(os.path.dirname(sys.executable) + "\\Images\\X-Icon.ico")
    else:
        icon = pygame.image.load(os.path.dirname(__file__) + "\\Images\\X-Icon.ico")
    
    pygame.display.set_icon(icon)

    screen.fill((255, 255, 255))

    pygame.draw.aaline(screen, (0, 0, 0), (0, SCREEN_HEIGHT/3), (SCREEN_WIDTH, SCREEN_HEIGHT/3))
    pygame.draw.aaline(screen, (0, 0, 0), (0, SCREEN_HEIGHT/3 * 2), (SCREEN_WIDTH, SCREEN_HEIGHT/3 * 2))
    pygame.draw.aaline(screen, (0, 0, 0), (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, SCREEN_HEIGHT))
    pygame.draw.aaline(screen, (0, 0, 0), (SCREEN_WIDTH/3 * 2, 0), (SCREEN_WIDTH/3 * 2, SCREEN_HEIGHT))

    block = [[[] for y in range(3)] for x in range(3)]
    y = 0

    for i in range(3):
        y += SCREEN_HEIGHT/6
        x = 0
        for j in range(3):
            x += SCREEN_WIDTH/6
            block[j][i] = [x, SCREEN_HEIGHT - y]
            x += SCREEN_WIDTH/6
        y += SCREEN_HEIGHT/6

    crash = False
    won = False
    draw = False
    text = False

    while not crash:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
                pygame.quit()
                break

            elif event.type == pygame.MOUSEBUTTONUP and not won:
                turned = turn(pygame.mouse.get_pos(), block, player_turn, board, screen)
                won = board.won

                if not won:
                    draw = board.draw()

                if player_turn == player1 and turned and not won or draw:
                    player_turn = player2
                elif turned and not won and not draw:
                    player_turn = player1

            elif event.type == pygame.KEYDOWN and (won or draw):
                if event.key == pygame.K_RETURN:
                    GameLoop()
                    crash = True
                    break
        
        if not text and won or draw:
            text = True
            screen.fill((255, 255, 255))
            if won:
                draw_text(screen, player_turn + " Won!", 50, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 25))
            else:
                draw_text(screen, "Draw", 50, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
            draw_text(screen, "Press Enter To Play Again", 40, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 25))
        
        if not crash:
            pygame.display.update()


if __name__ == "__main__":
    GameLoop()