def plus(b):
    return lambda a: a + b

def minus(b):
    return lambda a: a - b

def times(b):
    return lambda a: a * b

def divided_by(b):
    return lambda a: a // b

def zero(zero=None):
    if not zero:
        return 0
    else:
        return zero(0)

def one(one=None):
    if not one:
        return 1
    else:
        return one(1)

def two(two=None):
    if not two:
        return 2
    else:
        return two(2)

def three(three=None):
    if not three:
        return 3
    else:
        return three(3)

def four(four=None):
    if not four:
        return 4
    else:
        return four(4)

def five(five=None):
    if not five:
        return 5
    else:
        return five(5)

def six(six=None):
    if not six:
        return 6
    else:
        return six(6)

def seven(seven=None):
    if not seven:
        return 7
    else:
        return seven(7)

def eight(eight=None):
    if not eight:
        return 8
    else:
        return eight(8)

def nine(nine=None):
    if not nine:
        return 9
    else:
        return nine(9)

print(eight(divided_by(three())))