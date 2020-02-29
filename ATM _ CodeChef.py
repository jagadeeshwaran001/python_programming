x, y = input().split()
x, y = [int(x),float(y)]
if x % 5 == 0 and x + 0.5 < y:
    print(format(y - x - 0.5, '.2f'))
else:
    print(format(y, '.2f'))