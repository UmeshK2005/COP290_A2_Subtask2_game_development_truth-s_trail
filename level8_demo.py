from settings import * 
from sprites import Sprite
from groups import Allsprites 
from player import Player
import pytmx 
import math 


class obj_render_bg_wall1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/bg_wall1.png')
        resized_image = pygame.transform.scale(self.image, (900, 700))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(513, -181)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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


class obj_render_bg_wall2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/objects/bg_wall3.png')
        resized_image = pygame.transform.scale(self.image, (650,600))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(-137, -270)
        self.direction =vector()
        self.speed = 0       
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_carpet1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/rugRounded_NW.png')
        resized_image = pygame.transform.scale(self.image, (120, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(448, 417)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_pot1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_NE.png')
        resized_image = pygame.transform.scale(self.image, (50,60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(778, 604)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_pot2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_NE.png')
        resized_image = pygame.transform.scale(self.image, (50, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(98, 240)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_table1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/tableRound_SE.png')
        resized_image = pygame.transform.scale(self.image, (130, 130))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(704, 408)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_chair(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/chairDesk_SW.png')
        resized_image = pygame.transform.scale(self.image, (80, 120))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(699, 156)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_pot3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_NE.png')
        resized_image = pygame.transform.scale(self.image, (50, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1149, 401)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

#Level2-----------------------------------------------------------------
#------------------------------------------------------------------------

class obj_render_cat(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Sprites/Sprites/Temple/Decoration/statue_cat_NW.png')
        resized_image = pygame.transform.scale(self.image, (80, 100))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(151, 178)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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
        

class obj_render_dryer(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/washerDryerStacked_SE.png')
        resized_image = pygame.transform.scale(self.image, (100, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(224, 90)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_table2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/tableCrossCloth_NE.png')
        resized_image = pygame.transform.scale(self.image, (120, 80))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(372, 71)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_dustbin(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/shower_NW.png')
        resized_image = pygame.transform.scale(self.image, (40, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(497, 23)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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


class obj_render_desk(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/sideTableDrawers_SW.png')
        resized_image = pygame.transform.scale(self.image, (150, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(608, 207)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_lamp(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/lampRoundTable_NE.png')
        resized_image = pygame.transform.scale(self.image, (50, 50))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(747, 421)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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


class obj_render_sofa(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/lumeish - furniture pack/1.png')
        resized_image = pygame.transform.scale(self.image, (150, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(866, 254)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_bookshelf(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/furniture/bookshelfBooksRed_a.png')
        resized_image = pygame.transform.scale(self.image, (100, 170))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1096, 247)
        self.direction =vector()
        self.speed = 0        
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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


#Level3-----------------------------------------------------------------
#------------------------------------------------------------------------

class obj_render_tv(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/televisionModern_SE.png')
        resized_image = pygame.transform.scale(self.image, (130, 100))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(364, 21)
        self.direction =vector()
        self.speed = 0         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        # if keys[pygame.K_1]:
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

class obj_render_books(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Free isometric voxel room/PNGs/Books.png')
        resized_image = pygame.transform.scale(self.image, (55, 55))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1105, 239)
        self.direction =vector()
        self.speed = 100         
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_w]:
            input_vector.x+=a/2
            input_vector.y+=0.5
        if keys[pygame.K_a]:
            input_vector.x-=a/2
            input_vector.y-=0.5
        if keys[pygame.K_s]:
            input_vector.x-=a/2
            input_vector.y+=0.5
        if keys[pygame.K_d]:
            input_vector.x+=a/2
            input_vector.y-=0.5  
        if keys[pygame.K_1]:
             print(self.rect.topleft)
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
    def move(self,dt):
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt)


#-----------------------------------------------------------
#-----------------------------------------------------------

class level8_game:
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
        self.setup(self.tmx_map) 
        
        
        
    def setup(self, tmx_map):
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface = custom_font.render("Looks like some confidential files.Press 'f' to inspect the files", True, (0, 0, 0))
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name == 'bg_wall1':
                self.player1 = obj_render_bg_wall1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'bg_wall2':
                self.player1 = obj_render_bg_wall2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'carpet1':
                self.player1 = obj_render_carpet1((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'chair':
                self.player1 = obj_render_chair((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'table1':
                self.player1 = obj_render_table1((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'pot1':
                self.player1 = obj_render_pot1((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'pot2':
                self.player1 = obj_render_pot2((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'pot3':
                self.player1 = obj_render_pot3((obj.x, obj.y), self.all_sprites)    

        for obj in tmx_map.get_layer_by_name('Object Layer 2'):
            if obj.name == 'cat':
                self.player1 = obj_render_cat((obj.x, obj.y), self.all_sprites)
            if obj.name == 'dryer':
                self.player1 = obj_render_dryer((obj.x, obj.y), self.all_sprites)
            if obj.name == 'table':
                self.player1 = obj_render_table2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'dustbin':
                self.player1 = obj_render_dustbin((obj.x, obj.y), self.all_sprites)
            if obj.name == 'desk':
                self.player1 = obj_render_desk((obj.x, obj.y), self.all_sprites)
            if obj.name == 'sofa':
                self.player1 = obj_render_sofa((obj.x, obj.y), self.all_sprites)
            if obj.name == 'lamp':
                self.player1 = obj_render_lamp((obj.x, obj.y), self.all_sprites)
            if obj.name == 'bookshelf':
                self.player1 = obj_render_bookshelf((obj.x, obj.y), self.all_sprites)
            if obj.name == 'table2':
                self.player1 = obj_render_table2((obj.x, obj.y), self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Object Layer 3'):
            if obj.name == 'books':
                self.player1 = obj_render_books((obj.x, obj.y), self.all_sprites)
            if obj.name == 'tv':
                self.player1 = obj_render_tv((obj.x, obj.y), self.all_sprites)
            
        for obj in tmx_map.get_layer_by_name('Object Layer 4'):
            if obj.name == 'player':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['player']
                map = 'final_map5'
                self.player = Player(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                self.curr_posx = self.player.rect.x
                self.curr_posy = self.player.rect.y
                
                
    def run(self,dt):
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
        self.all_sprites.update(dt)
        self.display_surface.fill((76,105,113))
        background_path = "graphics/objects/level8_game.png"  
        background_image = pygame.image.load(background_path).convert()
        background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.offset.x = -(self.player.rect.center[0] - settings.WINDOW_WIDTH/2)
        self.offset.y = -(self.player.rect.center[1] - settings.WINDOW_HEIGHT/2)
        # Blit the background onto the display surface
        self.display_surface.blit(background_image, self.offset)
        
        self.all_sprites.draw(self.player.rect.center)
        
        
        if (self.curr_posx>=540 and self.curr_posx<=640)and(self.curr_posy>=245 and self.curr_posy<=315):
            self.display_surface.blit(self.text_surface, ((settings.WINDOW_WIDTH - self.text_surface.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface.get_height()))
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_f] :
                return 16
        return 8 
     
        