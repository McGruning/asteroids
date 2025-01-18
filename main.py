import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock obect to control the game's frame rate
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with black colour
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

       # Update the player
        player.update(dt)
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        dt = clock.tick(60) / 1000 # Tick method returns milliseconds, so we divide by 1000 to get seconds
    


if __name__ == "__main__":
    main()
   