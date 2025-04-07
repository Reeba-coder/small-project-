#Manipulating Tuples
countries=("Spain", "Italy", "India", "England", "Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)
#concatenate two tuples
countries=("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2=("India", "Vietnam", "China")
southEast=countries+countries2
print(southEast)
#count tuple
tup=(0,1,2,3,4,5,61,7,8,9,6,6,8,6)
res=tup.count(6)
print(res)
# Index Method : value error raise if elements not exits in tuple
res1=tup.index(6,6,13)
print("count of 6 in tuple is:" , res1)
# Lenght
res2=len(tup)
print(res2)