from client import WeisfeilerLehmanKernel

g1 = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
g2 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
g3 = {1: [2], 2: [1, 3], 3: [2]}

print("Isomorphic Check (g1 ~ g2):", WeisfeilerLehmanKernel.are_isomorphic(g1, g2))
print("Isomorphic Check (g1 ~ g3):", WeisfeilerLehmanKernel.are_isomorphic(g1, g3))
