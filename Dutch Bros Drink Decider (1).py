#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For my program, I have created a Dutch Bros. Drink Decider to help customers (especially my friends) decide what type of drink and flavor to order. I factored in the type of drink, level of caffeine, and flavor preferences of the user. 

#The program asks the user if they want a hot, iced, or blended drink to narrow down the options. 
drinktype_question = input("What type of drink do you prefer? \na) Hot \nb) Iced \nc) Blended\n")

#The program asks the user how much caffeine they prefer to narrow down the options. 
caffeine_question = input("\nHow much caffeine do you want in your drink today? \na) Tons of caffeine \nb) Some caffeine \nc) I don't believe in caffeine\n")

#The program uses if/then statements to coordinate a specific type of drink based on the user's preferences of drink style and caffeine. For example, if the user wants a hot drink with tons of caffeine, then they should order a hot americano.
if drinktype_question == "a":
  if caffeine_question == "a":
    print("\nYou should order a hot americano. We'll decide on a flavor next.\n")
  if caffeine_question == "b":
    print("\nYou should order a hot mocha or latte. We'll decide on a flavor next.\n")
  if caffeine_question == "c":
    print("\nYou should order a hot chocolate or steamed milk. We'll decide on a flavor next.\n")
if drinktype_question == "b":
  if caffeine_question == "a":
    print("\nYou should order an iced americano or cold brew. We'll decide on a flavor next.\n")
  if caffeine_question == "b":
    print("\nYou should order an iced mocha or latte. We'll decide on a flavor next.\n")
  if caffeine_question == "c":
    print("\nYou should order a chocolate milk. We'll decide on a flavor next.\n")
if drinktype_question == "c":
  if caffeine_question == "a":
    print("\nYou should order a freeze. We'll decide on a flavor next.\n")
  if caffeine_question == "b":
    print("\nYou should order a blended latte. We'll decide on a flavor next.\n")
  if caffeine_question == "c":
    print("\nYou should order a frost. We'll decide on a flavor next.\n")


# In[2]:


#The program tells the user that it will print a dataframe to provide a visual of all of the possible drink options.
print("To provide more detail, here's a dataframe of all possible drink options based on the type of drink you prefer and level of caffeine.\n")

#The program initializes pandas to present the dataframe.

# Import pandas library 
import pandas as pd 
  
#Initialize list of drink options
data = [['Hot', 'Tons of caffeine', 'Hot Americano'], ['Hot', 'Some caffeine', 'Hot mocha'], ['Hot', 'Some caffeine', 'Hot latte'], ['Hot', 'No caffeine', 'Hot chocolate'], ['Hot', 'No caffeine', 'Steamed milk'], ['Iced', 'Tons of caffeine', 'Iced americano'], ['Iced', 'Tons of caffeine', 'Cold brew'], ['Iced', 'Some caffeine', 'Iced mocha'], ['Iced', 'Some caffeine', 'Iced latte'], ['Iced', 'No caffeine', 'Chocolate milk'], ['Blended', 'Tons of caffeine', 'Freeze'], ['Blended', 'Some caffeine', 'Blended Latte'], ['Blended', 'No caffeine', 'Frost']] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Drink Type', 'Level of caffeine', 'Specific Drink']) 
  
# print dataframe. 
print(df) 

df.to_excel (r'C:\Users\Owner\Documents\Gonzaga Fall 2020\BMIS\dutch_decider.xlsx', index = False, header=True)


# In[3]:


#The program asks the user for their top two coffee flavors and recommends a flavor accordingly. 
first_flavor_question = input("\nWhat is your favorite flavor? \na) Vanilla \nb) Caramel \nc) Chocolate \nd) White Chocolate \ne) Hazelnut \nf) Irish Cream \ng) Chocolate Macadamia Nut \nh) Brown Sugar Cinammon \ni) Cinammon \nj) Peppermint \nk) Coconut \nl) Creme de Menthe\n")

second_flavor_question = input("\nWhat is your second favorite flavor? \na) Vanilla \nb) Caramel \nc) Chocolate \nd) White Chocolate \ne) Hazelnut \nf) Irish Cream \ng) Chocolate Macadamia Nut \nh) Brown Sugar Cinammon \ni) Cinammon \nj) Peppermint \nk) Coconut \nl) Creme de Menthe\n")

