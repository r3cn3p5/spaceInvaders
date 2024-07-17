import pygame
import invader
import invaders
import player
import edge
import projectile


def createInvaders():
    new_invaders = pygame.sprite.Group()
    for ran in range(1, 10):
        new_invaders.add(invader.Invader(2, ran))
        new_invaders.add(invader.Invader(3, ran))
        new_invaders.add(invader.Invader(4, ran))
    return new_invaders


from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode([invaders.SCREEN_WIDTH, invaders.SCREEN_HEIGHT])

edges = pygame.sprite.Group()
left_edge = edge.Edge(0, 0, 5, invaders.SCREEN_HEIGHT)
edges.add(left_edge)
right_edge = edge.Edge(invaders.SCREEN_WIDTH - 5, 0, 5, invaders.SCREEN_HEIGHT)
edges.add(right_edge)
top_edge = edge.Edge(0, 0, invaders.SCREEN_WIDTH, 5)
edges.add(top_edge)

invaders = createInvaders()

game_sprites = pygame.sprite.Group()
player1 = player.Player(10, 4)
game_sprites.add(player1)

MOVE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_ENEMY, 150)

player1_bullet = None

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
    if pressed_keys[pygame.K_SPACE] and not game_sprites.has(player1_bullet):
        player1_bullet = projectile.Projectile((player1.rect.left + 30, player1.rect.top-5))
        game_sprites.add(player1_bullet)

    # Updates
    for gs in game_sprites:
        gs.update(pressed_keys)

    hits = pygame.sprite.groupcollide(edges, invaders, False, False)
    if hits:
        if hits.get(left_edge):
            for i in invaders:
                i.send_right()

        if hits.get(right_edge):
            for i in invaders:
                i.send_left()

    pygame.sprite.groupcollide(edges, game_sprites, False, True)
    pygame.sprite.groupcollide(invaders, game_sprites, True, True)

    screen.fill((0, 0, 0))

    for r in invaders:
        screen.blit(r.curr_frame, r.rect)

    for gs in game_sprites:
        screen.blit(gs.curr_frame, gs.rect)

    # Flip the display
    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()




