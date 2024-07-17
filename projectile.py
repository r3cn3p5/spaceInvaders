import pygame
import invaders

fd1 = [[1],
       [1],
       [1]]


class Projectile(pygame.sprite.Sprite):
    def __init__(self, initialTopLeft):
        super(Projectile, self).__init__()

        frameData = [fd1]

        h = len(fd1)
        w = len(fd1[0])

        self.frames = []

        for f in frameData:
            frame = pygame.Surface((w * invaders.SCALE, h * invaders.SCALE))
            frame.fill((0, 0, 0))
            x = y = 0
            for line in f:
                for e in line:
                    if e == 1:
                        pygame.draw.rect(frame, (255, 255, 255), pygame.Rect(y, x, invaders.SCALE, invaders.SCALE))
                    y += invaders.SCALE
                y = 0
                x += invaders.SCALE
            self.frames.append(frame)

        self.rect = self.frames[0].get_rect(topleft=initialTopLeft)

        self.curr_frame = self.frames[0]
        self.speed = 3


    def update(self, pressed_keys):

        self.rect.move_ip(0, -self.speed)
