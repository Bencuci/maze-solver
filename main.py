from graphics import Window, Line, Point, Cell
        
def main():
    win = Window(800, 900)

    cell1 = Cell(Point(50, 50), Point(150, 150), win)

    cell2 = Cell(Point(200, 50), Point(300, 150), win)
    cell2.has_left_wall = False

    cell3 = Cell(Point(350, 50), Point(450, 150), win)
    cell3.has_top_wall = False

    cell4 = Cell(Point(500, 50), Point(600, 150), win)
    cell4.has_right_wall = False
    cell4.has_bottom_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    
    win.wait_for_close()

main()