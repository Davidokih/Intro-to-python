shopping_list = ["Apple","Juice","Ball","Books"]

# The list append method add objects at the end of a list
shopping_list.append("Water")
print(shopping_list)

# the insert all us to put value any where in a list
shopping_list.insert(2,"Banana")
print(shopping_list)

# The remove: remove an element from the list

shopping_list.remove("Apple")
print(shopping_list)

# To change a data in a list 
shopping_list[3] = "Strawberry"
print(shopping_list)

number_list = [1,2,3,4,5]

square_list = []

for num in number_list:
    square_list.append(num**2)

print(square_list)
# list comprension is to create a new list
square_list2 = [num**2 for num in number_list]
print(square_list2)


# Tuples

shopping_list2 = ("Apple","Juice","Ball","Books","Water")

item1,item2,item3,item4,item5 = shopping_list2
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

print(shopping_list2[0])
print(shopping_list2[1:3])

