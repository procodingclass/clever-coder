import pygame, sys
from  game import create_screen, gameplay, gameControls, score

screen = create_screen()

# Load images
background_surf = pygame.image.load("assets/background3.jpg")
start_surf = pygame.image.load("assets/startpopup.png")
score_surf =pygame.image.load("assets/scoreimg.png")

# scale images
background_surf = pygame.transform.scale(background_surf, (500, 1200))


over_font = pygame.font.Font('freesansbold.ttf', 25)

# initial y position of background
background_pos_y = -600

# declare variable game state
game_state = "initial"

while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and game_state == "initial":
                game_state = "play"

        gameControls(event)


    screen.fill((255,255,255))
    screen.blit(background_surf, (0, background_pos_y))

    gameplay()

    if(game_state == "initial"):
        screen.blit(start_surf,(70,120))

    elif(game_state == "play"):
        # moving the background
        background_pos_y+=1
        # resetting the background to -500
        if(background_pos_y == 0):
            background_pos_y = -500
    elif(game_state == "end"):
        screen.blit(score_surf,(120,150))
        score_text = over_font.render(str(score), False, (255,255,255))
        screen.blit(score_text,(240,250))




    pygame.display.update()
