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
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map):
        super().__init__(groups)
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'attack', True
      #  print(self.frames[self.state])
        self.image = self.frames[self.state][self.frame_index]
        self.map =map 
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.speed_fac = 1
        self.xsize_fac = 1 
        self.ysize_fac =1
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        self.rect.x=1218.0
        self.rect.y = 320.3
        self.direction =vector(0.0,0.0)
        self.speed = 0.0
        self.xsize =60
        self.ysize = 50
       # print("hi")
        if self.map =='final_map2':
            self.rect.center=(630,431)
            self.speed_fac = 1
            self.xsize_fac = 1 
            self.ysize_fac =1
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    
                
        
            
        
    def input(self):
        self.current_time = ((pygame.time.get_ticks())//1000)%9
     #   print(self.current_time)
        b=math.sqrt(3)
        input_vector= vector(0,0)
        if self.current_time >=0 and self.current_time<=2 :
            self.state = 'attack'
            input_vector.x += b/2
            input_vector.y +=0.5 
            self.facing_right =False  
        if self.current_time>2 and self.current_time<4:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==4 :
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time>4 and self.current_time<=7:
            self.state = 'attack'
            input_vector.x -= b/2 
            input_vector.y -=0.5 
            self.facing_right =False
        if self.current_time>7 and self.current_time<9:
            self.state ='attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==9:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
      #  print(input_vector)
             
            
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        if self.map=='final_map2':
            a = float(self.direction.x) * float(self.speed) 
       #     print(a,self.direction,self.speed,dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed 
            self.rect.y +=b 
         
        else:
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
          
         
    def update(self,dt):
     #   print(self.rect.x,self.rect.y)
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        
        self.animate(dt)
     #   print("fdf")
      #  print(self.curr_posx,self.curr_posy,self.current_time)
class obj_render_guard2(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map):
        super().__init__(groups)
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'attack', True
      #  print(self.frames[self.state])
        self.image = self.frames[self.state][self.frame_index]
        self.map =map 
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.speed_fac = 1
        self.xsize_fac = 1 
        self.ysize_fac =1
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        self.rect.x=1153
        self.rect.y = 280
        self.direction =vector(0.0,0.0)
        self.speed = 0.0
        self.xsize =60
        self.ysize = 50
       # print("hi")
        if self.map =='final_map2':
            self.rect.center=(630,431)
            self.speed_fac = 1
            self.xsize_fac = 1 
            self.ysize_fac =1
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    
                
        
            
        
    def input(self):
        self.current_time = ((pygame.time.get_ticks())//1000)%9
     #   print(self.current_time)
        b=math.sqrt(3)
        input_vector= vector(0,0)
        if self.current_time >=0 and self.current_time<=2 :
            self.state = 'attack'
            input_vector.x += b/2
            input_vector.y +=0.5 
            self.facing_right =False  
        if self.current_time>2 and self.current_time<4:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==4 :
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time>4 and self.current_time<=7:
            self.state = 'attack'
            input_vector.x -= b/2 
            input_vector.y -=0.5 
            self.facing_right =False
        if self.current_time>7 and self.current_time<9:
            self.state ='attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==9:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
      #  print(input_vector)
             
            
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        if self.map=='final_map2':
            a = float(self.direction.x) * float(self.speed) 
       #     print(a,self.direction,self.speed,dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed 
            self.rect.y +=b 
         
        else:
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
          
         
    def update(self,dt):
     #   print(self.rect.x,self.rect.y)
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        
        self.animate(dt)
     #   print("fdf")
      #  print(self.curr_posx,self.curr_posy,self.current_time)
class obj_render_guard3(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map):
        super().__init__(groups)
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'attack', True
      #  print(self.frames[self.state])
        self.image = self.frames[self.state][self.frame_index]
        self.map =map 
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.speed_fac = 1
        self.xsize_fac = 1 
        self.ysize_fac =1
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        self.rect.x=852
        self.rect.y = 382
        self.direction =vector(0.0,0.0)
        self.speed = 0.0
        self.xsize =60
        self.ysize = 50
       # print("hi")
        if self.map =='final_map2':
            self.rect.center=(630,431)
            self.speed_fac = 1
            self.xsize_fac = 1 
            self.ysize_fac =1
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    
                
        
            
        
    def input(self):
        self.current_time = ((pygame.time.get_ticks())//1000)%9
     #   print(self.current_time)
        b=math.sqrt(3)
        input_vector= vector(0,0)
        if self.current_time >=0 and self.current_time<=2 :
            self.state = 'attack'
            input_vector.x += b/2
            input_vector.y +=0.5 
            self.facing_right =False  
        if self.current_time>2 and self.current_time<4:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==4 :
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time>4 and self.current_time<=7:
            self.state = 'attack'
            input_vector.x -= b/2 
            input_vector.y -=0.5 
            self.facing_right =False
        if self.current_time>7 and self.current_time<9:
            self.state ='attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==9:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
      #  print(input_vector)
             
            
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        if self.map=='final_map2':
            a = float(self.direction.x) * float(self.speed) 
       #     print(a,self.direction,self.speed,dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed 
            self.rect.y +=b 
         
        else:
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
          
         
    def update(self,dt):
     #   print(self.rect.x,self.rect.y)
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        
        self.animate(dt)
     #   print("fdf")
      #  print(self.curr_posx,self.curr_posy,self.current_time)

class obj_render_guard4(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map):
        super().__init__(groups)
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'attack', True
      #  print(self.frames[self.state])
        self.image = self.frames[self.state][self.frame_index]
        self.map =map 
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.speed_fac = 1
        self.xsize_fac = 1 
        self.ysize_fac =1
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        self.rect.x=767
        self.rect.y = 654
        self.direction =vector(0.0,0.0)
        self.speed = 0.0
        self.xsize =60
        self.ysize = 50
       # print("hi")
        if self.map =='final_map2':
            self.rect.center=(630,431)
            self.speed_fac = 1
            self.xsize_fac = 1 
            self.ysize_fac =1
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    
                
        
            
        
    def input(self):
        self.current_time = ((pygame.time.get_ticks())//1000)%9
     #   print(self.current_time)
        b=math.sqrt(3)
        input_vector= vector(0,0)
        if self.current_time >=0 and self.current_time<=2 :
            self.state = 'attack'
            input_vector.x += b/2
            input_vector.y +=0.5 
            self.facing_right =False  
        if self.current_time>2 and self.current_time<4:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==4 :
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time>4 and self.current_time<=7:
            self.state = 'attack'
            input_vector.x -= b/2 
            input_vector.y -=0.5 
            self.facing_right =False
        if self.current_time>7 and self.current_time<9:
            self.state ='attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==9:
            self.state = 'attack'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
      #  print(input_vector)
             
            
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        if self.map=='final_map2':
            a = float(self.direction.x) * float(self.speed) 
       #     print(a,self.direction,self.speed,dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed 
            self.rect.y +=b 
         
        else:
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
          
         
    def update(self,dt):
     #   print(self.rect.x,self.rect.y)
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        
        self.animate(dt)
     #   print("fdf")
      #  print(self.curr_posx,self.curr_posy,self.current_time)





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
               #     print(tile)
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
            if obj.name == 'Guard 1':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['guards']
                map = 'final_map1'
                self.guard_game = obj_render_guard1(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                
                
            if obj.name == 'Guard 2':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['guards']
                map = 'final_map1'
                self.guard_game = obj_render_guard2(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
            if obj.name == 'Guard 3':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['guards']
                map = 'final_map1'
                self.guard_game = obj_render_guard3(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
            if obj.name == 'Guard 4':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['guards']
                map = 'final_map1'
                self.guard_game = obj_render_guard4(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                
                
                
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
        
        pygame.mixer.music.load('useful_images/l_theme_death_note.mp3')
        pygame.mixer.music.play(-1)
        self.all_sprites.update(dt)
        self.display_surface.fill((57,187,114))
        self.all_sprites.draw(self.player.rect.center)
        if (self.curr_posx<=1290 and self.curr_posx>=1180)and(self.curr_posy<=300 and self.curr_posy>=200):
            return 1 
        return 0 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
