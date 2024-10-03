import random, os, time

os.system("clear")


title = "MY Bingo Cards Generator"

print(f"{title: ^50}")

numbers = []

def ran():
  number = random.randint(1,90)
  return number

def prettyprint():
  print()
  for row in myBingoCard:
    for item in row:
      print(f"{item: ^10}", end=" | ")
    print()
  print()


for i in range(8):
  numbers.append(ran())

numbers.sort()

myBingoCard = [ [numbers[0], numbers[1], numbers[2]], [numbers[3], "BINGO", numbers[4]], [numbers[5], numbers[6], numbers[7]]]

prettyprint()

exes = 0

while True:
  number = input("What is the number called? ")
  for row in myBingoCard:
    if (int(number) in row):
      row[row.index(int(number))] = "X"
      exes+=1
  if exes == 8:
    print("BINGO, you won!")
    break    
  
  time.sleep(2)
  os.system("clear")   
  prettyprint()