#The program uses if/then statements to coordinate a specific flavor of drink based on the user's two favorite flavors. For example, if the user wants a drink with caramel and vanilla, then the Golden Eagle is their perfect flavor.
if first_flavor_question == "a":
  if second_flavor_question == "b":
    print("\nYour perfect flavor is the Golden Eagle!\n")
  if second_flavor_question == "d":
    print("\nYour perfect flavor is the White Zombie!\n")
  if second_flavor_question == "g":
    print("\nYour perfect flavor is the Toasted Mellow!\n")
if first_flavor_question == "b":
  if second_flavor_question == "a":
    print("\nYour perfect flavor is the Golden Eagle!\n")
  if second_flavor_question == "g":
    print("\nYour perfect flavor is the Wallaby!\n")
  if second_flavor_question == "k":
    print("\nYour perfect flavor is the German Chocolate!\n")
if first_flavor_question == "c":
  if second_flavor_question == "e": 
    print("\nYour perfect flavor is the Snickers!\n")
  if second_flavor_question == "d":
    print("\nYour perfect flavor is the Tuxedo!\n")
  if second_flavor_question == "g":
    print("\nYour perfect flavor is the Wallaby!\n")
  if second_flavor_question == "i":
    print("\nYour perfect flavor is the Molten Lava!\n")
  if second_flavor_question == "k":
    print("\nYour perfect flavor is the German Chocolate!\n")
  if second_flavor_question == "l":
    print("\nYour perfect flavor is the Grasshopper!\n")
  if second_flavor_question == "j":
    print("\nYour perfect flavor is the Peppermint Bark!\n")
if first_flavor_question == "d":
  if second_flavor_question == "b":
    print("\nYour perfect flavor is the Trifecta!\n")
  if second_flavor_question == "c":
    print("\nYour perfect flavor is the Trifecta!\n")
  if second_flavor_question == "e":
    print("\nYour perfect flavor is the Dream Weaver!\n")
  if second_flavor_question == "g":
    print("\nYour perfect flavor is the Cookie!\n")
  if second_flavor_question == "j":
    print("\nYour perfect flavor is the Peppermint Bark!\n")
  if second_flavor_question == "k":
    print("\nYour perfect flavor is the White Angel!\n")
  if second_flavor_question == "h": 
    print("\nYour perfect flavor is the Cinnamon Bun!\n")
if first_flavor_question == "e":
  if second_flavor_question == "d":
    print("\nYour perfect flavor is the Dream Weaver!\n")
  if second_flavor_question == "f":
    print("\nYour perfect flavor is the Nutty Irishman!\n")
  if second_flavor_question == "c": 
    print("\nYour perfect flavor is the Snickers!\n")
if first_flavor_question == "f":
  if second_flavor_question == "e": 
    print("\nYour perfect flavor is the Nutty Irishman!\n")
if first_flavor_question == "g":
  if second_flavor_question == "d": 
    print("\nYour perfect flavor is the Toasted Mellow!\n")
if first_flavor_question == "h":
  if second_flavor_question == "d": 
    print("\nYour perfect flavor is the Cinnamon Bun!\n")
if first_flavor_question == "i":
  if second_flavor_question == "c": 
    print("\nYour perfect flavor is the Molten Lava!\n")
if first_flavor_question == "j":
  if second_flavor_question == "d": 
    print("\nYour perfect flavor is the Peppermint Bark!\n")
  if second_flavor_question == "c": 
    print("\nYour perfect flavor is the Peppermint Bark!\n")
if first_flavor_question == "k":
  if second_flavor_question == "c": 
    print("\nYour perfect flavor is the German Chocolate!\n")
  if second_flavor_question == "b": 
    print("\nYour perfect flavor is the German Chocolate!\n")
  if second_flavor_question == "d": 
    print("\nYour perfect flavor is the White Angel!\n")
if first_flavor_question == "l":
  if second_flavor_question == "c": 
    print("\nYour perfect flavor is the Grasshopper!\n")
  else: 
    print("\nCongratulations, you have a unique combination. Stick to your two favorites!")
#If the user picks two favorite flavors outside of the realm of the secret menu, the else statement suggests that they stick to their unique combination.

print("Combine your perfect flavor with the recommended drink style for a cofee made for you!")
#The program suggests that the user consider both the drink style and flavor suggestions to order their perfect drink.


# In[ ]:




