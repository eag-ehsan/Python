import sys

import pygame


from scripts.utils import esLoadimg, esLoadAllImgs, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class esGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        


        self.assets = {
            'decor': esLoadAllImgs('tiles/decor'),
            'grass': esLoadAllImgs('tiles/grass'),
            'large_decor': esLoadAllImgs('tiles/large_decor'),
            'stone': esLoadAllImgs('tiles/stone'),
            'player': esLoadimg('entities/player.png'),
            'background': esLoadimg('background.png'),
            'clouds': esLoadAllImgs('clouds'),
            'player/idle': Animation(esLoadAllImgs('entities/player/idle'), img_dur=6),
            'player/run': Animation(esLoadAllImgs('entities/player/run'), img_dur=4),
            'player/jump': Animation(esLoadAllImgs('entities/player/jump')),
            'player/slide': Animation(esLoadAllImgs('entities/player/slide')),
            'player/wall_slide': Animation(esLoadAllImgs('entities/player/wall_slide')),
        }

        self.clouds = Clouds(self.assets['clouds'], count=16)


        self.movement = [0, 0]
        self.m_player = Player(self, (50, 50), (8, 15))
        self.m_tilemap = Tilemap(self, tile_size=16)
        self.esCamera = [0,0]


    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            self.esCamera[0] += (self.m_player.rect().centerx - self.display.get_width() / 2 - self.esCamera[0]) / 30
            self.esCamera[1] += (self.m_player.rect().centery - self.display.get_height() / 2 - self.esCamera[1]) / 30
            esCamera_render = (int(self.esCamera[0]), int(self.esCamera[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=esCamera_render)

            self.m_tilemap.render(self.display, offset=esCamera_render)
            self.m_player.update(self.m_tilemap, (self.movement[1] - self.movement[0],0))
            self.m_player.render(self.display, offset=esCamera_render)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 1
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 1
                    if event.key == pygame.K_UP:
                        self.m_player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 0
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 0
            
            #self.screen.blit(self.display, (0, 0))
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

esGame().run()