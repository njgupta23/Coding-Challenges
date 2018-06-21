"""
Get Load Order

Given a dictionary of dependencies and a module, write a function that will 
return the load order to run that module.

Example:

A: B, C
B: C, D
C:
D: E, F
E:
F:

load(E) => E
load(F) => F
load(D) => E, F, D OR F, E, D
load(B) => C, E, F, D, B

"""


def load(deps, mod):
    order = []
    seen = set()
    queue = Queue()

    queue.enqueue(mod)

    while queue:
        mod = queue.dequeue()
        seen.add(mod)
        order.append(mod)

        for dependency in deps[mod]:
            if dependency not in seen:
                queue.enqueue(dependency)

    return order[::-1]
