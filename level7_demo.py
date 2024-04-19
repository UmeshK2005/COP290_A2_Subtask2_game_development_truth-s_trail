from settings import * 
from sprites import Sprite
from groups import Allsprites 
from player import Player
import pytmx 
import math 

class obj_render_sofa1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeSofa_SE.png')
      #  print("found sofa img")
        resized_image = pygame.transform.scale(self.image, (200, 200))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(396, 117)
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

class obj_render_sofa2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeChair_SW.png')
        resized_image = pygame.transform.scale(self.image, (150, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(659,129)
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


class obj_render_table(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/tableCoffeeGlassSquare_NW.png')
        resized_image = pygame.transform.scale(self.image, (250, 200))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(496, 215)
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
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/kitchenCabinetUpperLow_SE.png')
        resized_image = pygame.transform.scale(self.image, (100, 100))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(119, 187)
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
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/kitchenCabinetUpperCorner_SW.png')
        resized_image = pygame.transform.scale(self.image, (130, 130))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1071, 316)
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

class obj_render_wall1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallBlue_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 300))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(488, -164)
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

class obj_render_wall2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallBlue_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 300))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(715, -30)
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

class obj_render_wall3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallBlue_a.png')
        resized_image = pygame.transform.scale(self.image, (250, 300))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(950, 97)
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

class obj_render_wall4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallBlue_b.png')
        resized_image = pygame.transform.scale(self.image, (250, 300))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(244, -162)
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

