import pygame                                        # impporting pygame
pygame.init()                                        # initilisation/Starting
win = pygame.display.set_mode((500, 480))            # win .i.e(window) is a veriable, display is a module adn set_mode is a function inside it which is used to display the surface on the monitor screen
pygame.display.set_caption("First Game")

walkleft = pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),  pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png') 
walkright = pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'),  pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png') 
background = pygame.image.load('bg.jpg')
standing = pygame.image.load('standing.png')

score = 0


clock = pygame.time.Clock() 


#___________________________________________________________MAIN CHAR.________________________________________________________________


class game_play():                                     # on third or fourth this clock of code is exicuted depending upon the input

    def __init__(self, x, y, width, height):
        
        self.x = x                                   # these x and y are the axis location of the pointer 
        self.y = y
        self.width = width                           # height and width is taken 64 specifically because it is the size of our taken character
        self.height = height
        self.vel = 5                                 # vel is used for velocity
        self.jump = False
        self.jump_size = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox = (self.x +22 , self.y, 21, 60)

    def char_motion(self):
            
        if self.walkcount + 1 >= 9:
            self.walkcount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkleft[self.walkcount], (self.x, self.y))
                self.walkcount += 1
                
            if self.right:
                win.blit(walkright[self.walkcount], (self.x, self.y))
                self.walkcount += 1

        else:
            if self.right:
                win.blit(walkright[0], (self.x, self.y))

            else:
                win.blit(walkleft[0], (self.x, self.y))
        self.hitbox = (self.x + 22 , self.y, 21, 60)
      #  pygame.draw.rect(win, (250, 0, 0), self.hitbox, 2)


    def hit(self):

        self.jump = False
        self.jump_size = 10
        self.x = 20
        self.y = 410
        self.wlakcount = 0
        font1 = pygame.font.SysFont("comicsance", 100, True, True)
        text = font.render("-5", 1, (250, 0, 0))
        win.blit(text, (250 - round(text.get_width()/ 2), 220))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i +=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i == 201
                    pygame.quit()
        
        


#_______________________________________________________ENEMY PART_____________________________________________________________________



class enemy_player():

    walkright = pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')
    walkleft = pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')
    bulleets = []

    def __init__(self, x, y, width, height, end):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.walkcount = 0
        self.end = end
        self.path = [self.x, self.end]
        self.facing = 1
        self.hitbox = [self.x +18, self.y, 38, 60]
        self.health = 9
        self.reduce = True
        

    def movement(self):


        if self.facing > 0:                

            if self.x + self.vel < self.path[1]:
                self.x += self.vel * self.facing
                
            else :
                self.facing = -1

        else:
            if self.x + self.vel > self.path[0] :
                self.x += self.vel * self.facing

            else:
                self.facing = 1
                

    def enemy_motion(self):

        self.movement()
        if self.reduce:
            if self.walkcount >= 11:
                self.walkcount = 0

            if self.facing > 0:
                win.blit(self.walkright[self.walkcount], (self.x, self.y))
                self.walkcount += 1
                
            else:
                win.blit(self.walkleft[self.walkcount], (self.x, self.y))
                self.walkcount += 1
                
            self.hitbox = [self.x +18, self.y, 38, 60]
          # pygame.draw.rect(win, (250, 0, 0), self.hitbox, 2)
            pygame.draw.rect(win, (200,100,90), (self.x, self.y - 10, 50, 10))
            pygame.draw.rect(win, (0,100,0)   , (self.x, self.y - 10, 50 - (5 * (9 - self.health)), 10))

    
    def hit(self):
        
        if self.health > 0:
            self.health -= 1

        else :
            self.reduce = False
        
        

#________________________________________________________BULLETS__________________________________________________________________________________
            

class projectile():                                  # on third or fourth this clock of code is exicuted depending upon the input

    def __init__(self, x, y, colour, facing, raidus):
        self.x = x
        self.y = y
        self.colour = colour
        self.facing = facing
        self.raidus = raidus
        self.vel = 10 * facing

    def proj_motion(self):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.raidus)


class enemy_projectile():

    def __init__(self, x, y, colour, facing, raidus):
        self.x = x
        self.y = y
        self.facing = facing
        self.colour = colour
        self.raidus = raidus
        self.vel = 15 * facing

    def enemy_bullet(self):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.raidus)
        
   

#________________________________________________________BLITING/ DRAWING__________________________________________________________________________

        
def image_drawing():                                 # second this block of code is exicuted
                                                     #the char_motion can be defined heir also but it is better to make a different function for it for future perpouse
    global walkcount                                 #  global is used so that we can change the variable inside a function
    win.blit(background,(0, 0))                      #  it will draw as well as fill the window with the background image starting from (0, 0) position - ____.blit(image,(left, top))
    game.char_motion()
    enemy.enemy_motion()
    text = font.render("Score: " + str(score), 1, (0, 0, 0))          # their is no explination of using 1 in text, we just have to use it
    win.blit(text,(350,20))

    for shots in bullets:   
        shots.proj_motion()

    for eshots in enemy_bullets:
        eshots.enemy_bullet()
        
    pygame.display.update()


