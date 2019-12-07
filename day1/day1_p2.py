def fuel(mass):
    tmp = mass // 3 - 2
    if tmp <= 0:
        return 0
    else:
        return tmp + fuel(tmp)

def main(lines):
    result = sum(map(fuel, lines))
    print(result)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = map(int, lines)
    main(lines)