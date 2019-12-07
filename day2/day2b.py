def program(codes):
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

    return result[0]
        
def main(codes):
    for i in range(99):
        for j in range(99):
            mem = codes.copy()
            mem[1] = i
            mem[2] = j
            if program(mem) == 19690720:
                print(i,j)
                return 100*i+j


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)