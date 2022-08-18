import random, sys
import pygame

pygame.init()

main_screen_width = 1280
main_screen_height = 720
main_screen = pygame.display.set_mode((main_screen_width, main_screen_height))

title = '반응 속도'
program_version = ' ver 0.1.0'
pygame.display.set_caption(title + program_version)

clock = pygame.time.Clock()
FPS = 60

input_boolean = False
step = 'wait'

nngt = 'NanumGothic.otf'
f = pygame.font.Font(nngt, 50)

#reaction_time = None

while True:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                if step == 'wait':
                    step = 'start'
                    #current_time = pygame.time.get_ticks()
                    time_delay = random.randrange(3, 11) * 1000
                    #reaction_time = current_time - recorded_time
                    recorded_time = current_time + time_delay
                elif step == 'start':
                    if current_time >= recorded_time:
                        if not input_boolean:
                            reaction_time = current_time - recorded_time
                            input_boolean = True
                        elif input_boolean:
                            step = 'wait'
                            input_boolean = False
                        

    main_screen.fill((0, 0, 0))


    if step == 'wait':
        text1 = '스페이스 키를 눌러 시작해 주세요.'
        text1_surf = f.render(text1, True, (255, 255, 255))
        text1_rect = text1_surf.get_rect()
        text1_rect.center = (main_screen_width / 2, main_screen_height / 2)
        main_screen.blit(text1_surf, text1_rect)
    elif step == 'start':
        if current_time >= recorded_time:
            if input_boolean:
                text1 = str(reaction_time / 1000) + '초입니다. 스페이스 키를 눌러 다시 시작하세요.'
                text1_surf = f.render(text1, True, (255, 255, 255))
                text1_rect = text1_surf.get_rect()
                text1_rect.center = (main_screen_width / 2, main_screen_height / 2)
                main_screen.blit(text1_surf, text1_rect)
            else:
                text1 = '스페이스 키를 누르세요.'
                text1_surf = f.render(text1, True, (255, 255, 255))
                text1_rect = text1_surf.get_rect()
                text1_rect.center = (main_screen_width / 2, main_screen_height / 2)
                main_screen.blit(text1_surf, text1_rect)
        else:
            text1 = '기다리세요.'
            text1_surf = f.render(text1, True, (255, 255, 255))
            text1_rect = text1_surf.get_rect()
            text1_rect.center = (main_screen_width / 2, main_screen_height / 2)
            main_screen.blit(text1_surf, text1_rect)

    
    
    pygame.display.update()
    clock.tick(FPS)