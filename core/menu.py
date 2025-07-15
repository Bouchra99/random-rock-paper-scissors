import pygame
from core.game import game
from core.scores import scores
from utils.constants import screen, FONT_20, YELLOW
from ui.button import Button

def menu():
    running = True 

    start_btn = Button("start game", (500 - 180)/2 , (400 - 50)/2 -30 , 180, 40, game)
    score_btn = Button("scores", (500 - 180)/2  , (400 - 50)/2 + 30, 180, 40, scores)
    
    while running: 
        screen.fill("black")

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            start_btn.handle_event(event)
            score_btn.handle_event(event)
        
        start_btn.draw(screen)
        score_btn.draw(screen)

        pygame.display.update()

    # pygame.quit()


    
    