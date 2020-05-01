import arcade
import math

# measurements to help easier drawing
center_to_center = 110
radius = 80
sin_cos_45 = math.sin(math.radians(45))
seat_offset = center_to_center * sin_cos_45


class dining_room(arcade.Window):

    def __init__(self):
        super().__init__(width=1000, height=500, title="Dining Room")
        self.set_location(50,50)
        arcade.set_background_color(arcade.color.BUBBLES)

        self.table_list = None
        self.table1_seats_list = None
        self.table2_seats_list = None
        self.table3_seats_list = None
        self.table4_seats_list = None
        self.table5_seats_list = None

    def setup(self):
        self.table_list = arcade.SpriteList()
        self.table1_seats_list = arcade.SpriteList()
        self.table2_seats_list = arcade.SpriteList()
        self.table3_seats_list = arcade.SpriteList()
        self.table4_seats_list = arcade.SpriteList()
        self.table5_seats_list = arcade.SpriteList()

        # TABLE 1 - BOTTOM LEFT
        table1_sprite = arcade.Sprite("sprites/table.png")
        table1_sprite.num = 1
        table1_sprite.center_x = 200
        table1_sprite.center_y = 125
        table1_sprite.width = 90
        table1_sprite.height = 150
        table1_sprite.status = "ready"
        table1_sprite.alpha = 50
        self.table_list.append(table1_sprite)

        seat1_1 = arcade.Sprite("sprites/face.png")
        seat1_1.center_x = 125
        seat1_1.center_y = 90
        seat1_1.width = 35
        seat1_1.height = 35
        seat1_1.alpha = 25
        seat1_1.sat = False
        self.table1_seats_list.append(seat1_1)

        seat1_2 = arcade.Sprite("sprites/face.png")
        seat1_2.center_x = 125
        seat1_2.center_y = 160
        seat1_2.width = 35
        seat1_2.height = 35
        seat1_2.alpha = 25
        seat1_2.sat = False
        self.table1_seats_list.append(seat1_2)

        seat1_3 = arcade.Sprite("sprites/face.png")
        seat1_3.center_x = 275
        seat1_3.center_y = 160
        seat1_3.width = 35
        seat1_3.height = 35
        seat1_3.alpha = 25
        seat1_3.sat = False
        self.table1_seats_list.append(seat1_3)

        seat1_4 = arcade.Sprite("sprites/face.png")
        seat1_4.center_x = 275
        seat1_4.center_y = 90
        seat1_4.width = 35
        seat1_4.height = 35
        seat1_4.alpha = 25
        seat1_4.sat = False
        self.table1_seats_list.append(seat1_4)

        # TABLE 2 - top LEFT
        table2_sprite = arcade.Sprite("sprites/table.png")
        table2_sprite.num = 2
        table2_sprite.center_x = 200
        table2_sprite.center_y = 350
        table2_sprite.width = 90
        table2_sprite.height = 150
        table2_sprite.status = "ready"
        table2_sprite.alpha = 50
        self.table_list.append(table2_sprite)

        seat2_1 = arcade.Sprite("sprites/face.png")
        seat2_1.center_x = 125
        seat2_1.center_y = 315
        seat2_1.width = 35
        seat2_1.height = 35
        seat2_1.alpha = 25
        seat2_1.sat = False
        self.table2_seats_list.append(seat2_1)

        seat2_2 = arcade.Sprite("sprites/face.png")
        seat2_2.center_x = 125
        seat2_2.center_y = 386
        seat2_2.width = 35
        seat2_2.height = 35
        seat2_2.alpha = 25
        seat2_2.sat = False
        self.table2_seats_list.append(seat2_2)

        seat2_3 = arcade.Sprite("sprites/face.png")
        seat2_3.center_x = 275
        seat2_3.center_y = 385
        seat2_3.width = 35
        seat2_3.height = 35
        seat2_3.alpha = 25
        seat2_3.sat = False
        self.table2_seats_list.append(seat2_3)

        seat2_4 = arcade.Sprite("sprites/face.png")
        seat2_4.center_x = 275
        seat2_4.center_y = 315
        seat2_4.width = 35
        seat2_4.height = 35
        seat2_4.alpha = 25
        seat2_4.sat = False
        self.table2_seats_list.append(seat2_4)

        #Table 3 - Center Round
        table3_sprite = arcade.Sprite("sprites/round_tab.png")
        table3_sprite.num = 3
        table3_sprite.color = arcade.color.LIGHT_BROWN
        table3_sprite.center_x = 500
        table3_sprite.center_y = 200
        table3_sprite.width = 190
        table3_sprite.height = 250
        table3_sprite.status = "ready"
        table3_sprite.alpha = 50
        self.table_list.append(table3_sprite)

        seat3_1 = arcade.Sprite("sprites/face.png")
        seat3_1.center_x = 500
        seat3_1.center_y = 200 + center_to_center
        seat3_1.width = 35
        seat3_1.height = 35
        seat3_1.alpha = 25
        seat3_1.sat = False
        self.table3_seats_list.append(seat3_1)

        seat3_2 = arcade.Sprite("sprites/face.png")
        seat3_2.center_x = 500 + seat_offset
        seat3_2.center_y = 200 +seat_offset
        seat3_2.width = 35
        seat3_2.height = 35
        seat3_2.alpha = 25
        seat3_2.sat = False
        self.table3_seats_list.append(seat3_2)

        seat3_3 = arcade.Sprite("sprites/face.png")
        seat3_3.center_x = 500 + center_to_center
        seat3_3.center_y = 200
        seat3_3.width = 35
        seat3_3.height = 35
        seat3_3.alpha = 25
        seat3_3.sat = False
        self.table3_seats_list.append(seat3_3)

        seat3_4 = arcade.Sprite("sprites/face.png")
        seat3_4.center_x = 500 + seat_offset
        seat3_4.center_y = 200 - seat_offset
        seat3_4.width = 35
        seat3_4.height = 35
        seat3_4.alpha = 25
        seat3_4.sat = False
        self.table3_seats_list.append(seat3_4)

        seat3_5 = arcade.Sprite("sprites/face.png")
        seat3_5.center_x = 500
        seat3_5.center_y = 200 - center_to_center
        seat3_5.width = 35
        seat3_5.height = 35
        seat3_5.alpha = 25
        seat3_5.sat = False
        self.table3_seats_list.append(seat3_5)

        seat3_6 = arcade.Sprite("sprites/face.png")
        seat3_6.center_x = 500 - seat_offset
        seat3_6.center_y = 200 - seat_offset
        seat3_6.width = 35
        seat3_6.height = 35
        seat3_6.alpha = 25
        seat3_6.sat = False
        self.table3_seats_list.append(seat3_6)

        seat3_7 = arcade.Sprite("sprites/face.png")
        seat3_7.center_x = 500 - center_to_center
        seat3_7.center_y = 200
        seat3_7.width = 35
        seat3_7.height = 35
        seat3_7.alpha = 25
        seat3_7.sat = False
        self.table3_seats_list.append(seat3_7)

        seat3_8 = arcade.Sprite("sprites/face.png")
        seat3_8.center_x = 500 - seat_offset
        seat3_8.center_y = 200 + seat_offset
        seat3_8.width = 35
        seat3_8.height = 35
        seat3_8.alpha = 25
        seat3_8.sat = False
        self.table3_seats_list.append(seat3_8)


        # TABLE 4 Top Right
        table4_sprite = arcade.Sprite("sprites/table.png")
        table4_sprite.num = 4
        table4_sprite.center_x = 800
        table4_sprite.center_y = 350
        table4_sprite.width = 90
        table4_sprite.height = 150
        table4_sprite.status = "ready"
        table4_sprite.alpha = 50
        self.table_list.append(table4_sprite)

        seat4_1 = arcade.Sprite("sprites/face.png")
        seat4_1.center_x = 725
        seat4_1.center_y = 315
        seat4_1.width = 35
        seat4_1.height = 35
        seat4_1.alpha = 25
        seat4_1.sat = False
        self.table4_seats_list.append(seat4_1)

        seat4_2 = arcade.Sprite("sprites/face.png")
        seat4_2.center_x = 725
        seat4_2.center_y = 386
        seat4_2.width = 35
        seat4_2.height = 35
        seat4_2.alpha = 25
        seat4_2.sat = False
        self.table4_seats_list.append(seat4_2)

        seat4_3 = arcade.Sprite("sprites/face.png")
        seat4_3.center_x = 875
        seat4_3.center_y = 385
        seat4_3.width = 35
        seat4_3.height = 35
        seat4_3.alpha = 25
        seat4_3.sat = False
        self.table4_seats_list.append(seat4_3)

        seat4_4 = arcade.Sprite("sprites/face.png")
        seat4_4.center_x = 875
        seat4_4.center_y = 315
        seat4_4.width = 35
        seat4_4.height = 35
        seat4_4.alpha = 25
        seat4_4.sat = False
        self.table4_seats_list.append(seat4_4)

        #Table 5- Bottom Right
        table5_sprite = arcade.Sprite("sprites/table.png")
        table5_sprite.num = 5
        table5_sprite.center_x = 800
        table5_sprite.center_y = 125
        table5_sprite.width = 90
        table5_sprite.height = 150
        table5_sprite.status = "ready"
        table5_sprite.alpha = 50
        self.table_list.append(table5_sprite)

        seat5_1 = arcade.Sprite("sprites/face.png")
        seat5_1.center_x = 725
        seat5_1.center_y = 90
        seat5_1.width = 35
        seat5_1.height = 35
        seat5_1.alpha = 25
        seat5_1.sat = False
        self.table5_seats_list.append(seat5_1)

        seat5_2 = arcade.Sprite("sprites/face.png")
        seat5_2.center_x = 725
        seat5_2.center_y = 160
        seat5_2.width = 35
        seat5_2.height = 35
        seat5_2.alpha = 25
        seat5_2.sat = False
        self.table5_seats_list.append(seat5_2)

        seat5_3 = arcade.Sprite("sprites/face.png")
        seat5_3.center_x = 875
        seat5_3.center_y = 160
        seat5_3.width = 35
        seat5_3.height = 35
        seat5_3.alpha = 25
        seat5_3.sat = False
        self.table5_seats_list.append(seat5_3)

        seat5_4 = arcade.Sprite("sprites/face.png")
        seat5_4.center_x = 875
        seat5_4.center_y = 90
        seat5_4.width = 35
        seat5_4.height = 35
        seat5_4.alpha = 25
        seat5_4.sat = False
        self.table5_seats_list.append(seat5_4)




    def on_draw(self):
        arcade.start_render()
        self.table_list.draw()
        self.table1_seats_list.draw()
        self.table2_seats_list.draw()
        self.table3_seats_list.draw()
        self.table4_seats_list.draw()
        self.table5_seats_list.draw()

        for table in self.table_list:
            #prevents square outline for table 3
            if table != self.table_list[2]:

                if table.status == "dirty":
                    # red box for bussers attention
                    arcade.draw_lrtb_rectangle_outline(table.center_x - table.width // 2,
                                                       table.center_x + table.width // 2,
                                                       table.center_y + table.height // 2,
                                                       table.center_y - table.height // 2,
                                                       arcade.color.RED, 10)
                    # top left to bottom right
                    arcade.draw_line(table.center_x-table.width // 2, table.center_y + table.height // 2,
                                     table.center_x + table.width // 2, table.center_y - table.height // 2,
                                     arcade.color.RED,10)
                    # bottom left to top right
                    arcade.draw_line(table.center_x-table.width // 2, table.center_y - table.height // 2,
                                     table.center_x + table.width // 2, table.center_y + table.height // 2,
                                     arcade.color.RED,10)

                # table name/number label
                arcade.draw_text("TABLE %d" % table.num, table.center_x -25, table.center_y +80, arcade.color.BLACK)
                # table outline
                arcade.draw_lrtb_rectangle_outline(table.center_x - table.width // 2,
                                                   table.center_x + table.width // 2,
                                                   table.center_y + table.height // 2,
                                                   table.center_y - table.height // 2,
                                                   arcade.color.BLACK,2)

                # seat 1 (bottom left)
                arcade.draw_rectangle_outline(table.center_x - table.width//2 - 30, table.center_y - 35,40,40,arcade.color.BLACK, 2)
                # seat 2 (top left)
                arcade.draw_rectangle_outline(table.center_x - table.width//2 - 30, table.center_y + 35,40,40, arcade.color.BLACK, 2)
                # seat 3 (top right)
                arcade.draw_rectangle_outline(table.center_x + table.width//2 + 30, table.center_y + 35,40,40, arcade.color.BLACK, 2)
                # seat 4 (bottom right)
                arcade.draw_rectangle_outline(table.center_x + table.width//2 + 30, table.center_y - 35,40,40, arcade.color.BLACK, 2)

            #custom shapes for round table
            else:
                if table.status == "dirty":
                    arcade.draw_circle_outline(table.center_x, table.center_y, table.width//2-15, arcade.color.RED, 10, 50)
                    arcade.draw_line(table.center_x - radius*math.cos(math.radians(45)), table.center_y +
                                     radius*math.cos(math.radians(45)),table.center_x + radius*math.cos(math.radians(45)),
                                     table.center_y - radius*math.cos(math.radians(45)), arcade.color.RED, 10)
                    arcade.draw_line(table.center_x - radius*math.cos(math.radians(45)), table.center_y -
                                     radius*math.cos(math.radians(45)),table.center_x + radius*math.cos(math.radians(45)),
                                     table.center_y + radius*math.cos(math.radians(45)), arcade.color.RED, 10)

                arcade.draw_circle_outline(table.center_x,table.center_y, 80, arcade.color.BLACK,2)
                arcade.draw_text("TABLE %d" % table.num, table.center_x -25, table.center_y +140, arcade.color.BLACK)



                #seat 1 (TOP - 12 o clock)
                arcade.draw_rectangle_outline(table.center_x, table.center_y + center_to_center, 40,40,
                                              arcade.color.BLACK,2)
                #seat 2 (top right)
                arcade.draw_rectangle_outline(table.center_x + seat_offset, table.center_y +seat_offset, 40, 40,
                                              arcade.color.BLACK, 2,45)
                #seat 3 (RIGHT - 3 o clock)
                arcade.draw_rectangle_outline(table.center_x + center_to_center, table.center_y, 40,40,
                                              arcade.color.BLACK,2)
                # seat 4 (bottom right)
                arcade.draw_rectangle_outline(table.center_x + seat_offset, table.center_y - seat_offset, 40, 40,
                                              arcade.color.BLACK, 2, 45)
                # seat 5 (BOTTOM - 6 o clock)
                arcade.draw_rectangle_outline(table.center_x, table.center_y - center_to_center, 40, 40,
                                              arcade.color.BLACK, 2)
                # seat 6 (bottom left)
                arcade.draw_rectangle_outline(table.center_x - seat_offset, table.center_y - seat_offset, 40, 40,
                                              arcade.color.BLACK, 2, 45)
                # seat 7 (LEFT - 9 o clock)
                arcade.draw_rectangle_outline(table.center_x - center_to_center, table.center_y, 40, 40,
                                              arcade.color.BLACK, 2)
                # seat 8 (top left)
                arcade.draw_rectangle_outline(table.center_x - seat_offset, table.center_y + seat_offset, 40,40,
                                              arcade.color.BLACK, 2,45)

    def on_update(self, delta_time: float):
        self.table_list.update()
        self.table1_seats_list.update()
        self.table2_seats_list.update()
        self.table3_seats_list.update()
        self.table4_seats_list.update()
        self.table5_seats_list.update()

        #Table1
        #lights up table sprite if at least one seat is sat in
        for seats in self.table1_seats_list:
            #someone is in a chair so the table is sat at
            if seats.sat and self.table_list[0].status == "ready":
                self.table_list[0].status = "sat"
                self.table_list[0].alpha = 255

        #Table 2 sprite
        for seats in self.table2_seats_list:
            if seats.sat and self.table_list[1].status == "ready":
                self.table_list[1].status = "sat"
                self.table_list[1].alpha = 255

        #Table 3 sprite
        for seats in self.table3_seats_list:
            if seats.sat and self.table_list[2].status == "ready":
                self.table_list[2].status = "sat"
                self.table_list[2].alpha = 255

        #Table 4 sprite
        for seats in self.table4_seats_list:
            if seats.sat and self.table_list[3].status == "ready":
                self.table_list[3].status = "sat"
                self.table_list[3].alpha = 255

        #Table 5 sprite
        for seats in self.table5_seats_list:
            if seats.sat and self.table_list[4].status == "ready":
                self.table_list[4].status = "sat"
                self.table_list[4].alpha = 255

        #if the table goes from sat in to empty it will turn to dirty
        #Table 1
        empty_seats_1 = 0
        for seats in self.table1_seats_list:
            if not seats.sat:
                empty_seats_1 += 1
        if empty_seats_1 == 4 and self.table_list[0].status == "sat":
            self.table_list[0].status = "dirty"

        #table 2
        empty_seats_2 = 0
        for seats in self.table2_seats_list:
            if not seats.sat:
                empty_seats_2 += 1
        if empty_seats_2 == 4 and self.table_list[1].status == "sat":
            self.table_list[1].status = "dirty"

        #Table 3
        empty_seats_3 = 0
        for seats in self.table3_seats_list:
            if not seats.sat:
                empty_seats_3 += 1
        if empty_seats_3 == 8 and self.table_list[2].status == "sat":
            self.table_list[2].status = "dirty"

        #table 4
        empty_seats_4 = 0
        for seats in self.table4_seats_list:
            if not seats.sat:
                empty_seats_4 += 1
        if empty_seats_4 == 4 and self.table_list[3].status == "sat":
            self.table_list[3].status = "dirty"

        #table 5
        empty_seats_5 = 0
        for seats in self.table5_seats_list:
            if not seats.sat:
                empty_seats_5 += 1
        if empty_seats_5 == 4 and self.table_list[4].status == "sat":
            self.table_list[4].status = "dirty"

    def on_key_press(self, symbol: int, modifiers: int):
            if not modifiers & arcade.key.MOD_SHIFT:

                #Table 1 Keys
                # toggles seat n at list [n-1], not "dirty" used to prevent patrons sitting at dirty tables
                if symbol == arcade.key.KEY_1:
                    if not self.table1_seats_list[0].sat and not self.table_list[0].status =="dirty":
                        self.table1_seats_list[0].sat = True
                        self.table1_seats_list[0].alpha = 255
                    elif self.table1_seats_list[0].sat:
                        self.table1_seats_list[0].sat = False
                        self.table1_seats_list[0].alpha = 25
                if symbol == arcade.key.KEY_2:
                    if not self.table1_seats_list[1].sat and not self.table_list[0].status == "dirty":
                        self.table1_seats_list[1].sat = True
                        self.table1_seats_list[1].alpha = 255
                    elif self.table1_seats_list[1].sat:
                        self.table1_seats_list[1].sat = False
                        self.table1_seats_list[1].alpha = 25
                if symbol == arcade.key.KEY_3:
                    if not self.table1_seats_list[2].sat and not self.table_list[0].status == "dirty":
                        self.table1_seats_list[2].sat = True
                        self.table1_seats_list[2].alpha = 255
                    elif self.table1_seats_list[2].sat:
                        self.table1_seats_list[2].sat = False
                        self.table1_seats_list[2].alpha = 25
                if symbol == arcade.key.KEY_4:
                    if not self.table1_seats_list[3].sat and not self.table_list[0].status == "dirty":
                        self.table1_seats_list[3].sat = True
                        self.table1_seats_list[3].alpha = 255
                    elif self.table1_seats_list[3].sat:
                        self.table1_seats_list[3].sat = False
                        self.table1_seats_list[3].alpha = 25

                #Table 2 keys
                if symbol == arcade.key.KEY_5:
                    if not self.table2_seats_list[0].sat and not self.table_list[1].status =="dirty":
                        self.table2_seats_list[0].sat = True
                        self.table2_seats_list[0].alpha = 255
                    elif self.table2_seats_list[0].sat:
                        self.table2_seats_list[0].sat = False
                        self.table2_seats_list[0].alpha = 25
                if symbol == arcade.key.KEY_6:
                    if not self.table2_seats_list[1].sat and not self.table_list[1].status == "dirty":
                        self.table2_seats_list[1].sat = True
                        self.table2_seats_list[1].alpha = 255
                    elif self.table2_seats_list[1].sat:
                        self.table2_seats_list[1].sat = False
                        self.table2_seats_list[1].alpha = 25
                if symbol == arcade.key.KEY_7:
                    if not self.table2_seats_list[2].sat and not self.table_list[1].status == "dirty":
                        self.table2_seats_list[2].sat = True
                        self.table2_seats_list[2].alpha = 255
                    elif self.table2_seats_list[2].sat:
                        self.table2_seats_list[2].sat = False
                        self.table2_seats_list[2].alpha = 25
                if symbol == arcade.key.KEY_8:
                    if not self.table2_seats_list[3].sat and not self.table_list[1].status == "dirty":
                        self.table2_seats_list[3].sat = True
                        self.table2_seats_list[3].alpha = 255
                    elif self.table2_seats_list[3].sat:
                        self.table2_seats_list[3].sat = False
                        self.table2_seats_list[3].alpha = 25

                #table 3 keys
                if symbol == arcade.key.Z:
                    if not self.table3_seats_list[0].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[0].sat = True
                        self.table3_seats_list[0].alpha = 255
                    elif self.table3_seats_list[0].sat:
                        self.table3_seats_list[0].sat = False
                        self.table3_seats_list[0].alpha = 25
                if symbol == arcade.key.X:
                    if not self.table3_seats_list[1].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[1].sat = True
                        self.table3_seats_list[1].alpha = 255
                    elif self.table3_seats_list[1].sat:
                        self.table3_seats_list[1].sat = False
                        self.table3_seats_list[1].alpha = 25
                if symbol == arcade.key.C:
                    if not self.table3_seats_list[2].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[2].sat = True
                        self.table3_seats_list[2].alpha = 255
                    elif self.table3_seats_list[2].sat:
                        self.table3_seats_list[2].sat = False
                        self.table3_seats_list[2].alpha = 25
                if symbol == arcade.key.V:
                    if not self.table3_seats_list[3].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[3].sat = True
                        self.table3_seats_list[3].alpha = 255
                    elif self.table3_seats_list[3].sat:
                        self.table3_seats_list[3].sat = False
                        self.table3_seats_list[3].alpha = 25
                if symbol == arcade.key.B:
                    if not self.table3_seats_list[4].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[4].sat = True
                        self.table3_seats_list[4].alpha = 255
                    elif self.table3_seats_list[4].sat:
                        self.table3_seats_list[4].sat = False
                        self.table3_seats_list[4].alpha = 25
                if symbol == arcade.key.N:
                    if not self.table3_seats_list[5].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[5].sat = True
                        self.table3_seats_list[5].alpha = 255
                    elif self.table3_seats_list[5].sat:
                        self.table3_seats_list[5].sat = False
                        self.table3_seats_list[5].alpha = 25
                if symbol == arcade.key.M:
                    if not self.table3_seats_list[6].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[6].sat = True
                        self.table3_seats_list[6].alpha = 255
                    elif self.table3_seats_list[6].sat:
                        self.table3_seats_list[6].sat = False
                        self.table3_seats_list[6].alpha = 25
                if symbol == arcade.key.COMMA:
                    if not self.table3_seats_list[7].sat and not self.table_list[2].status == "dirty":
                        self.table3_seats_list[7].sat = True
                        self.table3_seats_list[7].alpha = 255
                    elif self.table3_seats_list[7].sat:
                        self.table3_seats_list[7].sat = False
                        self.table3_seats_list[7].alpha = 25

                #Table 4 Keys
                if symbol == arcade.key.Q:
                    if not self.table4_seats_list[0].sat and not self.table_list[3].status =="dirty":
                        self.table4_seats_list[0].sat = True
                        self.table4_seats_list[0].alpha = 255
                    elif self.table4_seats_list[0].sat:
                        self.table4_seats_list[0].sat = False
                        self.table4_seats_list[0].alpha = 25
                if symbol == arcade.key.W:
                    if not self.table4_seats_list[1].sat and not self.table_list[3].status == "dirty":
                        self.table4_seats_list[1].sat = True
                        self.table4_seats_list[1].alpha = 255
                    elif self.table4_seats_list[1].sat:
                        self.table4_seats_list[1].sat = False
                        self.table4_seats_list[1].alpha = 25
                if symbol == arcade.key.E:
                    if not self.table4_seats_list[2].sat and not self.table_list[3].status == "dirty":
                        self.table4_seats_list[2].sat = True
                        self.table4_seats_list[2].alpha = 255
                    elif self.table4_seats_list[2].sat:
                        self.table4_seats_list[2].sat = False
                        self.table4_seats_list[2].alpha = 25
                if symbol == arcade.key.R:
                    if not self.table4_seats_list[3].sat and not self.table_list[3].status == "dirty":
                        self.table4_seats_list[3].sat = True
                        self.table4_seats_list[3].alpha = 255
                    elif self.table4_seats_list[3].sat:
                        self.table4_seats_list[3].sat = False
                        self.table4_seats_list[3].alpha = 25

                # Table 5 Keys
                if symbol == arcade.key.T:
                    if not self.table5_seats_list[0].sat and not self.table_list[4].status == "dirty":
                        self.table5_seats_list[0].sat = True
                        self.table5_seats_list[0].alpha = 255
                    elif self.table5_seats_list[0].sat:
                        self.table5_seats_list[0].sat = False
                        self.table5_seats_list[0].alpha = 25
                if symbol == arcade.key.Y:
                    if not self.table5_seats_list[1].sat and not self.table_list[4].status == "dirty":
                        self.table5_seats_list[1].sat = True
                        self.table5_seats_list[1].alpha = 255
                    elif self.table5_seats_list[1].sat:
                        self.table5_seats_list[1].sat = False
                        self.table5_seats_list[1].alpha = 25
                if symbol == arcade.key.U:
                    if not self.table5_seats_list[2].sat and not self.table_list[4].status == "dirty":
                        self.table5_seats_list[2].sat = True
                        self.table5_seats_list[2].alpha = 255
                    elif self.table5_seats_list[2].sat:
                        self.table5_seats_list[2].sat = False
                        self.table5_seats_list[2].alpha = 25
                if symbol == arcade.key.I:
                    if not self.table5_seats_list[3].sat and not self.table_list[4].status == "dirty":
                        self.table5_seats_list[3].sat = True
                        self.table5_seats_list[3].alpha = 255
                    elif self.table5_seats_list[3].sat:
                        self.table5_seats_list[3].sat = False
                        self.table5_seats_list[3].alpha = 25

            # reset table-Hold shift and press table #
            if modifiers & arcade.key.MOD_SHIFT:
                if symbol == arcade.key.KEY_1:
                    self.table_list[0].status = "ready"
                    self.table_list[0].alpha = 50
                if symbol == arcade.key.KEY_2:
                    self.table_list[1].status = "ready"
                    self.table_list[1].alpha = 50
                if symbol == arcade.key.KEY_3:
                    self.table_list[2].status = "ready"
                    self.table_list[2].alpha = 50
                if symbol == arcade.key.KEY_4:
                    self.table_list[3].status = "ready"
                    self.table_list[3].alpha = 50
                if symbol == arcade.key.KEY_5:
                    self.table_list[4].status = "ready"
                    self.table_list[4].alpha = 50

def main():
    window = dining_room()
    window.setup()
    arcade.run()

main()