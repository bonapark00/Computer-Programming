"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab12_p2.py
"""


def moderateDays(mydict):
    """
    Returns a list of days for which
    the average temperature was between 70 and 79 degrees.
    """
    # init
    result = []

    # check temperature range and append key if in right range
    for day in mydict.keys():
        if 70 <= mydict[day] <= 79:
            result.append(day)

    # return list
    return result
