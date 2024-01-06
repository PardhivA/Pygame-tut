import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("AIm to WIN")
clock = pygame.time.Clock()
test_font=  pygame.font.Font('font/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('./graphics/Sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()
text_surface = test_font.render('My Game', False ,'Black').convert()

snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
while True:
    # draw all our elements and update everything 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(sky_surface,(300,50))
    snail_x_pos -= 4
    if(snail_x_pos < -100): snail_x_pos = 600
    screen.blit(snail_surface,(snail_x_pos,270))
    pygame.display.update()
    clock.tick(60)