import pygame
import invaders

fd1 = [[1, 1],
       [1, 1],
       [1, 1],
       [1, 1],
       [1, 1]]


class Bullet(pygame.sprite.Sprite):
    def __init__(self, initialRow, initialColumn):
        super(Bullet, self).__init__()

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

        self.rect = self.frames[0].get_rect(
               topleft=(initialColumn * ((invaders.SCALE * w) + 10),
                        initialRow * ((invaders.SCALE * h) + 10)
                        )
        )

        self.curr_frame = self.frames[0]


