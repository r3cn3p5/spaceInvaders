import pygame
import invaders

fd1 = [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]]

fd2 = [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]


class Invader(pygame.sprite.Sprite):
    def __init__(self, initialRow, initialColumn):
        super(Invader, self).__init__()

        frameData = [fd1, fd2]

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
            topleft=(initialColumn * ((invaders.SCALE * w) + 10), initialRow * ((invaders.SCALE * h) + 10))
        )

        self.curr_frame = self.frames[0]

        self.speed = 3
        self.direction = 1
        self.drop = 1

    def send_left(self):
        self.direction = 0
        self.drop = 1

    def send_right(self):
        self.direction = 1
        self.drop = 1

    def update(self):

        if self.drop == 1:
            self.rect.move_ip(0, self.speed * 2)
            self.drop = 0

        if self.direction == 1:
            self.rect.move_ip(self.speed, 0)
        else:
            self.rect.move_ip(-self.speed, 0)

        if self.curr_frame == self.frames[0]:
            self.curr_frame = self.frames[1]
        else:
            self.curr_frame = self.frames[0]

