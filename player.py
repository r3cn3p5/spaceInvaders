import pygame
import invaders

from pygame.locals import (
    K_LEFT,
    K_RIGHT
)

fd1 = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Player(pygame.sprite.Sprite):
    def __init__(self, initialRow, initialColumn):
        super(Player, self).__init__()

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
                        pygame.draw.rect(frame, (0, 255, 0), pygame.Rect(y, x, invaders.SCALE, invaders.SCALE))
                    y += invaders.SCALE
                y = 0
                x += invaders.SCALE
            self.frames.append(frame)

        self.rect = self.frames[0].get_rect(
            topleft=(initialColumn * ((invaders.SCALE * w) + 10), initialRow * ((invaders.SCALE * h) + 10))
        )

        self.curr_frame = self.frames[0]

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > invaders.SCREEN_WIDTH:
            self.rect.right = invaders.SCREEN_WIDTH
