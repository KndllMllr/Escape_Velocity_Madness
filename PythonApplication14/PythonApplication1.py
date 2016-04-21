#Kendall Miller
#Nimoy Vaidya
#Programming I: final project
#game name: Escape Velocity Madness
import pygame, time, random

pygame.init()
#some global variables
x = 1
y = 1
hasyllwkey = 0
hasbluekey = 0
hasgrnkey = 0
hasredkey = 0
level_selector = 1
guard_move_counter = 0

display_width = 1000
display_height = 800

black = (30,30,30)
white = (255,255,255)
green = (0,100,0)
red = (255,0,0)
purple = (128,0,128)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Escape Velocity Madness')
clock = pygame.time.Clock()

# Decides which text file is used to populate the board array based on the value of level_selector
def choose_level():
    global level_selector
    global board
    if level_selector == 1:
        level = "level1.txt"
    if level_selector == 2:
        level = "level2.txt"
    if level_selector == 3:
        level = "level3.txt"
    with open(level) as level1:
        board = [line.split() for line in level1]

#loading all the assets to be used on the board and splash screen
prisoner = pygame.image.load('flash.png')
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
joker2 = pygame.image.load('joker2.png')
bigflash = pygame.image.load('flashbck.png')
bckrnd = pygame.image.load('blockwall.png')
exit = pygame.image.load('exit.png')

#loops through the board array and determines which asset to draw and where it should go
def draw_object():
    global board
    global guard_move_counter
    index_x=0
    index_y=0
    guard_move_counter += 1
    for i in board:
        index_x = 0
        for j in i:
            if j == 'P':
                draw_prisoner(50*index_x,50*index_y)
            elif j == 'H':
                draw_wall(50*index_x,50*index_y)
            elif j == 'F' or j == 'f':
                draw_exit(50*index_x,50*index_y)
            elif j == 'Y':
                draw_yllwdoor(50*index_x,50*index_y)
            elif j == 'B':
                draw_bluedoor(50*index_x,50*index_y)
            elif j == 'G':
                draw_grndoor(50*index_x,50*index_y)
            elif j == 'R':
                draw_reddoor(50*index_x,50*index_y)
            elif j == 'y':
                draw_yllwkey(50*index_x,50*index_y)
            elif j == 'b':
                draw_bluekey(50*index_x,50*index_y)
            elif j == 'g':
                draw_grnkey(50*index_x,50*index_y)
            elif j == 'r':
                draw_redkey(50*index_x,50*index_y)
            elif j == '!':
                draw_guard(50*index_x,50*index_y)
                if (guard_move_counter % 5) == 0:
                    #is meant to move the guard once every 5 ticks though sometimes moves more often than that for unknown reason.
                    guard_move(index_x,index_y)
                    
            index_x += 1
        index_y += 1

#a draw fucntion for each asset to simplify the process
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

def draw_floortile(x,y):
    screen.blit(floor,(x,y))

def draw_guard(x,y):
    screen.blit(joker,(x,y))

def draw_joker(x,y):
    screen.blit(joker2,(x,y))

def draw_flash(x,y):
    screen.blit(bigflash,(x,y))

def draw_bckrnd(x,y):
    screen.blit(bckrnd,(x,y))

def draw_exit(x,y):
    screen.blit(exit,(x,y))

#similar to the draw asset functions, but takes all necessary parameters for full text customization.
def draw_text(word,size,font_type,color,x,y):
    font = pygame.font.SysFont(font_type,size)
    label = font.render(word, 1, (color))
    screen.blit(label, (x,y))


#draws the floor of the prison
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

#gets the keyboard input from the user
def get_input():
    key = pygame.key.get_pressed()
    return key

#checks if the player has obtained the correct key for a door
def door_unlock(a):
    global hasyllwkey
    global hasbluekey
    global hasgrnkey
    global hasredkey
    if a == "Y" and hasyllwkey == 1:
        return True
    elif a == "B" and hasbluekey == 1:
        return True
    elif a == "G" and hasgrnkey == 1:
        return True
    elif a == "R" and hasredkey == 1:
        return True
    elif a == "Y" or a == "B" or a == "G" or a == "R":
        return False

#checks if the next space is a wall    
def is_wall(a):
    if a == "H":
        return True
    else: 
        return False

#checks if the next space is a key and which key it is 
def is_key(a):
    global hasyllwkey
    global hasbluekey
    global hasgrnkey
    global hasredkey
    if a == 'y':
        hasyllwkey = 1
        return True
    elif a == 'b':
        hasbluekey = 1
        return True
    elif a == 'g':
        hasgrnkey = 1
        return True
    elif a == 'r':
        hasredkey = 1
        return True
    else:
        return False

