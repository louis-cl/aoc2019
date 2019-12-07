def split(n):
    return [int(d) for d in str(n)]

def join(n):
    return int("".join([str(d) for d in n]))

def increasing(l):
    n = len(l)
    for i in range(n-1):
        if l[i] > l[i+1]: return False
    return True

def only2(s):
    n = len(s)
    last = s[0]
    count = 1
    for i in range(1,n):
        if s[i] == last:
            count += 1
        elif count == 2:
            return True
        else:
            count = 1
            last = s[i]
    return count != 2

def main(low, high):
    digits = split(low)
    count = 0
    for num in range(low, high):
        s = split(num)
        if len(set(s)) < 6 and increasing(s) and only2(s):
            count += 1
    return count

if __name__ == '__main__':
    print(main(284639, 748759))