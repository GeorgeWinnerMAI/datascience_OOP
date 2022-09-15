def sum10(array):
    ans = 0
    for i in range(10):
        ans += array[i]
    return ans


def zero10(array):
    ans = 0
    for i in range(10):
        ans += (not array[i])
    return ans


def num_steps(n):
    s = ""
    for i in range(n):
        s += str(i+1)
        print(s)


def num_steps_reverse(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()


def num_steps_square(n):
    for i in range(1, n * 2):
        sp = i if i < n else n * 2 - i
        print(' ' * (n - sp), end='')
        for j in range(1, sp + 1):
            print(j, end='')
        for j in range(sp - 1, 0, -1):
            print(j, end='')
        print()

