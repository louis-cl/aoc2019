import itertools
from collections import deque

def op(code):
    opcode = code % 100
    code = code // 100
    immediate1 = code % 10 == 1
    code = code // 10
    immediate2 = code % 10 == 1
    code = code // 10
    immediate3 = code % 10 == 1
    return (opcode, immediate1, immediate2, immediate3)


def program(codes, read, pointer):
    result = codes
    
    n = len(result)
    i = pointer

    def mem(pos, isIm = False):
        if isIm: return pos
        else: return result[pos]

    while i < n:
        (opcode, im1, im2, im3) = op(result[i])
        if opcode == 99:
            # print("HALTING")
            return False, -1, i
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
            result[a] = read.popleft()
            i += 2
        elif opcode == 4:
            a = result[i+1]
            res = mem(a, im1)
            # print('OUTPUT', res)
            i += 2
            return (True, res, i)
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
            raise Exception("something went wrong with {}".format(opcode))
        
def main(codes):
    perms = list(itertools.permutations(range(5, 10)))
    max_value = -100000
    for perm in perms:
        previous = 0
        done = False
        programs = [list(codes) for i in range(5)]
        pointer = [0]*5
        inputs = [deque([p]) for p in perm]
        lastOutput = -1
        while not done:
            state = True
            for i,j in enumerate(perm):
                inputs[i].append(previous)
                # print("INPUT", inputs[i])
                state, output, ptr = program(programs[i], inputs[i], pointer[i])
                if i == 4 and state:
                    # print("SAVING", output)
                    lastOutput = output
                pointer[i] = ptr
                previous = output
            done = not state
        # print("GOT ", lastOutput)
        if lastOutput > max_value:
            max_value = lastOutput
    if max_value == 21844737:
        print("ALL OK")

if __name__ == '__main__':
    with open('day7/input.txt', 'r') as f:
        lines = f.readlines()

    # lines[0] = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)