"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p1.py
"""


class Range:
    """class that contains range from start to end"""
    def __init__(self, start, end):
        """initialize range's start point and end point"""
        self.__start = start
        self.__end = end
        # check whether small is less than end
        if self.__start > self.__end:
            raise IndexError

    def __str__(self):
        """special method for return string of indicating range
            i.e. '10...15' """
        return str(self.__start) + '...' + str(self.__end)

    def __lt__(self, other):
        """special method for comparing two Range class
            return True when self's all values are smaller than other's"""
        # check self's endpoint and other's start point
        if self.__end - 1 < other.__start:
            return True
        else:
            return False
