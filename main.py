from settings import *
from level0 import level0_game
from level1 import level1_game
from level2 import level2_game 
import pygame
import sys
from pytmx.util_pygame import load_pygame
import math 
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Truth's Trail")
        self.tmx_maps = {2: load_pygame('final_map1.tmx')}
       # print(self.tmx_maps)
     #   self.tmx_mapping = {1: load_pygame('tiled/map2_iso.tmx')}
     #   print("TMX Mapping:", self.tmx_mapping)  # Add this line for debugging
        
    def fade_out(self):
        fade_surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.SRCALPHA)  # Create a surface with per-pixel alpha
        for alpha in range(0, 256, 2):  # Increase alpha to fade out
            fade_surface.fill((0, 0, 0, alpha))  # Fill with black with increasing alpha
            self.display_surface.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(10)  # Decreased delay for smoother transition

     

    def fade_in(self):
        fade_surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.SRCALPHA)
        for alpha in range(0, 256, 2):
            eased_alpha = math.pow(alpha / 255,2) * 255  # Apply ease-in function to alpha values
            fade_surface.fill((0, 0, 0, 255 - int(eased_alpha)))
            self.display_surface.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(10) 

    
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            
            a = level0_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)  # Pass display_surface to level function
          
            self.fade_out()
            if not a:
                break 
            
            b=level1_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
            self.fade_in()
            self.fade_out()
            if not b:
                break
            
            c = level2_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)  # No need to use .run()
            if not c:
                break            
            
             
                

if __name__ == '__main__':
    game = Game()
    game.run()

