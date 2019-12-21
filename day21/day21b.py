import sys
from collections import deque
sys.path.append('..')
from day9.day9b import program

def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    read = deque()
    p = program(memory.copy(), read)

    instr = [
        # jump if there's landing D and it's not ####
        # d & !(a & b & c)
        "OR A T",
        "AND B T",
        "AND C T",
        "NOT T J",
        "AND D J",

        # make sure you can walk E or double jump H
        # & (e | h)
        "NOT E T",
        "NOT T T",
        "OR H T",
        "AND T J",
        "RUN"
    ]
    inp = "\n".join(instr) + "\n"
    read.extend(map(ord, inp))
    try:
        while True:
            res = next(p)
            if res < 0 or res > 255:
                print(res)
            else:
                print(chr(res), end='')
            # print('>', res, chr(res))
    except StopIteration:
        pass
    # *_, res = p
    # print(">", res)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    # read reactions
    main(codes)

    


