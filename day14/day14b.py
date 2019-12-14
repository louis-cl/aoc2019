import sys
from collections import defaultdict
from dataclasses import dataclass
import bisect
import math

@dataclass
class Rule:
    factor: int
    products: dict


def main(rules, fuel):
    ore = 0
    needs = defaultdict(int)
    have = defaultdict(int)
    needs['FUEL'] = fuel
    # propagate
    try:
        while needs:
            want, qty = next(iter(needs.items()))
            del needs[want]
            # do i already have some ?
            qty, have[want] = max(0, qty - have[want]), max(0, have[want] - qty)
            if qty == 0: continue
            # not enough
            # print("need to cook", qty, "of", want)
            # check recipe, i need qty of want
            rule = rules[want]
            factor = rule.factor
            times = math.ceil(qty / factor)
            # print("apply rule",rule, times, "times")
            for prod,pfactor in rule.products.items():
                produced = pfactor*times
                if prod == 'ORE':
                    ore += produced
                else:
                    needs[prod] += produced
            # excess
            have[want] += (factor - qty % factor) % factor
    except StopIteration:
        pass
    # print("needs", needs)
    # print("have", have)
    return ore


def read(line):
    a, b = line.strip().split('=>')
    # result
    def f(x):
        qty, result = x.strip().split(' ')
        return (result.strip(), int(qty))
    
    products = {}
    for part in a.split(', '):
        name, qty = f(part)
        products[name] = qty
    
    name, qty = f(b)
    return name, Rule(qty, products)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # read reactions
    rules = dict(map(read, lines))

    class Search:
        def __getitem__(self, val):
            return main(rules, val)
    print(bisect.bisect(Search(), 10**12, hi=10**12)-1)