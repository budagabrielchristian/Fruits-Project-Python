def increase_price(fruit,price):
  list_of_fruits[fruit]=list_of_fruits[fruit]+price

def set_price_of_fruit(fruit,price):
    list_of_fruits[fruit]=price
    
def print_data(fruit):
  try:
    print("Price per kilogram ["+str(fruit)+']:'+str(list_of_fruits[fruit])+'$')
  except:
    print(str(fruit)+" is not in the list!")

def add_fruit(fruit,price):
    list_of_fruits[fruit]=price

def print_fruits():
  for fruit in list_of_fruits:
    print("1 kilogram x "+str(fruit)+" costs "+str(list_of_fruits[fruit])+'$')



list_of_fruits = {
  "Orange":7,
  "Tomato":20,
  "Strawberry":15,
  "Peach":3
}

#Tests:

increase_price("Orange",2)
set_price_of_fruit("Tomato",10)
print_data("Watermelon")
print_data("Orange")
add_fruit("Watermelon",26)
print_data("Watermelon")
print_fruits()
