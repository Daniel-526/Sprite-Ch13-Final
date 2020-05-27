#-------------------------------------------------------------------------------------------------------------------
#                   Chapter 13 Lab: Sprite
#Name: Daniel (11)                                           
#Date: 22/5/20
#-------------------------------------------------------------------------------------------------------------------
import sys
import pygame
import time

class Hero(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()

        #Load the sprite sheet
        sheet = pygame.image.load("hero.png")
        

        self.frame=[]
        for i in range(8):
           self.frame.append(pygame.Surface([100, 99]).convert())
           patch = (0 + 100*(i%8), 0 + 99*(i//8), 100, 99)
           self.frame[i].blit(sheet,(0, 0), patch)
           self.frame[i].set_colorkey((0, 0, 255)) 

        self.anim_frame = 0
        self.image=self.frame[0]                            
        self.rect=self.image.get_rect()

        self.rect.x = x
        self.rect.y = y                             
        self.deltax = 0
        self.deltay = 0
        self.face = 1

    def update(self,index):
        self.anim_frame = (self.anim_frame + index)%8

        if (self.deltax < 0) or (self.face == 2):
            self.image = pygame.transform.flip(self.frame[self.anim_frame], True, False)
            
        else:
            self.image = self.frame[self.anim_frame]

        self.rect.x += self.deltax
        self.rect.y += self.deltay
                             
                             
def main():

    pygame.init()


    main_surface = pygame.display.set_mode((720, 720))
    background=pygame.image.load("background.png").convert()


    hero = Hero(300, 300)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(hero)
    index = 0
                          
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                key = event.dict["key"]
                
                if key == 32:
                    hero.accel = -500
                    
                elif key == pygame.K_LEFT:
                   hero.deltax = -7
                   hero.face = 2
                   
                elif key == pygame.K_RIGHT:
                   hero.deltax = 7
                   hero.face = 1
                   
                elif key == pygame.K_UP:
                    hero.deltay = -7
                    
                elif key == pygame.K_DOWN:
                   hero.deltay = 7
                   
                else:
                   hero.deltax = 0
                   hero.deltay = 0
                   
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    hero.deltax = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    hero.deltay = 0
                    
            if (hero.deltax != 0) or (hero.deltay != 0):
                index = 1
                
            else:
                index = 0

        all_sprites.update(index)

        main_surface.blit(background,(0, 0))

        all_sprites.draw(main_surface)

        pygame.display.flip()

        time.sleep(0.08)  

if __name__=="__main__":    
    main()

# Great.
# Score: 100
