import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
prabowokontol = pygame.image.load("th (6).jpg").convert()

pygame.mixer.init()
pygame.mixer.music.load("prabowo.mp3")
pygame.mixer.music.play(-1)

prabowox = 0
prabowoy = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keypress = pygame.key.get_pressed()

    keya = keypress[pygame.K_a]
    keyb = keypress[pygame.K_b]
    keyc = keypress[pygame.K_c]
    keyd = keypress[pygame.K_d]
    keye = keypress[pygame.K_e]
    keyf = keypress[pygame.K_f]
    keyg = keypress[pygame.K_g]
    keyh = keypress[pygame.K_h]
    keyi = keypress[pygame.K_i]
    keyj = keypress[pygame.K_j]
    keyk = keypress[pygame.K_k]
    keyl = keypress[pygame.K_l]
    keym = keypress[pygame.K_m]
    keyn = keypress[pygame.K_n]
    keyo = keypress[pygame.K_o]
    keyp = keypress[pygame.K_p]
    keyq = keypress[pygame.K_q]
    keyr = keypress[pygame.K_r]
    keys = keypress[pygame.K_s]
    keyt = keypress[pygame.K_t]
    keyu = keypress[pygame.K_u]
    keyv = keypress[pygame.K_v]
    keyw = keypress[pygame.K_w]
    keyx = keypress[pygame.K_x]
    keyy = keypress[pygame.K_y]
    keyz = keypress[pygame.K_z]

    key_up = keypress[pygame.K_UP]
    key_down = keypress[pygame.K_DOWN]
    key_left = keypress[pygame.K_LEFT]
    key_right = keypress[pygame.K_RIGHT]

    if keyd or key_right:
        prabowox += 5
    if keya or key_left:
        prabowox -= 5
    if keyw or key_up:
        prabowoy -= 5
    if keys or key_down:
        prabowoy += 5

    prabowopos = [prabowox, prabowoy]
    print(prabowopos)

    screen.fill("black")
    screen.blit(prabowokontol, prabowopos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
