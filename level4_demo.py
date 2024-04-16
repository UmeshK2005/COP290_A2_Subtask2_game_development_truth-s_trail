from settings import * 
from sprites import Sprite
from groups import Allsprites 
from player import Player
import pytmx 
import math 

class obj_render_mansion(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_203804-removebg-preview.png')
     #   resized_image = pygame.transform.scale(self.image, (200, 100))
     #   self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1092,-70)
        self.direction =vector()
        self.speed = 0         
        
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
class obj_render_front_gate(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_215536-removebg-preview (1).png')
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(527,509)
        self.direction =vector()
        self.speed =0         
        
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=1
        if keys[pygame.K_LEFT]:
            input_vector.x-=1 
        if keys[pygame.K_DOWN]:
            input_vector.y+=1
        if keys[pygame.K_UP]:
            input_vector.y-=1 
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
class obj_render_guard1(pygame.sprite.Sprite):
    def __init__(self,pos,groups,start_pos,end_pos):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        resized_image = pygame.transform.scale(self.image, (25, 40))
        self.image = resized_image
        self.rect = self.image.get_frect(topleft = pos)
        self.rect.topleft=(1243,330)
        self.direction =vector()
        self.speed = 100  
        self.prev_motion =True 
        (a,b)=start_pos 
        (c,d)=end_pos
     #   print(a,b,c,d)
        self.a = a #1243
        self.b =b  #330
        self.c =c #800
        self.d =d     #400 
        self.move_x =(a-c)/1000 #0.443
        self.move_y =(d-b)/1000 #0.07 
        
        
    def input(self):
        input_vector=vector(0,0)
        
        if self.prev_motion==True:
            if self.rect.x>=self.c and self.rect.y<=self.d:
                input_vector.x-=self.move_x
                input_vector.y+=self.move_y
            else:
                self.prev_motion=False 
                self.rect.x=self.c
                self.rect.y =self.d
        else:
            if self.rect.x<=self.a and self.rect.y>=self.b:
                input_vector.x+=self.move_x
                input_vector.y-=self.move_y
            else:
                self.prev_motion=True 
                self.rect.x=self.a
                self.rect.y =self.b 
      #  print(input_vector)
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
         
        
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)
class obj_render_guard2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        resized_image = pygame.transform.scale(self.image, (25, 40))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        
        self.rect.topleft=(1140,278)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=1
        if keys[pygame.K_LEFT]:
            input_vector.x-=1 
        if keys[pygame.K_DOWN]:
            input_vector.y+=1
        if keys[pygame.K_UP]:
            input_vector.y-=1 
       # if keys[pygame.K_0]:
      #      print(self.rect.topleft) 
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)
class obj_render_guard3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        resized_image = pygame.transform.scale(self.image, (25, 40))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft =(761,683)
        self.direction =vector()
        self.speed = 0        
        
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=1
        if keys[pygame.K_LEFT]:
            input_vector.x-=1 
        if keys[pygame.K_DOWN]:
            input_vector.y+=1
        if keys[pygame.K_UP]:
            input_vector.y-=1 
     #   if keys[pygame.K_0]:
      #      print(self.rect.topleft) 
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)
class obj_render_guard4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        resized_image = pygame.transform.scale(self.image, (25, 40))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(842,385)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=1
        if keys[pygame.K_LEFT]:
            input_vector.x-=1 
        if keys[pygame.K_DOWN]:
            input_vector.y+=1
        if keys[pygame.K_UP]:
            input_vector.y-=1
       # if keys[pygame.K_0]:
        #    print(self.rect.topleft)  
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)




class level4_game:
    def __init__(self,tmx_map,level_frames):
        self.display_surface = pygame.display.get_surface()
    #    print("hi")
     
        self.all_sprites = Allsprites()
        self.collision_layers = ['Tile Layer 2','Tile Layer 3']
        self.anti_collision_layers = ['Tile Layer 1']
        
        self.collision_sprites = Allsprites()
        self.anti_collision_sprites =Allsprites()
        self.tmx_map =tmx_map
        self.level_frames = level_frames
        self.curr_posx = 0 
        self.curr_posy =0
        
        self.setup(self.tmx_map) 
       
    def get_anti_collision_sprites(self, tmx_map, layer_name):
        # Retrieve anti-collision sprites associated with the specified layer name
        anti_collision_sprites = Allsprites()
        # Loop through all layers in the map
        for layer in tmx_map.layers:
            # Check if the layer is the desired anti-collision layer
            if layer.name == layer_name:
                # Loop through all the tiles in the layer
                for x, y, gid in layer:
                    tile = tmx_map.get_tile_image_by_gid(gid)
                    # Check if the tile has collision properties
                    print(tile)
                   # Create a sprite for the tile and add it to the anti_collision_sprites group
                    sprite = Sprite()  # You need to define your Sprite class
                    sprite.image = tile
                    sprite.rect = pygame.Rect(x * tmx_map.tilewidth, y * tmx_map.tileheight, tmx_map.tilewidth, tmx_map.tileheight)
                    anti_collision_sprites.add(sprite)
       # print(anti_collision_sprites)
        return anti_collision_sprites

    def setup(self,tmx_map):
        #tiles
        tile_width = settings.TILE_SIZE
        tile_height = settings.TILE_SIZE // 2  # Assuming isometric tiles are twice as wide as tall
        map_width = tmx_map.width
        map_height = tmx_map.height
        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_map.get_tile_image_by_gid(gid)
                    if tile:
                        # Convert orthogonal coordinates to isometric
                        iso_x = (x - y) * tile_width 
                        iso_y = (x + y) * tile_height
                        if layer.name in self.collision_layers:
                            Sprite((iso_x + 1000, iso_y), tile, (self.all_sprites, self.collision_sprites))
                        elif layer.name in self.anti_collision_layers:
                            Sprite((iso_x + 1000, iso_y), tile, (self.all_sprites, self.anti_collision_sprites))
                        else:
                            Sprite((iso_x + 1000, iso_y), tile, self.all_sprites)


        #objects 
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name=='mansion':
                obj_render_mansion((obj.x,obj.y),self.all_sprites)
            if obj.name=='front_gate':
                obj_render_front_gate((obj.x,obj.y),self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 2'):
            if obj.name=='Guard 1':
                obj_render_guard1((obj.x,obj.y),self.all_sprites,(1243,330),(800,400))
            if obj.name=='Guard 2':
                obj_render_guard2((obj.x,obj.y),self.all_sprites)
            if obj.name=='Guard 3':
                obj_render_guard3((obj.x,obj.y),self.all_sprites)
            if obj.name=='Guard 4':
                obj_render_guard4((obj.x,obj.y),self.all_sprites)
                
                
                
        #moving objects 
        for obj in tmx_map.get_layer_by_name('Object Layer 3'):
            if obj.name =='player':
                pos = (obj.x,obj.y)
                groups =self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['player']
                map ='final_map1'
                self.player = Player(pos,groups,collision_sprites,anti_collision_sprites,frames,map)
                self.curr_posx = self.player.curr_posx
                self.curr_posy = self.player.curr_posy
                
                 
                
    
                
                
           
        
             
                
                
            
            
            
    def run(self,dt):
    
        
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
     #   print(self.curr_posx,self.curr_posy)
        
            
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        self.all_sprites.draw(self.player.rect.center)
        if (self.curr_posx<=1290 and self.curr_posx>=1180)and(self.curr_posy<=300 and self.curr_posy>=200):
            return True 
        return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
