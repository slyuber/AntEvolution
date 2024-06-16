import pygame
import sys
from ant import Ant
from menu import draw_menu

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Load background image
background_image = pygame.image.load('../assets/bkg.png')  # Ensure the path is correct


# Load ant images
ant_base_image = pygame.image.load('../assets/antBase.png')  # Ensure the path is correct
ant_anim_images = [
    pygame.image.load('../assets/antOne.png'),   # Ensure the path is correct
    pygame.image.load('../assets/antTwo.png')    # Ensure the path is correct
]

# Main loop
def main():
    running = True
    in_menu = True
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    in_menu = False
                    all_sprites.empty()  # Reset ants
                    for _ in range(20):  # Default to 20 ants
                        ant = Ant(ant_base_image, ant_anim_images)
                        all_sprites.add(ant)
                if event.key == pygame.K_r:
                    in_menu = True

        if in_menu:
            screen.blit(background_image, (0, 0))  # Draw the background image
            draw_menu(screen)
        else:
            # Update all sprites
            ants = all_sprites.sprites()
            for ant in ants:
                ant.update(ants)

            # Clear the screen
            screen.blit(background_image, (0, 0))  # Draw the background image  

            # Draw all sprites
            all_sprites.draw(screen)

        # Flip the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
