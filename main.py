import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Running')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_surf = test_font.render('My Game', False, (64,88,120))
score_rect=score_surf.get_rect(center=(400,50))

snail_surf = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      #  if event.type==pygame.MOUSEMOTION:
         # if  player_rect.collidepoint(event.pos):print('collision')
        if event.type==pygame.KEYDOWN:
        
            if event.key==pygame.K_SPACE:
                 player_gravity=-1

        

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    player_gravity+=0
    player_rect.y=player_gravity
    screen.blit(player_surf, player_rect)


    #keys=pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
       # print('jump')

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
        #print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    clock.tick(60)