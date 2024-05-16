from cell import Cell
from graphics import Window
import time
import random



class Maze:
    """
    This class represent the maze.
    """
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window = None, seed: int | None = None):
        """
        Construct a new object of Maze class.

        :param x1: x co-ordinate of starting point of the maze object in app-window.
        :param y1: y co-ordinate of starting point of the maze object in app-window.
        :param num_rows: number of rows present in this maze.
        :param num_cols: number of columns present in this maze.
        :param cell_size_x: width of a cell in this maze.
        :param cell_size_y: height of a cell in this maze.
        :param win: an object of Window class
        """
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        """
        This function create all cells of maje with help of _draw_cell() method.
        """
        # This loop and its inner help us to fill the empty maze with disired number of cells logically
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        # This loop draws that logically built image on canvas with help of _draw_cell(i, j) 
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        


    def _draw_cell(self, i: int, j: int):
        """
        This method draw a particular cell with help of draw method of Cell object.

        :param i: coloumn index of a cell.
        :param j: row index of a cell.
        """
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):

        """
        This method helps us to visualize what our alogorithm is doing in real time.
        """
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.25)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1,  self._num_rows- 1)


    def _break_walls_r(self, i: int, j: int):
        """
        This method create path from
        start to end breaking walls of
        cells in a random pattern using DFS.

        :param i: coloumn index of a cell.
        :param j: row index of a cell.
        """

        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            # Left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # Top
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # Bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]            

            # If moves left
            if i - 1 == next_index[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # If moves right
            if i + 1 == next_index[0]:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # If moves top
            if j - 1 == next_index[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # If moves down
            if j + 1 == next_index[1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        """
        Reset all the cell's visited propoerty to false.
        """ 

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        """
        Method solve maze by calling _solve_r(0, 0)
        """
        return self._solve_r(0, 0)


    def _solve_r(self, i :int, j :int):
        """
        Solve the maze with dfs algo.
        
        :param i: col index of cell.
        :param j: row index of cell.
        """

        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # Left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall :
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # Right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # Top
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # Bottom
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)          

        return False
