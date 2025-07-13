import pygame
import random
from ui.button import Button

pygame.init()

pygame.display.set_caption("menu")

screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

scissors = pygame.image.load("media/scissors.png")
paper = pygame.image.load("media/paper.png")
rock = pygame.image.load("media/rock.png")

scissors_width = scissors.get_width()
scissors_height = scissors.get_height()
directions = [1, 2, 3, 4, 5, 6, 7, 8]

YELLOW = (255, 255, 0)
FONT_16 = pygame.font.SysFont(None, 16)
FONT_20 = pygame.font.SysFont(None, 20)

def move_up(elem : pygame.Rect) :
  
    elem.y -= 2 
    return elem

def move_down(elem : pygame.Rect) :
  
    elem.y += 2 
    return elem
    
def move_right(elem : pygame.Rect) :
    # x = elem.x
    # if(x < screen.get_width() - elem.width ) : 
    elem.x += 2 
    return elem 

def move_left(elem : pygame.Rect) :
    # x = elem.x
    # if(x > 2) :
 
    elem.x -= 2 
    return elem 

def move(item):
        rect = item["rect"]
        direction = item["direction"]

        if direction == 1:  # Right
            if rect.x < screen.get_width() - rect.width:
                move_right(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 2:  # Left
            if rect.x > 0:
                move_left(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 3:  # Down
            if rect.y < screen.get_height() - rect.height:
                move_down(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 4:  # Up
            if rect.y > 16:
                move_up(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 5:  # Down-Right
            if rect.x < screen.get_width() - rect.width and rect.y < screen.get_height() - rect.height:
                move_right(rect)
                move_down(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 6:  # Down-Left
            if rect.x > 0 and rect.y < screen.get_height() - rect.height:
                move_left(rect)
                move_down(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 7:  # Up-Right
            if rect.x < screen.get_width() - rect.width and rect.y > 0:
                move_right(rect)
                move_up(rect)
            else:
                item["direction"] = random.choice(directions)

        elif direction == 8:  # Up-Left
            if rect.x > 0 and rect.y > 0:
                move_left(rect)
                move_up(rect)
            else:
                item["direction"] = random.choice(directions)

def scores(scores_list=None) :
    # show scores     
    running = True 
    pygame.display.set_caption("Scores list")
    if(scores_list == None) :
        running = False
    
    start_btn = Button("restart game", (500 - 180)/2 , (400 - 50)/2 + 100 , 180, 40, game)

    while running :     
        screen.fill("black")
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

def game():
    running = True
    pygame.display.set_caption("random rock-paper-scissors")
    scissors_data = []
    paper_data = []
    rock_data = []
    names = ["Bouchra", "ikhlasse", "Mohamed", "Abdel","Ayman"]
    score_list = [{"name" :  elem  , "score" : 0} for  elem in names]
    # disqualified = [] 

    for i in range(0,len(names)):
        scissors_rect = pygame.Rect(
            
            random.randint(0, (screen.get_width() - scissors_width)/4),
            random.randint(0, (screen.get_height() - scissors_height)/4),
            scissors_width,
            scissors_height
        )
        paper_rect = pygame.Rect(
            random.randint((screen.get_width() - scissors_width)*3/4, screen.get_width() - paper.get_width()),
            random.randint((screen.get_height() - scissors_height)*3/4, screen.get_height() - paper.get_height()),
            paper.get_width(),
            paper.get_height()
        )
        rock_rect = pygame.Rect(
            random.randint(0, ( screen.get_width() - paper.get_width())*1/4),
            random.randint((screen.get_height() - scissors_height)*3/4, screen.get_height() - rock.get_height()),
            rock.get_width(),
            rock.get_height()
        )
        score = 0
        paper_data.append({"rect": paper_rect, "direction": random.choice(directions),"name" : f'{names[i]}', "score" : score})
        rock_data.append({"rect": rock_rect, "direction": random.choice(directions), "name": f'{names[i]}', "score" : score})
        scissors_data.append({"rect": scissors_rect, "direction": random.choice(directions),"name": f'{names[i]}', "score" : score})


    

    while running:
        scissors_count = len(scissors_data)
        papers_count = len(paper_data)
        rocks_count  =len(rock_data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for item in scissors_data:
            move(item)
            screen.blit(scissors, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        for item in paper_data:
            move(item)
            screen.blit(paper, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        for item in rock_data:
            move(item)
            screen.blit(rock, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        for paper_item in paper_data[:]:
            for rock_item in rock_data[:]:
                if paper_item["rect"].colliderect(rock_item["rect"]):
                    # disqualified.append(rock_item)
                    for elem in score_list : 
                        if elem["name"] == paper_item["name"] :
                            elem["score"] += 10
                            break

                    rock_data.remove(rock_item)
                    # paper_item["score"] += 10
                    break

        for rock_item in rock_data[:]:
            for scissor_item in scissors_data[:]:
                if rock_item["rect"].colliderect(scissor_item["rect"]):
                    # disqualified.append(scissor_item)
                    for elem in score_list : 
                        # if elem["name"] == scissor_item["name"] :
                        #     elem["score"] += scissor_item["score"]
                        #     break
                        if elem["name"] == rock_item["name"] : 
                            elem["score"] += 10
                    scissors_data.remove(scissor_item)
                    # rock_item["score"] += 10
                    break

        for scissor_item in scissors_data[:]:
            for paper_item in paper_data[:]:
                if scissor_item["rect"].colliderect(paper_item["rect"]):
                    # disqualified.append(paper_item)
                    for elem in score_list : 
                        if elem["name"] == scissor_item["name"] :
                            # elem["score"] += paper_item["score"]
                            elem["score"] += 10
                            break
                    paper_data.remove(paper_item)
                    # scissor_item['score'] += 10
                    break

        pygame.display.update()
        clock.tick(60)

        if(
            scissors_count * papers_count == 0 and rocks_count == 0 or 
            scissors_count * rocks_count == 0 and papers_count == 0 or 
            rocks_count * papers_count == 0 and scissors_count == 0) : 
            for elem in rock_data : 
                for score in score_list : 
                    if score["name"] == elem["name"] :
                        score["score"] = max(100, score["score"] * 10)

                # elem["score"] *= 10
            for elem in scissors_data : 
                for score in score_list : 
                    if score["name"] == elem["name"] :
                        score["score"] = max(100, score["score"] * 10)

                # elem["score"] *= 10
            for elem in paper_data : 
                for score in score_list : 
                    if score["name"] == elem["name"] :
                        score["score"] = max(100, score["score"] * 10)
                    # elem["score"] *= 10
            
            running = False
            scores(score_list)
  
    
    

def main():
    menu()
    pygame.quit()

if __name__ == "__main__":
    main()
