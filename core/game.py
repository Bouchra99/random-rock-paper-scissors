import pygame
import random
from core.scores import scores
from utils.constants import (screen, FONT_16, YELLOW, background, scissors, paper, rock, 
                           directions, clock, scissors_width, scissors_height, hit, bg_2, bg_3)
from utils.movement import move
from utils.pickups import PickupManager


def game():
    running = True
    background.play(-1)
    pygame.display.set_caption("random rock-paper-scissors")
    scissors_data = []
    paper_data = []
    rock_data = []
    names = ["player 1", "player 2", "player 3", "player 4", "player 5"]
    score_list = [{"name": elem, "score": 0} for elem in names]
    pickup_manager = PickupManager()

    for i in range(0, len(names)):
        scissors_rect = pygame.Rect(
            random.randint(0, (screen.get_width() - scissors_width) // 4),
            random.randint(0, (screen.get_height() - scissors_height) // 4),
            scissors_width,
            scissors_height
        )
        paper_rect = pygame.Rect(
            random.randint((screen.get_width() - scissors_width) * 3 // 4, 
                          screen.get_width() - paper.get_width()),
            random.randint((screen.get_height() - scissors_height) * 3 // 4, 
                          screen.get_height() - paper.get_height()),
            paper.get_width(),
            paper.get_height()
        )
        rock_rect = pygame.Rect(
            random.randint(0, (screen.get_width() - paper.get_width()) // 4),
            random.randint((screen.get_height() - scissors_height) * 3 // 4, 
                          screen.get_height() - rock.get_height()),
            rock.get_width(),
            rock.get_height()
        )
        score = 0
        paper_data.append({"rect": paper_rect, "direction": random.choice(directions), 
                          "name": f'{names[i]}', "score": score})
        rock_data.append({"rect": rock_rect, "direction": random.choice(directions), 
                         "name": f'{names[i]}', "score": score})
        scissors_data.append({"rect": scissors_rect, "direction": random.choice(directions), 
                             "name": f'{names[i]}', "score": score})

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scissors_count = len(scissors_data)
        papers_count = len(paper_data)
        rocks_count = len(rock_data)

        current_time = pygame.time.get_ticks()
        pickup_manager.update(current_time)

        screen.fill("black")
        screen.blit(bg_3, (0, 0))

        # Check for pickup collisions
        game_objects = [scissors_data, paper_data, rock_data]
        pickup_manager.check_collisions(game_objects)
        
        clone_effects = pickup_manager.get_clone_effects()
        for clone_effect in clone_effects:
            target = clone_effect['target']
            # Determine which list the target belongs to and create a clone
            clone_rect = pygame.Rect(
                max(0, min(target["rect"].x + random.randint(-50, 50), 
                          screen.get_width() - target["rect"].width)),
                max(0, min(target["rect"].y + random.randint(-50, 50), 
                          screen.get_height() - target["rect"].height)),
                target["rect"].width,
                target["rect"].height
            )
            
            new_clone = {
                "rect": clone_rect,
                "direction": random.choice(directions),
                "name": target["name"],
                "score": 0
            }
            
            # Add clone to the appropriate list based on object type
            # We'll determine this by checking rect size
            if target["rect"].width == scissors_width and target["rect"].height == scissors_height:
                scissors_data.append(new_clone)
            elif target["rect"].width == paper.get_width():
                paper_data.append(new_clone)
            else:  
                rock_data.append(new_clone)

        for item in scissors_data:
            if not pickup_manager.is_frozen(item["name"], current_time):
                move(item)
            screen.blit(scissors, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        for item in paper_data:
            if not pickup_manager.is_frozen(item["name"], current_time):
                move(item)
            screen.blit(paper, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        for item in rock_data:
            if not pickup_manager.is_frozen(item["name"], current_time):
                move(item)
            screen.blit(rock, item["rect"])
            text = FONT_16.render(item["name"], True, YELLOW)
            text_rect = text.get_rect(midbottom=item["rect"].midtop)
            screen.blit(text, text_rect)

        pickup_manager.draw(screen)

        for paper_item in paper_data[:]:
            for rock_item in rock_data[:]:
                if paper_item["rect"].colliderect(rock_item["rect"]):
                    hit.play()
                    for elem in score_list:
                        if elem["name"] == paper_item["name"]:
                            elem["score"] += 10
                            break
                    rock_data.remove(rock_item)
                    break

        for rock_item in rock_data[:]:
            for scissor_item in scissors_data[:]:
                if rock_item["rect"].colliderect(scissor_item["rect"]):
                    hit.play()
                    for elem in score_list:
                        if elem["name"] == rock_item["name"]:
                            elem["score"] += 10
                            break
                    scissors_data.remove(scissor_item)
                    break

        for scissor_item in scissors_data[:]:
            for paper_item in paper_data[:]:
                if scissor_item["rect"].colliderect(paper_item["rect"]):
                    hit.play()
                    for elem in score_list:
                        if elem["name"] == scissor_item["name"]:
                            elem["score"] += 10
                            break
                    paper_data.remove(paper_item)
                    break

        pygame.display.update()
        clock.tick(60)

        # Check for game end conditions
        if (scissors_count * papers_count == 0 and rocks_count == 0 or 
            scissors_count * rocks_count == 0 and papers_count == 0 or 
            rocks_count * papers_count == 0 and scissors_count == 0):
            
            # Bonus points for survivors
            for elem in rock_data:
                for score in score_list:
                    if score["name"] == elem["name"]:
                        score["score"] = max(100, score["score"] * 10)

            for elem in scissors_data:
                for score in score_list:
                    if score["name"] == elem["name"]:
                        score["score"] = max(100, score["score"] * 10)

            for elem in paper_data:
                for score in score_list:
                    if score["name"] == elem["name"]:
                        score["score"] = max(100, score["score"] * 10)
            
            running = False
            background.stop()
            scores(score_list)