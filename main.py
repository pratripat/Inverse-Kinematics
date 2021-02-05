from globals import *
from tentacle import Tentacle

def main():
    #Making Tentable object
    t = Tentacle(10, pygame.math.Vector2(width//2, height//2), 30, pygame.math.Vector2(width//2, height))

    while True:
        screen.fill(black)

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Tentacle will follow the mouse
        t.run(pygame.mouse.get_pos())

        pygame.display.update()

main()
