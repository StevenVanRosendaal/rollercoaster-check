import lib_coasterimg as coasterimg
import time
import os

#Read check values
file1 = open("rules/age.txt", "r")
age_check = int(file1.read())
file1.close()
# Test 1
# Test 2
# Test 3
# Test 4
# Test 5
# Test 6
# Test 7
# Test 8
# Test 9
print("Steven van Rosendaal")
print("instappen")

#test
#test2

file2 = open("rules/height.txt", "r")
height_check = int(file2.read())
file1.close()

running = True
while running:

    #Get inputs
    os.system('cls')
    print("Rollercoaster-check™")
    age = input("Voer leeftijd in: ")
    height = input("Voer lengte in: ")
    age = int(age)
    height = int(height)

    #Process checks
    if(age > age_check and height > height_check):
        os.system('cls')
        print("Stap maar in!")
        print(coasterimg.get())
        time.sleep(2)

    else:
        os.system('cls')
        print("Je voldoet niet aan de voorwaarden...")
        print(coasterimg.sad())
        time.sleep(2)

    result = input("Druk op Enter om nog een keer te checken, of X om te stoppen\n\n")
    if(result.upper() == "X"):
        running = False
