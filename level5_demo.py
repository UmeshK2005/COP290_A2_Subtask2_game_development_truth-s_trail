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
        resized_image = pygame.transform.scale(self.image, (300, 220))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(847,377.0)
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
      #  if keys[pygame.K_1]:
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


class obj_render_sofa2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/loungeChairRelax_NE.png')
        resized_image = pygame.transform.scale(self.image, (180, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(750,489)
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
      #  if keys[pygame.K_1]:
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


class obj_render_pot1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_SW.png')
        resized_image = pygame.transform.scale(self.image, (60, 90))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(742,573)
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
    #    if keys[pygame.K_1]:
     #       print(self.rect.topleft)
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
        resized_image = pygame.transform.scale(self.image, (60, 90))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1157,384)
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
      #  if keys[pygame.K_1]:
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
class obj_render_desk1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/deskCorner_NE.png')
        resized_image = pygame.transform.scale(self.image, (400, 200))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(370,220)
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
      #  if keys[pygame.K_1]:
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
class obj_render_chair(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/chairDesk_SW.png')
        resized_image = pygame.transform.scale(self.image, (130, 130))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(513,138)
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
      #  if keys[pygame.K_1]:
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
class obj_render_desk2_initial(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image1 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2.png')
        self.image2 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2_open_key.png')
        self.image3 = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2_open.png')
        resized_image = pygame.transform.scale(self.image1, (150, 130))
        self.image = pygame.transform.flip(resized_image,True,False)
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(67,236)
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
        
        
        
        
        
        
        
class obj_render_desk2_open(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image):
        super().__init__(groups)
        self.image = image 
        resized_image = pygame.transform.scale(self.image, (150, 130))
        self.image = pygame.transform.flip(resized_image,True,False)
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(67,236)
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
      #  if keys[pygame.K_1]:
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
        
        
        
  
  
class obj_render_desk2_open_key(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image):
        super().__init__(groups)
        self.image  =image   #= pygame.image.load('graphics/kenney_furniturePack/Isometric/desk2_open_key.png')
        resized_image = pygame.transform.scale(self.image, (150, 130))
        self.image = pygame.transform.flip(resized_image,True,False)
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(67,236)
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
      #  if keys[pygame.K_1]:
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
        
                      
class obj_render_almirah(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/furniture/bookshelfBooksRed_b.png')
        resized_image = pygame.transform.scale(self.image, (150, 200))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(362,13)
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
      #  if keys[pygame.K_1]:
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
class obj_render_door1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/doorwayFront_NE.png')
        
        resized_image = pygame.transform.scale(self.image, (100, 150))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(189,109)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/pottedPlant_NW.png')
        resized_image = pygame.transform.scale(self.image, (60, 90))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(460,177)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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

class obj_render_wall1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallRed_a.png')
        resized_image = pygame.transform.scale(self.image, (350, 350))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(1106,199)
        self.direction =vector()
        self.speed =0         
        
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
      #  if keys[pygame.K_1]:
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
        
        
class obj_render_wall2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallRedDoor_a.png')
        resized_image = pygame.transform.scale(self.image, (350, 350))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(760,60)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallRed_a.png')
        resized_image = pygame.transform.scale(self.image, (350, 350))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(463,-85)
        self.direction =vector()
        self.speed =0         
        
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
      #  if keys[pygame.K_1]:
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
 
 
 
class obj_render_wall4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallRed_b.png')
        resized_image = pygame.transform.scale(self.image, (350, 350))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(117,-68)
        self.direction =vector()
        self.speed =0         
        
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
      #  if keys[pygame.K_1]:
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
        
        
        
        
        
class obj_render_wall5(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/IIP - Outlined/walls/wallRed_b.png')
        resized_image = pygame.transform.scale(self.image, (350, 350))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(-199,84)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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
        resized_image = pygame.transform.scale(self.image, (90, 50))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(454,468)
        self.direction =vector()
        self.speed =0         
        
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
      #  if keys[pygame.K_1]:
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
         

class obj_render_computer(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/computerScreen_SW.png')
        resized_image = pygame.transform.scale(self.image, (90, 90))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(472,232)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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


class obj_render_gate2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/doorwayFront_SW.png')
        resized_image = pygame.transform.scale(self.image, (90, 160))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(873,190)
        self.direction =vector()
        self.speed =0         
        
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
      #  if keys[pygame.K_1]:
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


class obj_render_chair2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/chairCushion_SW.png')
        resized_image = pygame.transform.scale(self.image, (120, 120))
        self.image = resized_image
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(881,325)
        self.direction =vector()
        self.speed =0         
        
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
    #    if keys[pygame.K_1]:
     #       print(self.rect.topleft)
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector 
         
    def move(self,dt):
        
        self.rect.topleft +=self.direction*self.speed*dt    
    def update(self,dt):
        self.input()
        self.move(dt) 


class obj_render_screen(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('useful_images/mansion_map.png')
        resized_image = pygame.transform.scale(self.image, (60, 30))
        self.image = pygame.transform.flip(resized_image,True,False)
        self.image = pygame.transform.rotate(self.image,-24)
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(481,255)#490,260
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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


class obj_render_desk3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/kenney_furniturePack/Isometric/desk_SW.png')
        self.image  = pygame.transform.scale(self.image, (200, 130))
      #  self.image = pygame.transform.flip(resized_image,True,False)
       # self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.topleft=(725,396)
        self.direction =vector()
        self.speed =0         
        
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
     #   if keys[pygame.K_1]:
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




class Guard_game(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map,player):
        
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'walk', True
      #  print(self.frames[self.state])
        self.image = self.frames[self.state][self.frame_index]
        self.map =map 
        self.rect = self.image.get_frect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.speed_fac = 1
        self.xsize_fac = 1 
        self.ysize_fac =1
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        self.rect.x=743.0
        self.rect.y = 580.3
        self.direction =vector(0.0,0.0)
        self.speed = 1.0
        self.xsize =30
        self.ysize = 50
        if self.map =='final_map2':
            self.rect.center=(630,431)
            self.speed_fac = 1
            self.xsize_fac = 1.5 
            self.ysize_fac =1.5
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    
                
        
            
        
    def input(self):
        self.current_time = ((pygame.time.get_ticks())//1000)%9
      #  print(self.current_time)
        b=math.sqrt(3)
        input_vector= vector(0,0)
        if self.current_time >=0 and self.current_time<=2 :
            self.state = 'walk'
            input_vector.x += b/2
            input_vector.y +=0.5 
            self.facing_right =True 
        if self.current_time>2 and self.current_time<4:
            self.state = 'idle'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =True
        if self.current_time==4 :
            self.state = 'idle'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time>4 and self.current_time<=7:
            self.state = 'walk'
            input_vector.x -= b/2 
            input_vector.y -=0.5 
            self.facing_right =False
        if self.current_time>7 and self.current_time<9:
            self.state = 'idle'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =False 
        if self.current_time==9:
            self.state = 'idle'
            input_vector.x += 0
            input_vector.y +=0 
            self.facing_right =True
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
      #  print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        
        self.animate(dt)
      #  print(self.curr_posx,self.curr_posy,self.current_time)







class level5_game:
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
        self.key2=0
        self.suspision =0
        self.caught =False 
        self.show_map =False 
        self.setup(self.tmx_map,self.key) 
        font_path = "graphics/docktrin.ttf"  # Path to the font file
        font_size = 36
        custom_font = pygame.font.Font(font_path, font_size)
        self.text_surface1 = custom_font.render("Need a key to open the door", True, (0, 0, 0))
        self.text_surface2 = custom_font.render("Something might be inside the drawer.Press 'f' to peep in ", True, (0, 0, 0))
        self.text_surface3 = custom_font.render("Press 'f' to acquire the key !", True, (0, 0, 0))
        self.text_surface4 = custom_font.render("Key taken!", True, (0, 0, 0))
        self.text_surface5 = custom_font.render("Press 'f' to enter the other room", True, (0, 0, 0))
        self.text_surface6 = custom_font.render("Press 'f' to enter this room", True, (0, 0, 0) )
        self.text_surface7 = custom_font.render("Looks like the map of the Mansion.Press 'k' for a closer view", True, (0, 0, 0))
        self.text_surface8 = custom_font.render("Press 'f' to exit the view", True, (0, 0, 0))
        custom_cursor_path = "useful_images/cursor.jpg"
        self.mouse_pressed =False         
          
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
        self.current_time =1000
        self.start_time2 =0
        self.current_time2 =1000
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        # Define suspicion attribute
        suspicion = 50  # Initial suspicion level (can be any value between 0 and 100)
        self.max_suspicion = 100
    def draw_suspicion_bar(self,surface, suspicion, max_suspicion, x, y, width, height):
        # Calculate the width of the suspicion bar based on current suspicion level
        bar_width = int((suspicion / max_suspicion) * width)
        # Draw the background bar
        # pygame.draw.rect(surface, self.RED, (x, y, width, height))
        # Draw the suspicion bar on top
        # pygame.draw.rect(surface, self.GREEN, (x, y, bar_width, height))    
    def play_button_clicked(self):
        self.current_time = (pygame.time.get_ticks())
       # print(self.current_time,self.start_time,self.mouse_pressed,self.key,self.curr_posx,self.curr_posy)
      #  print(self.curr_posx,self.curr_posy)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]and (self.curr_posx>=120 and self.curr_posx<=220 and self.curr_posy>=290 and self.curr_posy<=320)and(self.current_time-self.start_time>=500):
            self.start_time = pygame.time.get_ticks()
            if self.key ==0:
                self.key =1
            elif self.key==1:
                self.key=2
        if (self.current_time-self.start_time<5000 and self.current_time-self.start_time>0)  and self.key==1:
            self.display_surface.blit(self.text_surface3, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
        if (self.current_time-self.start_time<1000 and self.current_time-self.start_time>0)  and self.key==2:
            self.display_surface.blit(self.text_surface4, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
        else:
            self.mouse_pressed=False 



        
    def setup(self, tmx_map,key):
        map_image = pygame.image.load("graphics/useful_images/mansion_map.png").convert_alpha()
        self.map_image = pygame.transform.scale(map_image, (settings.WINDOW_WIDTH//2, settings.WINDOW_HEIGHT//2))
        
        # Iterate over objects in the map
        for obj in tmx_map.get_layer_by_name('Object Layer 2'):
            if obj.name == 'wall2':
                self.player1 = obj_render_wall2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'wall1':
                self.player1 = obj_render_wall1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'wall3':
                self.player1 = obj_render_wall3((obj.x, obj.y), self.all_sprites)
            if obj.name == 'wall4':
                self.player1 = obj_render_wall4((obj.x, obj.y), self.all_sprites)
            if obj.name == 'wall5':
                self.player1 = obj_render_wall5((obj.x, obj.y), self.all_sprites)
            if obj.name == 'carpet':
                self.player1 = obj_render_carpet((obj.x, obj.y), self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 1'):
            if obj.name == 'sofa1':
                self.player1 = obj_render_sofa1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'sofa2':
                self.player_sofa2 = obj_render_sofa2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'pot1':
                self.player1 = obj_render_pot1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'pot2':
                self.player1 = obj_render_pot2((obj.x, obj.y), self.all_sprites)
            if obj.name == 'chair':
                self.player1 = obj_render_chair((obj.x, obj.y), self.all_sprites)
            if obj.name == 'desk1':
                self.player1 = obj_render_desk1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'desk2':
                self.player_desk2 = obj_render_desk2_initial((obj.x, obj.y), self.all_sprites)
            
                
            if obj.name == 'almirah':
                self.player1 = obj_render_almirah((obj.x, obj.y), self.all_sprites)
            if obj.name == 'door1':
                self.player1 = obj_render_door1((obj.x, obj.y), self.all_sprites)
            if obj.name == 'pot3':
                self.player1 = obj_render_pot3((obj.x, obj.y), self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 3'):
            if obj.name == 'computer':
                self.player1 = obj_render_computer((obj.x, obj.y), self.all_sprites)
            if obj.name == 'gate2':
                self.player1 = obj_render_gate2((obj.x, obj.y), self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 4'):
            if obj.name == 'screen':
                self.player1 = obj_render_screen((obj.x, obj.y), self.all_sprites)
            if obj.name == 'chair2':
                self.player1 = obj_render_chair2((obj.x, obj.y), self.all_sprites)
        for obj in tmx_map.get_layer_by_name('Object Layer 5'):
            if obj.name == 'desk3':
                self.player1 = obj_render_desk3((obj.x, obj.y), self.all_sprites)
        
        


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
            if obj.name == 'guard':
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                collision_sprites = self.collision_sprites
                anti_collision_sprites = self.anti_collision_sprites
                frames = self.level_frames['guards']
                map = 'final_map2'
                self.guard_game = Guard_game(pos, groups, collision_sprites, anti_collision_sprites, frames, map,self.player_sofa2)
                
                

                
    def run(self,dt):        
        self.curr_posx =self.player.rect.x 
        self.curr_posy= self.player.rect.y 
        mouse_pos = pygame.mouse.get_pos()
        
        self.all_sprites.update(dt)
         
      #  print(self.guard_game.curr_posx,self.guard_game.curr_posy,"ds")
        self.display_surface.fill('white')
        background_path = "graphics/objects/level5map.jpeg"  
        background_image = pygame.image.load(background_path).convert()
        background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.offset.x = -(self.player.rect.center[0] - settings.WINDOW_WIDTH/2)
        self.offset.y = -(self.player.rect.center[1] - settings.WINDOW_HEIGHT/2)
        # Blit the background onto the display surface
        self.display_surface.blit(background_image, self.offset)
        
        self.all_sprites.draw(self.player.rect.center)
        if (self.curr_posx>=830 and self.curr_posx<=920)and(self.curr_posy>=260 and self.curr_posy<=300) and self.key2==0 :
          #  print("found")
            self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
        if (self.curr_posx>=210 and self.curr_posx<=310)and(self.curr_posy>=180 and self.curr_posy<=230) and self.key ==0:
          #  print("found")
            self.display_surface.blit(self.text_surface1, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
        if (self.curr_posx>=120 and self.curr_posx<=220 and self.curr_posy>=290 and self.curr_posy<=320) and self.key==0:
            self.display_surface.blit(self.text_surface2, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
        if (self.curr_posx>=210 and self.curr_posx<=310)and(self.curr_posy>=180 and self.curr_posy<=230) and self.key==2:
            self.display_surface.blit(self.text_surface5, ((settings.WINDOW_WIDTH - self.text_surface1.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface1.get_height()))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
              
                return 5 
        if (self.curr_posx>=830 and self.curr_posx<=920)and(self.curr_posy>=260 and self.curr_posy<=300) and self.key2==1 :
            self.display_surface.blit(self.text_surface6, ((settings.WINDOW_WIDTH - self.text_surface6.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface6.get_height()))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                return 14
        
            
            
                
                
                
            
            
        key1 = self.key 
        self.play_button_clicked()
        key2 =self.key 
        if key2>key1:
            for obj in self.tmx_map.get_layer_by_name('Object Layer 1'):
                if obj.name == 'desk2' and key2==1:
                    obj_render_desk2_open_key((obj.x, obj.y), self.all_sprites,self.player_desk2.image2)
                if obj.name == 'desk2' and key2==2:
                    obj_render_desk2_open_key((obj.x, obj.y), self.all_sprites,self.player_desk2.image3)
        self.display_surface.blit(self.custom_cursor_image, (mouse_pos[0] - self.custom_cursor_size[0] // 2, mouse_pos[1] - self.custom_cursor_size[1] // 2))
      #  print(self.guard_game.curr_posx,self.guard_game.curr_posy,"ds")
        self.offset.x = -(self.curr_posx - settings.WINDOW_WIDTH/2)
        self.offset.y = -(self.curr_posy - settings.WINDOW_HEIGHT/2)
        offset_pos = self.guard_game.rect.center +self.offset 
        self.display_surface.blit(self.guard_game.image, offset_pos)
        self.guard_game.update(dt)
        x1=self.guard_game.rect.center[0]-self.player.rect.center[0]
        x1+=22
        x2 = self.guard_game.rect.center[1]-self.player.rect.center[1]
        x2+=48
        p=math.sqrt(x1*x1+x2*x2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_4]:
            print(self.player.rect.center[0],self.player.rect.center[1],self.guard_game.rect.center[0],self.guard_game.rect.center[1]) 
            print(p,x1,x2)
        if p<=60 and self.caught ==False:
            self.suspision+=100 
        suspicion_bar_x = 50
        suspicion_bar_y = 50
        suspicion_bar_width = 200
        suspicion_bar_height = 30
        self.draw_suspicion_bar(self.display_surface, self.suspision, self.max_suspicion, suspicion_bar_x, suspicion_bar_y, suspicion_bar_width, suspicion_bar_height)
    
        self.current_time2 =(pygame.time.get_ticks()) 
        if self.suspision>=100:
            self.start_time2 = (pygame.time.get_ticks())
            self.suspision=0
            self.caught = True
       # print(self.current_time2,self.start_time2,self.caught)
        if self.caught and (self.current_time2-self.start_time2>=500):
            return -5 
        if (self.curr_posx>=380 and self.curr_posx<=490)and(self.curr_posy>=300 and self.curr_posy<=350) :
          #  print("found")
            if self.show_map ==False :
                self.display_surface.blit(self.text_surface7, ((settings.WINDOW_WIDTH - self.text_surface7.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface7.get_height()))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_k]:
                self.show_map =True 
            if keys[pygame.K_f]:
                self.show_map =False 
            if self.show_map ==True :
                self.display_surface.blit(self.map_image, (settings.WINDOW_WIDTH//4, settings.WINDOW_HEIGHT//4))
                self.display_surface.blit(self.text_surface8, ((settings.WINDOW_WIDTH - self.text_surface8.get_width()) // 2, 
                                                          settings.WINDOW_HEIGHT - self.text_surface8.get_height()-50))
        
            
        return 10 
       
        

        