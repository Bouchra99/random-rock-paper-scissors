import pygame
import random
from core.scores import scores
from utils.constants import screen, FONT_16, YELLOW, background, scissors, paper, rock, directions, clock, scissors_width, scissors_height,hit, bg_1
from utils.movement import move

def game():
    running = True
    background.play(-1)
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
        screen.blit(bg_1,(0,0))

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
                    hit.play()
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
                    hit.play()
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
                    hit.play()
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
            background.stop()
            scores(score_list)
  