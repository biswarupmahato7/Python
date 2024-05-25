import random
user=int(input('ENTER YOUR CHOICE- '))
computer=random.randint(0,2)
print('Computer Choice')
print(computer)

if user==computer : print('Draw')
elif computer==0 and user ==2: print('Computer win')
elif user==0 and computer==2: print('You Win')
elif computer>user: print('Computer Win')
elif user>computer: print('You Win')

