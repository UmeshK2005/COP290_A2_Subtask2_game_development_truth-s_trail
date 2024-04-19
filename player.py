from settings import * 
import math 
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites,anti_collision_sprites,frames,map ):
        super().__init__(groups)
        self.frames ,self.frame_index = frames,0
        self.state,self.facing_right = 'walk', True
        self.image = self.frames[self.state][self.frame_index]
        
        

        self.stamina =200000
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
        self.speed = 100.0
        self.xsize =30
        self.ysize = 50
        if self.map =='final_map2':
            self.rect.x=355.0
            self.rect.y = 409.3
            self.speed_fac = 1
            self.xsize_fac = 1.5 
            self.ysize_fac =1.5
        if self.map =='final_map3':
            self.rect.x=402
            self.rect.y = 311
            self.speed_fac = 1
            self.xsize_fac = 1.5 
            self.ysize_fac =1.5
        if self.map =='final_map4':
            self.rect.x=464
            self.rect.y = 385
            self.speed_fac = 1
            self.xsize_fac = 1.5 
            self.ysize_fac =1.5
        if self.map =='final_map5':
            self.rect.x=496
            self.rect.y = 402
            self.speed_fac = 1
            self.xsize_fac = 1.5 
            self.ysize_fac =1.5
        
            
           
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
       # print(input_vector)
        if keys[pygame.K_0]:
            print(self.rect.topleft,self.rect.y+0.4931*(self.rect.x))  
        if input_vector:
            self.direction =input_vector.normalize()
        else:
            self.direction = input_vector
        
        
    def move(self,dt):
        if self.map=='final_map2':
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
            self.collision2()
        elif self.map=='final_map3':
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
            self.collision3()
        elif self.map=='final_map4':
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
            self.collision4()
        
        elif self.map=='final_map5':
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
            self.collision5()
         
        else:
            a = float(self.direction.x) * float(self.speed) * float(dt)
            self.rect.x += float(a)
         #   self.collision('x')
            
            b= self.direction.y * self.speed *dt 
            self.rect.y +=b 
            self.collision1()
          #  self.collision('y')
     
        
    def collision2(self):
        x=self.rect.center[0]
        y= self.rect.center[1]
        a=math.sqrt(3)
        if y-(0.4452)*(x)>=300 and (x>=29 and x<=790) and (y>=285 and y<=605):
    #        print("1")
            self.rect = self.old_rect
        if y+(0.4452)*(x)>=880 and (x>=670 and x<=1000) and (y>=350 and y<=590):
    #        print("2")
            self.rect = self.old_rect
        if y+(0.4452)*(x)<=400 and (x>=80 and x<=205) and (y>=270 and y<=330):
    #        print("3")
            self.rect = self.old_rect
        if y+(0.4452)*(x)<=320 and (x>=-168 and x<=70) and (y>=250 and y<=380):
    #        print("4")
            self.rect = self.old_rect
        if y+(0.4452)*(x)<=320 and (x>=160 and x<=340) and (y>=140 and y<=230):
    #        print("5")
            self.rect = self.old_rect
        if y+(0.4452)*(x)>=390 and (x>=355 and x<=460) and (y>=180 and y<=260):
    #        print("6")
            self.rect = self.old_rect
        if y+(0.4452)*(x)<=640 and (x>=540 and x<=840) and (y>=240 and y<=380):
    #        print("7")
            self.rect = self.old_rect
        if y+(0.4452)*(x)>=700 and (x>=690 and x<=940) and (y>=280 and y<=420):
    #        print("8")
            self.rect = self.old_rect
            
        if y-(0.4452)*(x)>=150 and (x>=140 and x<=200) and (y>=200 and y<=250):
    #        print("9")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=0 and (x>=320 and x<=485) and (y>=125 and y<=185):
    #        print("10")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=130 and (x>=335 and x<=560) and (y>=265 and y<=380):
    #        print("11")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=120 and (x>=690 and x<=930) and (y>=430 and y<=540):
    #        print("12")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=-100 and (x>=500 and x<=1075) and (y>=90 and y<=490):
    #        print("13")
            self.rect = self.old_rect
    def collision1(self):
        x=self.rect.center[0]
        y= self.rect.center[1]
        a=math.sqrt(3)
        if y-(0.4452)*(x)>=330 and (x>=530 and x<=830) and (y>=570 and y<=760):
            self.rect = self.old_rect   
        if y-(0.4452)*(x)>=110 and (x>=1000 and x<=1500) and (y>=540 and y<=840):
            self.rect = self.old_rect 
        if y-(0.4452)*(x)>=20 and (x>=470 and x<=900) and (y>=210 and y<=440):
            self.rect = self.old_rect 
        if y-(0.4452)*(x)<=-160 and (x>=680 and x<=950) and (y>=120 and y<=250):
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=-70 and (x>=1260 and x<=1860) and (y>=440 and y<=730):
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=-200 and (x>=960 and x<=1100) and (y>=180 and y<=260):
            self.rect = self.old_rect  
    def collision3(self):
        x=self.rect.center[0]
        y= self.rect.center[1]
        a=math.sqrt(3)
        if y-(0.4452)*(x)>=210 and (x>=0 and x<=840) and (y>=150 and y<=600):
       #     print("1")
            self.rect = self.old_rect 
        if y-(0.4452)*(x)<=130 and (x>=60 and x<=200) and (y>=135 and y<=210):
        #    print("2")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=0 and (x>=370 and x<=550) and (y>=130 and y<=240):
         #   print("3")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=40 and (x>=625 and x<=750) and (y>=290 and y<=370):
       #     print("4")
            self.rect = self.old_rect
        if y-(0.4452)*(x)<=-130 and (x>=387 and x<=1170) and (y>=-67 and y<=382):
       #     print("5")
            self.rect = self.old_rect  
        if y-(0.4452)*(x)>=-10 and (x>=160 and x<=290) and (y>=70 and y<=150):
       #     print("6")
            self.rect = self.old_rect 
        if y+(0.4452)*(x)<=220 and (x>=-50 and x<=380) and (y>=0 and y<=250):
       #     print("7")
            self.rect = self.old_rect
        if y+(0.4452)*(x)>=280 and (x>=400 and x<=465) and (y>=85 and y<=110):
       #     print("8")
            self.rect = self.old_rect 
        if y+(0.4452)*(x)<=490 and (x>=530 and x<=640) and (y>=160 and y<=210):
      #      print("9")
            self.rect = self.old_rect 
        if y+(0.4452)*(x)>=555 and (x>=620 and x<=740) and (y>=200 and y<=275):
       #     print("10")
            self.rect = self.old_rect 
        if y+(0.4452)*(x)<=710 and (x>=740 and x<=880) and (y>=215 and y<=360):
       #     print("11")
            self.rect = self.old_rect 
        if y+(0.4452)*(x)>=860 and (x>=760 and x<=1200) and (y>=340 and y<=550):
       #     print("12")
            self.rect = self.old_rect   
    def collision4(self):
        x=self.rect.center[0]
        y= self.rect.center[1]
        a=math.sqrt(3)
        if y-(0.554)*(x)>=220 and (x>=-50 and x<=800) and (y>=180 and y<=670):
            self.rect = self.old_rect
        if y-(0.554)*(x)<=180 and (x>=60 and x<=150) and (y>=190 and y<=250):
            self.rect = self.old_rect
        if y-(0.554)*(x)<=50 and (x>=365 and x<=690) and (y>=215 and y<=400):
            self.rect = self.old_rect
        if y-(0.554)*(x)<=85 and (x>=610 and x<=700) and (y>=410 and y<=470):
            self.rect = self.old_rect
        if y-(0.554)*(x)<=-180 and (x>=920 and x<=1170) and (y>=300 and y<=450):
            self.rect = self.old_rect
        if y-(0.554)*(x)>=-30 and (x>=210 and x<=310) and (y>=90 and y<=150):
            self.rect = self.old_rect
        if y-(0.554)*(x)<=-230 and (x>=410 and x<=950) and (y>=-40 and y<=285):
            self.rect = self.old_rect
        if y+(0.554)*(x)>=1050 and (x>=680 and x<=1115) and (y>=415 and y<=630):
            self.rect = self.old_rect
        if y+(0.554)*(x)>=390 and (x>=355 and x<=570) and (y>=30 and y<=200):
            self.rect = self.old_rect
        if y+(0.554)*(x)<=870 and (x>=675 and x<=940) and (y>=315 and y<=470):
            self.rect = self.old_rect
        if y+(0.554)*(x)<=330 and (x>=125 and x<=310) and (y>=140 and y<=260):
            self.rect = self.old_rect
        if y+(0.554)*(x)<=260 and (x>=20 and x<=450) and (y>=-10 and y<=240):
            self.rect = self.old_rect
    def collision5(self):
        x=self.rect.center[0]
        y= self.rect.center[1]
        a=math.sqrt(3)
        if y-(0.4931)*(x)>=215 and (x>=-40 and x<=810) and (y>=200 and y<=670):
            self.rect = self.old_rect
        if y-(0.4931)*(x)<=-240 and (x>=450 and x<=720) and (y>=-60 and y<=100):
            self.rect = self.old_rect
        if y-(0.4931)*(x)<=-30 and (x>=545 and x<=690) and (y>=210 and y<=295):
            self.rect = self.old_rect
        if y-(0.4931)*(x)<=-125 and (x>=710 and x<=1200) and (y>=170 and y<=450):
            self.rect = self.old_rect
        if y-(0.4931)*(x)<=130 and (x>=630 and x<=760) and (y>=415 and y<=500):
            self.rect = self.old_rect
        if y-(0.4931)*(x)>= -40 and (x>=760 and x<=860) and (y>=330 and y<=400):
            self.rect = self.old_rect
        if y+(0.4931)*(x)>=950 and (x>=790 and x<=1130) and (y>=400 and y<=610):
            self.rect = self.old_rect
        if y+(0.4931)*(x)<=950 and (x>=740 and x<=850) and (y>=400 and y<=470):
            self.rect = self.old_rect
        if y+(0.4931)*(x)>=950 and (x>=630 and x<=760) and (y>=325 and y<=400):
            self.rect = self.old_rect
        if y+(0.4931)*(x)<=640 and (x>=690 and x<=780) and (y>=230 and y<=290):
            self.rect = self.old_rect
        if y+(0.4931)*(x)<=300 and (x>=70 and x<=540) and (y>=-10 and y<=260):
            self.rect = self.old_rect
        if y-(0.4931)*(x)<=-180 and (x>=409 and x<=730) and (y>=10 and y<=160):
            self.rect = self.old_rect
        if y+(0.4931)*(x)>=440 and (x>=550 and x<=670) and (y>=120 and y<=195):
            self.rect = self.old_rect
        
        

            
            

     
    
                        
                    
                    
                     
        
    def update(self,dt):
        self.curr_posx=self.rect.x 
        self.curr_posy=self.rect.y
    #    print(self.curr_posx,self.curr_posy)
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        self.get_state()
        self.animate(dt)