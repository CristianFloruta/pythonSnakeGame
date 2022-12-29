from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Create the initial snake consisting on 3 gold colored square segments (Turtle  instance)
        3 Turtle objects == 1 Snake object

        """
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("gold")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

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
        Change snake head direction by setting the head(ing) to head(ing) to "east" -> 0 degree to the left.
        """
        self.segments[0].setheading(180)

    def go_right(self):
        """
        Change snake head direction by setting the head(ing) to "west" -> 180 degree to the left.
        """
        self.segments[0].setheading(0)

    def go_up(self):
        """
        Change snake head direction by setting the head(ing) to "north" -> 90 degree to the left.
        """
        self.segments[0].setheading(90)

    def go_down(self):
        """
        Change snake head direction by setting the head(ing) to "south" -> 270 degree to the left.
        """
        self.segments[0].setheading(270)
