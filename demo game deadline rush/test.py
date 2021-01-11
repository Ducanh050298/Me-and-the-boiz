import pygame

FPS = 25
MainLoop = True
Loop1 = True         # Start app in Loop1
Loop2 = False        # Loop2 is idle

while MainLoop :
    # clock.tick(FPS)
    pygame.event.pump()
    keypress = pygame.key.get_pressed()
    keypress_dn  = tuple(x > y for x,y in zip(keypress, keypress_old))
    keypress_old = keypress
    if Loop1:
        if keypress_dn [pygame.K_ESCAPE] :
            Loop1 = False
            MainLoop = False
        if keypress_dn [pygame.K_2] :   # goto Loop2
            Loop1 = False
            Loop2 = True
        ...

    if Loop2:
        if keypress_dn [pygame.K_ESCAPE] :
            Loop2 = False
            MainLoop = False
        if keypress_dn [pygame.K_1] :   # goto Loop1
            Loop2 = False
            Loop1 = True
        ...

    pygame.display.flip( )

pygame.quit( )