import pygame

def bouncing_rect():
    global x1_speed, y1_speed, x2_speed,y2_speed
    moving_rect1.x+=x1_speed
    moving_rect1.y+=y1_speed
    moving_rect2.x += x2_speed
    moving_rect2.y += y2_speed

    # Colisão com as bordas da janela

    if moving_rect1.right >= win_w or moving_rect1.left <= 0:
        x1_speed *= -1
    if moving_rect1.bottom >= win_h or moving_rect1.top <= 0:
        y1_speed *= -1

    if moving_rect2.right >= win_w or moving_rect2.left <= 0:
        x2_speed *= -1
    if moving_rect2.bottom >= win_h or moving_rect2.top <= 0:
        y2_speed *= -1


    #
    collision_tolerance = 10
    if moving_rect1.colliderect(moving_rect2):
        if abs(moving_rect2.top - moving_rect1.bottom) < collision_tolerance or abs(
                moving_rect2.bottom - moving_rect1.top) < collision_tolerance < 0:
            y1_speed *= -1
        if abs(moving_rect2.right - moving_rect1.left) and x1_speed > 0 or abs(
                moving_rect2.left - moving_rect1.right) and x1_speed < 0:
            x1_speed *= -1
    #


    # Colisão entre retângulos
    collision_tolerance = 10
    if moving_rect1.colliderect(moving_rect2):
        if abs(moving_rect2.top - moving_rect1.bottom) < collision_tolerance and y1_speed > 0 or abs(moving_rect2.bottom - moving_rect1.top) < collision_tolerance and y1_speed < 0:
            y1_speed *= -1
        if abs(moving_rect2.right - moving_rect1.left) < collision_tolerance and x1_speed < 0 or abs(moving_rect2.left - moving_rect1.right) < collision_tolerance and x1_speed > 0:
            x1_speed *= -1

    if moving_rect2.colliderect(moving_rect1):
        if abs(moving_rect1.top - moving_rect2.bottom) < collision_tolerance and y2_speed > 0 or abs(moving_rect1.bottom - moving_rect2.top) < collision_tolerance and y2_speed > 0:
            y2_speed *= -1
        if abs(moving_rect1.right - moving_rect2.left) < collision_tolerance and x2_speed < 0 or abs(moving_rect1.left - moving_rect2.right) < collision_tolerance and x2_speed > 0:
            x2_speed *= -1




    pygame.draw.rect(win, 'Magenta', moving_rect1)
    pygame.draw.rect(win, 'Red', moving_rect2)



pygame.init()
clock = pygame.time.Clock()
win_w,win_h=800,800
win=pygame.display.set_mode((win_w,win_h))


x1,y1=100,100
moving_rect1 = pygame.Rect(350,350,x1,y1)
x1_speed,y1_speed=5,4
speed1 = pygame.math.Vector2(x1_speed,y1_speed)

x2,y2=200,100
moving_rect2 = pygame.Rect(300,600,x2,y2)
x2_speed,y2_speed=2,2
speed2 = pygame.math.Vector2(x2_speed,y2_speed)


run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((30,30,30))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)