from settings import *
from level0 import level0_game
from level1 import level1_game
from level2 import level2_game
from level3 import level3_game
from level4_demo import level4_game
from level5_demo import level5_game 
from level6_demo import level6_game 
from level7_demo import level7_game
from level8_demo import level8_game
from level9 import level9_game
from level10 import level10_game

import pygame
import sys
from pytmx.util_pygame import load_pygame
import os 
from moviepy.editor import VideoFileClip
from pygame.locals import * 

import math 
from os.path import join  
from support import * 
class Game:
    def __init__(self):
        pygame.init()
      #  pygame.mixer.init(driver='alsa')
        self.clock = pygame.time.Clock()
        self.cnt =0
        self.cnt1 =0
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
        caught_image = pygame.image.load("useful_images/busted.png").convert_alpha()
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
            
    def play_video(self, file_path):
        clip = VideoFileClip(file_path)
        clip.preview(fps=clip.fps)  # Play the video without fullscreen
        # Reset the display mode after video to ensure the size remains consistent
        pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        # Additionally force an update to the display to reapply the correct configuration
        pygame.display.flip()
    
    def display_image(self, image_path,check):
        # Load the image
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))  # Scale image to fit the screen

        # Blit the image to the display surface
        self.display_surface.blit(image, (0, 0))
        if check:
            self.display_surface.blit(self.text_surface, ((settings.WINDOW_WIDTH - self.text_surface.get_width()) // 2, 
                                                            self.text_surface.get_height()+50))
        pygame.display.flip()  # Update the display to show the image

        # Optionally, wait for a key press to continue after displaying the image
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (not check) and (event.key == pygame.K_SPACE):  # Press SPACE to continue
                        waiting = False    
                    elif (check) and (event.key == pygame.K_f):  # Press f to continue
                        self.stage4 = level4_game(self.tmx_maps[2],self.level_frames)
                        self.stage5 =level5_game(self.tmx_maps[3],self.level_frames)
                        self.stage6 =level6_game(self.tmx_maps[4],self.level_frames)
                        self.stage7 = level7_game(self.tmx_maps[5],self.level_frames)
                        self.stage8 =level8_game(self.tmx_maps[6],self.level_frames)
                        self.curr_stage =self.stage4
                        waiting = False      
        
    def display_image2(self, image_path):
        # Load the image
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        # Create a fade effect
        alpha = 255  # Start with full opacity
        fading = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    fading = True  # Start fading on mouse click
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Optional: Continue on space bar press
                        return

            if fading:
                alpha -= 5  # Reduce the opacity by 5
                if alpha <= 0:
                    return  # Exit once the image is fully faded

                # Apply the new alpha and update the display
                temp_image = image.copy()  # Create a copy to modify
                temp_image.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)
                self.display_surface.blit(temp_image, (0, 0))
            else:
                # Blit the image to the display surface without fading
                self.display_surface.blit(image, (0, 0))

            pygame.display.flip()  # Update the display
            self.clock.tick(30)  # Control the fade speed


   
        
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
        self.curr_stage=self.stage4   
     #   self.curr_stage.guard_game.curr_posx=518
      #  self.curr_stage.guard_game.curr_posy =92
        while True:
            self.cnt+=1
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            if self.cnt<=1:
                a = level0_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)  # Pass display_surface to level function
            
                self.fade_out()
                if not a:
                    break 
                
                self.play_video('graphics/useful_images/loading_video.mp4')  
                
                self.play_video('graphics/useful_images/vid1.mp4')  
                
                # self.display_image('useful_images/img_3.png')

                self.play_video('graphics/useful_images/vid2.mp4')  
                
                self.play_video('graphics/useful_images/vid3.mp4')  
                
                self.play_video('graphics/useful_images/vid5.mp4')  
                
                # self.display_image('useful_images/img_7.png')
            
                
                b=level1_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
                self.fade_in()
                self.fade_out()
                if not b:
                    break

                self.fade_in()
                self.fade_out()
            
            
          #  d =self.curr_stage.run(dt)
         #   if  d :
            #    print('true')
          #      self.display_surface.blit(text_surface, ((settings.WINDOW_WIDTH - text_surface.get_width()) // 2, 
           #                                               settings.WINDOW_HEIGHT - text_surface.get_height()))
              #  keys = pygame.key.get_pressed()
               # if keys[pygame.K_f]:
                   # print("hi")
         #   print(self.curr_stage.guard_game.curr_posx,self.curr_stage.guard_game.curr_posx," bhjjbjh")
         
         
         
         
         
         
         
         
         
         
         
         
         
         
            
            if self.cnt>0 and self.cnt1==0:
                d =self.curr_stage.run(dt)
                if d==1:
                    self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                            settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_f]:
                        self.fade_in()
                        self.display_image('useful_images/img_5_.png',False)
                        self.fade_out()
                        x = level3_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
                        if x==1 or x==3: 
                            pygame.mixer.music.load('useful_images/busted_sound.mp3')
                            pygame.mixer.music.play(0)
                            self.display_image('useful_images/busted.png',True)
                            continue
                            # keys = pygame.key.get_pressed()
                            # if keys[pygame.K_f]:
                            #     self.stage4 = level4_game(self.tmx_maps[2],self.level_frames)
                            #     self.stage5 =level5_game(self.tmx_maps[3],self.level_frames)
                            #     self.stage6 =level6_game(self.tmx_maps[4],self.level_frames)
                            #     self.stage7 = level7_game(self.tmx_maps[5],self.level_frames)
                            #     self.stage8 =level8_game(self.tmx_maps[6],self.level_frames)
                            #     self.curr_stage =self.stage4
                            
                                     
                        else :
                            self.curr_stage=self.stage5
                            continue 
                if d==-5 or d==-7:
                    pygame.mixer.music.load('useful_images/busted_sound.mp3')
                    pygame.mixer.music.play(0)
                    self.display_image('useful_images/busted.png',True)
                    continue
                    
                if d==5 :
                    self.curr_stage=self.stage6
                if d==12 or d==13 or d==14:
                    if d==13:
                        self.curr_stage =self.stage5 
                    elif d==14:
                        self.curr_stage =self.stage7 
                    else:
                        self.curr_stage =self.stage5 
                        self.curr_stage.key2=1 
                if d==7:
                    self.curr_stage = self.stage5 
                if d==18:
                    self.curr_stage = self.stage8
                if d==16:
                    self.cnt1=1 
            if self.cnt1==1:
                self.play_video('graphics/useful_images/vid4.mp4')  
                self.play_video('graphics/useful_images/vid6.mp4')  
                e=level2_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
                
                if e==1 or e==2:
                    pygame.mixer.music.load('useful_images/busted_sound.mp3')
                    pygame.mixer.music.play(0)
                    self.display_image('useful_images/busted.png',True)
                    continue 
                else :
                    self.play_video('graphics/useful_images/vid7.mp4')   
                    p=level9_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT) 
                    if p==2:
                        pygame.mixer.music.load('useful_images/busted_sound.mp3')
                        pygame.mixer.music.play(0)
                        self.display_image('useful_images/busted.png',True)
                        continue  
                    else :
                        pygame.mixer.music.load('useful_images/ending_note.mp3')
                        pygame.mixer.music.play(-1)
                        self.play_video('graphics/useful_images/vid8.mp4')                      
                        self.fade_in()
                        ans=level10_game(self.display_surface, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
                        if not ans:
                            break
                        self.fade_in()
                        self.play_video('useful_images/credits.mp4')                      
                        self.fade_out()
                        
                        
            pygame.display.update()
            
             
                

if __name__ == '__main__':
    game = Game()
    game.run()

