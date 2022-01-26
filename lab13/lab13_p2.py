"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p2.py
"""


class AvgList(list):
    """class AvgList is subclass of the built in list class.
        This class has computeAvg() method
        to calculate the average of values in list"""
    def computeAvg(self):
        """
        Computes the average of a list of numeric types.
        Raises the ValueError exception if a list element is neither
        an instance of an 'int' nor a 'float' class.
        """

        for i in self:
            if isinstance(i, int) == False and \
                    isinstance(i, float) == False:
                raise ValueError
        # init
        self.sum = 0
        # sum all elements
        for i in self:
            self.sum += i
        # calcualte the average
        self.avg = self.sum / len(self)

        return self.avg
