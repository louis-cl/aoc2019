def split(n):
    return [int(d) for d in str(n)]

def join(n):
    return int("".join([str(d) for d in n]))

def increasing(l):
    n = len(l)
    for i in range(n-1):
        if l[i] > l[i+1]: return False
    return True

def main(low, high):
    digits = split(low)
    count = 0
    for num in range(low, high):
        s = split(num)
        if len(set(s)) < 6 and increasing(s):
            count += 1
    return count

if __name__ == '__main__':
    main(284639, 748759)