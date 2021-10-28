from random import *

vinstmedbyte = 0
vinstutanbyte = 0
antal = 10000

for i in range(antal+1):

    # Ordna vinsterna
    doors = ['bil','get','get']

    # Blanda dörrarna
    shuffle(doors)

    # Deltagarens val
    guest = randint(0,2)

    # Programledarens val
    host = -1
    while True:
        host = randint(0,2)
        if host != guest and doors[host] == 'get':
            break
        
    # Kolla vinst för byte eller inte byte
    # Byte
    for change in range(0,3):
        if change != host and change != guest:
            break
    if doors[change] == 'bil':
        vinstmedbyte += 1

    # Ej byte
    if doors[guest] == 'bil':
        vinstutanbyte += 1

print("Monty hall simulering: {} simuleringar".format(antal))
print("Vinst med byte: ",vinstmedbyte)
print("Vinst utan byte: ",vinstutanbyte)
