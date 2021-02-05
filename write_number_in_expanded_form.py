"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    new = list(str(num))
    final = ''
    for i, e in enumerate(new):
        a = len(new) - (i + 1)
        if e != '0':
            final += (e + '0' * a + ' + ')
    return final[0:len(final)-3]

def expanded_form_short(num):
    num = list(str(num))
    return ' + '.join(e + '0' * (len(num) - i - 1) for i,e in enumerate(num) if e != '0')

if __name__ == '__main__':
    print(expanded_form_short(70304))