def main(codes):
    result = codes
    
    n = len(result)
    i = 0

    while i < n:
        opcode = result[i]
        if opcode == 99:
            break
        elif opcode == 1:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[d] = result[a] + result[b]
            i += 4
        elif opcode == 2:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[d] = result[a] * result[b]
            i += 4
        else:
            print("something went wrong ", opcode)
            break;

    print(result)
        


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    codes[2] = 2
    codes[1] = 12
    main(codes)