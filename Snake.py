import sys
import pygame
import random

class Block:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos

class Food :
    def __init__(self):
        x = random.randint(0,NB_CO - 1)
        y = random.randint(0,NB_LI - 1)
        self.block = Block(x,y)


    def draw_food(self):
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (72,212,98),rect)

class Snake :
    def __init__(self):
        self.body = [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = "RIGHT"


    def draw_snake(self):
         for block in self.body:
              x_coor = block.x * CELL_SIZE
              y_coor = block.y * CELL_SIZE
              block_rect = pygame.Rect(x_coor,y_coor,CELL_SIZE,CELL_SIZE)
              pygame.draw.rect(screen,(255,255,0),block_rect)

    def mov_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]

        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1 , old_head.y)


        elif self.direction == "LEFT":
            new_head = Block(old_head.x - 1, old_head.y)

        elif self.direction == "TOP":
            new_head = Block(old_head.x , old_head.y - 1)

        else :
            new_head = Block(old_head.x , old_head.y + 1)

        self.body.append(new_head)
        self.body.pop(0)










pygame.init()
NB_CO = 10
NB_LI = 15
CELL_SIZE = 40

screen = pygame.display.set_mode(size=(NB_CO * CELL_SIZE , NB_LI * CELL_SIZE))
timer = pygame.time.Clock()
pygame.display.set_caption("Snake")
pygame.mixer.init()
pygame.mixer.music.load("music/DAN_DA_DAN_OP___Otonoke_by_Creepy_Nuts___Netflix_Anime(256k).mp3")
pygame.mixer.music.play(-1)

game_on = True
food = Food()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,400)
def show_grid():
    for i in range(0,NB_CO):
        for j in range(0,NB_LI):
            rect = pygame.Rect(i * CELL_SIZE,j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen,pygame.Color('black'),rect, width= 1)


while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.mov_snake()



    pygame.display.update()

    screen.fill(pygame.Color("white"))
    show_grid()
    food.draw_food()
    snake.draw_snake()
    timer.tick(60)
