import random
heads=tails=0
for i in range(100):
 r=random.choice(['H','T'])
 heads+=r=='H'
 tails+=r=='T'
print('Heads',heads,'Tails',tails)
