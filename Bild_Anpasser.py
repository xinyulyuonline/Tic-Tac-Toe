import pygame
pygame.init()
image_path2 = "images/load/black.png"
image2 = pygame.image.load(image_path2)
resized_image = pygame.transform.scale(image2, (800, 800))
pygame.image.save(resized_image, 'images/load/black.png')
