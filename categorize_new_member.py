def open_or_senior(data):
    result = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result

if __name__ == "__main__":
    print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))