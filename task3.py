import pygame
pygame.init()
background=(153,50,204)
(winwidth,winheight)=(1000,600)
win=pygame.display.set_mode((winwidth,winheight))
win.fill(background)
pygame.display.set_caption("GET SWIFTY")
pygame.display.flip()

walkleft = pygame.image.load('rickl.png')
walkright = pygame.image.load('rickr.png') 
walkup=[pygame.image.load('rickrs.png'),pygame.image.load('rickls.png')]
walkdown=[pygame.image.load('rickdr.png'),pygame.image.load('rickdl.png')]
bg = pygame.image.load('bg.jpg') 
char = pygame.image.load('rick.png')

class rick(object):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.shift=5
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.walkposition=0
        self.flyposition=0

    def draw(self,win):
        if self.left:
            win.blit(walkleft,(self.x,self.y))
        elif self.right:
            win.blit(walkright,(self.x,self.y))
        elif self.up:
            win.blit(walkup[self.flyposition],(self.x,self.y))
        elif self.down:
            win.blit(walkdown[self.flyposition],(self.x,self.y))
        else:
            win.blit(char,(self.x,self.y))


def window():
    win.blit(bg,(0,0))
    man.draw(win)
    man1.draw(win)
    man2.draw(win)
    pygame.display.update()





man=rick(0,0,150,150)
man1=rick(150,150,150,150)
man2=rick(300,300,150,150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x-=man.shift
        man.left=True
        man.right=False
        man.up=False
        man.down=False
        man.walkposition=1

    elif keys[pygame.K_RIGHT] and man.x < winwidth-man.width:
        man.x+=man.shift
        man.left=False
        man.right=True
        man.up=False
        man.down=False
        man.walkposition=0

    elif keys[pygame.K_UP] and man.y >0:
        man.y-=man.shift
        man.left=False
        man.right=False
        man.up=True
        man.down=False
        if man.walkposition==0:
            man.flyposition=0
        elif man.walkposition==1:
            man.flyposition=1

    elif keys[pygame.K_DOWN] and man.y<winheight-man.height:
        man.y+=man.shift
        man.left=False
        man.right=False
        man.up=False
        man.down=True
        if man.walkposition==0:
            man.flypositon=0
        elif man.walkposition==1:
            man.flyposition=1
    else :
        man.left=False
        man.right=False
        man.up=False
        man.down=False
        man.walkposition=0
        man.flyposition=0

    if keys[pygame.K_LEFT] and man1.x > 0:
        man1.x-=man1.shift
        man1.left=True
        man1.right=False
        man1.up=False
        man1.down=False
        man1.walkposition=1

    elif keys[pygame.K_RIGHT] and man1.x < winwidth-man1.width:
        man1.x+=man1.shift
        man1.left=False
        man1.right=True
        man1.up=False
        man1.down=False
        man1.walkposition=0

    elif keys[pygame.K_UP] and man1.y >0:
        man1.y-=man1.shift
        man1.left=False
        man1.right=False
        man1.up=True
        man1.down=False
        if man1.walkposition==0:
            man1.flyposition=0
        elif man1.walkposition==1:
            man1.flyposition=1

    elif keys[pygame.K_DOWN] and man1.y<winheight-man1.height:
        man1.y+=man1.shift
        man1.left=False
        man1.right=False
        man1.up=False
        man1.down=True
        if man1.walkposition==0:
            man1.flypositon=0
        elif man1.walkposition==1:
            man1.flyposition=1
    else :
        man1.left=False
        man1.right=False
        man1.up=False
        man1.down=False
        man1.walkposition=0
        man1.flyposition=0


    if keys[pygame.K_LEFT] and man2.x > 0:
        man2.x-=man2.shift
        man2.left=True
        man2.right=False
        man2.up=False
        man2.down=False
        man2.walkposition=1

    elif keys[pygame.K_RIGHT] and man2.x < winwidth-man2.width:
        man2.x+=man2.shift
        man2.left=False
        man2.right=True
        man2.up=False
        man2.down=False
        man2.walkposition=0

    elif keys[pygame.K_UP] and man2.y >0:
        man2.y-=man2.shift
        man2.left=False
        man2.right=False
        man2.up=True
        man2.down=False
        if man2.walkposition==0:
            man2.flyposition=0
        elif man2.walkposition==1:
            man2.flyposition=1

    elif keys[pygame.K_DOWN] and man2.y<winheight-man2.height:
        man2.y+=man2.shift
        man2.left=False
        man2.right=False
        man2.up=False
        man2.down=True
        if man2.walkposition==0:
            man2.flypositon=0
        elif man2.walkposition==1:
            man2.flyposition=1
    else :
        man2.left=False
        man2.right=False
        man2.up=False
        man2.down=False
        man2.walkposition=0
        man2.flyposition=0
    window()

pygame.quit()