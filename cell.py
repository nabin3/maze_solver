from graphics import Point, Line, Window


class Cell:
    """
        Create an object of Cell class 
        :param win: a Window class object
    """
    def  __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        """ Take co-ordinate of top-left point and bottom-right point """
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color = "black")            
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color = "white")            

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color = "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color = "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color = "black")            
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color = "white")            

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color = "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color = "white")


    def draw_move(self, to_cell, undo: bool = False):
        """
        Draw line from the center of calling cell to the center of the input cell
        :param to_cell: it is the destination cell
        :param undo: If the undo flag is not set, the line you draw should be "red".
                     Otherwise, make it "gray" 
                     This is so that when we go to draw the path,
                     whenever we backtrack we can show that in a different
                     color to better visualize what's happening.
        """
        if self._win is None:
            return
        if undo:
            line_color = "grey"
        else:
            line_color = "red"

        # Calculating center point's co-ordinate of source cell
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        # Calculating center point's co-ordinate of destination cell
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        # Move left
        if self._x1 > to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x1, y_mid))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_cell._x2, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, line_color)

        # Move right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))

        # Move up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))

        # Move down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_x_mid, to_cell._y1), Point(to_x_mid, to_y_mid))