from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._root = Tk()
        self._root.title("Maze Solver") 
        self._canvas = Canvas(self._root, height=height, width=width)
        self._is_running = False

        self._canvas.pack()
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._is_running = True
        while self._is_running == True:
            self.redraw()
        print("Window closed")

    def close(self):
        self._is_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, p1, p2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left = p1
        self._bottom_left = Point(p1.x, p2.y)
        self._top_right = Point(p2.x, p1.y)
        self._bottom_right = p2
        self._win = win
    
    def draw(self):
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
