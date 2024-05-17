import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 30

#create game window
TARGET_RES = (1920, 1080)
SCREEN_SIZE = (1920, 1080)
SCREEN_SIZE = (1280, 720)

SCREEN_SCALE_FACTOR = (SCREEN_SIZE[0]/TARGET_RES[0])

screen = pygame.display.set_mode([SCREEN_SIZE[0], SCREEN_SIZE[1]])

pygame.display.set_caption("Parallax")

#define game variables
scroll = 0

ground_image = pygame.transform.rotozoom(pygame.image.load("ground.png").convert_alpha(), 0.0, SCREEN_SCALE_FACTOR)
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 4):
    bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
    for x in range (5):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed,0))
            speed += 0.2

def draw_ground():
    for x in range(15):
        screen.blit(ground_image, ((x * ground_width) - scroll * 2.2, SCREEN_SIZE[1] - ground_height))

#game loop
run = True
while run:
    clock.tick(FPS)

#draw world
    draw_bg()
    draw_ground()

    #get key presses
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

        #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()