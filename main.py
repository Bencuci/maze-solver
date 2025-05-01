from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
        
def main():
    win = Window(1000, 1000)

    starting_point = Point(20, 20)
    maze = Maze(starting_point, 12, 12, 70, 70, win)

    win.wait_for_close()

main()