set1 = {"Biswarup","Amit","Sumit"}
set2 = {"Ronaldo","Amit","Sandeep"}
set3 = {"Monika","Khana","Shikha"}

# print(set1.union(set2,set3)) # we can use tuple Here

# # print(set1 | set2 | set3)
# # UPDATE USING FUNCTION

# set1.update(set2)
# print(set1)

# set2.update(['Koushik','Nila'])
# print(set2)

# #UPDATE USING OPERATOR

# set3 |= set2
# print(set3)

print(set1.intersection(set2,set3))
print(set1 & set2)
print(set1.intersection(["Sumit","Rahul"]))





