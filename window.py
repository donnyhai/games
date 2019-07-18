import pygame, sys

pygame.init()

showed_display = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('Spielfeld')
showed_display.fill((100,25,255))


test_image = pygame.image.load('ball.jpg')
test_image_position = (test_image.get_width()-150, test_image.get_height()-400)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                showed_display.blit(test_image,test_image_position)
        pygame.display.update()