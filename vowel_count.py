def get_count(input_str: str) -> int:
    num_vowels = 0

    for i in input_str:
        if i in 'AaEeIiOoUu':
            num_vowels += 1
    return num_vowels

if __name__ == "__main__":
    print(get_count('Ameixa'))