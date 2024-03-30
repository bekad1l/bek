import pygame

pygame.init()

width , height = 652, 330

surface = pygame.display.set_mode((width, height))
name_pro = pygame.display.set_caption("Music player")

#load image 512 x 512
background = pygame.image.load('image/background.png')
stop_icon = pygame.image.load('image/stop_icon.png')
next_icon = pygame.image.load('image/next_icon.png')
previous_icon = pygame.image.load('image/previous_icon.png')
play_icon = pygame.image.load('image/play_icon.png')


#load music
pygame.mixer.music.load('music/Billie_Eilish-bad_guy.mp3')
pygame.mixer.music.load('music/Frank Sinatra-I Love You Baby.mp3')
pygame.mixer.music.load('music/Maneskin-I Wanna Be Your Slave.mp3')

playlist = {
    1: 'music/Billie_Eilish-bad_guy.mp3',
    2: 'music/Frank Sinatra-I Love You Baby.mp3',
    3: 'music/Maneskin-I Wanna Be Your Slave.mp3'
}

count_track = 1
run = True
FPS = 60
is_playing = False
tickrate = pygame.time.Clock()
paused_time = 0

while run:

    surface.blit(background, (0, 0))
    surface.blit(previous_icon, (100,155))
    
    if is_playing == False:
        surface.blit(play_icon,(262,155))
    else:
        surface.blit(stop_icon, (262,155))
        
    surface.blit(next_icon, (424,155))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_F7) and is_playing == False:
                # pause need for didn`t replay music
                if paused_time != 0:
                    pygame.mixer.music.unpause()
                    is_playing = True
                else:
                    pygame.mixer.music.load(playlist[count_track])
                    pygame.mixer.music.play()
                    is_playing = True
            elif event.key == pygame.K_F5 or event.key == pygame.K_LEFT:
                if count_track == 1:
                    count_track = 3
                else:
                    count_track -= 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif event.key == pygame.K_F6 or event.key == pygame.K_RIGHT:
                if count_track == 3:
                    count_track = 1
                else:
                    count_track += 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif (event.key == pygame.K_SPACE or event.key == pygame.K_F7) and is_playing == True:
                pygame.mixer.music.pause()
                is_playing = False
                paused_time = pygame.mixer.music.get_pos()

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()
