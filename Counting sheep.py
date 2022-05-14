def count_sheeps(sheep: list) -> int:
    sheep_count = 0
    for i in range(len(sheep)):
        if sheep[i] is True:
            sheep_count += 1
    return sheep_count

def one_line_count_sheep(sheep: list) -> int: return sheep.count(True)

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print(count_sheeps(array1))
print(one_line_count_sheep(array1))