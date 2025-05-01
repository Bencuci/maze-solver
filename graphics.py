from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__is_running = False

        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()
        print("Window closed")

    def close(self):
        self.__is_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

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
        self.__top_left = p1
        self.__bottom_left = Point(p1.x, p2.y)
        self.__top_right = Point(p2.x, p1.y)
        self.__bottom_right = p2
        self.__win = win
    
    def draw(self):
        if self.has_left_wall:
            line = Line(self.__top_left, self.__bottom_left)
            self.__win.draw_line(line, "black")
        
        if self.has_right_wall:
            line = Line(self.__top_right, self.__bottom_right)
            self.__win.draw_line(line, "black")
        
        if self.has_top_wall:
            line = Line(self.__top_left, self.__top_right)
            self.__win.draw_line(line, "black")
        
        if self.has_bottom_wall:
            line = Line(self.__bottom_left, self.__bottom_right)
            self.__win.draw_line(line, "black")
