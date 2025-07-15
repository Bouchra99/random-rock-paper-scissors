import pygame

from core.menu import menu

pygame.init()
pygame.display.set_caption("menu")


def main():
    menu()
    pygame.quit()

if __name__ == "__main__":
    main()
