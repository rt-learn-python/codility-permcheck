

def solution(input):
    # print(input)
    sorted = input
    sorted.sort()
    if sorted[0] != 1:
        return 0

    for x in range(1, len(sorted)):
        if input[x] - input[x - 1] != 1:
            return 0
    else:
        return 1


if __name__ == '__main__':
    solution()
