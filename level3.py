import pygame
from settings import *

def level3_game(screen, screen_width, screen_height):
    # Load the background image
    background_path = "useful_images/img_6.png"  
    background_image = pygame.image.load(background_path).convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    
    # Load and play the background music
    pygame.mixer.music.load('useful_images/detective_audio.mp3')
    pygame.mixer.music.play(-1)  # Loop the music indefinitely until stopped

    click_sound = pygame.mixer.Sound('useful_images/Click_sound.mp3')
    # Load the play button image
    first_option_path = "useful_images/option1.png"  
    first_option = pygame.image.load(first_option_path).convert_alpha()
    second_option_path = "useful_images/option2.png"  
    second_option = pygame.image.load(second_option_path).convert_alpha()
    third_option_path = "useful_images/option3.png"  
    third_option = pygame.image.load(third_option_path).convert_alpha()

    # Scale the play button to desired size
    first_option_size = (int((first_option.get_width() * 1.05)//4), int((first_option.get_height() * 1.05)//4))
    first_option = pygame.transform.scale(first_option, (250,120))
    first_option_enlarged_image = pygame.transform.scale(first_option, (290,150))
    second_option_size = ((int(second_option.get_width() * 1.05)//4), int((second_option.get_height() * 1.05)//4))
    second_option = pygame.transform.scale(second_option, (250,120))
    second_option_enlarged_image = pygame.transform.scale(second_option, (290,150))
    third_option_size = (int((third_option.get_width() * 1.05)//4), int((third_option.get_height() * 1.05)//4))
    third_option = pygame.transform.scale(third_option, (250,120))
    third_option_enlarged_image = pygame.transform.scale(third_option, (290,150))

    # Load the cursor image
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

    pygame.mouse.set_visible(False)

    # Position of the play button
    
    
    
    # Function to check if the mouse is over the play button
    def is_over_option(mouse_pos):
        a=mouse_pos[0]
        b=mouse_pos[1]
        if a>=985 and a<=1170:
            if b>=139 and b<=201:
                return 1 
            if b>=337 and b<=404:
                return 2 
            if b>=530 and b<=600:
                return 3 
        return 4 
    # Function to check if the play button is clicked
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse clicks
                mouse_pos = pygame.mouse.get_pos() 
             #   print(mouse_pos[0],mouse_pos[1])# Get the current mouse position
                if is_over_option(mouse_pos)!=4:
                    click_sound.play()  
                    return is_over_option(mouse_pos)
        
        # Draw the background image
        screen.blit(background_image, (0, 0))
        
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse is over the play button
        if is_over_option(mouse_pos)!=4:
            # Draw a semi-transparent surface to dim the background
            overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))  # Fill with black color with 50% transparency
            screen.blit(overlay, (0, 0))  # Draw the overlay

        # Draw the play button
        if is_over_option(mouse_pos)==1:
            screen.blit(first_option_enlarged_image, (950,100))  # Draw the enlarged play button
        else:
            screen.blit(first_option, (950, 100))  # Draw the normal size play button
        if is_over_option(mouse_pos)==2:
            screen.blit(second_option_enlarged_image, (950,300))  # Draw the enlarged play button
        else:
            screen.blit(second_option, (950, 300))
        if is_over_option(mouse_pos)==3:
            screen.blit(third_option_enlarged_image, (950,500))  # Draw the enlarged play button
        else:
            screen.blit(third_option, (950, 500))
        # Draw the custom cursor at the mouse position
        screen.blit(custom_cursor_image, (mouse_pos[0] - custom_cursor_size[0] // 2, mouse_pos[1] - custom_cursor_size[1] // 2))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(60)  # Limit to 60 frames per second

    return False


