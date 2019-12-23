from collections import deque

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

def readWithMode(mem, addr, off=0, mode=0):
    try:
        if mode == 0: return mem[addr]
        elif mode == 1: return addr
        elif mode == 2: return mem[addr+off]
        else: raise Exception("wrong read" + [off,mode,addr])
    except KeyError:
        return 0

def writeWithMode(mem, addr, value, off=0, mode=0):
    if mode == 0:
        mem[addr] = value
    elif mode == 2:
        mem[addr+off] = value
    else: raise Exception("wrong write" + [addr, value, off, mode])

def program(memory, out, ptr=0, mem_offset=0):
    while True:
        (op, [im1, im2, im3]) = opcode(memory[ptr])
        args = lambda n: unpack(memory, ptr+1, n)
        read = lambda addr,m: readWithMode(memory, addr, mem_offset, m)
        write = lambda addr,m,v: writeWithMode(memory, addr, v, mem_offset, m)
        if op == 99:
            yield "halt"
        elif op == 1: # ADD a b s
            a, b, s = args(3)
            val = read(a, im1) + read(b, im2)
            write(s, im3, val)
            ptr += 4
        elif op == 2: # MUL a b s
            a, b, s = args(3)
            val = read(a, im1) * read(b, im2)
            write(s, im3, val)
            ptr += 4
        elif op == 3: # IN s
            a = args(1)
            inp = (yield 'input') # input
            write(a, im1, inp)
            ptr += 2
        elif op == 4: # OUT s
            a = args(1)
            res = read(a, im1)
            if out:
                out.send(res)
            else:
                yield res
            ptr += 2
        elif op == 5: # NZ a j
            a, j = args(2)
            v = read(a, im1)
            if v != 0:
                ptr = read(j, im2)
            else:
                ptr += 3
        elif op == 6: # Z a j
            a, j = args(2)
            v = read(a, im1)
            if v == 0:
                ptr = read(j, im2)
            else:
                ptr += 3
        elif op == 7: # LT a b s
            a, b, s = args(3)
            v1 = read(a, im1)
            v2 = read(b, im2)
            write(s, im3, 1 if v1 < v2 else 0)
            ptr += 4
        elif op == 8: # EQ a b s
            a, b, s = args(3)
            v1 = read(a, im1)
            v2 = read(b, im2)
            write(s, im3, 1 if v1 == v2 else 0)
            ptr += 4
        elif op == 9: # OFF a
            a = args(1)
            mem_offset += read(a, im1)
            ptr += 2
        else:
            raise Exception("something went wrong " + op)
        

def printer():
    while True:
        n = (yield)
        print(n, end=',')

def main(codes):
    # codes to dict
    memory = {i:v for i,v in enumerate(codes)}
    # print(list(program(memory, deque([1]))))
    pp = printer()
    pp.send(None)

    pro = program(memory, pp)
    pro.send(None)
    print(pro.send(1))
    # pro.send(1)
    # output = p.send(2) # read

if __name__ == '__main__':
    with open('day9/input.txt', 'r') as f:
        lines = f.readlines()

    # lines[0] = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)