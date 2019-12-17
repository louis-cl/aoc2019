import re

def from_regex(st, regex):
    result = re.match(regex, st)
    methods = [result.group(i) for i in range(1,4)]
    routine = st
    for m,k in zip(methods,"ABC"):
        routine = routine.replace(m, k)
    return routine, methods

def regexp(st):
    return from_regex(st, r'^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$')
    
def iterative(st, methods=3, max_method_size=20):
    patt = [r'^']
    for i in range(1, methods+1):
        patt.append(r'(.{{1,{}}})'.format(max_method_size+1))
        if i == 1:
            patt.append(r'\1*')
        else:
            middle = r'|'.join(map(lambda x: r'\{}'.format(x), range(1,i+1)))
            patt.append(r'(?:{})*'.format(middle))
    patt.append(r'$')
    return from_regex(st, r''.join(patt))