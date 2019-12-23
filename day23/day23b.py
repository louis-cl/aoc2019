import sys
from collections import deque
sys.path.append('..')
from day9.day9b_alt import program


def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    programs = []
    reads = []
    
    queue = deque()

    for i in range(50):
        p = program(memory.copy(), None)
        reads.append(deque([]))
        p.send(None)
        res = p.send(i)
        if res != "input":
            raise Exception('not input')
        else:
            queue.append((i,p))
        programs.append(p)

    nat = None
    natY = set()
    # iddle means got -1 and still did not give output
    iddles = [False]*50
    e = 0
    try:
        while queue:
            k,p = queue.popleft()
            # NAT CHECK
            if not any(reads) and all(iddles):
                print('empty read!')
                # send nat paquet
                if nat == None: raise Exception('null nat packet')
                reads[0].append(nat)
                if nat[1] in natY:
                    print("SECOND Y", nat[1])
                    exit(0)
                natY.add(nat[1])
                print('nat releasing', nat)

            # check input pending
            if reads[k]:
                # send to computer
                x,y = reads[k].popleft()
                a = p.send(x)
                if a != 'input': raise Exception('received half packet')
                a = p.send(y)
                print('SENT', (x,y), 'to', k, 'got', a)
                # if a != 'input': raise Exception('LOOK 2')
            else:
                a = p.send(-1)
                iddles[k] = a == 'input'

            print('after sending', -1, 'to', k, 'got', a)
            while a != 'input':
                # packing incoming !!
                x = p.send(None)
                y = p.send(None)
                if a == 255:
                    nat = (x,y)
                    print('got nat packet', (x,y))
                else:
                    print('sent', (x,y), 'to pc', a)
                    reads[a].append((x,y))
                # again ?
                a = p.send(None)
                print('after send', a)
            
            # here a is input, so queue for more
            queue.append((k,p))

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

    


