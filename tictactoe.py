import pygame
from pygame.locals import *
import time


pygame.init()
sw=800
sh=600
screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("TIC TAC TOE")
CLOCK = pygame.time.Clock()
font_32 = pygame.font.Font("freesansbold.ttf", 32)
font_120 = pygame.font.Font("freesansbold.ttf", 120)
first_vertical= pygame.Rect(250,0,3,600)
second_vertical= pygame.Rect(520,0,3,600)

turn_player = 'x' #if 0 then X's turn, if 1 then O's turn
position_X = 0
position_Y = 0
winner=None
draw=False
row=None
col=None
x_img = pygame.transform.scale(pygame.image.load("imgs/X.jpg"),(80,80))
o_img = pygame.transform.scale(pygame.image.load("imgs/O.jpg"),(80,80))
game_array = [[None]*3,[None]*3,[None]*3] #to check the postions of winning
images=[]

def draw_symbol(ro,co):
    global position_X, position_Y,turn_player, images
    row=ro
    col=co
    print("enter")
    # print(col)
    # print(row)
    if row == 1:
        position_Y = 70
    if row == 2:
        position_Y = 270
    if row == 3:
        position_Y = 480
    if col == 1:
        position_X = 70
    if col == 2:
        position_X = 320
    if col == 3:
        position_X = 580
    game_array[row-1][col-1]=turn_player
    if (turn_player == 'x'):
        # print("bli")
        images.append((position_X,position_Y, x_img))
        turn_player = 'o'
    else:
        images.append((position_X,position_Y, o_img))
        turn_player = 'x'
    pygame.display.update()


def status_draw():
    global winner, turn_player, draw
    if winner is None:
        message = turn_player.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'
    text = font_32.render(message, 1, (0, 0, 0))
    screen.blit(text, (0,0))
    resetmsg = font_32.render("Press R to Restart the game!!", True, (0, 0, 0))
    screen.blit(resetmsg, (300, 0))
    pygame.display.update()

def userclick():
    mx,my= pygame.mouse.get_pos()
    print(mx,my)
    if 0<mx<250:
        col=1
    elif 251<mx<520:
        col=2
    elif 521<mx<800:
        col=3
    else:
        col=0
    if 0<my<200:
        row=1
    elif 201<my<400:
        row=2
    elif 401<my<600:
        row=3
    else:
        row=0
    print(col)
    if (row and col and game_array[row - 1][col - 1] is None):
       draw_symbol(row,col)
       check_win()



def check_win():
    global game_array, winner, draw, position_Y, position_X
    # print(game_array)
    # check for winning rows
    for row in range(0, 3):
        if ((game_array[row][0] == game_array[row][1] == game_array[row][2]) and (game_array[row][0] is not None)):
            # this row won
            winner = game_array[row][0]
            pygame.draw.line(screen, (250, 0, 0),(30,position_Y+30),(750,position_Y+30),4)
            break

    # check for winning columns
    for col in range(0, 3):
        if (game_array[0][col] == game_array[1][col] == game_array[2][col]) and (game_array[0][col] is not None):
            # this column won
            winner = game_array[0][col]
            # draw winning line
            pygame.draw.line(screen, (250, 0, 0), (position_X+40,30),(position_X+40,580), 4)
            break

    # check for diagonal winners
    if (game_array[0][0] == game_array[1][1] == game_array[2][2]) and (game_array[0][0] is not None):
        # game won diagonally left to right
        winner = game_array[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (650, 525), 4)

    if (game_array[0][2] == game_array[1][1] == game_array[2][0]) and (game_array[0][2] is not None):
        # game won diagonally right to left
        winner = game_array[0][2]
        pygame.draw.line(screen, (250, 70, 70), (672, 50), (90, 540), 4)

    if (all([all(row) for row in game_array]) and winner is None):
        draw = True
    status_draw()


def disp_imgs():
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),first_vertical)
    pygame.draw.rect(screen, (0, 0, 0), second_vertical)
    pygame.draw.line(screen,(0,0,0),(0,200),(800,200),2)
    pygame.draw.line(screen,(0,0,0),(0,400),(800,400),2)
    status_draw()
    for image in images:
        x, y, IMAGE = image
        screen.blit(IMAGE, (x,y))
    pygame.display.update()

def reset_game():
    global game_array, winner, turn_player, draw, images,row,col, position_Y, position_X
    print("reset")
    # time.sleep(3)
    turn_player = 'x'  # if 0 then X's turn, if 1 then O's turn
    position_X = 0
    position_Y = 0
    winner = None
    draw = False
    row = None
    col = None
    game_array = [[None] * 3, [None] * 3, [None] * 3]  # to check the postions of winning
    images = []
    disp_imgs()


disp_imgs()
running=True
col=0
row=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                userclick()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_r:
                reset_game()

    disp_imgs()
    check_win()
    # if turn_player=='x':
    #     turnmsg = font_32.render("X's Turn", True, (0, 0, 255))
    #     screen.blit(turnmsg, (0,0))
    # elif turn_player == 'o':
    #     turnmsg = font_32.render("O's Turn", True, (0, 0, 255))
    #     screen.blit(turnmsg,(0,0))


    CLOCK.tick(3)
    pygame.display.update()






