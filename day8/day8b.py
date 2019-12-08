W = 25
H = 6
from collections import Counter

def main(codes):
    t = W*H
    n = len(codes)
    print('have', n / t)
    layers = []
    for i in range(100):
        layers.append(codes[150*i:150*i+150])

    final_result = layers[0]
    for l in layers[1:]:
        result = list(final_result)
        for i,(a,b) in enumerate(zip(final_result, l)):
            if a == 2:
                result[i] = b
        final_result = result

    def p(d):
        return 'X' if d == 0 else '-'
        
    for i in range(6):
        print("".join(map(str, map(p, final_result[i*25:(i+1)*25]))))
    


if __name__ == '__main__':
    with open('day8/input.txt', 'r') as f:
        lines = f.readlines()

    codes = lines[0]
    codes = list(map(int, codes))
    main(codes)