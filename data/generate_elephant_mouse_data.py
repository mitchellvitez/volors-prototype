import random

elephant = ((4000, 7000), (2.5, 4), 'elephant')
mouse = ((.05, .8), (.065, .2), 'mouse')

def rando(r):
   return '%.2f' % random.uniform(*r)

for i in range(1000):
    animal = random.choice([elephant, mouse])
    with open("sample.csv", "a") as f:
        f.write(','.join([rando(animal[0]), rando(animal[1]), animal[2]]))
        f.write('\n')

