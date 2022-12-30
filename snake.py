from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the initial snake consisting on 3 gold colored square segments (Turtle  instances)
        3 Turtle objects == 1 Snake object

        """
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("gold")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self, position):
        """
        Create a new Turtle object (shape = "square", color= "gold")
        Send the new segment to the position given by .extend method

        :param position: - is position of the last segment of the snake
                         - is given by the .extend method
        :return: an additional element of the segments list (the list with all Turtle objects that define the Snake)
        """
        new_segment = Turtle("square")
        new_segment.color("gold")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        extend the snake with one segment at the end of the snake ("segments" list)
        used the .add_segment method
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Mimic snake movement!
        Create the impression that all snake segments are linked to the head.
        Objects are moved in reversed order: from tale to head (from last to first).
        Doing this snake body will follow the head.
        All segments will play the head role at some point in the loop.
        """
        for segm_num in range(len(self.segments) - 1, 0, -1):
            new_x_coord = self.segments[segm_num - 1].xcor()
            new_y_coord = self.segments[segm_num - 1].ycor()
            self.segments[segm_num].goto(new_x_coord, new_y_coord)
        self.segments[0].forward(MOVE_DISTANCE)

    def go_left(self):
        """
        Change snake head direction by setting the head(ing) to head(ing) to "east" -> 0 degree to the left,
        unless current heading is to "west" 0
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        """
        Change snake head direction by setting the head(ing) to "west" -> 180 degree to the left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        """
        Change snake head direction by setting the head(ing) to "north" -> 90 degree to the left.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """
        Change snake head direction by setting the head(ing) to "south" -> 270 degree to the left.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
