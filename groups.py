from settings import * 
class Allsprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface=pygame.display.get_surface()
        self.offset = vector(400,0)
    def draw(self,target_pos):
        self.offset.x = -(target_pos[0] - settings.WINDOW_WIDTH/2)
        self.offset.y = -(target_pos[1] - settings.WINDOW_HEIGHT/2)
        for sprite in self:
            offset_pos = sprite.rect.topleft +self.offset 
            
            self.display_surface.blit(sprite.image,offset_pos)
        