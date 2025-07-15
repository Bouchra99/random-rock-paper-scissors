import pygame
import random
from utils.constants import screen, directions

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
