import pygame, sys

from gameobject import GameObject

pygame.init()

# 16:9 aspect ratio
screen_size = (800, 450)
screen = pygame.display.set_mode(screen_size)

screen.fill((255, 255, 255))

def gameLoop():

    g1 = GameObject( 0, 0 )
    g2 = GameObject( 100, 100 )

    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('closing...')
                isRunning = False
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        mouse_pos = pygame.mouse.get_pos()

        # ( x, y )

        g1.translate( mouse_pos[0], mouse_pos[1] )
        
        g1.render( screen )
    
        pygame.display.flip()


if __name__ == '__main__':
    gameLoop()
