import os

import pygame

BASE_IMG_PATH = 'data/images/'

def esLoadimg(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def esLoadAllImgs(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(esLoadimg(path + '/' + img_name))
    return images