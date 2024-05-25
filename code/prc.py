# a=input("Enter a int value \n")
# b=input("Enter a  value \n")
# c=3
# print(a+b+str(c))

# print (34+1)
# length=len("Biswarup")
# print("your name has "+str(length)+"characters")

# a=input("Enter 1st num: ")

# sum=int(a[0])+int(a[1])
# print(sum)

# print(4//2)
# print(4/2)
# print(2**7)

# hight=input('Enter your hight ')
# weight=input("Enter your weight ")
# print("BMI IS =")
# print(int(weight)/(int(hight)**2))

# print(4<7 and 7>1)

# c=True
# print(not(c))

# a=5
# b=5

# print( a is b)
# print (a==b)

# print(id(a))
# print(id(b))

# Str="Biswarup"
# print("i" in Str)

# print("Bis"not in Str)

# l=[1,3,4,5,6,8,7,53,2]
# print(77 in l)

# print(round(7)) #7
# print(round(7,2)) #7
# print(round(7.652,2)) #7.65
# print(round(7.5)) #8
# print(round(6.5)) #6 Nearest even integer 
# print(round(665,-1)) #660
# print(round(675,-1)) #680

# name="Biswarup"
# age=22
# height=5.6

# print(f"My name is {name}, I am {age} years old.My height is {height} meters")

# age=int(input("Enter your age: "))
# r_year= 90 - age
# r_day=r_year*365
# r_months= r_year * 12
# r_week = r_year * 52

# print(f"i have {r_year} years, {r_months} months , {r_week} weeks , {r_day} days left") 

# num=int(input("Enter A NUMBER  "))

# if(num % 2== 0):
#     print("Even Number ")
# else:
#     print("Odd number")

# height=int(input("What is your height "))
# if(height>3):
#     print("You can ride ")
#     age=int(input("Enter your age: "))
#     if(age<=18):
#         print("You have to pay Rs-150")
#     else:
#         print("You have to pay 500 ")
# else:
#     print("You can't ride")

# weight = int(input("Enter your weight "))
# height = float(input("Enter your Height "))
# bmi = round(weight/height**2)

# print(f" Your Bmi is- {bmi} ")
# if(bmi>= 16 and bmi<=18 ):
#     print("Under Weight")
# elif(bmi>= 18 and bmi<=24):
#     print("Normal")
# elif(bmi>=25 and bmi<=29):
#     print("OverWeight")
# else:
#     print("Obese")
      
# year=int(input('enter Year '))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#  print("Leper")
# else: print("Not a Leper")

# def find_next_leap_year(current_year):
#     while True:
#         if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
#             return current_year
#         current_year += 1

# year = int(input('Enter Year: '))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f'{year} is not a leper')
#     next_leap_year = find_next_leap_year(year)
#     print(f"The next leap year after {year} is: {next_leap_year}")

# pizza=input("Enter your Pizza Size: ")
# total=0

# if(pizza=="Small"):
#     price = 100
#     pepoSmall=input("Need pepperoni ?")
#     if(pepoSmall=="Yes"):
#         price+=30

# elif(pizza=="Medium"):
#     price=200
#     pepoMid=input("Need pepperoni ?")
#     if(pepoMid=="Yes"):
#         price+=50
# elif(pizza=="Large"):
#     price=300


# cheese=input("Need extra Cheese ? ")
# if(cheese=="Yes"):
#   price+=20
  
# total=price
# print(f"Your total Bill- {total}")  

# name=input("Enter your name ")
# print(name.lower())

# print(len(name))

# roll=[1,2,3,4,5,6]
# name=["Biswarup","Bipul","Rahul","Amit"]
# print(roll)
# print(len(name)) #op-4

# print(roll[-1]) #Fetch from backward op-6

# print(roll[1:3]) #print start idx,end idx-1
# print(roll[1:6:2]) # third Argument represent skip op- [2, 4, 6]

# roll2=[3,5,2,1,9,7]
# roll2.sort()  #[1, 2, 3, 5, 7, 9]
# roll2.reverse() #[9, 7, 5, 3, 2, 1]
# print(roll2)
# print(max(roll2)) 
# print(min(roll2)) 

# roll2.append(70)
# roll2.insert(2,34)

# roll2.extend([1,23,4])
# roll2[1:2]=[0,0] #[3, 0, 0, 0, 9, 7, 1, 23, 4]
# roll2.pop(0)                 
# print(roll2)

# roll=[1,2,3,4,5,6,7]
# print(roll)
# roll[1:2]=[9,8,7]
# print(roll)
# # roll.pop()
# print(roll)
# print(roll.count(7))

# text="Hello Biswarup how are you?"
# new_txt=text.split(" ")
# print(new_txt)
# list2=[10,12,['Biswarup','Shyam','Ram'],6]
# print(list2[2][2])

# row1=[1,1,1]
# row2=[1,1,1]
# row3=[1,1,1]
# matrix=[row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")


# position=input('Enter the Position you Want to Hide- ')

# row_num=int(position[0])
# col_num=int(position[1])

# row_Selected=matrix[row_num-1]
# row_Selected[col_num-1]='X'
# print(f"{row1}\n{row2}\n{row3}")

# tuple1=(10,1,-12,15,12,12)
# tuple2=("Biswarup","Mahato")
# tuple3=(10,1.3,-12,"Biswa")

# tuple4=(10,)  #For Signal Item Tuple put a ,
# tuple5=(10)

# # print(len(tuple1))
# # print(max(tuple1))
# print(tuple1.count(12))
# tuple7=(tuple1,tuple2) #Nested Tuple

# list=[1,2,3,4,5]
# print(tuple(list))

set1={10,56,90,"Biswarup",True}
print(set1)
set2=set() #Empty Set
print(type(set1))
print(type(set2))
set1.add(22)
print(set1)
print(len(set1))
set1.remove(10) #if key not present it gives error
set.discard(12) #if key not present it gives the same SET

set1.pop() #Remove any random key
set1.add()