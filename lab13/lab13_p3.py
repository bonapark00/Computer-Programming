"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p3.py
"""

# Import our own constants:
import self as self

from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle


class auto_doboggi_man(doboggi_man):
    """
    Class auto_doboggi_man, the autonomous doboggi-collector.

    The auto_doboggi_man class is a subclass of the doboggi_man class. It
    inherits all data attributes and methods from the doboggi_man class. It
    overrides the move() method of the doboggi_man class to automatically
    navigate doboggi_man across the screen.

    it has two methods, __init__ and move().
    by move() method dogboggi man would automatically find and eat food,
    and avoid two ghosts.
    """

    def __init__(self, x=0, y=0):
        """Special method to initialize a doboggi_man object"""
        doboggi_man.__init__(self, x, y)  # call __init__() of the superclass
        self.dir = 'east'  # set initial direction
        self.steps = STEPMAX  # remaining steps
        self.isYum = False  # no
        self.isYumOff = False  # bubble

        self.num_eat = 0  # how many dogboggi that dogboggi man ate
        self.num_avoid = 0  # how many ghost that dogboggi man avoided

    def move(self):
        """method to move dogboggi man automatically"""

        # init
        # get 2 ghosts
        self.g1 = ghosts[0]
        self.g2 = ghosts[1]

        # get 3 dogboggi
        self.d_upper_t = []
        self.d_upper_pos = []

        for i in food:
            if list(i.getPosition())[1] < 0:  # one dogboggi below ghosts
                self.d_below_t = i
                self.d_below_pos = i.getPosition()
            else:
                self.d_upper_t.append(i)
                self.d_upper_pos.append(i.getPosition())
        # 2 dogboggi above ghosts
        self.d_upper1_t = self.d_upper_t[0]
        self.d_upper1_pos = self.d_upper_pos[0]
        self.d_upper2_t = self.d_upper_t[-1]
        self.d_upper2_pos = self.d_upper_pos[-1]

        # if hit walls, change direction
        if self.dir == 'east' and self.ttl.xcor() > X_MAX:
            self.turnWest()
            return
        if self.dir == 'west' and self.ttl.xcor() < -X_MAX:
            self.turnEast()
            return
        if self.dir == 'north' and self.ttl.ycor() > Y_MAX:
            self.turnSouth()
            return
        if self.dir == 'south' and self.ttl.ycor() < -Y_MAX:
            self.turnNorth()
            return

        def goToFood(food):
            """Go to food, and eat the food"""

            # init
            x_distance = food.ttl.xcor() - self.ttl.xcor()
            y_distance = food.ttl.ycor() - self.ttl.ycor()

            # first, move horizontally
            if x_distance > 15:
                self.turnEast()
                self.ttl.forward(10)
            elif x_distance < -15:
                self.turnWest()
                self.ttl.forward(10)
            # then, move vertically
            elif (-15 <= x_distance <= 15) and abs(y_distance) > 15:
                if y_distance > 0:
                    self.turnNorth()
                    self.ttl.forward(10)
                else:
                    self.turnSouth()
                    self.ttl.forward(10)
            # find and eat dogboggi
            elif abs(x_distance) <= 15 and abs(y_distance) <= 15:
                self.num_eat += 1
                return

        def avoiding(g):
            """Go up while avoiding g(ghost)"""

            self.turnNorth()  # go up
            # dogboggi man is far below g
            if g.ttl.ycor() - self.ttl.ycor() > 35:
                self.ttl.forward(10)

            elif 25 < (g.ttl.ycor() - self.ttl.ycor()) <= 35:
                # stop when dogboggi is near g
                if ((g.ttl.xcor() > X_MAX - 30) and \
                    (self.ttl.xcor() < -X_MAX + 50)) or \
                        (abs(g.ttl.xcor() - self.ttl.xcor()) <= 100):
                    return
                else:
                    self.ttl.forward(10)
            elif -25 < (g.ttl.ycor() - self.ttl.ycor()) <= 25:
                self.ttl.forward(10)
            # finally avoid g
            elif (g.ttl.ycor() - self.ttl.ycor()) <= -25:
                self.num_avoid += 1
                return

        # implement moving dogboggiman
        # eat the lowest dogboggi
        if self.num_eat == 0:
            goToFood(self.d_below_t)
        # avoid lower ghost
        elif self.num_eat == 1 and self.num_avoid == 0:
            avoiding(self.g1)
        # avoid upper ghost
        elif self.num_eat == 1 and self.num_avoid == 1:
            avoiding(self.g2)
        # eat one of upper dogbiggi
        elif self.num_eat == 1 and self.num_avoid == 2:
            goToFood(self.d_upper1_t)
        # eat the last dogboggi
        elif self.num_eat == 2 and self.num_avoid == 2:
            goToFood(self.d_upper2_t)
