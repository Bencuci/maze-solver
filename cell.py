from graphics import Point, Line, Window

class Cell:
    def __init__(self, p1, p2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left = p1
        self._bottom_left = Point(p1.x, p2.y)
        self._top_right = Point(p2.x, p1.y)
        self._bottom_right = p2
        self._center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
        self._win = win
    
    def draw(self):
        if not self._win:
            return

        if self.has_left_wall:
            line = Line(self._top_left, self._bottom_left)
            self._win.draw_line(line, "black")
        
        if self.has_right_wall:
            line = Line(self._top_right, self._bottom_right)
            self._win.draw_line(line, "black")
        
        if self.has_top_wall:
            line = Line(self._top_left, self._top_right)
            self._win.draw_line(line, "black")
        
        if self.has_bottom_wall:
            line = Line(self._bottom_left, self._bottom_right)
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        
        line = Line(self._center, to_cell._center)
        self._win.draw_line(line, color)