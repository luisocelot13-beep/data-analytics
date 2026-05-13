doubler = lambda n: n *2
print(doubler('banana'))

tripler = lambda x: x * 3
print(tripler(5))


def multiplier (n):
    return lambda x: x * n

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier (6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(3))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))