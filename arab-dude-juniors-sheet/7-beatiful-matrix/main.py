import math

if __name__ == "__main__":
    matrix = []
    cnt = 0
    oneMatrixIndex = 2
    while len(matrix) != 5:
        x = input().split(" ")
        matrix.append(list(map(int, x)))
    if 1 in matrix[0]:
        cnt += 2
        oneMatrixIndex = 0
    if 1 in matrix[-1]:
        cnt += 2
        oneMatrixIndex = 4
    if 1 in matrix[1]:
        cnt += 1
        oneMatrixIndex = 1
    if 1 in matrix[-2]:
        cnt += 1
        oneMatrixIndex = 3
    oneIndex = matrix[oneMatrixIndex].index(1)
    if oneIndex == 0 or oneIndex == 4:
        cnt += 2
    elif oneIndex == 1 or oneIndex == 3:
        cnt += 1
    print(cnt)    