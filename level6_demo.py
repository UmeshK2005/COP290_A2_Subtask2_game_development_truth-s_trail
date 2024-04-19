from settings import * 
from sprites import Sprite
from groups import Allsprites 
from player import Player
import pytmx 
import math 

class obj_render_bed(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/bedDouble_SW.png')
        resized_image = pygame.transform.scale(self.image, (300, 220))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(425,78)
        self.direction =vector()
        self.speed = 0         
        
    
    

class obj_render_carpet(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/Props/rugLargePurple.png')
        resized_image = pygame.transform.scale(self.image, (150, 100))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(304, 274)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_lamp(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/lampRoundFloor_SW.png')
        resized_image = pygame.transform.scale(self.image, (40, 90))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(436,6)
        self.direction =vector()
        self.speed = 0        
        
    

class obj_render_drawer(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/dryer_SW.png')
        resized_image = pygame.transform.scale(self.image, (70, 70))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(479,58)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_wall1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallTan_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(473,-118)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_wall2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallTan_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(709, -10)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_wall3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallTan_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(936, 104)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_wall4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallTan_b.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(229, -108)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_wall5(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallTan_b.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(9,-4)
        self.direction =vector()
        self.speed = 0        
        
    


#Level2-----------------------------------------------------------------
#------------------------------------------------------------------------

class obj_render_window(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Free isometric voxel room/PNGs/Mirror 1.png')
        resized_image = pygame.transform.scale(self.image, (100, 100))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(127, 59)
        self.direction =vector()
        self.speed = 0        
        
    

class obj_render_curtain2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/Props/courtainBlue_b.png')
        resized_image = pygame.transform.scale(self.image, (105, 135))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(302, -45)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_curtain(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/Props/courtainPeach_b.png')
        resized_image = pygame.transform.scale(self.image, (100, 100))
        self.image=pygame.transform.flip(resized_image,True,False)
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(475,5)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_drawer3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/dryer_SW.png')
        resized_image = pygame.transform.scale(self.image, (80, 80))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(692, 188)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_table(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/tableCoffeeGlassSquare_NW.png')
        resized_image = pygame.transform.scale(self.image, (200, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(672, 277)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_almirah(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Free isometric voxel room/PNGs/shelving 2.png')
        resized_image = pygame.transform.scale(self.image, (200, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(820, 59)
        self.direction =vector()
        self.speed =0         
        
    

class obj_render_stool(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/lumeish - furniture pack/30.png')
        resized_image = pygame.transform.scale(self.image, (60, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(729, 535)
        self.direction =vector()
        self.speed = 0         
        
    


#Level3-----------------------------------------------------------------
#------------------------------------------------------------------------

class obj_render_drawer2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image1 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2.png')
        self.image2 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2_open_key.png')
        self.image3 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2_open.png')
        self.image1 = pygame.transform.flip(self.image1,True,False)
        self.image2 = pygame.transform.flip(self.image2,True,False)
        self.image3 = pygame.transform.flip(self.image3,True,False)
        resized_image1 = pygame.transform.scale(self.image1, (120, 120))
        resized_image2 = pygame.transform.scale(self.image2, (120, 120))
        resized_image3 = pygame.transform.scale(self.image3, (120, 120))
        self.image2 = resized_image2
        self.image3 = resized_image3
        
        self.image = resized_image1
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(151, 153)
        self.direction =vector()
        self.speed = 0   
class obj_render_drawer2_open_key(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image):
        super().__init__(groups)
        
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(151, 153)
        self.direction =vector()
        self.speed = 0   
class obj_render_drawer2_open(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image):
        super().__init__(groups)
        
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(151, 153)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_book(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Free isometric voxel room/PNGs/Books.png')
        resized_image = pygame.transform.scale(self.image, (40, 40))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(878, 106)
        self.direction =vector()
        self.speed = 0         
        
    


class obj_render_safe2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/bathroomCabinet_SW.png')
        resized_image = pygame.transform.scale(self.image, (70, 120))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1007, 225)
        self.direction =vector()
        self.speed = 0         
        
    

class obj_render_safe(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/bathroomMirror_SW.png')
        resized_image = pygame.transform.scale(self.image, (55, 65))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(890, 155)
        self.direction =vector()
        self.speed = 0      
        
    

#-----------------------------------------------------------
#-----------------------------------------------------------

class level6_game:
    def __init__(self,tmx_map,level_frames):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Allsprites()
        self.collision_layers = []
        self.anti_collision_layers = []
        self.offset = vector(0,0)
        self.collision_sprites = Allsprites()
        self.anti_collision_sprites =Allsprites()
        self.tmx_map =tmx_map
        self.level_frames = level_frames
        self.curr_posx = 0 
        self.curr_posy =0
        self.key=0
        self.vault_show =False 
        self.image_show =False 
        self.vault_unlocked =False 
        self.setup(self.tmx_map) 
        custom_cursor_path = "useful_images/cursor.jpg"
        self.mouse_pressed =False 
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface_1_ = custom_font.render("Looks like a picture and a drawer, kinda sus...", True, (0, 0, 0))
        self.text_surface1 = custom_font.render("Press 'G' to view the picture and 'F' to open the drawer!", True, (0, 0, 0))
        
        self.text_surface1_ = custom_font.render("Press 'G' to view picture and 'F' to take key!", True, (0, 0, 0))
        self.text_surface2_ = custom_font.render("Ahh! Another key... Press 'f' to take it", True, (0, 0, 0))
        self.text_surface2 = custom_font.render("Again,the drawer kinda looks sus..." , True, (0, 0, 0))
        self.text_surface3 = custom_font.render("It looks like some key,Press 'f' to take it !", True, (0, 0, 0))
        self.text_surface4 = custom_font.render("Key taken!", True, (0, 0, 0))
        self.text_surface5 = custom_font.render("Press 'G' to exit view", True, (0, 0, 0))
        self.text_surface6 = custom_font.render("Press 'k' to return to reception", True, (0, 0, 0))
        self.text_surface7 = custom_font.render("This vault seems somewhat weird.Press 'f' to examine.", True, (0, 0, 0))
        self.text_surface8 = custom_font.render("Oh,The vault is asking for a 3-digit long passcode.Press 'G' to enter the passcode.", True, (0, 0, 0))
        self.text_surface11 = custom_font.render("Excellent!!!,The vault is opened!!!,But behold!!", True, (0, 0, 0))
        self.text_surface12 = custom_font.render("Damnnn!!!, a secret room behind the vault.Press 'f' to enter .", True, (0, 0, 0))
        
        self.text_surface_tries1 = custom_font.render("You have only 2-tries left!", True, (0, 0, 0))
        self.text_surface_tries2 = custom_font.render("You have only 1-try left!", True, (0, 0, 0))
        self.text_surface_tries3 = custom_font.render("The passcode is wrong!", True, (0, 0, 0))
        
        cursor_image = pygame.image.load(custom_cursor_path).convert_alpha()
        cursor_mask = pygame.mask.from_surface(cursor_image)
        non_transparent_points = cursor_mask.outline()
        min_x = min([p[0] for p in non_transparent_points])
        max_x = max([p[0] for p in non_transparent_points])
        min_y = min([p[1] for p in non_transparent_points])
        max_y = max([p[1] for p in non_transparent_points])
        cursor_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        cursor_surface = pygame.Surface(cursor_rect.size, pygame.SRCALPHA)
        cursor_surface.blit(cursor_image, (0, 0), cursor_rect)
        self.custom_cursor_size = (50, 50)  # Adjust the dimensions as needed
        self.custom_cursor_image = pygame.transform.scale(cursor_surface, self.custom_cursor_size)
        pygame.mouse.set_visible(False)
        self.start_time =0
        self.start_time1=0
        self.current_time =1000
        self.current_time_vault =1000
        self.start_time_vault =0 
        self.start_time_pass =0 
        self.current_time_pass = 1000 
        self.current_time1=1000
        self.start_time1 =0
        self.tries =3 
        self.clock = pygame.time.Clock()
    
    def draw_text(self,surface, text, color, x, y,i):
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_path1 = "graphics/Lobster_1.3.otf"
        font_size1 = 36
        font_size2 = 80
        custom_font1 = pygame.font.Font(font_path, font_size1)
        custom_font2 = pygame.font.Font(font_path1, font_size2)
        self.text_surface9 = custom_font1.render(text, True, color)
        self.text_surface10 = custom_font2.render(text, True, color)
        if i==0:
            surface.blit(self.text_surface9, (x, y))    
        if i==1:
            surface.blit(self.text_surface10,(x,y))
    def input_box(self, screen, message):
        user_input = ''
        half_screen_width = screen.get_width() // 2
        half_screen_height = screen.get_height() // 2
        input_rect = pygame.Rect(half_screen_width // 2, half_screen_height, half_screen_width, 100)  # Half of the screen width and height, centered
        num_boxes = 3  # Number of boxes
        box_width = input_rect.width // num_boxes
        box_height = input_rect.height
        corner_radius = 20  # Adjust the corner radius as needed
        active = True

        while active:
            pygame.draw.rect(screen, (255, 255, 255), input_rect, border_radius=corner_radius)

            for i in range(num_boxes):
                box_rect = pygame.Rect(input_rect.x + i * box_width, input_rect.y, box_width, box_height)
                pygame.draw.rect(screen, (0, 0, 0), box_rect, width=2, border_radius=corner_radius)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key == pygame.K_g:
                        return "0"  # If 'g' is pressed, add "0" to the input
                    elif len(user_input) < num_boxes * 2:  # Limit input to 6 characters
                        user_input += event.unicode

            # Display message above input box
            self.draw_text(screen, message, (0, 0, 0), input_rect.x, input_rect.y-40 , 0)
            # Display user input inside boxes
            for i, char in enumerate(user_input):
                box_center_x = input_rect.x + i * (box_width) + box_width // 2
                box_center_y = input_rect.y + box_height // 2
                self.draw_text(screen, char, (0, 0, 0), box_center_x, box_center_y-40, 1)

            pygame.display.flip()

        return user_input


# Ensure you define the draw_text method and clock attribute appropriately in your class


    
    
    
    
    
        
    def play_button_clicked(self):
        self.current_time = (pygame.time.get_ticks())
       # print(self.key,self.image_show)
     #   print(self.current_time,self.start_time1,self.image_show,self.key,self.curr_posx,self.curr_posy)
      #  print(self.curr_posx,self.curr_posy)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]and (self.curr_posx>=230 and self.curr_posx<=260 and self.curr_posy>=130 and self.curr_posy<=200)and(self.current_time-self.start_time>=500):
            self.start_time = pygame.time.get_ticks()
            if self.key ==0:
                self.key =1
            elif self.key==1:
                self.key=2
        if keys[pygame.K_g]and (self.curr_posx>=230 and self.curr_posx<=260 and self.curr_posy>=130 and self.curr_posy<=200)and(self.current_time-self.start_time1>=500) and self.image_show ==False:
        #    print("hi")
            self.start_time1 = pygame.time.get_ticks()
            self.image_show = True 
             
        
        elif  self.image_show ==True :
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_g] and (self.current_time-self.start_time1>=500):
         #       print("dfs")
                self.start_time1 = pygame.time.get_ticks()
                self.image_show =False 
            
        
        if self.image_show :
        #    print("fdsfds")
            self.display_surface.blit(self.man_image, (settings.WINDOW_WIDTH//4, settings.WINDOW_HEIGHT//4))
            self.display_surface.blit(self.text_surface5, ((settings.WINDOW_WIDTH - self.text_surface5.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface5.get_height()-50))
        else:
        #    if (self.current_time-self.start_time<100 and self.current_time-self.start_time>0)  and self.key==1:
         #       self.display_surface.blit(self.text_surface3, ((settings.WINDOW_WIDTH - self.text_surface3.get_width()) // 2, 
           #                                               settings.WINDOW_HEIGHT - self.text_surface3.get_height()-50))
            if (self.current_time-self.start_time<1000 and self.current_time-self.start_time>0)  and self.key==2:
                self.display_surface.blit(self.text_surface4, ((settings.WINDOW_WIDTH - self.text_surface4.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface4.get_height()-50))
            else:
                self.mouse_pressed=False 
        
        
        
    def setup(self, tmx_map):
        man_image = pygame.image.load("graphics/useful_images/man_image.jpeg").convert_alpha()
        self.man_image = pygame.transform.scale(man_image, (settings.WINDOW_WIDTH//2, settings.WINDOW_HEIGHT//2))
        background_path = "graphics/objects/level6_game.png"  
        background_image = pygame.image.load(background_path).convert()
        self.background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name == 'bed':
                self.player1 = obj_render_bed((obj.x, obj.y), self.all_sprites)
            if obj.name == 'carpet':
                self.player1 = obj_render_carpet((obj.x, obj.y), self.all_sprites)
            if obj.name == 'lamp':
                self.player1 = obj_render_lamp((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'drawer':
                self.player1 = obj_render_drawer((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'wall1':
                self.player1 = obj_render_wall1((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'wall2':
                self.player1 = obj_render_wall2((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'wall3':
                self.player1 = obj_render_wall3((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'wall4':
                self.player1 = obj_render_wall4((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'wall5':
                self.player1 = obj_render_wall5((obj.x, obj.y), self.all_sprites)    
        for obj in tmx_map.get_layer_by_name('Object Layer 2'):
            if obj.name == 'window':
                self.player1 = obj_render_window((obj.x, obj.y), self.all_sprites)
            if obj.name == 'curtain2':
                self.player1 = obj_render_curtain2((obj.x, obj.y), self.all_sprites)
            # if obj.name == 'curtain':
            #     self.player1 = obj_render_curtain((obj.x, obj.y), self.all_sprites)
            if obj.name == 'almirah':
                self.player1 = obj_render_almirah((obj.x, obj.y), self.all_sprites)
            if obj.name == 'drawer3':
                self.player1 = obj_render_drawer3((obj.x, obj.y), self.all_sprites)
            if obj.name == 'table':
                self.player1 = obj_render_table((obj.x, obj.y), self.all_sprites)
            if obj.name == 'stool':
                self.player1 = obj_render_stool((obj.x, obj.y), self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 3'):
            if obj.name == 'books':
                self.player1 = obj_render_book((obj.x, obj.y), self.all_sprites)
            if obj.name == 'safe2':
                self.player1 = obj_render_safe2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'safe':
                self.player1 = obj_render_safe((obj.x, obj.y), self.all_sprites)
            if obj.name == 'drawer2':
                self.player_drawer = obj_render_drawer2((obj.x, obj.y), self.all_sprites)          
                
        for obj in tmx_map.get_layer_by_name('Object Layer 4'):
            if obj.name == 'player':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['player']
                map = 'final_map3'
                self.player = Player(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                self.curr_posx = self.player.rect.x
                self.curr_posy = self.player.rect.y
                
                
    def run(self,dt):
    
        
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
        self.all_sprites.update(dt)
        self.display_surface.fill((76,105,113))
        
        self.offset.x = -(self.player.rect.center[0] - settings.WINDOW_WIDTH/2)
        self.offset.y = -(self.player.rect.center[1] - settings.WINDOW_HEIGHT/2)
        # Blit the background onto the display surface
        self.display_surface.blit(self.background_image, self.offset)
        
        self.all_sprites.draw(self.player.rect.center)
        if (self.curr_posx>=230 and self.curr_posx<=260)and(self.curr_posy>=130 and self.curr_posy<=200) and self.key ==0:
          #  print("found")
            self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
            self.display_surface.blit(self.text_surface_1_, ((settings.WINDOW_WIDTH - self.text_surface_1_.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface_1_.get_height()-50))
        if (self.curr_posx>=230 and self.curr_posx<=260)and(self.curr_posy>=130 and self.curr_posy<=200) and self.key ==1:
          #  print("found")
            self.display_surface.blit(self.text_surface1_, ((settings.WINDOW_WIDTH - self.text_surface1_.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1_.get_height()))
            self.display_surface.blit(self.text_surface2_, ((settings.WINDOW_WIDTH - self.text_surface2_.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface2_.get_height()-50))
        
        key1 = self.key 
        self.play_button_clicked()
        key2 =self.key 
     #   print(self.key)
        if key2>key1:
            for obj in self.tmx_map.get_layer_by_name('Object Layer 3'):
                if obj.name == 'drawer2' and key2==1:
                    obj_render_drawer2_open_key((obj.x, obj.y), self.all_sprites,self.player_drawer.image2)
                if obj.name == 'drawer2' and key2==2:
                    obj_render_drawer2_open((obj.x, obj.y), self.all_sprites,self.player_drawer.image3)
        if self.key!=2:
            self.display_surface.blit(self.text_surface6, ((settings.WINDOW_WIDTH - self.text_surface6.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface6.get_height()-100))
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_k] :
                return 13
        if self.key==2:
            self.display_surface.blit(self.text_surface6, ((settings.WINDOW_WIDTH - self.text_surface6.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface6.get_height()-100))
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_k] :
                return 12
            
       # self.display_surface.blit(self.custom_cursor_image, (mouse_pos[0] - self.custom_cursor_size[0] // 2, mouse_pos[1] - self.custom_cursor_size[1] // 2))
         
        if (self.curr_posx>=930 and self.curr_posx<=990)and(self.curr_posy>=275 and self.curr_posy<=320):
            if self.vault_show==False and self.vault_unlocked==False :
                self.display_surface.blit(self.text_surface7, ((settings.WINDOW_WIDTH - self.text_surface7.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface7.get_height()-50))
            keys = pygame.key.get_pressed()
            self.current_time_vault =pygame.time.get_ticks()
            if keys[pygame.K_f] :
                self.start_time_vault =pygame.time.get_ticks()
                self.vault_show=True 
            if self.vault_show and (self.current_time_vault-self.start_time_vault)<=3000:
                
                self.display_surface.blit(self.text_surface8, ((settings.WINDOW_WIDTH - self.text_surface8.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface8.get_height()-50))
            else:
                self.vault_show =False 
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_g]:
                    passcode = self.input_box(self.display_surface, "Enter 3-digit passcode:")
                    if passcode !="kd6":
                        self.start_time_pass =(pygame.time.get_ticks()) 
                        if passcode!="0":
                            self.tries-=1
                    if passcode =="kd6":
                        self.start_time_pass =(pygame.time.get_ticks())
                        self.tries=3
                        self.vault_unlocked=True
                        self.vault_show =True 
                    if self.tries<=0:
                        return -6
            self.current_time1 =pygame.time.get_ticks()
        #    print(self.vault_unlocked,self.current_time1,self.start_time1,self.tries)
            self.current_time_pass = (pygame.time.get_ticks()) 
            if self.vault_unlocked==False and (self.current_time1-self.start_time1)>=1000:
                    
                if self.tries==2:
                    
                    self.display_surface.blit(self.text_surface_tries1, ((settings.WINDOW_WIDTH - self.text_surface_tries1.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries1.get_height()-100))
                elif self.tries ==1:
                    self.display_surface.blit(self.text_surface_tries2, ((settings.WINDOW_WIDTH - self.text_surface_tries2.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries2.get_height()-100))
                 
                if self.current_time_pass-self.start_time_pass<=1000 and self.tries !=3:
                    self.display_surface.blit(self.text_surface_tries3, ((settings.WINDOW_WIDTH - self.text_surface_tries3.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries3.get_height()-150))
                    
            if self.vault_unlocked==True :
           #     print("hi")
                self.display_surface.blit(self.text_surface11, ((settings.WINDOW_WIDTH - self.text_surface11.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface11.get_height()-50))
                self.display_surface.blit(self.text_surface12, ((settings.WINDOW_WIDTH - self.text_surface12.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface12.get_height()))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    return 18
                
            
                
            
             
        #return False 
        return 6 
        