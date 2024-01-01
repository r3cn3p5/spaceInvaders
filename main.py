import pygame
import invader
import invaders
import player
import edge

from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([invaders.SCREEN_WIDTH, invaders.SCREEN_HEIGHT])

edges = pygame.sprite.Group()
left_edge = edge.Edge(0, 0, 5, invaders.SCREEN_HEIGHT)
edges.add(left_edge)
right_edge = edge.Edge(invaders.SCREEN_WIDTH - 5, 0, 5, invaders.SCREEN_HEIGHT)
edges.add(right_edge)

invaders = pygame.sprite.Group()
for r in range(1, 10):
    invaders.add(invader.Invader(2, r))
    invaders.add(invader.Invader(3, r))
    invaders.add(invader.Invader(4, r))

player1 = player.Player(10, 4)

MOVE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_ENEMY, 150)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOVE_ENEMY:
            invaders.update()

    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys)

    hits = pygame.sprite.groupcollide(edges, invaders, False, False)
    if hits:
        if hits.get(left_edge):
            for i in invaders:
                i.send_right()

        if hits.get(right_edge):
            for i in invaders:
                i.send_left()


    # Fill the background with white
    screen.fill((0, 0, 0))

    for r in invaders:
        screen.blit(r.curr_frame, r.rect)

    screen.blit(player1.curr_frame, player1.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
