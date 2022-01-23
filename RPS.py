
import random
import time
r = int(input('enter the no. of rounds:'))
n = input('enter the name: ')
nm = n.title()
count_1 = 0
count = 0
for i in range(r):
    a = input('enter the rock paper scissor: ')
    s = a.lower()
    print('Please wait.....')
    time.sleep(1)
    print(nm ,'you genrate:',s)
    time.sleep(1)
    res = random.choice(['rock','paper','scissor'])
    print('system genrate: ',res)
    if s == 'scissor' and res == 'rock':
        count += 1
    elif s == 'scissor' and res == 'paper':
        count_1 += 1
    elif s == 'rock' and res == 'scissor':
        count_1 += 1
    elif s == 'rock' and res == 'paper':
        count += 1
    elif s == 'paper' and res == 'scissor':
        count += 1
    elif s == 'paper' and res == 'rock':
        count_1 += 1
    elif s == res:
        count+=0
        count_1+=0
    else:
        print('please check characters you entered')

print('Please wait for the result......')
time.sleep(5)
print(nm, 'your score is', count_1)
print('computer score is: ', count)
print('And The Winner is........')
time.sleep(3)
if count > count_1:
    print('computer win.')
elif count == count_1:
    print('draw')
else:
    print(nm, 'congratulations you win.')
