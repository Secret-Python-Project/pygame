import sys, pygame

def play_game():
    pygame.init()
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    black = 0, 0, 0

    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
          
      screen.fill(black)
      pygame.display.flip()

if __name__ == "__main__":
  play_game()