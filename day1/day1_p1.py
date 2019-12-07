def fuel(mass):
    return mass // 3 - 2

def main(lines):
    result = sum(map(fuel, lines))
    print(result)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = map(int, lines)
    main(lines)