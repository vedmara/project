import random
lotto = []
lot = []
count = 0
for i in range(0,7):
    n = random.randint(1,60)
    lotto.append(n)
print(lotto)
l = input("your numbers ")
l = l.split()
for i in range(0,len(l)):
    lot.append(int(l[i]))
print(lot)

for y in range(0, len(lot)):
    if lot[y] in lotto:
        count+=1
print(count)
if count == 3:
    print(20)
if count == 4:
    print(40)
if count == 5:
    print(100)
if count == 6:
    print(10000)
if count == 7:
    print(1000000)
else:
    print('try again!')
