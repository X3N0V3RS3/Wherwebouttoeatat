import random,os

os.system("clear")

resteraunts = ["McDoanlds", "Panera", "Jasons Deli", "Random Chinese Resteraunt", "Wendys", "Sonic","Chipotle","Burger King", "Deez Nutz","Stay At Home and Cook", "Noodles Company", "Pho 79","Shake Shack","Chick Fil A", "Dairy Queen", "Subway", "Ruby Tueday", "CAVA", "Taco Bell", "Village Inn", "Arbys","Random Pizza Place",
"Dennys","Hardees", "Chilis"]


print(random.choice(resteraunts))

#Whos Paying (Minigame)

group = input("How many people are in you party :")

payer = random.randint(1,int(group))

mode = input('''Mode 1 = One Person Pays for everyone

Mode 2 = One Person Pays for a Random amount of people in the party everyone else pays for themeselves


Mode 3 = Everyone in the party pitches in to pay for one person :''')

if mode == '1':
  print(f"Person Number {payer} is paying for everyone No Respins")

elif mode == '2':
  print(f"Person Number {payer} is paying for {payer} People in the Party No Respins")

elif mode == '3':
  print(f"Everyone is paying for Person {payer}")

else:
  print("Mode not in range")
