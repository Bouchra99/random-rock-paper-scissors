import pygame
from utils.constants import screen, FONT_20, YELLOW, bg_1
from ui.button import Button


def scores(scores_list=None) :
    from core.game import game # circular import
    running = True 
    pygame.display.set_caption("Scores list")
    if(scores_list == None) :
        running = False
    
    start_btn = Button("restart game", (500 - 180)/2 , (400 - 50)/2 + 100 , 180, 40, game)

    while running :     
        screen.fill("black")
        screen.blit(bg_1,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

            start_btn.handle_event(event)

        start_btn.draw(screen)

        for item in scores_list:
            score = FONT_20.render(f'{item["name"]}    :   {item["score"]}',True, YELLOW)
            screen.blit(score ,((screen.get_width() - score.get_rect().width) / 2, 20*(scores_list.index(item)+1) + 80))
            # score_rect = score.get_rect()
        
        pygame.display.update()

    # print("scores")
