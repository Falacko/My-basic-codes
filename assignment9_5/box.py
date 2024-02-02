class Box:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    def __init__(self):
        self.__owner = None
        self.__left_side = False
        self.__right_side = False
        self.__up_side = False 
        self.__down_side = False
    
    def get_owner(self):
        return self.__owner
    

    def add_owner(self, owner):
        self.__owner = owner


    def has_line_on_side(self, side):
        if side == Box.LEFT:
            return self.__left_side
        elif side == Box.UP:
            return self.__up_side
        elif side == Box.RIGHT:
            return self.__right_side
        elif side == Box.DOWN:
            return self.__down_side
        else:
            return False 
    

    def add_line(self, side):
        if side == 0:
            if self.__left_side:
                return False
            else:
                self.__left_side = True
                return True
        elif side == 1:
            if self.__up_side:
                return False
            else:
                self.__up_side = True
                return True
        elif side == 2:
            if self.__right_side:
                return False
            else:
                self.__right_side = True
                return True
        elif side == 3:
            if self.__down_side:
                return False
            else:
                self.__down_side = True
                return True
        


    def four_lines_placed(self):
        return self.__left_side and self.__right_side and self.__up_side and self.__down_side