#__________________________________________________________MAIN LOOP________________________________________________________________________________

    
font = pygame.font.SysFont("comicsans", 30, True, True)                 # used for writing text on the screen (font name, size, bold, itelic)
run = True                                                              # the game will be exicuting contineously
bullets = []
enemy_bullets = []
shoot_time = 0
enemy_shoot_time = 0
game = game_play(200, 410, 64, 64)
enemy = enemy_player(30, 410, 64, 64, 400)
while run:                                          # first this block of code is exicuted         
    clock.tick(30)

    if enemy.reduce:
        if game.hitbox[1]  < enemy.hitbox[1] + enemy.hitbox[3] and game.hitbox[1] + game.hitbox[3] > enemy.hitbox[1] :                  # char. colliding with the enemy
            if game.hitbox[0] + round(game.hitbox[2]/2) < enemy.hitbox[0] + enemy.hitbox[2] and game.hitbox[0]  > enemy.hitbox[0]:      # it works for both side i.e right and left side
                game.hit()
                score -= 5

    if shoot_time > 0:
        shoot_time += 1

    if shoot_time == 6:
        shoot_time = 0

    if enemy.reduce:
    
        if enemy_shoot_time < 20:
            enemy_shoot_time += 1
            
        if enemy_shoot_time >= 20:
            enemy_shoot_time = 0
    
    
    #pygame.time.delay(30)                          # after 100 mili seconde the next line will be exicuted 

    for event in pygame.event.get():                # heir the event in pygame.event.ge tell's us which button the user is pressing from the keyboard or at what position the cursor is and then we can define what it will do for that input
                                                    # the word event can not be replaced by any other word like- events,evonts... 
        if event.type == pygame.QUIT:               # without this line x button in the display surface will not work     #  it isimp. to write QUIT in capital letters
                run = False                 


    for shots in bullets:

        if enemy.reduce:
            if shots.y + shots.raidus < enemy.hitbox[1] + enemy.hitbox[3] and shots.y - shots.raidus > enemy.hitbox[1] :    # after coming in this loop it will also exicute the loop -(if shots.x < 500 and shots.x > 0:) due to which the the bullet will move                  
                if shots.x + shots.raidus < enemy.hitbox[0] +enemy.hitbox[2] and shots.x > enemy.hitbox[0]:                 # it works for both side i.e right and left side
                    enemy.hit()
                    score += 1
                    bullets.pop(bullets.index(shots))
            
        if shots.x < 500 and shots.x > 0:            # heir we can take 500 and 0 values but if we are at the (0,0) or (500,500) position then the bullets will stop incrementing
            shots.x += shots.vel
        
        else:
            bullets.pop(bullets.index(shots))       # it is ues to terminate the list veriable
             


    for eshots in enemy_bullets:

        if eshots.y + eshots.raidus < game.hitbox[1] + game.hitbox[3] and eshots.y - eshots.raidus > game.hitbox[2]:
            if eshots.x + eshots.raidus < game.hitbox[0] + game.hitbox[2] and eshots.x > game.hitbox[0]:
                enemy.hit()
                score -= 1
                enemy.health += 2
                enemy_bullets.pop(enemy_bullets.index(eshots)) 
        
        if eshots.x < 500 and eshots.x > 0:
            eshots.x += eshots.vel

        else:
            enemy_bullets.pop(enemy_bullets.index(eshots))
            
####### heir the prassing of keys is not taken under above for loop because then we have to press is repeatedly to move pointer , where as it is not hapening is case of while loop #############
 

    keys = pygame.key.get_pressed()                 # heir key is a module and python.key.get_pressed() is its function. It returns 0 for keys which are not pressed and 1 for pressed keys 


########## NOTE - if we use elif then only one condition can be exicuted at a time as it will not allow to ec=xcess the next elif statment as long as it is true but if we only use if conditions for all then more then one conditions can be exicuted #################

    if enemy_shoot_time == 0:
        
        if enemy.facing > 0:
            facing = 1
        if enemy.facing < 0:
            facing = -1
            
        enemy_bullets.append(enemy_projectile(round(enemy.x + enemy.width / 2), round(enemy.y + enemy.height / 2), (150, 0, 0), facing, 6))
        enemy_shoot_time += 1 

    if keys[pygame.K_SPACE] and shoot_time == 0:
        if len(bullets) < 5:
            if game.left:
                facing = -1
            else:
                facing = 1
            bullets.append(projectile(round(game.x + game.width / 2), round(game.y + game.height / 2), (0, 0, 0), facing, 6))  # heir the value if (game.x + game.width / 2) is stored in self.x on projectile class which is later transfered to the shots.x  
            shoot_time = 1

    if keys[pygame.K_LEFT] and game.x >= game.vel:
        game.x -= game.vel
        game.left = True
        game.right = False
        game.standing = False

    elif keys[pygame.K_RIGHT] and game.x < 500 - game.width :
        game.x += game.vel
        game.left = False
        game.right = True
        game.standing = False

    else:
        game.standing = True
   
    if not (game.jump):

        if keys[pygame.K_UP]:
            game.jump = True
            game.left = False
            game.right = False
            game.standing = True
           
    else:
            
        if game.jump_size >= -10:
                game.y -= (game.jump_size * 3) 
                game.jump_size -= 1

        else :
                 game.jump = False
                 game.jump_size = 10
                 

    image_drawing()                                  # this will call the image_drawing function every time
               

pygame.quit()
    


    
