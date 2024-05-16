from tkinter import Tk, BOTH, Canvas


class Point:
    """
    Construct a new 'Point' object.
    :param x: The x co-ordinate of the point, default value = 0
    :param y: The y co-ordinate of the point, default value = 0
    """
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Line:
    """
        Construct a new "Line" object.
        :param point1: Start point of the line
        :param point2: End point of the line
    """
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        """
        Calls the canvas's create_line() method 
        """
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)


class Window:
    """
    A class that represents a GUI window using Tkinter.
    """

    def __init__(self, width: int, height: int):
        """
        Constructs a new 'Window' object.

        :param width: The width of the window.
        :param height: The height of the window.
        """
        self.__root_widget = Tk()
        self.__root_widget.title("Maze-Solver")
        self.__canvas = Canvas(self.__root_widget, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str = "black"):
        """
        Calls the line's draw() method to draw a line in canvas.
        """
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        """
        Calls the root widget's update_idletasks() and update() method to redraw the window.
        """
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        """
        Sets the '__is_running' state to True. Then, continuously redraws the window as long as '__is_running' is True.
        """
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window Closed")

    def close(self):
        """
        Sets the '__is_running' state to False. This stops the 'wait_for_close' method from continually redrawing the window.
        """
        self.__is_running = False


