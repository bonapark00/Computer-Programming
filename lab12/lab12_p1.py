"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab12_p1.py
"""


def addDailyTemp(mydict, day, temperature):
    """
    Add key 'day' and value 'temperature' to the dictionary 'mydict'
    only if the key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned.
    """
    # check key 'day' present in mydict
    if day not in mydict.keys():
        mydict[day] = temperature

    # return dictionary
    return mydict