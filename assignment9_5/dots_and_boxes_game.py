from box import Box


class DotsAndBoxesGame:
    TIE = "tie"
    PLAYER1 = "A"
    PLAYER2 = "B"
    def __init__(self, grid_width, grid_height, player_name_1, player_name_2): 
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__player_name_1 = player_name_1
        self.__player_name_2 = player_name_2
        self.__grid = self.create_grid()
    
    def create_grid(self):
        grid = []
        for i in range(self.__grid_height):
            grid2 = []
            for k in range(self.__grid_width):
                box = Box()
                grid2.append(box)
            grid.append(grid2)
        return grid
 
    def add_line(self, x, y, side, player):
        x = (x - 1)
        y = (y - 1)
        box1: Box = self.__grid[x][y]
        succ = box1.add_line(side)
        if succ:
            self.update_neighbour_of_box(x, y, side)
            if box1.four_lines_placed():
                box1.add_owner(player)
            box2: Box = self.get_neighbour_on_side(side, x , y)
            if box2 and box2.four_lines_placed() and box2.get_owner() is not None:
                box2.add_owner(player)
            if box1.four_lines_placed() or (box2 is not None and box2.four_lines_placed()):
                return True, True
            else:
                return True, False
        else:
            return False, False     

    def update_neighbour_of_box(self, row_index, column_index, side):
        neighbour = self.get_neighbour_on_side(row_index, column_index, side)
        if neighbour is not None:
            if side == Box.RIGHT:
                neighbour.add_line(Box.LEFT)
            elif side == Box.DOWN:
                neighbour.add_line(Box.UP)
            elif side == Box.LEFT:
                neighbour.add_line(Box.RIGHT)
            elif side == Box.UP:
                neighbour.add_line(Box.DOWN)
            
    def get_neighbour_on_side(self, side, row_index, column_index):
        if 0 <= row_index < self.__grid_height and 0 <= column_index < self.__grid_width:
            box1 = self.__grid[row_index][column_index]
            
            if side == Box.LEFT:
                if column_index >= 0:    
                    return self.__grid[row_index][column_index - 1]
                else:
                    return None
            if side == Box.DOWN:
                if row_index < self.__grid_height - 1:
                    return self.__grid[row_index + 1][column_index]
                else:
                    return None
            if side == Box.RIGHT:
                if column_index < self.__grid_width - 1:
                    return self.__grid[row_index][column_index + 1]
                else:
                    return None
            if side == Box.UP:
                if row_index > 0:
                    return self.__grid[row_index - 1][column_index]
                else:
                    return None 
        else:
            return None                 
    def calculate_points_of_player(self, player):
        points = 0
        for row in self.__grid:
            for box in row:
                if box.get_owner() == player:
                    points += 1
        return points
    
    def is_ended(self):
        for rivi in self.__grid:
            for box in rivi:
                if box.get_owner() is None:
                    return False
        return True
    

    def winner(self):
        player1_winner = self.calculate_points_of_player(self.__player_name_1)
        player2_winner = self.calculate_points_of_player(self.__player_name_2)
        if player1_winner > player2_winner:
            return self.__player_name_1
        elif player1_winner < player2_winner:
            return self.__player_name_2
        else:
            return DotsAndBoxesGame.TIE

    def give_score(self):
        tulos = "\nScore:\n\n"
        p1 = f"{self.__player_name_1} ({self.PLAYER1})"
        p2 = f"{self.__player_name_2} ({self.PLAYER2})"
        tulos1 = f"{p1:<15s} | {p2:<15s}"
        tulos += f"{tulos1}\n{'-' * 37}\n"
        tulos += f"{self.calculate_points_of_player(self.PLAYER1):<15d}{' | '}{self.calculate_points_of_player(self.PLAYER2):<15d}\n"
        tulos += f"{tulos1}\n"
        return tulos

    def one_row_of_grid(self, row_index):
        rivi1 = ""
        rivi = self.__grid[row_index]
        if row_index % 2 == 0:
            rivi1 += "   "
            for grid in range(len(rivi) + 1):
                rivi1 += "o"
                if grid < len(rivi):
                    box: Box = rivi[grid]
                    if box.has_line_on_side(Box.RIGHT):
                        rivi1 += "--"
                    else:
                        rivi1 += "    "
            rivi1 += "\n"
        else:
            rivi1 += "    "
            for grid in range(len(rivi)):
                box: Box = rivi[grid]
                if box.four_lines_placed():
                    rivi1 += f" {box.get_owner()} |"
                else:
                    rivi1 += "    "
            rivi1 += "\n"
        
        return rivi1


    def __str__(self):
        result = "      "
        for k in range(1, self.__grid_width + 1):
            result += f"{k:<5}"
        result += "\n"
        
        for i in range(self.__grid_height):
            result += f"{i + 1:<2}   "
            for j in range(self.__grid_width):
                result += "o"
                box = self.__grid[i][j]
                if j < self.__grid_width - 1:
                    if box.has_line_on_side(Box.RIGHT):
                        result += "--"
                    else:
                        result += "   "
            result += "\n"
            
            if i < self.__grid_height - 1:
                result += "      "
                for j in range(self.__grid_width):
                    box = self.__grid[i][j]
                    if box.has_line_on_side(Box.DOWN):
                        result += "  |  "
                    else:
                        result += "     "
                result += "\n"

        result += self.give_score()
        return result