import pygame


pygame.init()

window = pygame.display.set_mode([500,500])
pygame.display.set_caption("Dining Room")
bg_color = (231,254,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (211,211,211)
GREEN = (0,128,0)
RED = (134,1,17)


seat_list = None

running = True



def redraw():
    window.fill((bg_color))  # background color

    tabletop = pygame.sprite.Sprite
    tabletop.status = "ready"

    if tabletop.status == "ready":
        pygame.draw.rect(window, GREY, (180, 180, 90, 160))
    if tabletop.status == "sat":
        pygame.draw.rect(window,GREEN,(180,180,90,160))
    if tabletop.status == "dirty":
        pygame.draw.rect(window, RED, (180, 180, 90, 160))


    seat1 = pygame.sprite.Sprite
    seat1.status = "empty"
    if seat1.status == "full":
        pygame.draw.rect(window,BLACK,(120, 280,40,40))
    pygame.draw.rect(window,GREY,(120, 280,40,40),2)

    seat2 = pygame.sprite.Sprite
    seat2.status = "empty"
    if seat2.status == "full":
        pygame.draw.rect(window,BLACK,(120, 200,40,40))
    pygame.draw.rect(window, GREY, (120, 200, 40, 40), 2)

    seat3 = pygame.sprite.Sprite
    seat3.status = "empty"
    if seat3.status == "full":
        pygame.draw.rect(window,BLACK,(290, 200,40,40))
    pygame.draw.rect(window, GREY, (290, 200, 40, 40), 2)

    seat4 = pygame.sprite.Sprite
    seat4.status = "full"
    if seat4.status == "full":
        pygame.draw.rect(window,BLACK,(290,280,40,40))
    pygame.draw.rect(window, GREY, (290, 280, 40, 40), 2)


    seat_list = []

    seat_list.append(seat1)
    seat_list.append(seat2)
    seat_list.append(seat3)
    seat_list.append(seat4)

    for seat in seat_list:
        if seat.status=="full":
            tabletop.sat = True

    pygame.display.update()


# main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        seat_list[0].sat = True
    #if keys[pygame.K_2]:
        #seat 2 has person
    #if keys[pygame.K_3]:
        #seat 3 has person
    #if keys[pygame.K_4]:
        #seat 4 has person

    redraw()

pygame.quit()

