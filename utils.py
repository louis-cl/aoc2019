from math import gcd 
from functools import reduce
import re

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def integers(s):
    return re.findall(r'-?\d+', s.strip())