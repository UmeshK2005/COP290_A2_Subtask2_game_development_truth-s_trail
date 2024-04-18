from settings import *
from level0 import level0_game
from level1 import level1_game
from level4_demo import level4_game
from level5_demo import level5_game 
from level6_demo import level6_game 
from level7_demo import level7_game
from level8_demo import level8_game 
import pygame
import sys
from pytmx.util_pygame import load_pygame
import math 
from os.path import join  
from support import * 
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.import_assets()
        pygame.display.set_caption("Truth's Trail")
        self.tmx_maps = {2: load_pygame('final_map1.tmx'),3:load_pygame('final_map2.tmx'),4:load_pygame('final_map3.tmx'),5:load_pygame('final_map4.tmx'),6:load_pygame('final_map5.tmx')}
        self.stage4 =level4_game(self.tmx_maps[2],self.level_frames)
        self.stage5 =level5_game(self.tmx_maps[3],self.level_frames)
        self.stage6 =level6_game(self.tmx_maps[4],self.level_frames)
        self.stage7 =level7_game(self.tmx_maps[5],self.level_frames)
        self.stage8 =level8_game(self.tmx_maps[6],self.level_frames)
        self.curr_stage = self.stage4
        caught_image = pygame.image.load("graphics/useful_images/busted.jpeg").convert_alpha()
        self.caught_image = pygame.transform.scale(caught_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface = custom_font.render("Press 'f' to respawn to last checkpoint", True, (0, 0, 0))
    #    print(self.level_frames['player'])
     #   print(self.level_frames['guards'])
    def import_assets(self):
            self.level_frames ={
                'player' : import_sub_folders('graphics/imageonline'),
                'guards' : import_sub_folders('graphics/police')
                
            }
        
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
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface1 = custom_font.render("Press 'F' to go inside Mansion!", True, (255, 255, 255))
        self.curr_stage=self.stage8   
      #  self.curr_stage.guard_game.curr_posx=518
      #  self.curr_stage.guard_game.curr_posy =92
        visited = []
        while True:
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
           
            a = level0_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)  # Pass display_surface to level function
          
            self.fade_out()
            if not a:
                break 
            
            

            # b=level1_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
            # self.fade_in()
            # self.fade_out()
            # if not b:
            #     break
            
        
            
          #  d =self.curr_stage.run(dt)
         #   if  d :
            #    print('true')
          #      self.display_surface.blit(text_surface, ((settings.WINDOW_WIDTH - text_surface.get_width()) // 2, 
           #                                               settings.WINDOW_HEIGHT - text_surface.get_height()))
              #  keys = pygame.key.get_pressed()
               # if keys[pygame.K_f]:
                   # print("hi")
         #   print(self.curr_stage.guard_game.curr_posx,self.curr_stage.guard_game.curr_posx," bhjjbjh")
            
            
            # d =self.curr_stage.run(dt)
            # if d==1:
            #     self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
            #                                               settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
            #     keys = pygame.key.get_pressed()
            #     if keys[pygame.K_f]:
            #         self.curr_stage=self.stage5
            #         continue 
            # if d==-5:
                
            #     self.display_surface.blit(self.caught_image, (0,0))
            #     self.display_surface.blit(self.text_surface, ((settings.WINDOW_WIDTH - self.text_surface.get_width()) // 2, 
            #                                               settings.WINDOW_HEIGHT - self.text_surface.get_height()))
            #     keys = pygame.key.get_pressed()
            #     if keys[pygame.K_f]:
            #         self.stage5 =level5_game(self.tmx_maps[3],self.level_frames)
            #         self.stage6 =level6_game(self.tmx_maps[4],self.level_frames)
            #         self.curr_stage =self.stage5
            #         continue 
                 
            # if d==5 :
            #     self.curr_stage=self.stage6
            # if d==12 or d==13 or d==14:
            #     if d==13:
            #         self.curr_stage =self.stage5 
            #     elif d==14:
            #         self.curr_stage =self.stage7 
            #     else:
            #         self.curr_stage =self.stage5 
            #         self.curr_stage.key2=1 
            
                    
            pygame.display.update()
            
                     
            
             
                

if __name__ == '__main__':
    game = Game()
    game.run()

