from settings import * 
import math 
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map ):
        
        super().__init__(groups)
        
        
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'walk', True
        self.image = self.frames[self.state][self.frame_index]
        
        

        self.stamina =200000
        
        
        self.rect = self.image.get_frect(topleft = pos)
        self.old_rect = self.rect.copy()
        
        self.curr_posx = self.rect.x
        self.curr_posy = self.rect.y  
        
        self.rect.x=743.0
        self.rect.y = 580.3
        self.direction =vector(0.0,0.0)
        self.speed = 100.0
        self.xsize =30
        self.ysize = 50
        if map=='final_map2':
            self.speed_fac = 1
            self.xsize_fac = 1 
            self.ysize_fac =1
            self.rect.x = 0
            self.rect.y =0
           
        self.collision_sprites = collision_sprites
        self.anti_collision_sprites = anti_collision_sprites 
            
        
        
    def animate(self,dt):
        self.frame_index +=settings.ANIMATION_SPEED*dt 
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image,True,False)
        resized_image = pygame.transform.scale(self.image, (self.xsize*self.xsize_fac, self.ysize*self.ysize_fac))
        self.image = resized_image
    def get_state(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] :
                self.state ='jump'
                self.speed = 200*self.speed_fac
                self.stamina-=1
        
        else:
            
            if (self.direction.x==0) and (self.direction.y==0):
                self.state = 'idle'
                self.speed = 100*self.speed_fac
                self.stamina=min(self.stamina+5,200)
            else:
                self.state = 'walk'
                self.speed =100*self.speed_fac
                self.stamina=min(self.stamina+3,200)
        
            
        
    def input(self):
        a=math.sqrt(3)
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_RIGHT]:
            input_vector.x+=a/2
            input_vector.y-=0.5
            self.facing_right =True 
        if keys[pygame.K_LEFT]:
            input_vector.x-=a/2
            input_vector.y+=0.5
            self.facing_right=False 
        if keys[pygame.K_DOWN]:
            input_vector.x+=a/2
            input_vector.y+=0.5
            self.facing_right =True
        if keys[pygame.K_UP]:
            input_vector.x-=a/2
            input_vector.y-=0.5
            self.facing_right =False
      #  print(input_vector)
        if keys[pygame.K_0]:
            print(self.rect.topleft)  
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        a = float(self.direction.x) * float(self.speed) * float(dt)
      #  print(self.rect.topleft)
        self.rect.x += float(a)
        self.collision('x')
        
        b= self.direction.y * self.speed *dt 
        self.rect.y +=b 
        self.collision('y')
     #   print(self.rect.topleft)
        
    
    
    
    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
            #    print("hi")
            # Calculate the center points of the player's and sprite's rectangles
                player_center = self.rect.center
                sprite_center = sprite.rect.center

            # Calculate the distances between the centers along the axes
                dx = sprite_center[0] - player_center[0]
                dy = sprite_center[1] - player_center[1]

            # Calculate the widths and heights of the player and sprite rectangles
                player_width = self.rect.width
                player_height = self.rect.height
                sprite_width = sprite.rect.width
                sprite_height = sprite.rect.height

            # Calculate the minimum distance required for a collision to occur
                min_distance_x = (player_width + sprite_width) / 2
                min_distance_y = (player_height + sprite_height) / 2

            # Check if the absolute difference between the distances along the axes is less than the minimum distance
                if abs(dx) < min_distance_x and abs(dy) < min_distance_y:
                    # Resolve the collision based on the axis
                    if axis == 'x':
                        # Resolve collision along the x-axis
                        if dx > 0:
                            # Player is to the left of the sprite
                            self.rect.right = sprite.rect.left
                        else:
                            # Player is to the right of the sprite
                            self.rect.left = sprite.rect.right
                    elif axis == 'y':
                        # Resolve collision along the y-axis
                        if dy > 0:
                            # Player is above the sprite
                            self.rect.bottom = sprite.rect.top
                        else:
                            # Player is below the sprite
                            self.rect.top = sprite.rect.bottom
      #  print(self.anti_collision_sprites)
    #    for sprite in self.anti_collision_sprites:
          #  print(sprite)
      #      if sprite.rect.colliderect(self.rect)==True:
     #           print("true")
       #     if sprite.rect.colliderect(self.rect)==False:
        #        print("false")
            
            

     
    
                        
                    
                    
                     
        
    def update(self,dt):
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        self.get_state()
        self.animate(dt)