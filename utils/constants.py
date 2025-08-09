import pygame 
pygame.font.init()
pygame.mixer.init()

WIDTH= 500
HIGHT = 400
screen = pygame.display.set_mode((WIDTH, HIGHT))
clock = pygame.time.Clock()

scissors = pygame.image.load("assets/media/scissors.png")
paper = pygame.image.load("assets/media/paper.png")
rock = pygame.image.load("assets/media/rock.png")



scissors_width = scissors.get_width()
scissors_height = scissors.get_height()
directions = [1, 2, 3, 4, 5, 6, 7, 8]

YELLOW = (255, 255, 0)
# FONT_16 = pygame.font.SysFont('consolas', 14)
# FONT_20 = pygame.font.SysFont('consolas', 18)
FONT_16 = pygame.font.Font("assets/font.ttf", 8)
FONT_20 = pygame.font.Font("assets/font.ttf", 12)

background = pygame.mixer.Sound('assets/sounds/fight-for-the-future.mp3')
hit = pygame.mixer.Sound('assets/sounds/hit.wav')
pick_sound = pygame.mixer.Sound('assets/sounds/pickup.wav')
show_pickup =  pygame.mixer.Sound('assets/sounds/show_pickup.wav')
bg_1 = pygame.image.load('assets/media/bg1.jpg')
bg_2 = pygame.image.load('assets/media/bg2.jpg')
bg_3 = pygame.image.load('assets/media/bg3.jpg')