from collections import defaultdict

def opcode(code):
    op = code % 100
    code = code // 100
    immediate1 = code % 10
    code = code // 10
    immediate2 = code % 10
    code = code // 10
    immediate3 = code % 10
    return (op, [immediate1, immediate2, immediate3])

def program(memory):
    i = 0
    relative = 0

    def mem(pos, mode):
        if mode == 1: return pos
        elif mode == 2: return memory[pos+relative]
        elif mode == 0: return memory[pos]
        else: raise Exception("PROBLEM mode")

    def write(pos, mode):
        if mode == 2: return pos+relative
        else: return pos

    while True:
        (op, [im1, im2, im3]) = opcode(memory[i])
        if op == 99:
            break
        elif op == 1:
            a = memory[i+1]
            b = memory[i+2]
            d = memory[i+3]
            memory[write(d, im3)] = mem(a, im1) + mem(b, im2)
            i += 4
        elif op == 2:
            a = memory[i+1]
            b = memory[i+2]
            d = memory[i+3]
            memory[write(d, im3)] = mem(a, im1) * mem(b, im2)
            i += 4
        elif op == 3:
            a = memory[i+1]
            # input
            print("INPUT 2")
            memory[write(a, im1)] = 2
            i += 2
        elif op == 4:
            a = memory[i+1]
            res = mem(a, im1)
            print(res)
            i += 2
        elif op == 5:
            a = memory[i+1]
            b = memory[i+2]
            v = mem(a, im1)
            if v != 0:
                i = mem(b, im2)
            else:
                i += 3
        elif op == 6:
            a = memory[i+1]
            b = memory[i+2]
            v = mem(a, im1)
            if v == 0:
                i = mem(b, im2)
            else:
                i += 3
        elif op == 7:
            a = memory[i+1]
            b = memory[i+2]
            c = memory[i+3]
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            if v1 < v2:
                memory[write(c, im3)] = 1
            else:
                memory[write(c,im3)] = 0
            i += 4
        elif op == 8:
            a = memory[i+1]
            b = memory[i+2]
            c = memory[i+3]
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            if v1 == v2:
                memory[write(c, im3)] = 1
            else:
                memory[write(c, im3)] = 0
            i += 4
        elif op == 9:
            a = memory[i+1]
            relative += mem(a, im1)
            i += 2
        else:
            print("something went wrong ", op)
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