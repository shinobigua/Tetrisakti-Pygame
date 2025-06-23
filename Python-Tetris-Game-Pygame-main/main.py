# Pygame - Tetris

import pygame, sys
from game import Game
from colors import Colors
from button import Button

pygame.init()

screen = pygame.display.set_mode((800, 620))
pygame.display.set_caption("TetrisBoss Menu")
clock = pygame.time.Clock()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render(" Score", True, Colors.white)
next_surface = title_font.render("Next nih", True, Colors.white)
game_over_surface = title_font.render("Sorry lu GAGAL!", True, Colors.white)

# Ngatur besar dan letak kotak
next_rect = pygame.Rect(330, 250, 150, 120)
score_rect = pygame.Rect(330, 50, 120, 60)

background = pygame.image.load("Graphics/background.png").convert()
start_button = Button("Graphics/start_button.png", (300, 150), 0.65)
exit_button = Button("Graphics/exit_button.png", (300, 300), 0.65)
pause_button = Button("Graphics/exit_button.png", (660, 10), 0.4)
resume_button = Button("Graphics/start_button.png", (300, 300), 0.6)

game_state = "menu"
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

def show_menu():
    screen.fill("black")
    screen.blit(background, (0, 0))
    start_button.draw(screen)
    exit_button.draw(screen)

def run_tetris():
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)

    
    screen.blit(score_surface, (score_rect.x + 15, score_rect.y - 30))
    screen.blit(next_surface, (next_rect.x + 20, next_rect.y - 40))

    if game.game_over:
        screen.blit(game_over_surface, (score_rect.x - 10, next_rect.y + 180))

    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(center=score_rect.center))

    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    game.draw(screen)
    pause_button.draw(screen)

def show_pause_screen():
    screen.fill((30, 30, 30))
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Dijeda", True, Colors.white)
    screen.blit(text, (280, 200))
    resume_button.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "menu":
            if start_button.is_pressed():
                game_state = "playing"
            if exit_button.is_pressed():
                pygame.quit()
                sys.exit()

        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    game.game_over = False
                    game.reset()
                if not game.game_over:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    if event.key == pygame.K_RIGHT:
                        game.move_right()
                    if event.key == pygame.K_DOWN:
                        game.move_down()
                        game.update_score(0, 1)
                    if event.key == pygame.K_UP:
                        game.rotate()

            if event.type == GAME_UPDATE and not game.game_over:
                game.move_down()

        if game_state == "playing":
            if pause_button.is_pressed():
                game_state = "paused"

        if game_state == "paused":
            if resume_button.is_pressed():
                game_state = "playing"

    if game_state == "menu":
        show_menu()
    elif game_state == "playing":
        run_tetris()
    elif game_state == "paused":
        show_pause_screen()

    pygame.display.update()
    clock.tick(60)
