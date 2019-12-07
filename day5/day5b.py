def op(code):
    opcode = code % 100
    code = code // 100
    immediate1 = code % 10 == 1
    code = code // 10
    immediate2 = code % 10 == 1
    code = code // 10
    immediate3 = code % 10 == 1
    return (opcode, immediate1, immediate2, immediate3)


def program(codes):
    result = codes
    
    n = len(result)
    i = 0

    def mem(pos, isIm = False):
        if isIm: return pos
        else: return result[pos]

    while i < n:
        (opcode, im1, im2, im3) = op(result[i])
        if opcode == 99:
            break
        elif opcode == 1:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[d] = mem(a, im1) + mem(b, im2)
            i += 4
        elif opcode == 2:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[d] = mem(a, im1) * mem(b, im2)
            i += 4
        elif opcode == 3:
            a = result[i+1]
            result[a] = 5
            i += 2
        elif opcode == 4:
            a = result[i+1]
            res = mem(a, im1)
            print(res)
            i += 2
        elif opcode == 5:
            a = result[i+1]
            b = result[i+2]
            v = mem(a, im1)
            if v != 0:
                i = mem(b, im2)
            else:
                i += 3
        elif opcode == 6:
            a = result[i+1]
            b = result[i+2]
            v = mem(a, im1)
            if v == 0:
                i = mem(b, im2)
            else:
                i += 3
        elif opcode == 7:
            a = result[i+1]
            b = result[i+2]
            c = result[i+3]
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            if v1 < v2:
                result[c] = 1
            else:
                result[c] = 0
            i += 4
        elif opcode == 8:
            a = result[i+1]
            b = result[i+2]
            c = result[i+3]
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            if v1 == v2:
                result[c] = 1
            else:
                result[c] = 0
            i += 4
        else:
            print("something went wrong ", opcode)
            break;
        
def main(codes):
    program(codes)


if __name__ == '__main__':
    with open('day5/input.txt', 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)