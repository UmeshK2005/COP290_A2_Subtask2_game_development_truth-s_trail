import pygame
import pytmx 
from settings import *

def level1_game(screen, screen_width, screen_height):
    # Load the background image
    background_path = "useful_images/img_7.png"  
    background_image = pygame.image.load(background_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    
    click_sound = pygame.mixer.Sound('useful_images/Click_sound.mp3')
    
    custom_cursor_path = "useful_images/cursor.jpg"  
    cursor_image = pygame.image.load(custom_cursor_path).convert_alpha()
    
    # Create a mask for the cursor image
    cursor_mask = pygame.mask.from_surface(cursor_image)
    non_transparent_points = cursor_mask.outline()
    min_x = min([p[0] for p in non_transparent_points])
    max_x = max([p[0] for p in non_transparent_points])
    min_y = min([p[1] for p in non_transparent_points])
    max_y = max([p[1] for p in non_transparent_points])
    cursor_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    cursor_surface = pygame.Surface(cursor_rect.size, pygame.SRCALPHA)
    cursor_surface.blit(cursor_image, (0, 0), cursor_rect)

    # Decrease the size of the custom cursor
    custom_cursor_size = (50, 50)  # Adjust the dimensions as needed
    custom_cursor_image = pygame.transform.scale(cursor_surface, custom_cursor_size)
    custom_cursor_image2 = pygame.transform.scale(cursor_surface,(70,70))
    pygame.mouse.set_visible(False)

    # Position of the play button
    play_button_x = 0
    play_button_y = 0
    
    # Function to check if the mouse is over the play button
    def is_over_play_button(mouse_pos):
        a=mouse_pos[0]
        b=mouse_pos[1]
        if a>=122 and a<=682 and b>=331 and b<=436:
            return True 
        else:
            return False 

    # Function to check if the play button is clicked
    def play_button_clicked(mouse_pos):
        return is_over_play_button(mouse_pos)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse clicks
                mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
              #  print(mouse_pos[0],mouse_pos[1])
                if play_button_clicked(mouse_pos):
                    click_sound.play()  
                    return True 
        
        # Draw the background image
        screen.blit(background_image, (0, 0))
        
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse is over the play button
        if is_over_play_button(mouse_pos):
            screen.blit(custom_cursor_image2, (mouse_pos[0] - custom_cursor_size[0] // 2, mouse_pos[1] - custom_cursor_size[1] // 2))
             
        else:
        
        # Draw the custom cursor at the mouse position
            screen.blit(custom_cursor_image, (mouse_pos[0] - custom_cursor_size[0] // 2, mouse_pos[1] - custom_cursor_size[1] // 2))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(60)  # Limit to 60 frames per second

    return False   


