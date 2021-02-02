"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""

def clean_string(s):
    n = []
    for i in s:
        if '#' not in i:
            n += i
        else:
            if len(n) >= 1:
                del(n[-1])
    return ''.join(n)

print(clean_string("abc#d##c"))