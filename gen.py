import random

# list
prefixos = ["Anarco", "Monarco", "Comuno", "Neo", "Eco", "Turbo", "Social", "Ultra", "Omni", "Minarco"]
sufixos = ["fobia", "ista", "man", "zoo", "byte", "filia", "tropia", "arquia", "cracia", "ismo"]

# func
def gerar_nome():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    return prefixo + sufixo

# gen
for _ in range(5):
    print(gerar_nome())
