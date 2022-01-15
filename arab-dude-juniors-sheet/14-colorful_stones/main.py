if __name__ == "__main__":
    pos = 0
    stones = list(input())
    instructions = list(input())
    for c in instructions:
        if  stones[pos] == c:
            pos += 1
    print(pos + 1)