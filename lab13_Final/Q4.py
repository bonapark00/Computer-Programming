def check(x):
    if x < 0:
        raise ValueError('Too small!')
    elif x == 0:
        raise ValueError('Zero not allowed!')
    elif x > 150:
        raise OverflowError('Too large!')


def getInput():
    try:
        val = int(input('Enter an integer: '))
        check(val)
    except ValueError as msg:
        val = 1
        print(1)
    except OverflowError as msg:
        print(2)
        raise msg

    return val


try:
    val = getInput()
except ValueError:
    print(30000)
except OverflowError:
    print(40000)