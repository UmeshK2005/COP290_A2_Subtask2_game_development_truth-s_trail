from settings import * 
from sprites import Sprite
from groups import Allsprites 
from player import Player
import pytmx 
import math 
class obj_render_sofa1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeSofa_NE.png')
        resized_image = pygame.transform.scale(self.image, (100, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(0,0)
        self.direction =vector()
        self.speed = 200         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=a/2
            input_vector.y+=1/2
        if keys[pygame.K_LEFT]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_DOWN]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_UP]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
       # if keys[pygame.K_0]:
       #     print(self.rect.topleft)
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)


class level5_game:
    def __init__(self,tmx_map,level_frames):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Allsprites()
        self.collision_layers = []
        self.anti_collision_layers = []
        
        self.collision_sprites = Allsprites()
        self.anti_collision_sprites =Allsprites()
        self.tmx_map =tmx_map
        self.level_frames = level_frames
        self.curr_posx = 0 
        self.curr_posy =0
        self.setup(self.tmx_map) 
        
        
    def setup(self, tmx_map):

        # Iterate over objects in the map
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name == 'sofa1':
                self.player1 = obj_render_sofa1((obj.x, obj.y), self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Object Layer 6'):
            if obj.name == 'player':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['player']
                map = 'final_map2'
                self.player = Player(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                self.curr_posx = self.player.rect.x
                self.curr_posy = self.player.rect.y

                
    def run(self,dt):
    
        
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
     #   print(self.curr_posx,self.curr_posy)
        
            
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        background_path = "graphics/objects/level5map.jpeg"  
        background_image = pygame.image.load(background_path).convert()
        background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        # Blit the background onto the display surface
        self.display_surface.blit(background_image, (0, 0))
        
        self.all_sprites.draw(self.player.rect.center)
       # if (self.curr_posx<=1290 and self.curr_posx>=1180)and(self.curr_posy<=300 and self.curr_posy>=200):
       #     return True 
        #return False 