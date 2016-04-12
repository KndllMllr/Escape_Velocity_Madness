import sys, pygame
import time

pygame.init()
x = 1
y = 1
hasyllwkey = 0
hasbluekey = 0
hasgrnkey = 0
hasredkey = 0
num = 0                                                                                                            #y
board =     [["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"], #0
             ["H", "P", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "H"], #1
             ["H", "_", "_","YD", "_", "_","BD", "_", "_", "H", "_", "_","RD", "_", "_","GD", "_", "_", "H", "H"], #2
             ["H","YK", "_", "H", "_", "_", "H", "_", "!", "H","BK", "_", "H", "_", "_", "H", "_", "_", "H", "H"], #3
             ["H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H"], #4
             ["H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "H"], #5
             ["H", "_", "_","YD", "_", "!","BD", "_", "_", "H", "_", "_","RD", "_", "_","GD", "_", "_", "H", "H"], #6
             ["H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "H"], #7
             ["H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H"], #8
             ["H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_","RK", "H", "H"], #9
             ["H", "_", "_","YD", "_", "_","BD", "_", "_", "H", "_", "_","RD", "_", "_","GD", "_", "_", "H", "H"], #10
             ["H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "_", "_", "H", "H"], #11
             ["H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H", "H", "H", "_", "_", "H", "H", "H", "H", "H"], #12
             ["H","GK", "_","YD", "_", "_", "H", "!", "_", "H", "_", "_", "H", "_", "_", "H", "H", "H", "H", "H"], #13
             ["H", "_", "_", "H", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","BD", "_", "_", "_", "H"], #14
             ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "F", "H"]] #15
           #x  0   1    2    3    4    5    6   7    8    9    10   11   12   13   14   15   16   17   18   19 
display_width = 1000
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)


screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Escape Velocity Madness')
clock = pygame.time.Clock()

prisoner = pygame.image.load('flash.png')
chip = pygame.image.load('chip-south.png')
floor = pygame.image.load('th.jpg')
wall = pygame.image.load('wall.png')
yllwdoor = pygame.image.load('yllwdoorkey.png')
grndoor = pygame.image.load('grndoorkey.png')
bluedoor = pygame.image.load('bluedoorkey.png')
reddoor = pygame.image.load('reddoorkey.png')
yllwkey = pygame.image.load('yllwkey.png')
grnkey = pygame.image.load('grnkey.png')
bluekey = pygame.image.load('bluekey.png')
redkey = pygame.image.load('redkey.png')
joker = pygame.image.load('joker.gif')



def draw_object():
    global board
    index_x=0
    index_y=0
    for i in board:
        index_x = 0
        for j in i:
            if j == 'P':
                draw_prisoner(50*index_x,50*index_y)
            elif j == 'H':
                draw_wall(50*index_x,50*index_y)
            elif j == 'F':
                draw_chip(50*index_x,50*index_y)
            elif j == 'YD':
                draw_yllwdoor(50*index_x,50*index_y)
            elif j == 'BD':
                draw_bluedoor(50*index_x,50*index_y)
            elif j == 'GD':
                draw_grndoor(50*index_x,50*index_y)
            elif j == 'RD':
                draw_reddoor(50*index_x,50*index_y)
            elif j == 'YK':
                draw_yllwkey(50*index_x,50*index_y)
            elif j == 'BK':
                draw_bluekey(50*index_x,50*index_y)
            elif j == 'GK':
                draw_grnkey(50*index_x,50*index_y)
            elif j == 'RK':
                draw_redkey(50*index_x,50*index_y)
            elif j == '!':
                draw_guard(50*index_x,50*index_y)


                
            index_x = index_x+1
        index_y = index_y+1

def draw_yllwdoor(x,y):
    screen.blit(yllwdoor,(x,y))

def draw_bluedoor(x,y):
    screen.blit(bluedoor,(x,y))

def draw_grndoor(x,y):
    screen.blit(grndoor,(x,y))

def draw_reddoor(x,y):
    screen.blit(reddoor,(x,y))

def draw_bluekey(x,y):
    screen.blit(bluekey,(x,y))

def draw_yllwkey(x,y):
    screen.blit(yllwkey,(x,y))

def draw_grnkey(x,y):
    screen.blit(grnkey,(x,y))

def draw_redkey(x,y):
    screen.blit(redkey,(x,y))

def draw_wall(x,y):
    screen.blit(wall,(x,y))

def draw_prisoner(x,y):
    screen.blit(prisoner,(x,y))

def draw_chip(x,y):
    screen.blit(chip,(x,y))

def draw_floortile(x,y):
    screen.blit(floor,(x,y))

def draw_guard(x,y):
    screen.blit(joker,(x,y))

def draw_text(word,size,color,x,y):
    font = pygame.font.SysFont("Stencil",size)
    label = font.render(word, 1, (color))
    screen.blit(label, (x,y))



def draw_floor():
    global board
    i = 0
    j = 0
    for row in board:
        i = 0
        for column in row:
            draw_floortile(i,j)
            i = i+50
        j = j+50

def get_input():
    key = pygame.key.get_pressed()
    return key

def door_unlock(a):
    global hasyllwkey
    global hasbluekey
    global hasgrnkey
    global hasredkey
    if a == "YD" and hasyllwkey == 1:
        return True
    elif a == "BD" and hasbluekey == 1:
        return True
    elif a == "GD" and hasgrnkey == 1:
        return True
    elif a == "RD" and hasredkey == 1:
        return True
    elif a == "YD" or a == "BD" or a == "GD" or a == "RD":
        return False
        
def is_wall(a):
    if a == "H":
        return True
    else: 
        return False
        
def is_key(a):
    global hasyllwkey
    global hasbluekey
    global hasgrnkey
    global hasredkey
    if a == 'YK':
        hasyllwkey = 1
        return True
    elif a == 'BK':
        hasbluekey = 1
        return True
    elif a == 'GK':
        hasgrnkey = 1
        return True
    elif a == 'RK':
        hasredkey = 1
        return True
    else:
        return False
        
def is_win(a):
    if a == "F":
        return True
    else: 
        return False
        
def is_dead(a):
    if a == "!":
        return True
    else:
        return False
def death_message(num):
   if num < 15:
       print("You were mauled to death by hungry rats")
   elif num >= 15 and num < 25:
       print("You fell into a very deep pit full of giant spiders")
   elif num >= 25 and num < 35:
       print("You tripped and broke your neck")
   elif num >= 35 and num < 45:
       print("You took an arrow to the knee")
   elif num >= 45:
       print("You have died of dysentery")

def board_move(key,board):
    global x
    global y
    if key[pygame.K_w]:
        board[y - 1][x] = "P"
        board[y][x] = "_"
        y = y - 1
        return
    elif key[pygame.K_a]:
        board[y][x-1] = "P"
        board[y][x] = "_"
        x = x - 1
        return
    elif key[pygame.K_s]:
        board[y + 1][x] = "P"
        board[y][x] = "_"
        y = y + 1
        return
    elif key[pygame.K_d]:
        board[y][x+1] = "P"
        board[y][x] = "_"
        x = x + 1
        return

def game_logic(move,key):
    global num
    global x
    global y
    global board
    if door_unlock(move):
        board_move(key,board)
        draw_object()
        print('You use the key to unlock the door')
        return False
    elif door_unlock(move) == False:
        draw_object()
        print("Find the key to unlock the door")
        return False
    elif is_win(move):
        board_move(key,board)
        draw_object()
        print("You have brought great honor to your family")
        #time.sleep(3)
        return True
    elif is_key(move):
        board_move(key,board)
        draw_object()
        print("you picked up the key!")
        return False
    elif is_wall(move):
        draw_object()
        print("Dishonor to your family")
        return False
    elif is_dead(move):
        board_move(key,board)
        draw_object()
        death_message(num)
        return True
    else:
        num = num + 1
        board_move(key,board)
        draw_object()
        return False

def game():
    global x
    global y
    global board
    pressed = False
    while not pressed:
        key = get_input()
        screen.fill(blue)
        pygame.draw.rect(screen,black,(400,330,200,50))
        pygame.draw.rect(screen,black,(400,400,200,50))
        pygame.draw.rect(screen,black,(400,470,200,50))
        draw_text("START",35,red,445,340)
        draw_text("OPTIONS",35,red,430,410)
        draw_text("QUIT",35,red,455,480)
        (posx,posy) = pygame.mouse.get_pos()
        if posx >= 400 and posx <= 600 and posy >= 330 and posy <= 380:
            pygame.draw.rect(screen,black,(390,325,220,60))
            draw_text("START",45,red,433,335)
            if pygame.mouse.get_pressed() == (True,False,False):
                pressed = True
        elif posx >= 400 and posx <= 600 and posy >= 400 and posy <= 450:
            pygame.draw.rect(screen,black,(390,395,220,60))
            draw_text("OPTIONS",45,red,405,405)
        elif posx >= 400 and posx <= 600 and posy >= 470 and posy <= 520:
            pygame.draw.rect(screen,black,(390,465,220,60))
            draw_text("QUIT",45,red,445,475)
            if pygame.mouse.get_pressed() == (True,False,False):
                quit()
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pressed = True
                quit()
        pygame.display.update()
        clock.tick(60)
    caught = False
    while not caught:
        key = get_input()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                caught = True
        screen.fill(white)
        draw_floor()
        draw_object()
        if key[pygame.K_w]:
            move = board[y-1][x]
            caught = game_logic(move,key)
        elif key[pygame.K_a]:
            move = board[y][x-1] 
            caught = game_logic(move,key)
        elif key[pygame.K_s]:
            move = board[y+1][x]
            caught = game_logic(move,key)
        elif key[pygame.K_d]:
            move = board[y][x+1]
            caught = game_logic(move,key)
        elif key[pygame.K_ESCAPE]:
            game()
        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    quit()
game()