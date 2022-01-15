d = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    a = input().lower()
    b = input().lower()
    for i in range(len(a)):
        x = d.find(a[i])
        y = d.find(b[i])
        if x > y:
            print("1")
            break
        elif x < y:
            print("-1")
            break
        elif x == y and (i+1) == len(a):
            print('0')