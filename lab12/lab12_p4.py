"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab12_p4.py
"""


class Fraction(object):
    """
    Class to represent a number as a fraction
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
            raise ValueError('requires type int')
        # Check that denominator is non-zero:
        if d == 0:
            raise ZeroDivisionError('requires non-zero denominator')

        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d

        # reduce fraction
        self.reduce()

    def reduce(self):
        """Reduce self to simplest terms
           by dividing both numerator and denominator by GCD"""

        # init to think sign and figure separately
        sign = +1
        if self.num * self.denom < 0:
            sign = -1

        self.num = abs(self.num)
        self.denom = abs(self.denom)

        # get GCD
        if self.num >= self.denom:
            self.big = self.num
            self.small = self.denom
        else:
            self.big = self.denom
            self.small = self.num
        self.rem = self.big % self.small
        if self.rem == 0:
            self.GCD = self.small
        else:
            while self.rem == 0:
                self.rem = self.big % self.small
                self.big = self.small
                self.small = self.rem
            self.GCD = self.rem

        # divide num and denom by GCD and restore sign
        self.num = self.num // self.GCD * sign
        self.denom = self.denom // self.GCD

    def adjust(self, factor):
        """Multiplies numerator and denominator by factor"""
        self.f = factor
        # multiply factor to both num and denom
        self.num = self.num * factor
        self.denom = self.denom * factor

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        # multiply nums and denoms from each self and other
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        # reduce to common and add
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __float__(self):
        """ Returns a float-value of the Fraction object """
        return self.num / self.denom  # result of / is of type float