#checks if the next space is a winning space. F for a level win and f for a game win        
def is_win(a):
    if a == "F":
        return True
    elif a == "f":
        quit()
    else: 
        return False

#checks if the next space contains a guard that will kill the player  
def is_dead(a):
    if a == "!":
        return True
    else:
        return False

#if the player has died, displays a taunting death message
def death_message():
   draw_text("YOU DIED",45,"timesnewroman",red,365,400)

#determines how to update the array based upon player keyboard input
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

#simple random movement for the joker guards
def guard_move(index_x,index_y):
    global board
    direction = random.randrange(4)
    if direction == 0 and board[index_y-1][index_x] == '_':
        board[index_y][index_x] = '_'
        board[index_y-1][index_x] = '!'
    elif direction == 1 and board[index_y+1][index_x] == '_':
        board[index_y][index_x] = '_'
        board[index_y+1][index_x] = '!'
    elif direction == 2 and board[index_y][index_x-1] == '_':
        board[index_y][index_x] = '_'
        board[index_y][index_x-1] = '!'
    elif direction == 3 and board[index_y][index_x+1] == '_':
        board[index_y][index_x] = '_'
        board[index_y][index_x+1] = '!'

#uses the player's input to check which type of space the next space is and what actions to take based on that.
def game_logic(move,key):
    global x
    global y
    global board
    global level_selector
    global hasyllwkey
    global hasbluekey
    global hasgrnkey
    global hasredkey
    if door_unlock(move):
        board_move(key,board)
        draw_object()
        return False
    elif door_unlock(move) == False:
        draw_object()
        return False
    elif is_win(move):
        board_move(key,board)
        draw_object()
        level_selector += 1
        x = 1
        y = 1
        hasyllwkey = 0
        hasbluekey = 0
        hasgrnkey = 0
        hasredkey = 0
        choose_level()
        game()
        return False
    elif is_key(move):
        board_move(key,board)
        draw_object()
        return False
    elif is_wall(move):
        draw_object()
        return False
    elif is_dead(move):
        board_move(key,board)
        draw_object()
        return True
    else:
        board_move(key,board)
        draw_object()
        return False

#the main game loop and splash sceen loop
def game():
    global x
    global y
    global board
    global level_selector
    pressed = False
    #this loop is the splash screen and hard codes objects to specific locations
    #would need to generalize this if resolution scaling were added, but didn't get to that
    while not pressed:
        screen.fill(black)
        draw_bckrnd(0,0)
        draw_joker(250,0)
        draw_flash(200,100)
        draw_text("Slow down Flash!",35,"gigi",purple,730,30)
        draw_text("I think you're",35,"gigi",purple,730,60)
        draw_text("Starting to Fade",35,"gigi",purple,730,90)
        pygame.draw.rect(screen,green,(50,330,200,50))
        pygame.draw.rect(screen,green,(50,400,200,50))
        pygame.draw.rect(screen,green,(50,470,200,50))
        draw_text("PLAY",35,"Stencil",white,105,340)
        draw_text("NEW GAME",35,"Stencil",white,65,410)
        draw_text("QUIT",35,"Stencil",white,105,480)
        (posx,posy) = pygame.mouse.get_pos()
        if posx >= 50 and posx <= 250 and posy >= 330 and posy <= 380:
            pygame.draw.rect(screen,green,(40,325,220,60))
            draw_text("PLAY",45,"Stencil",white,90,335)
            if pygame.mouse.get_pressed() == (True,False,False):
                pressed = True
        elif posx >= 50 and posx <= 250 and posy >= 400 and posy <= 450:
            pygame.draw.rect(screen,green,(40,395,220,60))
            draw_text("NEW GAME",40,"Stencil",white,50,405)
            if pygame.mouse.get_pressed() == (True,False,False):
                level_selector = 1
                x = 1
                y = 1
                choose_level()
                pressed = True
        elif posx >= 50 and posx <= 250 and posy >= 470 and posy <= 520:
            pygame.draw.rect(screen,green,(40,465,220,60))
            draw_text("QUIT",45,"Stencil",white,95,475)
            if pygame.mouse.get_pressed() == (True,False,False):
                quit()
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        #refresh 60 times every second
        clock.tick(60)
    caught = False
    #runs the game for as long as the caught variale = false
    while not caught:
        key = get_input()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
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
        #refresh 15 time every second
        clock.tick(15)
    death_message()
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
#initial function calls that start the game
choose_level()
game()