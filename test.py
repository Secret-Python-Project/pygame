import sys, pygame


def play_game():
    pygame.init()
    size = 320, 240
    screen = pygame.display.set_mode(size)
    black = 0, 0, 0

    display_loading_screen(black, screen)

    while True:
        respond_to_quit()


def display_loading_screen(black, screen):
    screen.fill(black)
    pygame.display.flip()


def respond_to_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    play_game()
