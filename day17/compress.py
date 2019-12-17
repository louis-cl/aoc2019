import re

def regexp(st):
    result = re.match(r'^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$', st)
    methods = [result.group(i) for i in range(1,4)]
    routine = st
    for m,k in zip(methods,"ABC"):
        routine = routine.replace(m, k)
    return routine, methods