class obj_render_wall5(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallBlue_b.png')
        resized_image = pygame.transform.scale(self.image, (250, 300))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(18, -31)
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

class obj_render_window1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Free isometric voxel room/PNGs/Mirror 2.png')
        resized_image = pygame.transform.scale(self.image, (80, 80))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(996, 187)
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

class obj_render_window2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/paneling_SE.png')
        resized_image = pygame.transform.scale(self.image, (60, 105))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(331, -69)
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

class obj_render_drawer(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/dryer_SE.png')
        resized_image = pygame.transform.scale(self.image, (80, 80))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(225, 143)
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
        resized_image = pygame.transform.scale(self.image, (50, 65))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(768, 617)
        self.direction = vector()
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
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/trashcan_SE.png')
        resized_image = pygame.transform.scale(self.image, (40, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(476, -7)
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

class obj_render_laptop(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/laptop_SW.png')
        resized_image = pygame.transform.scale(self.image, (80, 80))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(565, 244)
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

class obj_render_carpet(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/rugRounded_NW.png')
        resized_image = pygame.transform.scale(self.image, (200, 130))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(389, 368)
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

class obj_render_sofa3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeChair_NE.png')
        resized_image = pygame.transform.scale(self.image, (150, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(640, 364)
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

class obj_render_sofa4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeSofaCorner_SW.png')
        resized_image = pygame.transform.scale(self.image, (250, 250))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(738, 194)
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

class obj_render_pot(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_NW.png')
        resized_image = pygame.transform.scale(self.image, (40, 60))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(738, 194)
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

class obj_render_table3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/kitchenCabinet_SW.png')
        resized_image = pygame.transform.scale(self.image, (120, 120))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(944, 276)
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



#-----------------------------------------------------------
#-----------------------------------------------------------

class level7_game:
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
        self.clock = pygame.time.Clock()
        self.tries =3
        self.current_time_pass=1000
        self.start_time_pass =0 
        self.current_time_show=1000
        self.start_time_show =0 
        self.image_show =False 
        self.laptop_unlocked =False 

    def draw_text(self,surface, text, color, x, y,i):
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size1 = 36
        font_size2 = 100
        custom_font1 = pygame.font.Font(font_path, font_size1)
        custom_font2 = pygame.font.Font(font_path, font_size2)
        self.text_surface7 = custom_font1.render(text, True, color)
        self.text_surface8 = custom_font2.render(text, True, color)
        if i==0:
            surface.blit(self.text_surface7, (x, y))    
        if i==1:
            surface.blit(self.text_surface8,(x,y))
    def input_box(self, screen, message):
        user_input = ''
        half_screen_width = screen.get_width() // 2
        half_screen_height = screen.get_height() // 2
        input_rect = pygame.Rect(half_screen_width // 2, half_screen_height - 50, half_screen_width, 100)  # Half of the screen width and height, centered
        box_width = input_rect.width // 6
        box_height = input_rect.height
        corner_radius = 20  # Adjust the corner radius as needed
        active = True

        while active:
            # Fill only half of the screen with white
            pygame.draw.rect(screen, (255, 255, 255), input_rect, border_radius=corner_radius)

            for i in range(6):
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
                    elif event.unicode.isdigit() and len(user_input) < 6:  # Accept only digits and limit input to 6 characters
                        user_input += event.unicode

            # Display message above input box
            self.draw_text(screen, message, (0, 0, 0), input_rect.x, input_rect.y - 40,0)
            # Display user input inside boxes
            for i, char in enumerate(user_input):
                self.draw_text(screen, char, (0, 0, 0), input_rect.x + i * box_width + 15, input_rect.y + 15,1)

            pygame.display.flip()
            self.clock.tick()

        return user_input



# Ensure you define the draw_text method and clock attribute appropriately in your class



        
    def setup(self, tmx_map):
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface1 = custom_font.render("The laptop is locked ,press 'f' to enter 6-digit passcode", True, (0, 0, 0))
        self.text_surface2 = custom_font.render("Press 'f' to exit the view", True, (0, 0, 0))
        self.text_surface3 = custom_font.render("Laptop Unlocked!!!, Appears like a chess-puzzle. Press 'f' to view the puzzle", True, (0, 0, 0))
        self.text_surface4 = custom_font.render("Press 'K' to return to the reception ", True, (0, 0, 0))
        self.text_surface_tries1 = custom_font.render("You have only 2-tries left!", True, (0, 0, 0))
        self.text_surface_tries2 = custom_font.render("You have only 1-try left!", True, (0, 0, 0))
        self.text_surface_tries3 = custom_font.render("The passcode is wrong!", True, (0, 0, 0))
        chess_image = pygame.image.load("graphics/useful_images/chess_puzzle.png").convert_alpha()
        self.chess_image = pygame.transform.scale(chess_image, (settings.WINDOW_WIDTH//2+200, settings.WINDOW_HEIGHT//2+200))
        
        
        
        
        
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
        #    print(obj.name)
            if obj.name == 'sofa1':
                self.player1 = obj_render_sofa1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'sofa2':
                self.player1 = obj_render_sofa2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'table':
                self.player1 = obj_render_table((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'table2':
                self.player1 = obj_render_table2((obj.x, obj.y), self.all_sprites)    
            if obj.name == 'table1':
                self.player1 = obj_render_table1((obj.x, obj.y), self.all_sprites)    
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
            if obj.name == 'drawer':
                self.player1 = obj_render_drawer((obj.x, obj.y), self.all_sprites)
            if obj.name == 'window2':
                self.player1 = obj_render_window2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'window1':
                self.player1 = obj_render_window1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'pot2':
                self.player1 = obj_render_pot2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'dustbin':
                self.player1 = obj_render_dustbin((obj.x, obj.y), self.all_sprites)
            if obj.name == 'carpet':
                self.player1 = obj_render_carpet((obj.x, obj.y), self.all_sprites)
            if obj.name == 'sofa3':
                self.player1 = obj_render_sofa3((obj.x, obj.y), self.all_sprites)
            if obj.name == 'laptop':
                self.player1 = obj_render_laptop((obj.x, obj.y), self.all_sprites)
            if obj.name == 'sofa4':
                self.player1 = obj_render_sofa4((obj.x, obj.y), self.all_sprites)
            if obj.name == 'table3':
                self.player1 = obj_render_table3((obj.x, obj.y), self.all_sprites)
            if obj.name == 'pot':
                self.player1 = obj_render_pot((obj.x, obj.y), self.all_sprites)


        for obj in tmx_map.get_layer_by_name('Object Layer 3'):
            if obj.name == 'player':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['player']
                map = 'final_map4'
                self.player = Player(pos, groups, collision_sprites, anti_collision_sprites, frames, map)
                self.curr_posx = self.player.rect.x
                self.curr_posy = self.player.rect.y
                
                
    def run(self,dt):
    
        
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
        self.all_sprites.update(dt)
        self.display_surface.fill('white')
        background_path = "graphics/objects/level7_game.jpeg"  
        background_image = pygame.image.load(background_path).convert()
        background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.offset.x = -(self.player.rect.center[0] - settings.WINDOW_WIDTH/2)
        self.offset.y = -(self.player.rect.center[1] - settings.WINDOW_HEIGHT/2)
        # Blit the background onto the display surface
        self.display_surface.blit(background_image, self.offset)
        
        self.all_sprites.draw(self.player.rect.center)
        
        
        if (self.curr_posx>=490 and self.curr_posx<=570 and self.curr_posy>=320 and self.curr_posy<=370) :
            self.current_time_pass=(pygame.time.get_ticks())
            if self.laptop_unlocked==False and self.image_show==False and (self.current_time_pass-self.start_time_pass)>=1000:
                self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
                if self.tries==2:
                    
                    self.display_surface.blit(self.text_surface_tries1, ((settings.WINDOW_WIDTH - self.text_surface_tries1.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries1.get_height()-50))
                elif self.tries ==1:
                    self.display_surface.blit(self.text_surface_tries2, ((settings.WINDOW_WIDTH - self.text_surface_tries2.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries2.get_height()-50))
                keys = pygame.key.get_pressed()
                 
                if self.current_time_pass-self.start_time_pass<=1000:
                    self.display_surface.blit(self.text_surface_tries3, ((settings.WINDOW_WIDTH - self.text_surface_tries3.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface_tries3.get_height()-100))
                if keys[pygame.K_f]:
                    passcode = self.input_box(self.display_surface, "Enter 6-digit passcode:")
                    if passcode !="191167":
                        self.start_time_pass =(pygame.time.get_ticks()) 
                        
                        self.tries-=1
                    if passcode =="191167":
                        self.start_time_pass =(pygame.time.get_ticks())
                        self.tries=3
                        self.laptop_unlocked=True
                    if self.tries<=0:
                        return -7
            if self.laptop_unlocked:
                self.display_surface.blit(self.text_surface3, ((settings.WINDOW_WIDTH - self.text_surface3.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface3.get_height()))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    self.start_time_pass =(pygame.time.get_ticks())
                    self.image_show =True 
                    self.laptop_unlocked=False  
                
            elif self.image_show:
                keys = pygame.key.get_pressed()
            
                if keys[pygame.K_f] and (self.current_time_pass-self.start_time_pass>=500):
                    self.start_time_pass = pygame.time.get_ticks()
                    self.image_show =False
            if self.image_show:
                self.display_surface.blit(self.chess_image, (settings.WINDOW_WIDTH//4-100, settings.WINDOW_HEIGHT//4-100))
                self.display_surface.blit(self.text_surface2, ((settings.WINDOW_WIDTH - self.text_surface2.get_width()) // 2, 
                                                          self.text_surface2.get_height()-50))
        if self.image_show==False:
            self.display_surface.blit(self.text_surface4, ((settings.WINDOW_WIDTH - self.text_surface4.get_width()) // 2, 
                                                          self.text_surface4.get_height()-50))
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_k]:
                return 7 
                
                    
            
                
                
        '''
                self.display_surface.blit(self.text_surface3, ((settings.WINDOW_WIDTH - self.text_surface3.get_width()) // 2, 
                                                                settings.WINDOW_HEIGHT - self.text_surface3.get_height()))
                keys = pygame.key.get_pressed()
                self.current_time_show =(pygame.time.get_ticks()) 
                
                if keys[pygame.K_f]:
                    
                    self.display_surface.blit(self.chess_image, (settings.WINDOW_WIDTH//4-200, settings.WINDOW_HEIGHT//4-200))
                    self.display_surface.blit(self.text_surface2, ((settings.WINDOW_WIDTH - self.text_surface2.get_width()) // 2, 
                                                          self.text_surface2.get_height()-50))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_k]:
                    self.image_show=False 
                    '''
                    
       # if (self.curr_posx<=1290 and self.curr_posx>=1180)and(self.curr_posy<=300 and self.curr_posy>=200):
       #     return True 
        #return False 
        