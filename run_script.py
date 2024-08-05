import threading


def start_script(setup_script, main_loop_script):
    t = threading.Thread(target=lambda: run_script(setup_script, main_loop_script))
    t.start()


def run_script(setup_script, main_loop_script):
    setup = setup_script
    main_loop = [f'    {i}\n' for i in main_loop_script.splitlines()]

    code = f'''
import sys
from sprite import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Pygame App")

{"".join(setup)}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

{"".join(main_loop)}

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()'''
    exec(code)
