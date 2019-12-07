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
            a = mem(i+1)
            b = mem(i+2)
            d = mem(i+3)
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
            result[a] = 1 # input
            i += 2
        elif opcode == 4:
            a = result[i+1]
            res = mem(a, im1)
            print(res)
            i += 2
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