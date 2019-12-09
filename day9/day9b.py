from collections import defaultdict
from functools import partial

def unpack(dic, start, size):
    if size == 1: return dic[start]
    return [dic[i] for i in range(start, start+size)]

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
    mem_offset = 0

    def mem(pos, mode):
        if mode == 1: return pos
        elif mode == 2: return memory[pos+mem_offset]
        elif mode == 0: return memory[pos]
        else: raise Exception("PROBLEM mode")

    def write(pos, mode):
        if mode == 2: return pos+mem_offset
        else: return pos

    def readWithMode(mem, addr, off=0, mode=0):
        if mode == 0: return mem[addr]
        elif mode == 1: return addr
        elif mode == 2: return mem[addr+off]
        else: raise Exception("wrong read" + [mem,off,mode,addr])

    
    args = partial(unpack, memory)

    while True:
        (op, [im1, im2, im3]) = opcode(memory[i])
        if op == 99:
            break
        elif op == 1: # ADD a b s
            a, b, s = args(i+1, 3)
            memory[write(s, im3)] = mem(a, im1) + mem(b, im2)
            i += 4
        elif op == 2: # MUL a b s
            a, b, s = args(i+1, 3)
            memory[write(s, im3)] = mem(a, im1) * mem(b, im2)
            i += 4
        elif op == 3: # IN s
            a = args(i+1, 1)
            # input
            print("INPUT 2")
            memory[write(a, im1)] = 1
            i += 2
        elif op == 4: # OUT s
            a = args(i+1, 1)
            res = mem(a, im1)
            print(res)
            i += 2
        elif op == 5: # NZ a j
            a, j = args(i+1, 2)
            v = mem(a, im1)
            if v != 0:
                i = mem(j, im2)
            else:
                i += 3
        elif op == 6: # Z a j
            a, j = args(i+1, 2)
            v = mem(a, im1)
            if v == 0:
                i = mem(j, im2)
            else:
                i += 3
        elif op == 7: # LT a b s
            a, b, s = args(i+1, 3)
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            memory[write(s, im3)] = 1 if v1 < v2 else 0
            i += 4
        elif op == 8: # EQ a b s
            a, b, s = args(i+1, 3)
            v1 = mem(a, im1)
            v2 = mem(b, im2)
            memory[write(s, im3)] = 1 if v1 == v2 else 0
            i += 4
        elif op == 9: # OFF a
            a = args(i+1, 1)
            mem_offset += mem(a, im1)
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