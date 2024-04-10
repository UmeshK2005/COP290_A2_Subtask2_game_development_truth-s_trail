from settings import * 
from sprites import Sprite 
import pytmx 

class obj_render_mansion(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_203804-removebg-preview.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000 
class obj_render_front_gate(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_215536-removebg-preview (1).png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000    
class obj_render_Guard1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000   
class obj_render_Guard2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000  
class obj_render_Guard3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000        
class obj_render_Guard4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/Screenshot_2024-04-03_205745-removebg-preview.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction =vector()
        self.speed = 1000         
        
        
        
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
    def __init__(self,tmx_map):
        self.display_surface = pygame.display.get_surface()
        
        
        self.all_sprites = pygame.sprite.Group()
        
        
        self.setup(tmx_map)
        
    def setup(self,tmx_map):
        #for x,y,surf in tmx_map.get_layer_by_name('Tile Layer 1').tiles():
        #    Sprite((x*settings.TILE_SIZE,y*settings.TILE_SIZE),surf,self.all_sprites)
        tile_width = settings.TILE_SIZE
        tile_height = settings.TILE_SIZE // 2  # Assuming isometric tiles are twice as wide as tall

        map_width = tmx_map.width
        map_height = tmx_map.height

        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = tmx_map.get_tile_image_by_gid(gid)
                    if tile:
                    # Convert orthogonal coordinates to isometric
                        iso_x = (x - y) * tile_width 
                        iso_y = (x + y) * tile_height
                    

            # Create the sprite at the adjusted position
                        Sprite((iso_x+1000, iso_y), tile, self.all_sprites)

        
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name=='mansion':
                obj_render_mansion((obj.x,obj.y),self.all_sprites)
            if obj.name=='front_gate':
                obj_render_front_gate((obj.x,obj.y),self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 2'):
            if obj.name=='Guard 1':
                obj_render_Guard1((obj.x,obj.y),self.all_sprites)
            if obj.name=='Guard 2':
                obj_render_Guard2((obj.x,obj.y),self.all_sprites)
            if obj.name=='Guard 3':
                obj_render_Guard3((obj.x,obj.y),self.all_sprites)
            if obj.name=='Guard 4':
                obj_render_Guard4((obj.x,obj.y),self.all_sprites)
                
                
            
            
            
    def run(self,dt):
       # print("hi")
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        