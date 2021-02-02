def sum_array(arr: list):
    #your code here
    if arr is not None and len(arr) >= 3:
        arr.sort()
        arr.pop(0)
        arr.pop(-1)
        result = 0
        for i in arr:
            result = result + i
        return result
    return 0

if __name__ == "__main__":  
    print(sum_array([-6, -20, -1, -10, -12]))