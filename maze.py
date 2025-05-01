import time
from cell import Cell
from graphics import Point

class Maze:
    def __init__(self, starting_point, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._starting_point = starting_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            cells_in_col = []
            for j in range(self._num_rows):
                cell_top_left = Point(
                    self._starting_point.x + (self._cell_size_x * i),
                    self._starting_point.y + (self._cell_size_y * j)
                )
                cell_bottom_right = Point(
                    cell_top_left.x + self._cell_size_x,
                    cell_top_left.y + self._cell_size_y
                )
                cell = Cell(cell_top_left, cell_bottom_right, self._win)
                cells_in_col.append(cell)
        
            self._cells.append(cells_in_col)
        
        for col in self._cells:
            for cell in col:
                cell.draw()
                self._animate()
    
        self._break_entrance_and_exit()
    
    def _animate(self):
        if not self._win:
            return

        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

        self._win.redraw()
