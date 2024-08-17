import sys
from minecraft import mcje 
from game import Game
from colors import Colors

mcje.init()

title_font = mcje.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = mcje.Rect(320, 55, 170, 60)
next_rect = mcje.Rect(320, 215, 170, 180)

screen = mcje.display.set_mode((500, 620))
mcje.display.set_caption("Python Tetris")

clock = mcje.time.Clock()

game = Game()

GAME_UPDATE = mcje.USEREVENT
mcje.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in mcje.event.get():
        if event.type == mcje.QUIT:
            mcje.quit()
            sys.exit()
        if event.type == mcje.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == mcje.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == mcje.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == mcje.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == mcje.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    mcje.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    mcje.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    mcje.display.update()
    clock.tick(60)
