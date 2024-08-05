
def run_script(setup_script, main_loop_script):
    print(setup_script)
    print(main_loop_script)
    setup = setup_script
    main_loop = [f'    {i}' for i in main_loop_script.splitlines()]

    print(''.join(main_loop))

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
