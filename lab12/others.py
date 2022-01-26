class Fraction(object):
    """
    Class to represent a number as a fraction
    Examples: 1/2, 2/5
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
        self.reduce()

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __float__(self):
        """ Returns a float-value of the Fraction object """
        return self.num / self.denom  # result of / is of type float

    def reduce(self):
        """
        Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD).
        Also removes the signs if both numerator and denominator are
        negative. Whole numbers (1, 2, ...) are represented as
        1/1, 2/1, 3/1, ...
        """

        # Find all aliquots of numerator
        aliquot_num = []
        if self.num < 0:
            self.num = self.num * (-1)
            for a in range(1, self.num + 1):
                if self.num % a == 0:
                    aliquot_num.append(a)
            self.num = self.num * (-1)
        else:  # which means self.num > 0
            for a in range(1, self.num + 1):
                if self.num % a == 0:
                    aliquot_num.append(a)

        # Find all aliquots of denominator
        aliquot_denom = []
        if self.denom < 0:
            self.denom = self.denom * (-1)
            for b in range(1, self.denom + 1):
                if self.denom % b == 0:
                    aliquot_denom.append(b)
            self.denom = self.denom * (-1)
        else:  # which means self.denom > 0
            for b in range(1, self.denom + 1):
                if self.denom % b == 0:
                    aliquot_denom.append(b)

        # Find GCD of numerator and denominator
        common_divisor = []
        for i in range(len(aliquot_num)):
            for j in range(len(aliquot_denom)):
                if aliquot_num[i] == aliquot_denom[j]:
                    common_divisor.append(aliquot_num[i])
        GCD = max(common_divisor)

        # Divide both numerator and denominator by GCD
        self.num = int(self.num / GCD)
        self.denom = int(self.denom / GCD)

        # If both numerator and denominator are negative,
        # removes the signs
        if self.num < 0 and self.denom < 0:
            self.num = self.num * (-1)
            self.denom = self.denom * (-1)

    def adjust(self, factor):
        """ Multiplies numerator and denominator by factor """
        self.num = self.num * factor
        self.denom = self.denom * factor

print(Fraction(6,-8))