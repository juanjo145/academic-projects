def main():
    while True:
        number_of_sticks = int(input())
        if number_of_sticks == 0:
            break
        sticks = list(map(int, input().split()))
        smallest_length = 51
        for length in range(1, 51):
            if is_valid(length, sticks, 0):
                smallest_length = length
        print(smallest_length)

def is_valid(length, sticks, index):
    if index == len(sticks):
        return True
    if sticks[index] > length:
        return False
    return is_valid(length, sticks, index + 1) or is_valid(length - sticks[index], sticks, index + 1)

if __name__ == "__main__":
    main()