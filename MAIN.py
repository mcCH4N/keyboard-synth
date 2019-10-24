import pygame

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False

import fluidsynth

fs = fluidsynth.Synth()
fs.start(driver="dsound")
# synth choose
fs.program_select(0, fs.sfload("FT-EGuitarDistortion-20161103.sf2"), 0, 0)
fs.program_select(1, fs.sfload("Dance Trance.sf2"), 0, 0)
fs.program_select(2, fs.sfload("guitar.sf2"), 0, 0)
fs.program_select(3, fs.sfload("Pulse Wobbler.sf2"), 0, 0)
#set synth
n=0
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # barcode chromatic notes 2 octaves
            #____Change synth______________________________________#
                if event.key == pygame.K_COMMA:
                    if n==0:
                        n=2
                    elif n==2:
                        n=0
                elif event.key == pygame.K_PERIOD:
                    n=0
            #___________________________________________#
                elif event.key == pygame.K_q:
                    fs.noteon(n, 48, 127)
                elif event.key == pygame.K_w:
                    fs.noteon(n, 49, 127)
                elif event.key == pygame.K_e:
                    fs.noteon(n, 50, 127)
                elif event.key == pygame.K_r:
                    fs.noteon(n, 51, 127)
                elif event.key == pygame.K_t:
                    fs.noteon(n, 52, 127)
                elif event.key == pygame.K_y:
                    fs.noteon(n, 53, 127)
                elif event.key == pygame.K_u:
                    fs.noteon(n, 54, 127)
                elif event.key == pygame.K_i:
                    fs.noteon(n, 55, 127)
                elif event.key == pygame.K_o:
                    fs.noteon(n, 56, 127)
                elif event.key == pygame.K_p:
                    fs.noteon(n, 57, 127)
                elif event.key == pygame.K_a:
                    fs.noteon(n, 58, 127)
                elif event.key == pygame.K_s:
                    fs.noteon(n, 59, 127)
                elif event.key == pygame.K_d:
                    fs.noteon(n, 60, 127)
                elif event.key == pygame.K_f:
                    fs.noteon(n, 61, 127)
                elif event.key == pygame.K_g:
                    fs.noteon(n, 62, 127)
                elif event.key == pygame.K_h:
                    fs.noteon(n, 63, 127)
                elif event.key == pygame.K_j:
                    fs.noteon(n, 64, 127)
                elif event.key == pygame.K_k:
                    fs.noteon(n, 65, 127)
                elif event.key == pygame.K_l:
                    fs.noteon(n, 66, 127)
                elif event.key == pygame.K_z:
                    fs.noteon(n, 67, 127)
                elif event.key == pygame.K_x:
                    fs.noteon(n, 68, 127)
                elif event.key == pygame.K_c:
                    fs.noteon(n, 69, 127)
                elif event.key == pygame.K_v:
                    fs.noteon(n, 70, 127)
                elif event.key == pygame.K_b:
                    fs.noteon(n, 71, 127)
                elif event.key == pygame.K_n:
                    fs.noteon(n, 72, 127)
                # If it is an arrow key, reset vector back to zero

                # Chords
                if event.key == pygame.K_1:
                    fs.noteon(0, 48, 127)
                    fs.noteon(0, 52, 127)
                    fs.noteon(0, 55, 127)
                elif event.key == pygame.K_2:
                    # Cmaj7
                    fs.noteon(0, 48, 127)
                    fs.noteon(0, 52, 127)
                    fs.noteon(0, 55, 127)
                    fs.noteon(0, 59, 127)
                elif event.key == pygame.K_3:
                    # Dmin
                    fs.noteon(0, 50, 127)
                    fs.noteon(0, 53, 127)
                    fs.noteon(0, 57, 127)
                elif event.key == pygame.K_4:
                    # Dmaj
                    fs.noteon(0, 50, 127)
                    fs.noteon(0, 54, 127)
                    fs.noteon(0, 57, 127)
                elif event.key == pygame.K_5:
                    # Emin
                    fs.noteon(0, 52, 127)
                    fs.noteon(0, 55, 127)
                    fs.noteon(0, 59, 127)
                elif event.key == pygame.K_6:
                    # Emaj
                    fs.noteon(0, 52, 127)
                    fs.noteon(0, 56, 127)
                    fs.noteon(0, 59, 127)
                elif event.key == pygame.K_7:
                    # Fmaj
                    fs.noteon(0, 53, 127)
                    fs.noteon(0, 57, 127)
                    fs.noteon(0, 60, 127)
                elif event.key == pygame.K_8:
                    # Gmaj
                    fs.noteon(0, 55, 127)
                    fs.noteon(0, 59, 127)
                    fs.noteon(0, 62, 127)
                elif event.key == pygame.K_9:
                    # Amin
                    fs.noteon(0, 57, 127)
                    fs.noteon(0, 60, 127)
                    fs.noteon(0, 64, 127)

        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    fs.noteoff(n, 48)
                elif event.key == pygame.K_w:
                    fs.noteoff(n, 49)
                elif event.key == pygame.K_e:
                    fs.noteoff(n, 50)
                elif event.key == pygame.K_r:
                    fs.noteoff(n, 51)
                elif event.key == pygame.K_t:
                    fs.noteoff(n, 52)
                elif event.key == pygame.K_y:
                    fs.noteoff(n, 53)
                elif event.key == pygame.K_u:
                    fs.noteoff(n, 54)
                elif event.key == pygame.K_i:
                    fs.noteoff(n, 55)
                elif event.key == pygame.K_o:
                    fs.noteoff(n, 56)
                elif event.key == pygame.K_p:
                    fs.noteoff(n, 57)
                elif event.key == pygame.K_a:
                    fs.noteoff(n, 58)
                elif event.key == pygame.K_s:
                    fs.noteoff(n, 59)
                elif event.key == pygame.K_d:
                    fs.noteoff(n, 60)
                elif event.key == pygame.K_f:
                    fs.noteoff(n, 61)
                elif event.key == pygame.K_g:
                    fs.noteoff(n, 62)
                elif event.key == pygame.K_h:
                    fs.noteoff(n, 63)
                elif event.key == pygame.K_j:
                    fs.noteoff(n, 64)
                elif event.key == pygame.K_k:
                    fs.noteoff(n, 65)
                elif event.key == pygame.K_l:
                    fs.noteoff(n, 66)
                elif event.key == pygame.K_z:
                    fs.noteoff(n, 67)
                elif event.key == pygame.K_x:
                    fs.noteoff(n, 68)
                elif event.key == pygame.K_c:
                    fs.noteoff(n, 69)
                elif event.key == pygame.K_v:
                    fs.noteoff(n, 70)
                elif event.key == pygame.K_b:
                    fs.noteoff(n, 71)
                elif event.key == pygame.K_n:
                    fs.noteoff(n, 72)

                # Chords
                if event.key == pygame.K_1:
                    fs.noteoff(0, 48)
                    fs.noteoff(0, 52)
                    fs.noteoff(0, 55)
                elif event.key == pygame.K_2:
                    # Cmaj7
                    fs.noteoff(0, 48)
                    fs.noteoff(0, 52)
                    fs.noteoff(0, 55)
                    fs.noteoff(0, 59)
                elif event.key == pygame.K_3:
                    # Dmin
                    fs.noteoff(0, 50)
                    fs.noteoff(0, 53)
                    fs.noteoff(0, 57)
                elif event.key == pygame.K_4:
                    # Dmaj
                    fs.noteoff(0, 50)
                    fs.noteoff(0, 54)
                    fs.noteoff(0, 57)
                elif event.key == pygame.K_5:
                    # Emin
                    fs.noteoff(0, 52)
                    fs.noteoff(0, 55)
                    fs.noteoff(0, 59)
                elif event.key == pygame.K_6:
                    # Emaj
                    fs.noteoff(0, 52)
                    fs.noteoff(0, 56)
                    fs.noteoff(0, 59)
                elif event.key == pygame.K_7:
                    # Fmaj
                    fs.noteoff(0, 53)
                    fs.noteoff(0, 57)
                    fs.noteoff(0, 60)
                elif event.key == pygame.K_8:
                    # Gmaj
                    fs.noteoff(0, 55)
                    fs.noteoff(0, 59)
                    fs.noteoff(0, 62)
                elif event.key == pygame.K_9:
                    # Amin
                    fs.noteoff(0, 57)
                    fs.noteoff(0, 60)
                    fs.noteoff(0, 64)
pygame.quit()
