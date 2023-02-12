phone_book = {"Danzi kaya": "+234 9162822742","David OKih": "+234 9162822742","Precious": "+234 9162822742"}


print(phone_book)
print(phone_book["David OKih"])

# Another way to create a dictionary using the dict function
inventory = dict()
inventory["banans"] = 25
inventory["apples"] = 102
inventory["oranges"] = 54
inventory["watermalons"] = 4

print(inventory)
print(inventory["apples"])

# Method to display the keys and value indivisually

print(inventory.keys())
print(inventory.values())

# the method item return the key and value as a tuple

print(inventory.items())

for key in inventory:
    inventory[key] += 100

print(inventory)

for key,value in inventory.items():
    if value > 200:
        print("Too many", key)
    else:
        print("Enough", key)

inventory = {'Milk':[4,1000,'dairy'],
             
             'Apples':[2,3,'fruits'],

             'Onions':[1,50,'vegetables'],

             'Oranges':[1.5,1000,'fruits'],

             'Bread':[3,100,'bakery'],

             'Bananas':[5,300,'fruits']}

shopping_list = [('milk',1), ('apples',4), ('onions', 5), ('oranges',5), ('bread',2), ('bananas',10)]

def check_stock(shopping_list, inventory):
  #Create the empty shopping_list_updated
  updated_shopping_list = []
  #Write a for loop to iterate over each item in your shopping list
  for element in shopping_list:
    item, amount = element
    #Access the available stock in your inventory
    inventory_value = inventory[item]
    if amount > inventory_value[1]:
      amount = inventory_value[1]
      print("We dont have enough stock of", item,"you can buy a maximum amount of",inventory_value[1])
    #append item and amount to your updated shopping list
    updated_shopping_list.append((item,amount))
  return updated_shopping_list


updated_shopping_list = check_stock(shopping_list, inventory)
print("Your updated shopping list:", updated_shopping_list)