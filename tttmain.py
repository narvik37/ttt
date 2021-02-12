import pygame, sys
# from pygame.locals import *
# from tttAI import *

# # Define the colors we will use in RGB format
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
 
# # Set the height and width of the screen
# size  = [400,300]
# screen= pygame.display.set_mode(size)
  
# pygame.display.set_caption("Game Title")
  
# #Loop until the user clicks the close button.


clock= pygame.time.Clock()
fps = 30

width = 400
height = 300

center_x = width / 2
center_y = height / 2
box_size = 80
text_size = 50

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill(WHITE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        pygame.display.flip()

if __name__ == '__main__':
    main()

# menu

class Menu(object):
    #생성자 초기화
    def __init__(self, screen):
        self.font = pygame.font.Font('LexiGulim.ttf', 20)
        self.screen = screen
        self.draw_menu()
    #메뉴 그리기
    def draw_menu(self):
        x = center_x - width / 4
        self.new_btn = self.make_text('New Game', BLACK, WHITE, x, height-30)
        x = center_x + width / 4
        self.quit_btn = self.make_text('Quit Game', BLACK, WHITE, x, height-30)
    def result(self, msd_id):
        msg = {
            'X' : 'YOU LOST',
            'O' : 'YOU WIN',
            'draw' : 'DRAW',
        }
        self.make_text(msg[msg_id], BLUE, WHITE, center_x, 30)

    def make_text(self, text, color, bgcolor, cx, cy):
        mytext = self.font.render(text, True, color, bgcolor)
        rect = mytext.get_rect()
        rect.center = (cx, cy)
        self.screen.blit(mytext, rect)
        return rect
    
    def check_rect(self, pos):
        if self.new_btn.collidepoint(pos):
            return True
        elif self.quit_btn.collidepoint(pos):
            terminate()
        return False

    def is_continue(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    if(self.check_rect(event.pos)):
                        return
            pygame.display.update()
            clock.tick(fps)

# TTT
# run_game
# terminate

def terminate():
    pygame.quit()
    sys.exit()







