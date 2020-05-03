# Seats are controlled with 1,2,3,4 keys as a toggle. Grey is a ready table, green is sat and red is dirty
# seats are grey when they are empty and black when they are filled. SPACEBAR will reset the table when it
# goes dirty and wont allow seating.
#
#
import pygame

bg_color = (231,254,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (211,211,211)
GREEN = (0,128,0)
RED = (134,1,17)


class Seat(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.sat = False


    def update(self):
        if self.sat:
            self.image.fill(BLACK)
        if not self.sat:
            self.image.fill((GREY))

class Table(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90, 160))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.status = "ready"

    def update(self):
        if table.status == "ready":
            self.image.fill(GREY)
        if self.status == "sat":
            self.image.fill(GREEN)
        if self.status == "dirty":
            self.image.fill(RED)





pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Dining Room")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
seat1 = Seat(160,340)
all_sprites.add(seat1)
seat2 = Seat(160, 260)
all_sprites.add(seat2)
seat3 = Seat(320, 260)
all_sprites.add(seat3)
seat4 = Seat(320, 340)
all_sprites.add(seat4)

table = Table(240,300)
all_sprites.add(table)

seat_sprites = pygame.sprite.Group()
seat_sprites.add(seat1)
seat_sprites.add(seat2)
seat_sprites.add(seat3)
seat_sprites.add(seat4)

#game loop
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            #seat 1 (bottom left)
            #if event.key == pygame.K_1 and table.status != "dirty":
            if event.key == pygame.K_1 and table.status != "dirty":
                if not seat1.sat:
                    seat1.sat = True
                else:
                    seat1.sat = False



            #seat 2 (Top Left)
            if event.key == pygame.K_2 and table.status != "dirty":
                if not seat2.sat:
                    seat2.sat = True
                else:
                    seat2.sat = False

            #seat 3 (Top Right)
            if event.key == pygame.K_3 and table.status != "dirty":
                if not seat3.sat:
                    seat3.sat = True
                else:
                    seat3.sat = False

            #seat 4 (bottom right)
            if event.key == pygame.K_4 and table.status != "dirty":
                if not seat4.sat:
                    seat4.sat = True
                else:
                    seat4.sat = False

            if event.key == pygame.K_SPACE:
                for seat in seat_sprites:
                    seat.sat = False
                    if table.status == "dirty":
                        table.status = "ready"


            filled_seats = 0
            for seat in seat_sprites:
                if seat.sat:
                    filled_seats += 1
                    table.status = "sat"
                elif table.status == "sat" and filled_seats == 0:
                    table.status = "dirty"







    #update
    all_sprites.update()

    #draw
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()