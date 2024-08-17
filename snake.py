import pygame
import sys
import random
from pygame.math import Vector2

class snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False

        self.head_up=pygame.image.load('graphics/head_Up.png').convert_alpha()
        self.head_down=pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right=pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left=pygame.image.load('graphics/head_left.png').convert_alpha()

        self.tail_up=pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down=pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right=pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left=pygame.image.load('graphics/tail_left.png').convert_alpha()

        self.body_vertical=pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal=pygame.image.load('graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr=pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl=pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br=pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl=pygame.image.load('graphics/body_bl.png').convert_alpha()


    def draw_snake(self):
        self.update_head_graphics()
        for index,block in enumerate(self.body):
           x_pos=int(block.x*cell_size)
           y_pos=int(block.y*cell_size)
           block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

           if index==0:
              screen.blit(self.head_right,block_rect)
           else:
              pygame.draw.rect(screen,(150,100,100),block_rect)

    def update_head_graphics(self):
       head_relation=self.body[1]-self.body[0]
       if head_relation==Vector2(1,0): 
          self.head=self.head_left
       elif head_relation==Vector2(-1,0):
          self.head=self.head_right
       elif head_relation==Vector2(0,1): 
          self.head=self.head_up
       elif head_relation==Vector2(0,-1): 
          self.head=self.head_down

    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]

    def add_block(self):   
        self.new_block=True  

class Fruit:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y =random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
        # create an x and y position
        # draw a square

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        screen.blit(apple,fruit_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y =random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
    
class main():
    def __init__(self):
        self.snake=snake()
        self.fruit=Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
     self.fruit.draw_fruit()
     self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        if not 0<=self.snake.body[0].x<=cell_number or not 0<=self.snake.body[0].y<=cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
         if block== self.snake.body[0]:
            self.game_over()

    def game_over(self):
        pygame.quit()
        exit() 

pygame.init()
cell_size = 20
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size ))
clock = pygame.time.Clock()
apple=pygame.image.load('graphics/apple.png').convert_alpha()
screen_update=pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

main_game=main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==screen_update:
            main_game.update()
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                  if main_game.snake.direction.y!=1:
                    main_game.snake.direction=Vector2(0,-1)
                if event.key==pygame.K_DOWN:
                  if main_game.snake.direction.y!=-1:
                    main_game.snake.direction=Vector2(0,1)
                if event.key==pygame.K_LEFT:
                   if main_game.snake.direction.x!=1: 
                    main_game.snake.direction=Vector2(-1,0)
                if event.key==pygame.K_RIGHT:
                   if main_game.snake.direction.x!=-1:
                    main_game.snake.direction=Vector2(1,0)    

    screen.fill((175, 215, 70))
    main_game.draw_elements() 
    pygame.display.update()
    clock.tick(60)

