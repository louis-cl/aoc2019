from collections import defaultdict

def op(code):
    opcode = code % 100
    code = code // 100
    immediate1 = code % 10
    code = code // 10
    immediate2 = code % 10
    code = code // 10
    immediate3 = code % 10
    return (opcode, immediate1, immediate2, immediate3)


def program(codes):
    result = codes
    
    n = len(result)
    i = 0
    relative = 0

    def mem(pos, mode):
        if mode == 1: return pos
        elif mode == 2: return result[pos+relative]
        elif mode == 0: return result[pos]
        else: raise Exception("PROBLEM mode")

    def write(pos, mode):
        if mode == 2: return pos+relative
        else: return pos

    while True:
        (opcode, im1, im2, im3) = op(result[i])
        if opcode == 99:
            break
        elif opcode == 1:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[write(d, im3)] = mem(a, im1) + mem(b, im2)
            i += 4
        elif opcode == 2:
            a = result[i+1]
            b = result[i+2]
            d = result[i+3]
            result[write(d, im3)] = mem(a, im1) * mem(b, im2)
            i += 4
        elif opcode == 3:
            a = result[i+1]
            # input
            print("INPUT 1")
            result[write(a, im1)] = 1
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
                result[write(c, im3)] = 1
            else:
                result[write(c,im3)] = 0
            i += 4
        elif opcode == 8:
            a = result[i+1]
            b = result[i+2]
            c = result[i+3]
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            if v1 == v2:
                result[write(c, im3)] = 1
            else:
                result[write(c, im3)] = 0
            i += 4
        elif opcode == 9:
            a = result[i+1]
            relative += mem(a, im1)
            i += 2
        else:
            print("something went wrong ", opcode)
            break;
        
def main(codes):
    # codes to dict
    memory = defaultdict(lambda: 0)
    for i,v in enumerate(codes):
        memory[i] = v
    program(memory)
    


if __name__ == '__main__':
    with open('day9/input.txt', 'r') as f:
        lines = f.readlines()

    # lines[0] = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)